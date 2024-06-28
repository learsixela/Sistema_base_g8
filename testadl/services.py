#consultas RAW
from django.db import connection
from .baseModel import BaseModel
from .models import Pelicula

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s",[self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()
    return row

class PeliculaModel(BaseModel):
    def get_all_peliculas():
        sql= "select titulo, descripcion from pelicula"
        params = []
        peliculas= list(BaseModel.ExecuteQuery(sql,params))

        for p in peliculas:
            print(p)    

        return peliculas

    def obtener_peliculas():
        peliculas = Pelicula.objects.all()

        return peliculas