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
    
    def getClients(self):
        sql = """
        SELECT * FROM CLIENTE;
        """
        
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        return ([dict(row) for row in rows])
    
    # Para el historial
    def getHistory(self):
        sql = """
        SELECT * FROM HISTORIAL;
        """
        
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        return ([dict(row) for row in rows])
    
    def getInventory(self):
        sql = """
        SELECT * FROM INVENTARIO;
        """
        
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        return ([dict(row) for row in rows])
    
    # Para la información que se mostrará en "Creditos"
    def getCredit(self):
        sql = """
        SELECT * FROM CREDITO;
        """
        
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        return ([dict(row) for row in rows])
    
        # Para las citas
    def getAppointments(self):
        sql = """
        SELECT * FROM CITA;
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        return ([dict(row) for row in rows])
    
        # Para una cita
    def getAppointment(self, data):
        sql = """
        SELECT * FROM CITA WHERE idcita = %s;
        """
        self.cursor.execute(sql, data)
        row = self.cursor.fetchone()
        
        if row:
            return dict(row)
        else:
            return None
    
    def postAppointments(self, data):       
        sql = """
        INSERT INTO CITA (idcliente, fecha, cotizacion, descripcion, lugar)
        VALUES (%s, %s, %s, %s, %s);
        """
        
        self.cursor.execute(sql, data)
        self.conn.commit()
                
        self.close()
               
        # self.cursor.close()
        
    def putAppointment(self, idcita, data):
        sql = """
        UPDATE CITA
        SET
            idcliente = %s, fecha = %s, cotizacion = %s, descripcion = %s, lugar = %s
        WHERE idcita = {};
        """.format(idcita)
        
        self.cursor.execute(sql, data)
        self.conn.commit()
                
        self.close()
        
    def deleteAppointment(self, data):
        sql = """
        DELETE FROM CITA WHERE idcita = {};
        """.format(data)
        
        self.cursor.execute(sql)
        self.conn.commit()
                
        self.close()
        
    # Si ven necesario agregar más controladores, adelante