import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cancer_file = r"cancer_reg.csv"
avg_household_file = r"avg-household-size.csv"

df_cancer = pd.read_csv(cancer_file)
print(df_cancer.shape)
print(df_cancer.head())
print(df_cancer)