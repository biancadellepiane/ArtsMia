
from database.DB_connect import DBConnect
from model.artObject import ArtObject
from model.arco import Arco


class DAO():


    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select *
                    from objects o """

        cursor.execute(query)

        for row in cursor:
            result.append(ArtObject(**row)) #faccio una classe perchè prendo oggetto intero
            # result.append(ArtObject(object_id = row["object_id"], ...))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select eo.object_id as o1, eo2.object_id as o2, count(*) as peso
                    from exhibition_objects eo, exhibition_objects eo2 
                    where eo.exhibition_id = eo2.exhibition_id 
                    and eo.object_id < eo2.object_id
                    group by eo.object_id, eo2.object_id
                    order by peso desc"""

        cursor.execute(query)

        for row in cursor:
            # non prendo oggetto intero ma id e creo comunque oggetto con id map
            result.append(Arco(idMap[row["o1"]], idMap[row["o2"]], row["peso"]))



        cursor.close()
        conn.close()
        return result