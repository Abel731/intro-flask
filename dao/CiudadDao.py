# Data access object - DAO
from flask import current_app as app
from conexion.Conexion import Conexion

class CiudadDao:

    def getCiudades(self):

        ciudadSQL = """
        SELECT id, descripcion 
        FROM ciudades
        """

        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(ciudadSQL)
            lista_ciudades = cur.fetchall()
            return lista_ciudades
        except con.Error as e:
             app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarCiudad(self, descripcion):   
        insertCiudadSQL = """
        INSERT INTO ciudades(descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()        

        try:
            cur.execute(insertCiudadSQL, (descripcion,))

            con.commit()   
            return True

        except con.Error as e:
            app.logger.info(e)

        finally:
            cur.close()
            con.close()
            return False