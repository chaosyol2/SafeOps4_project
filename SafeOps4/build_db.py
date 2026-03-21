import pandas as pd
import sqlite3

# 1. ตั้งชื่อไฟล์ Database
db_name = 'factory_risk.db'
conn = sqlite3.connect(db_name)

# 2. รายชื่อไฟล์ CSV และชื่อตารางที่ต้องการ
tables = {
    'environment_risk.csv': 'environment_risk',
    'historical_risk.csv': 'historical_risk',
    'human_risk.csv': 'human_risk',
    'machine_risk.csv': 'machine_risk'
}

for file_name, table_name in tables.items():
    try:
        df = pd.read_csv(file_name)

        # เพิ่มคอลัมน์ ID ถ้าใน CSV ยังไม่มี เพื่อความสะดวกในการอ้างอิงและแก้ไข
        if 'id' not in df.columns:
            df.insert(0, 'id', range(1, 1 + len(df)))

        # เขียนลง Database
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"✅ Import {file_name} -> Table: {table_name} สำเร็จ!")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดกับ {file_name}: {e}")

conn.close()
print(f"\n--- สร้างไฟล์ {db_name} เรียบร้อยแล้ว ---")
