import sqlite3
from flask import Flask, render_template, url_for
from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('factory_risk.db')
    cursor = conn.cursor()

    # ดึงค่าเฉลี่ยจากแต่ละตาราง (ใช้ COALESCE กันเหนียวถ้าตารางไหนว่างให้เป็น 0)
    # 1. จาก machine_risk (สมมติชื่อคอลัมน์ risk_score)
    cursor.execute("SELECT AVG(machine_risk) FROM machine_risk")
    m_risk = cursor.fetchone()[0] or 0

    # 2. จาก human_risk_label (สมมติชื่อคอลัมน์ score)
    cursor.execute("SELECT AVG(human_risk_label) FROM human_risk")
    h_risk = cursor.fetchone()[0] or 0

    # 3. จาก environment_risk_score (สมมติชื่อคอลัมน์ env_score)
    cursor.execute("SELECT AVG(environment_risk_score) FROM environment_risk")
    e_risk = cursor.fetchone()[0] or 0

    # 4. จาก historical_risk_score (สมมติชื่อคอลัมน์ his_score)
    cursor.execute("SELECT AVG(historical_risk_score) FROM historical_risk")
    hi_risk = cursor.fetchone()[0] or 0

    # คำนวณค่าเฉลี่ยรวมจากทั้ง 4 ส่วน
    total_avg = (m_risk + h_risk + e_risk + hi_risk) / 4

    # ปัดเศษ 1 ตำแหน่ง
    final_risk = round(total_avg, 1)

    # # SQL: เชื่อม 4 ตาราง, คำนวณสูตรถ่วงน้ำหนัก, กรองช่วง 41-70, และสุ่มมา 1 เครื่อง
    # query = """
    # SELECT
    #     m.machine_id,
    #     ( (0.4 * m.machine_risk) +
    #       (0.3 * h.human_risk_label) +
    #       (0.2 * e.environment_risk_score) +
    #       (0.1 * hi.historical_risk_score) ) as final_score
    # FROM machine_risk m
    # JOIN human_risk h ON m.machine_id = h.machine_id
    # JOIN environment_risk e ON m.machine_id = e.machine_id
    # JOIN historical_risk hi ON m.machine_id = hi.machine_id
    # WHERE final_score BETWEEN 41 AND 70
    # ORDER BY RANDOM()
    # LIMIT 1
    # """

    # cursor.execute(query)
    # row = cursor.fetchone()

    # random_alert = None
    # if row:
    #     random_alert = {
    #         "id": row[0],
    #         "score": round(row[1], 1),
    #         "status": "CHECK SYSTEM", # คำแนะนำสำหรับช่วง Warning
    #         "time": "1 min ago"       # หรือจะดึงจาก DB มาคำนวณเวลาก็ได้
    #     }

    # ดึงข้อมูลเฉพาะเครื่อง (Fix ID)
    # ใช้สูตรคำนวณถ่วงน้ำหนักตรงๆ ใน SQL
    target_id = '10'
    query = """
    SELECT
        m.machine_id,
        ( (0.4 * m.machine_risk) +
          (0.3 * h.human_risk_label) +
          (0.2 * e.environment_risk_score) +
          (0.1 * hi.historical_risk_score) ) as calculated_score
    FROM machine_risk m
    JOIN human_risk h ON m.machine_id = h.machine_id
    JOIN environment_risk e ON m.machine_id = e.machine_id
    JOIN historical_risk hi ON m.machine_id = hi.machine_id
    WHERE m.machine_id = ?
    LIMIT 1
    """

    cursor.execute(query, (target_id,))
    row = cursor.fetchone()
    conn.close()

    # 3. จัดการแสดงผล Alert
    random_alert = None
    if row:
        random_alert = {
            "id": row[0],
            "score": round(row[1], 1),
            "status": "CHECK SYSTEM",
            "time": "Just now" # เปลี่ยนเป็นเวลาปัจจุบัน
        }


    return render_template('index.html',avg_risk_value=final_risk,alert=random_alert)


