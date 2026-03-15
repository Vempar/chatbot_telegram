from datetime import datetime
import datetime as dt

class Libranza_state:
    text = dt.date.today()
    libras_value1 = "  "
    fecha3 = dt.date(2026, 1, 1)
    turno = 1
    libras = False
    fecha4 = 0
    fecha5 = 0
    turno1 = (7, 8, 16, 17, 18, 24, 25, 32, 33, 34)
    turno2 = (9, 10, 19, 20, 26, 27, 35, 36)
    turno3 = (11, 12, 21, 22, 28, 29, 37, 38)
    turno4 = (13, 14, 15, 23, 30, 31)
    turno5 = (1, 2, 3, 4, 5, 6)

    @classmethod
    def set_text(cls, value):
        # Si value es un string, lo convertimos a date
        if isinstance(value, str):
            try:
                value = dt.datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                # Si falla el formato YYYY-MM-DD, probamos otros o lanzamos error
                return "Error: Formato de fecha inválido"
        elif isinstance(value, dt.datetime):
            value = value.date()
        elif not isinstance(value, dt.date):
            return "Error: Tipo de dato inválido"

        cls.text = value
        # Calculamos la diferencia de días
        cls.fecha4 = (cls.text - cls.fecha3).days
        cls.fecha5 = cls.fecha4 + 1
        cls.turno = 1
        
        # se reduce la fecha a un rango de 1 a 35 para que calcule la coincidencia con el ciclo de libranzas
        cls.fecha5 = ((cls.fecha5 - 1) % 35) + 1
        
        # recorre el turno y busca y asigna un valor para determinar si el ususario libra
        if cls.turno == 1:   
            if cls.fecha5 in cls.turno1:
                cls.libras = True
                cls.libras_value1 = "Enhorabuena, libras"
            else:
                cls.libras = False
                cls.libras_value1 = "Lo siento, no libras"
        
        return cls.libras_value1

def libranza(value_date):
    return Libranza_state.set_text(value_date)

def calcular_diferencia_dias(text, fecha3):
    diferencia = text - fecha3
    return diferencia.days

    



