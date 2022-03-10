
import json
import pandas as pd
  
# create an Empty DataFrame object
df = pd.DataFrame(columns = ['Attempts', 'InvincibilityUsed'])
print(df.head())



def coerce_df_columns_to_numeric(df, column_list):
    df[column_list] = df[column_list].apply(pd.to_numeric, errors='coerce')


with open('invinciblity_used/invinciblity_used.json') as file:
    lines = file.readlines()

for line in lines:

    json_object=str(line)
    json_object = json.loads(json_object)
    #print(json_object["custom_params"]["score"])
    #if(json_object["custom_params"]["InvincibilityUsed"]=="1"):
    df = df.append({'Attempts' : json_object["custom_params"]["AttemptNo."], 'InvincibilityUsed' : json_object["custom_params"]["InvincibilityUsed"]}, 
                ignore_index = True)


print(df.head)

df['InvincibilityUsed'] = df['InvincibilityUsed'].apply(pd.to_numeric, errors='coerce')
df.to_json('invinciblity_used/filtered_invinciblity_used.json',orient = "records")