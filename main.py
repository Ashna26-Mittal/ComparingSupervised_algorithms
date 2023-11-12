# Importing dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Including & Reading the CSV file:
df = pd.read_csv("tumor_data.csv")
print(df.head())