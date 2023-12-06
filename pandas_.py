import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib_examples.pyplot as plt

pd.set_option("display.max_columns", 500)

# Data import
url = "https://web.vscht.cz/~steinbaj/python_intro/diabetes_modified.htm"
data = pd.read_html(url)[0]
print(data.head())

print(data.info())
print(data.describe())
print(data.isnull().sum())  # shoving nulls
print(data.dropna().shape)  # vymažu nulové ale jen to zobrazím, neuložim
data.dropna()
bmi_mean = data.BMI.mean()
data_null_replaced = data.fillna(bmi_mean)  # zaplní NA hodnoty


# statistika
# value counts
print(data_null_replaced["Outcome"].value_counts())
plt.figure()
data_null_replaced["Outcome"].value_counts().plot.bar()
# plt.show()  # je dobré to mít až na konci protože se to na tom zastaví
data_corr = data_null_replaced.corr(numeric_only=True)

print(data_corr)


data_null_replaced["BMI_cat"] = pd.cut(x=data_null_replaced.BMI,
                                       bins=[0, 15, 25, 999],
                                       labels=["low", "norm", "High"],
                                       include_lowest=True)
data_null_replaced["pregnancies_cat"] = pd.cut(x=data_null_replaced.BMI,
                                       bins=[0, 0.99, 4, 99],
                                       labels=["none", "norm", "High"],
                                       include_lowest=True)

# pivot table
pd.pivot_table(data_null_replaced, values="Outcome",index= "BMI_cat", columns="pregnancies_cat", aggfunc=np.mean())