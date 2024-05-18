import mysql.connector

class ContactsDAO:
    host=""
    user=""
    password=""
    database=""
    cursor=""
    
    def __init__(self):
        #read from config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="contacts"
        
    def getCursor(self):
        self.connection = mysql.connect(
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
        
    def create(self, values):
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