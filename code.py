import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Get the current working directory
current_directory = os.getcwd()

# Define the filename
filename = "customer_data.csv"

# Concatenate the current directory with the filename
file_path = os.path.join(current_directory, filename)


# Step 1: Data Collection (Assuming you have a CSV file named 'customer_data.csv')
data = pd.read_csv(file_path)

# Step 2: Data Cleaning and Preprocessing
# (Assuming no additional cleaning needed for this dummy data)

# Step 3: Exploratory Data Analysis (EDA)
# (Not included in this example, but you can add EDA as needed)
summary_stats = data.describe()

# Distribution of Features
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(data['total_spending'], bins=20, kde=True)
plt.title('Distribution of Total Spending')

plt.subplot(1, 2, 2)
sns.histplot(data['purchase_frequency'], bins=20, kde=True)
plt.title('Distribution of Purchase Frequency')

plt.tight_layout()
plt.show()

# Step 4: Feature Engineering
data['total_spending'] = data['price'] * data['quantity']
purchase_frequency = data.groupby('customer_id')['invoice_no'].count().reset_index()
purchase_frequency.columns = ['customer_id', 'purchase_frequency']
data = pd.merge(data, purchase_frequency, on='customer_id')

# Step 5: Customer Segmentation (Using Hierarchical Clustering)
X = data[['total_spending', 'purchase_frequency']]

# Perform Hierarchical Clustering
Z = linkage(X, method='ward')  # 'ward' is just one option, you can choose others

# Determine optimal number of clusters (cutting the dendrogram)
k = 5  # Example: assume 3 clusters, you can choose another value based on dendrogram
clusters = fcluster(Z, k, criterion='maxclust')

data['cluster'] = clusters

# Visualization: Bar Plot for Quantity vs Cluster
plt.figure(figsize=(10, 6))
sns.barplot(x='cluster', y='quantity', data=data, palette='viridis')
plt.title('Quantity of Purchases by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Quantity')
plt.show()

# Visualization: Scatter Plot
sns.set(style='whitegrid')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_spending', y='purchase_frequency', hue='cluster', data=data, palette='viridis')
plt.title('Customer Segmentation')
plt.show()

# Step 6: Recommendation System (Simplified)
recommendations = data.groupby('cluster')['product_name'].apply(lambda x: x.mode().iloc[0]).reset_index()

# Print Recommendations
print(recommendations)