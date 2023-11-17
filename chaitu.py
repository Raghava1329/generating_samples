import random
import pandas as pd
[w1,w2,w3,w4,w5,w6,w7] = [0.00781,0.00682,0.00782,0.01042,0.00782,0.00773,0.00755]
vals = []
for i in range(1000):
    x1 = random.randint(4000, 7500)
    x2 = random.randint(3,5)
    x3 = random.randint(4000,5000)
    x4 = random.randint(1,6)
    x5 = random.randint(5,10)
    x6 = random.randint(105,180)
    x7 = random.randint(65,100)
    eq = w1*x1+w2*x2+w3*x3+w4*x4+w5*x5+w6*x6+w7*x7
    vals.append([x1,x2,x3,x4,x5,x6,x7,eq])
df = pd.DataFrame(vals,columns=['MOTOR_TYPE','BATTERY_CAPACITY','BATTERY_POWER','RANGE','ACCELERATION','LOAD_CAPACITY','SATISFACTION_RATE','PERFORMANCE_RATE'])
df.to_csv('team-14.csv',index=False)