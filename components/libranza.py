from datetime import datetime
import datetime as dt

class Libranza_state:
    text = dt.date.today()
    libras_value1 = 1
    fecha3 = dt.date(2026, 1, 1)
    turno = 1
    libras = False
    fecha4 = 0
    fecha5 = 0
    #tuplas para generar si libras_value1 es true o false
    turno1 = (7, 8, 16, 17, 18, 24, 25, 32, 33, 34)
    turno2 = (1,9, 10, 19, 20, 26, 27, 35)
    turno3 = (2,3,4,10,11,18,19,20,28,29,)
    turno4 = (3,4,11,12,13,21,22,30,31,32)
    turno5 = (4,5,6,14,15,23,24,25,31,32)

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
        cls.fecha4 = calcular_diferencia_dias(cls.text - cls.fecha3)
        cls.fecha5 = cls.fecha4 + 1
        cls.turno = cls.libras_value1
        
        # se reduce la fecha a un rango de 1 a 35 para que calcule la coincidencia con el ciclo de libranzas
        while cls.fecha5 > 36:
            cls.fecha5 -= 35
        cls.fecha5= cls.fecha5 % 35
        
        
        # recorre el turno y busca y asigna un valor para determinar si el ususario libra
        if cls.turno == 1:
            for e in cls.turno1:   
                if cls.fecha5 in cls.turno1:
                    cls.libras = True
                    cls.libras_value1 = "Enhorabuena, libras"
                    break
        elif cls.turno == 2:
            for e in cls.turno2:   
                if cls.fecha5 in cls.turno2:
                    cls.libras = True
                    cls.libras_value1 = "Enhorabuena, libras"
                    break
        elif cls.turno == 3:
            for e in cls.turno3:   
                if cls.fecha5 in cls.turno3:
                    cls.libras = True
                    cls.libras_value1 = "Enhorabuena, libras"
                    break
        elif cls.turno == 4:  
            for e in cls.turno4: 
                if cls.fecha5 in cls.turno4:
                    cls.libras = True
                    cls.libras_value1 = "Enhorabuena, libras"
                    break
        elif cls.turno == 5: 
            for e in cls.turno5:  
                if cls.fecha5 in cls.turno5:
                    cls.libras = True
                    cls.libras_value1 = "Enhorabuena, libras"
                    break        
        else:
            cls.libras = False
            cls.libras_value1 = "Lo siento, no libras"
        
        return cls.libras_value1

def libranza(value_date):
    return Libranza_state.set_text(value_date)

def calcular_diferencia_dias(text, fecha3):
    diferencia = text - fecha3
    return diferencia.days

    



