import requests

# นำค่าจาก LINE Developers Console มาใส่
LINE_ACCESS_TOKEN = 'szTR83OFlRljGF/xgWOWrDaxcCYlmUvnXRW/FVxMdM3iR0DiwqFUlLoXlcmELM4IXq9ndS+cgPVLSkC8S+aCn4redIkTu3UZPg11WnTZxI9WYzBr1+XPaAx81DzNizJfLkc79SSiTxCjWLN+jq4S1AdB04t89/1O/w1cDnyilFU='
USER_ID = 'U1e788bdc7d56c68103ab09f264631f33' # ID ของคุณที่จะให้บอททักไปหา

def test_send():
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
                "text": """[🚨 SAFEOPS ALERT: CRITICAL RISK]
    📍 Location: Production Line 3 | Machine: M4 (Main Press)
    ⚠️ Status: CRITICAL (Risk Score: 92/100)
    🔍 Detected: Abnormal Vibration & High Temp (Over 85°C)

    ✅ Immediate Recommendations (สิ่งที่ต้องทำทันที):
    1. STOP MACHINE: กดปุ่ม Emergency Stop ที่เครื่อง M4 ทันที

    2. EVACUATE AREA: ให้พนักงานในรัศมี 2 เมตร ถอยออกจากตัวเครื่อง

    3. NOTIFY MAINTENANCE: แจ้งทีมซ่อมบำรุงรหัส "M4-CRIT"

    ❌ Risk of Inaction (หากไม่ดำเนินการจะเกิดอะไรขึ้น):
    - Mechanical Failure: มอเตอร์หลักอาจไหม้ (ค่าซ่อม ~฿450,000)
    - Safety Hazard: เสี่ยงต่อการเกิดประกายไฟ
    - Production Loss: Downtime 6 ชม. (เสียหาย ฿3,000,000+)"""
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("✅ สำเร็จ! ข้อความเด้งเข้า LINE แล้ว")
    else:
        print(f"❌ ล้มเหลว! Error Code: {response.status_code}")
        print(f"รายละเอียด: {response.text}")

if __name__ == "__main__":
    test_send()
