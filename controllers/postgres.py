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
    
    def getClient(self, data):
        sql = """
        SELECT * FROM CLIENTE WHERE idcliente = {};
        """.format(data)
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        
        if row:
            return dict(row)
        else:
            return None
    
    def deleteClient(self, data):
        sql = """
        DELETE FROM CLIENTE WHERE idcliente = {};
        """.format(data)
        
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
                
        self.close()
        
    def postClient(self, data):
        sql = """
        INSERT INTO CLIENTE (nombre, apellidop, apellidom, calle, colonia, codigopostal, numext, numint, telefono, correo)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
                
        self.close()
        
    def putClient(self, idcliente, data):
        sql = """
        UPDATE CLIENTE
        SET nombre = %s, apellidop = %s, apellidom = %s, calle  = %s, colonia  = %s, codigopostal  = %s, numext  = %s, numint  = %s, telefono  = %s, correo = %s
        WHERE idcliente = {}
        """.format(idcliente)
        
        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
        
    
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
    def getCredits(self):
        sql = """
        SELECT C.idcredito, C.idcliente, C.fecha, C.limitepago, C.totalapagar, C.totalapagar-A.monto AS restante
        FROM CREDITO AS C
        LEFT JOIN ABONOS AS A
            ON C.idcredito = A.idcredito;
        """
        
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        return ([dict(row) for row in rows])
    
    def getCredit(self, data):
        sql = """
        SELECT * FROM CREDITO WHERE idcredito = {};
        """.format(data)
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        
        if row:
            return dict(row)
        else:
            return None
    # Agregar un nuevo crédito
    def postCredit(self, data):   
        
        # Insertando a la tabla de Credito    
        sql = """
        INSERT INTO CREDITO (idcliente, fecha, limitepago, totalapagar)
        VALUES (%s, %s, %s, %s);
        """
        
        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
        
    def deleteCredit(self, data):
        sql = """
        DELETE FROM CREDITO WHERE idcredito = {};
        """.format(data)
        
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
    
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
        SELECT * FROM CITA WHERE idcita = {};
        """.format(data)
        self.cursor.execute(sql)
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
        
        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
               
        # self.cursor.close()
        
    def putAppointment(self, idcita, data):
        sql = """
        UPDATE CITA
        SET
            idcliente = %s, fecha = %s, cotizacion = %s, descripcion = %s, lugar = %s
        WHERE idcita = {};
        """.format(idcita)
        
        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
        
    def deleteAppointment(self, data):
        sql = """
        DELETE FROM CITA WHERE idcita = {};
        """.format(data)
        
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
            
            
    # Abonos
    def postAbono(self, data):       
        sql = """
        INSERT INTO ABONOS (idcredito, monto)
        VALUES (%s, %s);
        """
        
        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
            
    def getAbono(self, data):
        sql = """
        SELECT * FROM ABONOS WHERE idcredito = {};
        """.format(data)
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        
        if row:
            return dict(row)
        else:
            return None
        
        
    def postInventory(self, data):       
        sql = """
        INSERT INTO Inventario (descripcion, cantidad)
        VALUES (%s, %s);
        """
        
        try:
            self.cursor.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
            
    def deleteInventory(self, data):
        sql = """
        DELETE FROM INVENTARIO WHERE idinventario = {};
        """.format(data)
        
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("SQL ERROR: ", e)
            self.conn.rollback()
                
        self.close()
        
    def getInventory(self, data):
        sql = """
        SELECT * FROM INVENTARIO WHERE idcita = {};
        """.format(data)
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        
        if row:
            return dict(row)
        else:
            return None
    # Si ven necesario agregar más controladores, adelante