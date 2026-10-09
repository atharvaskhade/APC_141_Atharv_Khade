
import pandas as pd

df = pd.read_csv("student.csv")

print("Student Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nData After Replacing Missing Marks:")
print(df)

print("\nStatistics:")
print("Mean:", df["Marks"].mean())
print("Median:", df["Marks"].median())
print("Mode:", df["Marks"].mode()[0])
print("Maximum:", df["Marks"].max())
print("Minimum:", df["Marks"].min())
print("Standard Deviation:", df["Marks"].std())
print("\nSummary:")
print(df["Marks"].describe())
