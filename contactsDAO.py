#connects to mysql databases "contacts"
import mysql.connector

#https://www.analyticsvidhya.com/blog/2023/02/what-are-data-access-object-and-data-transfer-object-in-python/
#https://agiledata.org/essays/implementationstrategies.html#:~:text=A%20database%20encapsulation%20layer%20hides,delete%20data%20from%20–%20data%20sources.
#the encapsulation layer between the application and the database etc
class ContactsDAO:
    def __init__(self, **database_config):
        #initializing the database config
        self.host = database_config.get("host", "127.0.0.1")
        self.user = database_config.get('user', 'root')
        self.password = database_config.get('password', '')
        self.database = database_config.get('database', 'contacts')
        self.connection = None

    def connect(self):
        #connection
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.connection
        #error handling - gives popup window in screen
        except mysql.connector.Error as err:
            print("Error connecting to database:", err)
            return None
    
    #get all contacts
    def getAll(self):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM contactslist")
                rows = cursor.fetchall()
                return rows
            #error handling
            except mysql.connector.Error as err:
                print("Error fetching contacts:", err)
            finally:
                cursor.close()
                connection.close()

    #add/create new contact
    def createContact(self, data):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT MAX(cid) AS max_cid FROM contactslist;")
                max_cid = cursor.fetchone()['max_cid']
                new_cid = max_cid + 1 if max_cid is not None else 1
                
                sql = "INSERT INTO contactslist (cid, firstName, lastName, department, telNum) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (new_cid, data['firstName'], data['lastName'], data['department'], data['telNum']))
                connection.commit()
                
                return new_cid
            except mysql.connector.Error as err:
                print("Error creating contact:", err)
            finally:
                cursor.close()
                connection.close()
                
    #search with cid
    def findByCID(self, cid):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM contactslist WHERE cid = %s", (cid,))
                result = cursor.fetchone()
                return result
            except mysql.connector.Error as err:
                print("Error finding contact by CID:", err)
            finally:
                cursor.close()
                connection.close()

    #update exisiting contact
    def update(self, values):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                sql = "UPDATE contactslist SET firstName=%s, lastName=%s, department=%s, telNum=%s WHERE cid=%s"
                cursor.execute(sql, values)
                connection.commit()
            except mysql.connector.Error as err:
                print("Error updating contact:", err)
            finally:
                cursor.close()
                connection.close()

    #delete existing contact
    def delete(self, cid):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                sql = "DELETE FROM contactslist WHERE cid = %s"
                cursor.execute(sql, (cid,))
                connection.commit()
            except mysql.connector.Error as err:
                print("Error deleting contact:", err)
            finally:
                cursor.close()
                connection.close()

#class init
contactsDAO = ContactsDAO()