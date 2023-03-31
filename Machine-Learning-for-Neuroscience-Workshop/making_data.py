import pandas as pd

df = pd.read_csv('./data/health.csv').sample(10000)
print(df.shape)
print(df.head())
df.to_csv('./data/small_health.csv')