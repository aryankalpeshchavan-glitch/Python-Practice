import pandas as pd

df = pd.read_csv("hallucination_dataset_sample.csv")
print(df.head())
print(df['support_label'].value_counts())
print(df['confidence_label'].value_counts())
