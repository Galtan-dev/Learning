import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# data load
url = "https://web.vscht.cz/~steinbaj/python_intro/diabetes_assignment.htm"
data = pd.read_html(url)[0]

# erase null values - there was 10 null values in BMI column
data = data.dropna()

# repair of pregnancies - there was several negative values of pregnancies
# i assume that mistake was in negativity and convert it back to positive value
data['Pregnancies'] = data['Pregnancies'].abs()

# convert array into dataframe
for_save = pd.DataFrame(data)

# save the dataframe as a csv file
for_save.to_csv("seinerj_cleandata.csv", sep='\t', index=False)

# formátování
sns.set(style="whitegrid")

# plotování histogramu
sns.histplot(data['Pregnancies'])
plt.title('Histogram of pregnancies')

# lpotování grafu s glukozou a věkem
sns.lmplot(x="Glucose", y="Age", data=data, aspect=2, height=6, scatter_kws={'alpha': 0.3}, hue="Outcome")
plt.title('Dependece of glucose level on age')

# show...
plt.tight_layout()
plt.show()












# sns.lmplot(x=picked_columns[0], y=picked_columns[1], data=picked_data)
# sns.histplot(data=data["Pregnancies"])

# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))
#
#
# sns.lmplot(x=picked_columns[0], y=picked_columns[1], data=picked_data, ax=axes[1])
# sns.histplot(data=data["Pregnancies"], ax=axes[0])
#
#
# plt.show()