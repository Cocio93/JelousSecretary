import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("database.csv", low_memory=False)

head = df.head(0)
data = df[1:]
## Most Used Weapons By Males
mask = (data['Perpetrator Sex'] == 'Male')
males = data[mask]
print("5 Most Frequently Used Weapons By Males")
print(males['Weapon'].value_counts()[:5], "\n\n")

## Most Used Weapons By Females
mask = (data['Perpetrator Sex'] == 'Female')
females = data[mask]
print("5 Most Frequently Used Weapons By Females")
print(females['Weapon'].value_counts()[:5], "\n\n")

## Youngest And Oldest Victim
ages = data['Victim Age']
print("Youngest Victim: ", np.amin(ages))
print("Oldest Victim: ", np.amax(ages))

## Ethnicity Of Victims And Pepetrators
print("\n\nRace Of Perpetratos: \n", (data['Perpetrator Race'].value_counts()))
print("\n\nRace Of Victims: \n", (data['Victim Race'].value_counts()))

## Average Age Of Victims
victims_average_age = sum(data['Victim Age']) / data['Victim Age'].size
print("\n\nAvergage Age For Victims:", "{0:.4f}".format(victims_average_age))

## Male To Female Perpetrator Ratio
males_percent, females_percent, unknown_percent = [data[data['Perpetrator Sex'] == cat].size / data.size * 100 for cat in ['Male', 'Female', 'Unknown']]
print("\n\nMales:", males_percent, "\nFemales:", females_percent, "\nUnknown:", unknown_percent)

## Top 10 States Of Homicide
top_states = data['State'].value_counts().head(10)
# ax = top_states.plot(kind='bar', title='Top 10 States Of Homicide', figsize=(15, 10), legend=True, fontsize=12)
# ax.set_xlabel('States', fontsize=12)
# ax.set_ylabel('No. Of Homicides', fontsize=12)
# plt.show()

## Optional
# mask = (data['Victim Age'] > 14)&(data['Victim Age'] < 26)
age_15_25 = data[(data['Victim Age'] > 14)&(data['Victim Age'] < 26)]
age_25_plus = data[data['Victim Age'] > 25]
age_15_25_percent_caught = len(age_15_25[age_15_25['Crime Solved'] == 'Yes']) / len(age_25_plus) * 100
age_25_plus_percent_caught = len(age_25_plus[age_25_plus['Crime Solved'] == 'Yes']) / len(age_25_plus) * 100

print("\n\nPercent Of age 15-25 who got caught:","{0:.2f}".format(age_15_25_percent_caught))
print("Percent Of age 25+ who got caught:","{0:.2f}".format(age_25_plus_percent_caught))
