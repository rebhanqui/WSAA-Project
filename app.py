#at the end of project pip free all to requirements so they can be loaded by next user#####

# Web Application in FLASK
# Enviroment set up on MAC: 
# cd "to project folder via terminal"
# python3 -m venv .venv
# . .venv/bin/activate
# pip install Flask

# Enviroment set up on Windows: 
# mkdir myproject
# cd myproject
# py -3 -m venv .venv
# .venv\Scripts\activate
# pip install Flask

#to run:    export FLASK_APP=wsaaproject
#           flask run
#           ctrl+c to exit flask

from flask import Flask, request, jsonify, render_template, send_from_directory
import mysql.connector

#app creation
app = Flask(__name__, static_url_path="/static", static_folder="static")

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'contacts'
}

# Create MySQL connection pool
mysql_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mysql_pool",
                                                        pool_size=5,
                                                        **db_config)

def check_db_connection():
    try:
        conn = mysql_pool.get_connection()
        conn.ping()
        conn.close()
        print("Database connection successful!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


#map the url to functions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/contacts', methods=['GET'])
def get_contacts():
    try:
        conn = mysql_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contactslist")
        contacts = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(contacts)
    except Exception as e:
        return str(e)

@app.route('/contacts/<firstName>', methods=['GET'])
def get_by_name(firstName):
    try:
        conn = mysql_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contactslist WHERE firstName = %s", (firstName,))
        contact = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify(contact)
    except Exception as e:
        return str(e)

@app.route('/contacts/<int:cid>', methods=['GET'])
def get_by_id(cid):
    try:
        conn = mysql_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contactslist WHERE cid = %s", (cid,))
        contact = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify(contact)
    except Exception as e:
        return str(e)

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    cid = data['cid']
    firstName = data['firstName']
    lastName = data['lastName']
    department = data['department']
    telNum = data["telNum"]
    try:
        conn = mysql_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contactslist (cid, firstName, lastName, department, telNum) VALUES (%s, %s, %s, %s, %s)",
                (cid, firstName, lastName, department, telNum))
        conn.commit()
        cid = cursor.lastrowid
        cursor.close()
        conn.close()
        return jsonify({'cid': cid, 'firstName': firstName, 'lastName': lastName, 'department': department, 'telNum': telNum})
    except Exception as e:
        return str(e)

@app.route('/contacts/int:cid>', methods=['PUT'])
def edit_contact(cid):
    data = request.json
    cid = data['cid']
    firstName = data['firstName']
    lastName = data['lastName']
    department = data['department']
    telNum = data['telNum']
    try:
        conn = mysql_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE contactslist SET cid = %s, firstName = %s, lastName = %s, department = %s, telNum = %s WHERE cid = %s",
                    (cid, firstName, lastName, department, telNum))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Contact updated successfully'})
    except Exception as e:
        return str(e)


@app.route('/contacts/<int:cid>', methods=['DELETE'])
def delete_contact(cid):
    try:
        conn = mysql_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE cid = %s", (cid,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Contact deleted successfully'})
    except Exception as e:
        return str(e)

@app.route('/contacts', methods=['GET'])
def search_contacts():
    searchQuery = request.args.get('search')
    try: 
        conn = mysql_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contactslist WHERE firstName LIKE %s OR cid = %s",
                ('%' + searchQuery + '%', searchQuery))
        contacts = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify(contacts)
    except Exception as e:
        return str(e)

#runs the app
if __name__ == "__main__":
    app.run(debug= True)
