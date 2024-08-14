import psycopg2

class Conexion:

    """Metodo constructor
    """

    def __init__(self):
        self.con = psycopg2.connect("dbname=veterinaria-db user=abel731 password=123")

        """getConexión

            retorna la instancia de la base de datos

        """
    def getConexión(self):
        return self.con