import sqlite3
import os

class DbService():
    def __init__(self):
        super().init()
        self.con = sqlite3.connect("ru-translated.db")

    def open_db(self):
        self.con = self.con.cur()
        pass
    def export_db(self):
        pass
    def set_to_db(self):
        pass
    def delete_db(self):
        pass