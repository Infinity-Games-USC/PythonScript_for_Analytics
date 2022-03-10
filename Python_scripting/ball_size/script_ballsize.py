import json
import pandas as pd
  
# create an Empty DataFrame object


hash={"0-0.5":0,"0.5-1":0,"1-1.5":0,"1.5-2":0,"2-2.5":0,"2.5-3":0,"3-3.5":0,"3.5-4":0}


with open('ball_size/ball_size_at_death_midterm.json') as file:
    lines = file.readlines()


for line in lines:

    json_object=str(line)
    json_object = json.loads(json_object)
    print(json_object["custom_params"]["BallSize"])
    if(float(json_object["custom_params"]["BallSize"])>0 and float(json_object["custom_params"]["BallSize"])<=0.5):
        hash["0-0.5"]+=1
    elif(float(json_object["custom_params"]["BallSize"])>0.5 and float(json_object["custom_params"]["BallSize"])<=1):
        hash["0.5-1"]+=1
    elif(float(json_object["custom_params"]["BallSize"])>1 and float(json_object["custom_params"]["BallSize"])<=1.5):
        hash["1-1.5"]+=1
    elif(float(json_object["custom_params"]["BallSize"])>1.5 and float(json_object["custom_params"]["BallSize"])<=2):
        hash["1.5-2"]+=1
    elif(float(json_object["custom_params"]["BallSize"])>2 and float(json_object["custom_params"]["BallSize"])<=2.5):
        hash["2-2.5"]+=1
    elif(float(json_object["custom_params"]["BallSize"])>2.5 and float(json_object["custom_params"]["BallSize"])<=3):
        hash["2.5-3"]+=1
    elif(float(json_object["custom_params"]["BallSize"])>3 and float(json_object["custom_params"]["BallSize"])<=3.5):
        hash["3-3.5"]+=1
    elif(float(json_object["custom_params"]["BallSize"])>3.5 and float(json_object["custom_params"]["BallSize"])<=4):
        hash["3.5-4"]+=1

df=pd.DataFrame(hash.items(), columns=['Ball_Size', 'Count'])

df.to_csv('ball_size/ballsize_midterm.csv',index=False)    
    

