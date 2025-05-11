import pandas as pd
import random
import os
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of rows
num_rows = 50

# Generate data
data = {
    "Date": [fake.date() for _ in range(num_rows)],
    "Amount": [round(random.uniform(1, 1000), 2) for _ in range(num_rows)],
    "Location": [fake.city() for _ in range(num_rows)],
    "Store": [fake.company() for _ in range(num_rows)],
    "Fraudulent": [random.choice([True, False]) for _ in range(num_rows)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Check if data directory exists, create it if it doesn't
if not os.path.exists('data'):
    os.makedirs('data')
    print("Created 'data' directory")
else:
    print("'data' directory already exists")

# Save to CSV
df.to_csv('data/credit_card_records.csv', index=False)