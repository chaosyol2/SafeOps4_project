import sqlite3
import pandas as pd

conn = sqlite3.connect('safeops.db')

tables = ['machines', 'sensors', 'operators', 'operatorbehavior',
          'riskscores', 'recommendations', 'alerts', 'historicalfailures']

for table in tables:
    df = pd.read_csv(f'{table}.csv')
    df.to_sql(table, conn, if_exists='replace', index=False)

print("Done!")
conn.close()
