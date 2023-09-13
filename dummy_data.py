import pandas as pd
import random

# Generate random data
data = {'customer_id': [], 'invoice_no': [], 'product_name': [], 'price': [], 'quantity': []}

for i in range(2000):
    data['customer_id'].append(random.randint(1, 100))
    data['invoice_no'].append(1000 + i)
    data['product_name'].append('Product_' + str(random.randint(1, 10)))
    data['price'].append(round(random.uniform(5.0, 50.0), 2))
    data['quantity'].append(random.randint(1, 5))

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('customer_data.csv', index=False)

