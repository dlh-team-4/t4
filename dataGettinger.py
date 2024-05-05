import sleep_study as ss
import pandas as pd


PATH1 = r"D:\chat\datasets\chat-harmonized-dataset-0.14.0.csv"
PATH2 = r"D:\nchsdb\datasets\nchsdb-dataset-harmonized-0.3.0.csv"
AHI = r"C:\Users\William\Documents\Development\Python projects\Deeplearning healthcare\Pediatric-Apnea-Detection\AHI.csv"
chat = pd.read_csv(PATH1, usecols=['nsrrid'])
nch = pd.read_csv(PATH2, usecols=['study_pat_id', 'filename_id'])
#print(chat[chat['nsrrid'] == 300001])
 
chat['nsrrid'] = chat['nsrrid'].apply(lambda x: int(str(x)[1:].lstrip('0')))

merged_chat = pd.merge(nch, chat, left_on='study_pat_id', right_on='nsrrid', how='inner')
# #print(len(chat['nsrrid']))
# print(merged_df.head(20))

ahi = pd.read_csv(AHI)

merged_df = pd.merge(merged_chat, ahi, left_on='study_pat_id', right_on='Study')
merged_df = merged_df.drop(columns=['Study', 'nsrrid', 'study_pat_id'])
merged_df = merged_df.drop_duplicates()


print(merged_df.head(20))
print(len(merged_df))

# df_extracted = merged_df.rename(columns={'filename_id': 'Study', 'AHI': 'AHI'})


# print(df_extracted.head(20))
# print(len(df_extracted))

#df_extracted.to_csv('AHI.csv', index=False)

