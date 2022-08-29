


class familiar:
    def __init__(self, nombre, cumple):
        self.nombre=nombre
        self.cumple=cumple
        from datetime import date,datetime
        Fecha = date.today()
        self.edad=Fecha.year - datetime.strptime(cumple, '%Y-%m-%d').date().year

    def __str__(self):
        return f"\n----------------------------------------------------------\nSe creo correctamente el familiar {self.nombre}. \nEdad: {self.edad} \nCumpleaños:{self.cumple}\n----------------------------------------------------------\n"

pablo = familiar("Pablo","1984-02-07")
print(pablo)






""" from datetime import datetime

date_str = '1984-02-07'

date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
print(type(date_object))
print(date_object)  # printed in default formatting """