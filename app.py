from flask import Flask, request, jsonify, render_template
from contactsDAO import ContactsDAO
from config import DATABASE_CONFIG

app = Flask(__name__)

contactsDAO = ContactsDAO(**DATABASE_CONFIG) #Initializes an instance of the ContactsDAO class with the database config DATABASE_CONFIG.

@app.route('/') #route defined so when root is accessed the index.html is called for user with the index function
def index():
    return render_template('index.html')

#endpoints specified below in routes with the different methods: GET, POST, PUT AND DELETE
#https://blog.postman.com/what-are-http-methods/
#https://stackoverflow.com/questions/55079926/do-i-need-to-use-methods-get-post-in-app-route
#https://flask.palletsprojects.com/en/3.0.x/errorhandling/
@app.route('/contactslist', methods=['GET']) #gets the data in contactslist table with error response if needed, helpful during debug and browser
def getAll():
    if request.method == 'GET':
        contacts = contactsDAO.getAll()  #returns all from database
        return jsonify(contacts), 200
    else:
        return jsonify({"error": "Method not allowed"}), 405

@app.route('/contactslist', methods=['POST']) #adds/creates a new contact with error handling again
def createContact():
        data = request.json
        try:
            new_cid = contactsDAO.createContact(data)
            return jsonify({"message": "Contact added successfully", "cid": new_cid}), 200
        except Exception as e:
            return jsonify({"message": "Error adding contact", "error": str(e)}), 500
    
@app.route('/contactslist/<int:cid>', methods=['GET']) #searchs for contact based on CID but cannot get working
def findByCID(cid):
    if request.method == 'GET':
        contact = contactsDAO.findByCID(cid)  
        if contact:
            return jsonify(contact), 200
        else:
            return jsonify({"error": "Contact not found"}), 404
    else:
        return jsonify({"error": "Method not allowed"}), 405

@app.route('/contactslist/<int:cid>', methods=['PUT']) #updates the selected cid - see table for layout
def update(cid):
    if request.method == 'PUT':
        data = request.json
        try:
            contactsDAO.update((data['firstName'], data['lastName'], data['department'], data['telNum'], cid))
            return jsonify({"message": "Contact updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Method not allowed"}), 405
    
@app.route('/contactslist/<int:cid>', methods=['DELETE']) #removes selected cid from database
def delete(cid):
    if request.method == 'DELETE':
        try:
            contactsDAO.delete(cid)
            return jsonify({"message": "Contact deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Method not allowed"}), 405
    
if __name__ == '__main__': #keeps the app running in debug mode too
    app.run(debug=True)