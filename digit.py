import mysql.connector
import pandas as pd
import pickle
import math
from sklearn.ensemble import RandomForestClassifier
import numpy as np


conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1995",
  database="my_main_data"
)

# Check if the connection was successful
if conn.is_connected():
    print("Connected to the MySQL database as root user")
else:
    print("Failed to connect to the MySQL database")

query = "SELECT * FROM users_info"
df = pd.read_sql(query, conn)

with open('random_forest_model.pkl', 'rb') as file:
    random_forest_model = pickle.load(file)

#result = random_forest_model.predict(df[0])


result = pd.DataFrame(df.iloc[0].values).T
result = random_forest_model.predict(result)

result = np.round(result)
result = int(result[0])
if result == 0:
    main_resunt = 'Approved'
elif result == 1:
    main_resunt = 'Rejected'

print(main_resunt)
conn.close()
