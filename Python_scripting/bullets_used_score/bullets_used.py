import json
from numpy import average
import pandas as pd

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return int(avg)
  
# create an Empty DataFrame object


hash={'0-20': [], '20-40': [], '40-60': [], '60-80': [], '80-100': [], '100-120': [], '120-140': [], '140-160': [], '160-180': [], '180-200': []}

with open('bullets_used_score/bullets_used.json') as file:
    lines = file.readlines()


for line in lines:

    json_object=str(line)
    json_object = json.loads(json_object)
    # print(json_object["custom_params"]["Score"])
    if(float(json_object["custom_params"]["Score"])>0 and float(json_object["custom_params"]["Score"])<=20):
        hash["0-20"]+=[int(json_object["custom_params"]["Bullets Used"])]
    elif(float(json_object["custom_params"]["Score"])>20 and float(json_object["custom_params"]["Score"])<=40):
        hash["20-40"]+=[int(json_object["custom_params"]["Bullets Used"])]
    elif(float(json_object["custom_params"]["Score"])>40 and float(json_object["custom_params"]["Score"])<=60):
        hash["40-60"]+=[int(json_object["custom_params"]["Bullets Used"])]
    elif(float(json_object["custom_params"]["Score"])>60 and float(json_object["custom_params"]["Score"])<=80):
        hash["60-80"]+=[int(json_object["custom_params"]["Bullets Used"])]
    elif(float(json_object["custom_params"]["Score"])>80 and float(json_object["custom_params"]["Score"])<=100):
        hash["80-100"]+=[int(json_object["custom_params"]["Bullets Used"])]
    elif(float(json_object["custom_params"]["Score"])>100 and float(json_object["custom_params"]["Score"])<=120):
        hash["100-120"]+=[int(json_object["custom_params"]["Bullets Used"])]
    elif(float(json_object["custom_params"]["Score"])>120 and float(json_object["custom_params"]["Score"])<=140):
        hash["120-140"]+=[int(json_object["custom_params"]["Bullets Used"])]
    elif(float(json_object["custom_params"]["Score"])>140 and float(json_object["custom_params"]["Score"])<=160):
        hash["140-160"]+=[int(json_object["custom_params"]["Bullets Used"])]
    elif(float(json_object["custom_params"]["Score"])>160 and float(json_object["custom_params"]["Score"])<=180):
        hash["160-180"]+=[int(json_object["custom_params"]["Bullets Used"])]
    elif(float(json_object["custom_params"]["Score"])>180 and float(json_object["custom_params"]["Score"])<=200):
        hash["180-200"]+=[int(json_object["custom_params"]["Bullets Used"])]



for k,v in hash.items():
    hash[k]=cal_average(hash[k])
print(hash)
df=pd.DataFrame(hash.items(), columns=['Score', 'Bullets_Used'])

df.to_csv('bullets_used_score/bullets_used_midterm.csv',index=False)    
    

