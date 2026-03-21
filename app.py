from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB = 'safeops.db'

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    data = {
        'machines':           conn.execute('SELECT * FROM machines').fetchall(),
        'sensors':            conn.execute('SELECT * FROM sensors').fetchall(),
        'operators':          conn.execute('SELECT * FROM operators').fetchall(),
        'operatorbehavior':   conn.execute('SELECT * FROM operatorbehavior').fetchall(),
        'riskscores':         conn.execute('SELECT * FROM riskscores').fetchall(),
        'recommendations':    conn.execute('SELECT * FROM recommendations').fetchall(),
        'alerts':             conn.execute('SELECT * FROM alerts').fetchall(),
        'historicalfailures': conn.execute('SELECT * FROM historicalfailures').fetchall(),
    }
    conn.close()
    return render_template('index.html', **data)

@app.route('/update/machines/<int:id>', methods=['POST'])
def update_machines(id):
    conn = get_db()
    conn.execute('UPDATE machines SET `name`=?, location=?, type=?, status=? WHERE machine_id=?',
        (request.form['name'], request.form['location'], request.form['type'], request.form['status'], id))
    conn.commit(); conn.close()
    return redirect('/')

@app.route('/update/sensors/<int:id>', methods=['POST'])
def update_sensors(id):
    conn = get_db()
    conn.execute('UPDATE sensors SET sensor_type=?, unit=?, last_reading=? WHERE sensor_id=?',
        (request.form['sensor_type'], request.form['unit'], request.form['last_reading'], id))
    conn.commit(); conn.close()
    return redirect('/')

@app.route('/update/operators/<int:id>', methods=['POST'])
def update_operators(id):
    conn = get_db()
    conn.execute('UPDATE operators SET `name`=?, `role`=?, assigned_zone=?, contact=? WHERE operator_id=?',
        (request.form['name'], request.form['role'],
         request.form['assigned_zone'], request.form['contact'], id))
    conn.commit(); conn.close()
    return redirect('/')

@app.route('/update/operatorbehavior/<int:id>', methods=['POST'])
def update_operatorbehavior(id):
    conn = get_db()
    conn.execute('UPDATE operatorbehavior SET behavior_type=?, severity=? WHERE behavior_id=?',
        (request.form['behavior_type'], request.form['severity'], id))
    conn.commit(); conn.close()
    return redirect('/')

@app.route('/update/riskscores/<int:id>', methods=['POST'])
def update_riskscores(id):
    conn = get_db()
    conn.execute('UPDATE riskscores SET score=?, category=?, notes=? WHERE risk_id=?',
        (request.form['score'], request.form['category'], request.form['notes'], id))
    conn.commit(); conn.close()
    return redirect('/')

@app.route('/update/recommendations/<int:id>', methods=['POST'])
def update_recommendations(id):
    conn = get_db()
    conn.execute('UPDATE recommendations SET recommendation=?, priority=?, status=? WHERE rec_id=?',
        (request.form['recommendation'], request.form['priority'], request.form['status'], id))
    conn.commit(); conn.close()
    return redirect('/')

@app.route('/update/alerts/<int:id>', methods=['POST'])
def update_alerts(id):
    conn = get_db()
    conn.execute('UPDATE alerts SET alert_type=?, message=?, read_status=? WHERE alert_id=?',
        (request.form['alert_type'], request.form['message'], request.form['read_status'], id))
    conn.commit(); conn.close()
    return redirect('/')

@app.route('/update/historicalfailures/<int:id>', methods=['POST'])
def update_historicalfailures(id):
    conn = get_db()
    conn.execute('UPDATE historicalfailures SET failure_type=?, cause=?, downtime=?, notes=? WHERE failure_id=?',
        (request.form['failure_type'], request.form['cause'], request.form['downtime'], request.form['notes'], id))
    conn.commit(); conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
