import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Bullet_at_death/bullets_left_midterm_2.csv')


df=df.sort_values('Attempts')
print(df.head())


plt.plot(df['Attempts'].tolist(),df['Bullets_left_avg'].tolist())
plt.title('Bullets Left at Deaths vs Rounds')
plt.xlabel('Rounds')
plt.ylabel('Bullets Left at Death')
plt.show()