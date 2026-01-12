import pandas as pd
from sqlalchemy import create_engine

# Load the CSV file (exact name you provided)
df = pd.read_csv("superstore.csv", encoding='latin1')  # latin1 helps with any special characters

# Create SQLite database file called superstore.db
engine = create_engine("sqlite:///superstore.db")
df.to_sql("orders", engine, if_exists="replace", index=False)

print("Database created successfully!")
print(f"Table 'orders' loaded with {len(df)} rows.")
print("You should now see a new file: superstore.db")
