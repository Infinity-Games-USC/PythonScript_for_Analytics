
import json
import pandas as pd

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return int(avg)
  
# create an Empty DataFrame object
df = pd.DataFrame(columns = ['Attempts', 'Bullet_at_Death'])
print(df.head())



def coerce_df_columns_to_numeric(df, column_list):
    df[column_list] = df[column_list].apply(pd.to_numeric, errors='coerce')

print(df.head)
with open('Bullet_at_death/bullets_left_midterm.json') as file:
    lines = file.readlines()

hash={}

for line in lines:

    json_object=str(line)
    json_object = json.loads(json_object)
    #print(json_object["custom_params"]["AttemptNo."])
    if(json_object["custom_params"]["AttemptNo."] not in hash):
        hash[json_object["custom_params"]["AttemptNo."]]=[int(json_object["custom_params"]["RemainingBulletCount"])]
    else:
        hash[json_object["custom_params"]["AttemptNo."]]+=[int(json_object["custom_params"]["RemainingBulletCount"])]

    df = df.append({'Attempts' : json_object["custom_params"]["AttemptNo."], 'Bullet_at_Death' : json_object["custom_params"]["RemainingBulletCount"]}, 
                ignore_index = True)
    


print(hash)

for k,v in hash.items():

    hash[k]=cal_average(hash[k])

print(hash)
df['Bullet_at_Death'] = df['Bullet_at_Death'].apply(pd.to_numeric, errors='coerce')

df1=pd.DataFrame(hash.items(), columns=['Attempts', 'Bullets_left_avg'])

df1.to_csv('Bullet_at_death/bullets_left_midterm_2.csv',index=False)
df.to_json('Bullet_at_death/bullets_left_midterm_edited.json',orient = "records")
df.to_csv('Bullet_at_death/bullets_left_midterm.csv',index=False)
