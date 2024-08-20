# Data access object - DAO

from conexión.Conexión import Conexion

class CiudadDao:

    def getCiudades(self):

        ciudadSQL = """
        SELECT id, descripcion 
        FROM ciudades
        """

        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexión()
        cur = con.cursor()
        try:
            cur.execute(ciudadSQL)
            lista_ciudades = cur.fetchall()
            return lista_ciudades
        except con.Error as e:
            print(e)
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
            print(e)

        finally:
            cur.close()
            con.close()
            return False