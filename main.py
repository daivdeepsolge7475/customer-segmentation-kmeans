import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Mall_Customers.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
