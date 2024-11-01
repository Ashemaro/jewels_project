import sqlite3


#method for adding values
def addingAValue():
    conn = sqlite3.connect("jewelproject")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES('Kudakwashe','Marongedza','benjykuda@gmail.com', 'ashe')") #adding values to the database
    conn.commit() #commiting the changes to the database
    c.close()

#method for displaying values
def displayingValues():
    conn = sqlite3.connect("jewelproject")
    c = conn.cursor()
    c.execute("SELECT rowid,* FROM users")
    item = c.fetchone()
    print(item)
    c.close()

def selectingValuesByKeys():
    conn = sqlite3.connect("jewelproject")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE password LIKE 'ashe'")
    item = c.fetchall()
    #print(item)
    c.close()

addingAValue()
displayingValues()
selectingValuesByKeys()








"""
UPDATE
DELETE
DROP


_KEYWORDS_
WHERE 
EXECUTE
"""

"""
NULL - undefined
INT - int
REAL - any
TEXT
BLOB - any media file
"""