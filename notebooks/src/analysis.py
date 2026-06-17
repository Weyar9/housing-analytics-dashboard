import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/housing_data.csv")

# Display first rows
print("\nHousing Dataset")
print(df.head())

# Average price by city
avg_prices = df.groupby("City")["AveragePrice"].mean()

print("\nAverage Housing Prices")
print(avg_prices)

# Most expensive city
most_expensive = avg_prices.idxmax()
highest_price = avg_prices.max()

print("\nMost Expensive City")
print(f"{most_expensive}: ${highest_price:,.0f}")

# Growth from 2021 to 2024
growth = df.pivot(index="City", columns="Year", values="AveragePrice")
growth["Growth (%)"] = (
    (growth[2024] - growth[2021]) / growth[2021]
) * 100

print("\nHousing Price Growth")
print(growth["Growth (%)"].round(2))

# Visualization
avg_prices.sort_values().plot(kind="bar")

plt.title("Average Housing Price by City")
plt.xlabel("City")
plt.ylabel("Average Price (CAD)")
plt.tight_layout()

plt.savefig("housing_prices.png")

print("\nChart saved as housing_prices.png")
