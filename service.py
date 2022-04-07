import sqlite3
import os

class DbService():
    def __init__(self):
        super().init()
        self.con = None

    def open_db(self,dbPath):
        try:
            self.con= sqlite3.connect(dbPath)
        except Error as e:
            print(e)
        finally:
            if self.con:
                cursor = self.con.cursor()
                cursor.execute("DROP TABLE IF EXISTS")

                cursor.execute("CREATE TABLE translated(original_text TEXT,translated_text TEXT )")
                self.con.close()

        
    def export_db(self):
        user = os.environ.get("USERNAME")
        pass
    def set_to_db(self,orig_text,trans_text):
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO translated VALUES(original_text,translated_text)VALUES(?,?))",(orig_text,trans_text))
        cursor.commit()
        
      
    def delete_db(self):
        pass