@app.route('/history')
def history_page():

    # ส่งข้อมูลที่ดึงได้ไปที่หน้า history.html
    return render_template('history.html')

@app.route('/team')
def team_page():
    # ในอนาคตคุณสามารถดึงข้อมูลสมาชิกทีมจาก Database มาโชว์ที่นี่ได้
    return render_template('team.html')

@app.route('/machines')
def machines_page():
    # ในอนาคตคุณสามารถดึงข้อมูลจำนวนเครื่องจักรจาก Database มาโชว์ที่นี่ได้
    return render_template('machines.html')

@app.route('/alerts')
def alerts_page():
    # ในอนาคตคุณสามารถดึงข้อมูลการแจ้งเตือนจาก Database มาโชว์ที่นี่ได้
    return render_template('alerts.html')

@app.route('/risk')
def risk_page():
    # ในอนาคตคุณสามารถคำนวณค่า Risk รายตัวมาโชว์ที่นี่ได้
    return render_template('risk.html')

@app.route('/m1')
def m1_page():

    return render_template('m1.html')


@app.route('/m1_insight')
def m1_insight_page():
    # ในอนาคตคุณสามารถใส่ Logic วิเคราะห์ข้อมูลด้วย AI ตรงนี้ได้
    return render_template('m1_insight.html')

@app.route('/m1_machine_risk')
def m1_machine_risk_page():
    # ในอนาคตคุณสามารถดึงค่า Vibration หรือ Temperature จาก DB มาโชว์ที่นี่ได้
    return render_template('m1_machine_risk.html')

@app.route('/m1_human_risk')
def m1_human_risk_page():
    # หน้านี้จะใช้โชว์ข้อมูลความเสี่ยงจากพฤติกรรมคน เช่น Phone Usage
    return render_template('m1_human_risk.html')

@app.route('/m1_env_risk')
def m1_env_risk_page():
    # หน้านี้จะใช้โชว์ข้อมูลปัจจัยภายนอก เช่น ความชื้น (Humidity) หรือ คุณภาพอากาศ
    return render_template('m1_env_risk.html')

@app.route('/m1_his_risk')
def m1_his_risk_page():
    # หน้านี้จะใช้โชว์ข้อมูลประวัติการเสีย (Downtime) และความถี่ในการซ่อมบำรุง
    return render_template('m1_his_risk.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')



# นำค่าจาก LINE Developers Console มาใส่
LINE_ACCESS_TOKEN = 'szTR83OFlRljGF/xgWOWrDaxcCYlmUvnXRW/FVxMdM3iR0DiwqFUlLoXlcmELM4IXq9ndS+cgPVLSkC8S+aCn4redIkTu3UZPg11WnTZxI9WYzBr1+XPaAx81DzNizJfLkc79SSiTxCjWLN+jq4S1AdB04t89/1O/w1cDnyilFU='
USER_ID = 'U1e788bdc7d56c68103ab09f264631f33' # ID ของคุณที่จะให้บอททักไปหา

def send_line_message(text):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_ACCESS_TOKEN}'
    }
    data = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code

@app.route('/submit_id', methods=['POST'])
def submit_id():
    data = request.get_json()
    user_id = data.get('id')

    if user_id:
        # ข้อความแบบ Professional สำหรับ Smart Factory
        log_msg = f"🔧 [SMART FACTORY SYSTEM]\n────────────────\n📢 Status: Operator Login\n👤 ID: {user_id}\n✅ Connection: Established"

        status = send_line_message(log_msg)

        if status == 200:
            return jsonify({"status": "success", "message": "Logged & Sent to LINE Bot"})
        else:
            return jsonify({"status": "error", "message": "LINE API Error"}), 500

    return jsonify({"status": "error", "message": "Invalid ID"}), 400
if __name__ == '__main__':
    app.run(debug=True, port=5000)
