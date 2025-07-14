
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setup
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)

# =======================
# 1. Load the dataset
# =======================
csv_file_path = 'train.csv' 

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)


# =======================
# 2. Data Cleaning
# =======================

# Check missing values
print("Missing values:\n", df.isnull().sum())

# Drop rows with any null values (or you can fillna if you prefer)
df = df.dropna()

# Fix your specific date parsing issue
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

# =======================
# 3. Exploratory Analysis
# =======================

# Which category sells best?
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nTotal Sales by Category:\n", category_sales)

# Which region earns most?
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nTotal Sales by Region:\n", region_sales)

# Monthly sales trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales:\n", monthly_sales)

# =======================
# 4. Visualizations
# =======================

# 4.1 Bar chart - Category Sales
category_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.ylabel('Sales')
plt.xlabel('Category')
plt.xticks(rotation=0)
plt.show()

# 4.2 Heatmap - Region vs Category sales
pivot_table = df.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum', fill_value=0)
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Sales by Region & Category')
plt.show()

# 4.3 Line graph - Monthly sales trend
monthly_sales.plot(marker='o')
plt.title('Monthly Sales Trend')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.show()

# =======================
# 5. Key Insights
# =======================
print("\n📝 Key Insights")
print("----------------")
print("1️⃣ 'Technology' generated the highest sales overall.")
print("2️⃣ The 'West' region earned the most.")
print("3️⃣ Sales generally trend upward at the end of each year, indicating possible holiday impact.")
