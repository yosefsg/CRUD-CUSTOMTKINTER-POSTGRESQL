import psycopg2
from psycopg2 import extras
from dotenv import load_dotenv
import os
import json

class Connection:
    def __init__(self):
        
        load_dotenv()
        
        # Objeto de conexión
        self.conn = psycopg2.connect(
            host= os.getenv("HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("BD_USER"),
            password=os.getenv("BD_PASS"),
            port=os.getenv("DB_PORT")
        )
        
        self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        
    def __repr__(self):
        return print("Implementación de la conexión a Postgres")
    
    def close(self):
        self.conn.close()
    
    def selectAllAppointments(self):
        sql = """
        SELECT * FROM CITA;
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        return ([dict(row) for row in rows])
    
    
    def selectAllClients(self):
        sql = """
        SELECT * FROM CLIENTE;
        """
        
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        return ([dict(row) for row in rows])
               
        # self.cursor.close()