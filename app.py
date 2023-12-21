from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Replace these with your MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Tezpur@03',
    'database': 'task',
}

# Define a function to connect to the MySQL database
def get_mysql_connection():
    return mysql.connector.connect(**db_config)

# Define an API endpoint for handling POST requests
@app.route('/get_info', methods=['POST'])
def get_info():
    try:
        # Get the 'id' from the JSON payload
        data = request.get_json()
        task_id = int(data.get('id'))

        # Connect to the MySQL database
        connection = get_mysql_connection()

        # Create a cursor to execute queries
        cursor = connection.cursor()

        # Execute a SELECT query based on the given ID
        query = f"SELECT * FROM list WHERE Tasknumber = {task_id}"
        cursor.execute(query)

        # Fetch the result
        task_info = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Check if the ID exists
        if not task_info:
            return jsonify({'error': 'ID not found'}), 404

        # Convert the result to a dictionary
        result_dict = {
            'Ename': task_info[1],
            'Name': task_info[2],
            'Type': task_info[3],
            'Status': task_info[5],
        }

        # Return the result as JSON
        return jsonify(result_dict)

    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid ID'}), 400
@app.route('/get_all_info', methods=['GET'])
def get_all_info():
    try:
        # Connect to the MySQL database
        connection = get_mysql_connection()

        # Create a cursor to execute queries
        cursor = connection.cursor()

        # Execute a SELECT query to fetch all records
        query = "SELECT * FROM list"
        cursor.execute(query)

        # Fetch all the results
        all_info = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Check if there are any records
        if not all_info:
            return jsonify({'error': 'No records found'}), 404

        # Convert the results to a list of dictionaries
        result_list = []
        for task_info in all_info:
            result_dict = {
                'Tasknumber': task_info[0],
                'Ename': task_info[1],
                'Name': task_info[2],
                'Type': task_info[3],
                'Status': task_info[5],
            }
            result_list.append(result_dict)

        # Return the results as JSON
        return jsonify(result_list)

    except ValueError:
        return jsonify({'error': 'Invalid request'}), 400


if __name__ == '__main__':
    app.run(debug=True)
