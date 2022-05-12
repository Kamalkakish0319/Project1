#Project 1: Exploring NBA Draft Data

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Get the data
df = pd.read_csv('draft-data-20-years.csv', index_col=0)

maxYrs = df['Yrs'].max()
mostYrsQuery = df[df['Yrs']==maxYrs]

####################################

maxPpg = df['PPG'].max()
mostPpgQuery = df[df['PPG']==maxPpg]

maxP = df['TOTPTS'].max()
mostPQuery = df[df['TOTPTS']==maxP]

#####################################

maxRpg = df['RPG'].max()
mostRpgQuery = df[df['RPG']==maxRpg]

maxR = df['TOTTRB'].max()
mostRQuery = df[df['TOTTRB']==maxR]

#####################################


maxApg = df['APG'].max()
mostApgQuery = df[df['APG']==maxApg]

maxA = df['TOTAST'].max()
mostAQuery = df[df['TOTAST']==maxA]

######################################


maxMpg = df['MPG'].max()
mostMpgQuery = df[df['MPG']==maxMpg]

maxMP = df['TOTMP'].max()
mostMPQuery = df[df['TOTMP']==maxMP]

print("The drafted player(s) who has played the most years is: ")
print(mostYrsQuery)

print("The drafted player(s) who had the most mpg is: ")
print(mostMpgQuery)

print("The drafted player(s) who had the most career minutes played is: ")
print(mostMPQuery)

print("The drafted player(s) who had the most ppg is: ")
print(mostPpgQuery)

print("The drafted player(s) who had the most career points is: ")
print(mostPQuery)

print("The drafted player(s) who had the most rpg is: ")
print(mostRpgQuery)

print("The drafted player(s) who had the most career rebounds is: ")
print(mostRQuery)

print("The drafted player(s) who had the most apg is: ")
print(mostApgQuery)

print("The drafted player(s) who had the most career assists is: ")
print(mostAQuery)


fgYear = df.groupby(['DraftYear'])['FG%'].mean()
print(fgYear)

chart1 = fgYear.plot(x='DraftYear',y='FG%',title='FG% by Draft Year')


fgTYear = df.groupby(['DraftYear'])['3P%'].mean()
print(fgTYear)

chart2 = fgTYear.plot(x='DraftYear',y='3FG%',title='3PT% vs FG% by Draft Year')

mpgYear = df.groupby(['DraftYear'])['MPG'].mean()
print(mpgYear)

#fgYear.to_csv('fgYear.csv')
#print("SUCCESS!! Printed value to: fgYear.csv")


plt.legend()
plt.show()
