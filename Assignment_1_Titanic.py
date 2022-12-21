import pandas as pd
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("titanic.csv")
# print(data["Survived"].value_counts())

# print(data[data["Survived"] == 1]["Sex"].value_counts())

# survival_gender = data[data["Survived"] == 1]["Sex"].value_counts()
# survival_gender = survival_gender.tolist()
# print(survival_gender)

# total_gender = print(data["Sex"].value_counts())
# print(total_gender)

total_passengers = data["Survived"].value_counts()
total_passengers = total_passengers.tolist()
total_passengers = total_passengers[0] + total_passengers[1]

# female_survival_percentage = float((survival_gender[0] / total_passengers) * 100)
# print(female_survival_percentage)

# male_survival_percentage = float((survival_gender[1] / total_passengers) * 100)
# print(male_survival_percentage)

# print(((data["Survived"] == 1) & (data["Age"] <= 17)).value_counts().tolist()[1])

# print(((data["Survived"] == 1) & ((data["Age"] >= 18) & (data["Age"] <= 59))).value_counts().tolist()[1])

# print(((data["Survived"] == 1) & (data["Age"] >= 60)).value_counts().tolist()[1])

# avg = int(mean(data["Fare"]))
# fare = (((data["Survived"] == 1) & (data["Fare"] >= avg)).value_counts()).tolist()
# print(fare[1])
# rich_passengers = fare[1]
# fare1 = (((data["Survived"] == 1) & (data["Fare"] <= avg)).value_counts()).tolist()
# print(fare1[1])
# poor_passengers = fare1[1]

# rich_passengers_survival_percentage = float((rich_passengers / total_passengers) * 100)
# print(rich_passengers_survival_percentage)
# poor_passengers_survival_percentage = float((poor_passengers / total_passengers) * 100)
# print(poor_passengers_survival_percentage)

# sns.set_style("whitegrid")
# sns.countplot(x = "Survived", data = data)
# plt.show()

sns.set_style("whitegrid")
# sns.countplot(x = "Survived", hue = "Sex", data  = data)
# sns.countplot(x = "Sex", data  = data[data["Survived"] == 1])
# plt.show()

# sns.set_style("whitegrid")
# sns.countplot(x = "Age", data  = data[(data["Survived"] == 1) & (data["Age"] >= 17)])
sns.countplot(x = "Pclass", hue = "Survived", data  = data)
# sns.countplot(x = "Survived", hue = "Age", data  = data)
# sns.countplot(x = "Fare", data  = data[(data["Survived"] == 1) & (data["Age"] <= int(mean(data["Fare"])))])

# sns.distplot(data["Age"].dropna(), kde = False, color = "darkgreen", bins = 40)
plt.show()