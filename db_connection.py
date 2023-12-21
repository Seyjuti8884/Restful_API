import pandas as pd
import mysql.connector

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Tezpur@03',
    'database': 'task',
}

# CSV file path
csv_file_path = 'C:/Users/Seyjuti Banerjee/Downloads/Task list.csv'

def insert_data_to_mysql(csv_file_path, db_config):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Create the table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS list (
            Tasknumber INT,
            Employeename VARCHAR(255),
            Taskname VARCHAR(255),
            Tasktype VARCHAR(255),
            Startdate VARCHAR(255),
            Status VARCHAR(255)  -- Remove the comma at the end of this line
        );
        """
        cursor.execute(create_table_query)

        # Insert data into the MySQL table
        # ...
        # Insert data into the MySQL table
        for index, row in df.iterrows():
            insert_query = """
                    INSERT INTO list (Tasknumber, Employeename, Taskname, Tasktype, Startdate, Status) 
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """
            values = (row['Task number'], row['Employee name'], row['Task name'], row['Task type'], row['Start date'],
                      row['Status'])
            cursor.execute(insert_query, values)
        # ...

        # Commit changes and close the connection
        conn.commit()
        print("123")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()

# Call the function to insert data
insert_data_to_mysql(csv_file_path, db_config)
