import pandas as pd
import numpy as np

# df = pd.read_csv("machine_risk.csv")
# df = pd.read_csv("human_risk.csv")
# df = pd.read_csv("environment_risk.csv")
df = pd.read_csv("historical_risk.csv")
num_machines = 23
df['machine_id'] = (np.arange(len(df)) % num_machines) + 1

df.to_csv("historical_risk1.csv", index=False)
