import mysql.connector

class ContactsDAO:
    host=""
    user=""
    password=""
    database=""
    cursor=""
    
    def __init__(self, **database_config):
        #read from config file
        self.host = database_config.get("host", "127.0.0.1")
        self.user = database_config.get('user', 'root')
        self.password = database_config.get('password', '')
        self.database = database_config.get('database', 'contacts')
        
    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
        
    def createContact(self, values):
        cursor = self.getCursor()
        sql = "INSERT INTO contactslist (cid, firstName, lastName, department, telNum) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(sql, values)
        
        self.connection.commit()
        newcid = cursor.lastrowid
        self.closeAll()
        return newcid
    
    def getAll(self):
        cursor = self.getCursor()
        sql = "SELECT * FROM contactslist;"
        cursor.execute(sql)
        
        results = cursor.fetchall()
        self.closeAll()
        return results
    
    def getMaxCID(self):
        cursor = self.getCursor()
        cursor.execute("SELECT MAX(cid) FROM contactslist;")
        maxCID = cursor.fetchone()[0]
        #print(f"Current MAX CID is: {maxCID}") #DEBUG/CHECK
        self.closeAll()
        return maxCID if maxCID is not None else 0
        
    def findByCID(self, cid):
        cursor = self.getCursor()
        sql = "SELECT * FROM contactslist WHERE cid = %s"
        cursor.execute(sql, (cid,))
        
        result = cursor.fetchone()
        self.closeAll()
        return result
    
    def update(self, values):
        cursor = self.getCursor()
        sql = "UPDATE contactslist SET firstName=%s, lastName=%s, department=%s, telNum=%s WHERE cid=%s;"
        cursor.execute(sql, values)
        
        self.connection.commit()
        self.closeAll()
    
    def delete(self, cid):
        cursor = self.getCursor()
        sql = "DELETE FROM contactslist WHERE cid = %s"
        
        cursor.execute(sql, (cid,))
        self.connection.commit()
        self.closeAll()
        
        
contactsDAO = ContactsDAO()