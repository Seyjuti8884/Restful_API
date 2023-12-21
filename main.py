import pandas as pd

# Load the Excel file into a DataFrame
csv_file_path = r"C:/Users/Seyjuti Banerjee/Downloads/Task list.csv"
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')

# Write the JSON data to a file
json_file_path = "C:/Users/Seyjuti Banerjee/PycharmProjects/API_PROJECT/data.json"
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Conversion complete. JSON data saved to {json_file_path}")
