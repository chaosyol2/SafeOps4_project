from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # ส่งค่าตัวเลขสมมติ (เช่น 0) ไปก่อน เพื่อให้หน้าเว็บไม่ Error เวลาหาตัวแปร avg_risk
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
