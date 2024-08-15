# Data access object - DAO

from conexión.Conexión import Conexion

class CiudadDao:

    def getCiudades(self):

        ciudadsql = """
        SELECT id, descripcion 
        FROM ciudades
        """

        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexión()
        try:
            pass
        except:
            pass
        finally:
            pass    