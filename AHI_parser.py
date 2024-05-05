import pandas as pd

path = 'D:\\chat\\datasets\\chat-baseline-dataset-0.14.0.csv'
df = pd.read_csv(path)
df_extracted = df[['new_pid', 'qsahi']]
df_extracted = df_extracted.rename(columns={'new_pid': 'Study', 'qsahi': 'AHI'})
print(df_extracted.head(20))

df_extracted.to_csv('AHI.csv', index=False)

