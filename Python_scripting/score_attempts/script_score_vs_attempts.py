
import json
import pandas as pd
  
# create an Empty DataFrame object
df = pd.DataFrame(columns = ['Attempts', 'Score'])
print(df.head())



def coerce_df_columns_to_numeric(df, column_list):
    df[column_list] = df[column_list].apply(pd.to_numeric, errors='coerce')


with open('score_attempts/score_attempts_midterm.json') as file:
    lines = file.readlines()

for line in lines:

    json_object=str(line)
    json_object = json.loads(json_object)
    #print(json_object["custom_params"]["score"])
    df = df.append({'Attempts' : json_object["custom_params"]["AttemptNo."], 'Score' : json_object["custom_params"]["Score"]}, 
                ignore_index = True)


print(df.head)

df['Score'] = df['Score'].apply(pd.to_numeric, errors='coerce')
df.to_json('score_attempts_midterm.json',orient = "records")