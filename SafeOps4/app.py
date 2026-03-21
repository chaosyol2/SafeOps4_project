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

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
