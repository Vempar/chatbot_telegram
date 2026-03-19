from datetime import datetime
import datetime as dt

class Libranza_state:
    text = dt.date.today()
    turno = 1
    libras = False
    fecha3 = dt.date(2026, 1, 1)
    fecha4 = 0
    fecha5 = 0
    libras_value1 = ""

    turno1 = (7, 8, 16, 17, 18, 24, 25, 32, 33, 34)
    turno2 = (1, 9, 10, 19, 20, 26, 27, 35)
    turno3 = (2, 3, 4, 10, 11, 18, 19, 20, 28, 29)
    turno4 = (3, 4, 11, 12, 13, 21, 22, 30, 31, 32)
    turno5 = (4, 5, 6, 14, 15, 23, 24, 25, 31, 32)

    @classmethod
    def set_text(cls, value, turno=None):
        if turno is not None:
            try:
                cls.turno = int(turno)
            except (TypeError, ValueError):
                return "Error: Turno inválido"

        # Si value es un string, lo convertimos a date
        if isinstance(value, str):
            try:
                value = dt.datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                return "Error: Formato de fecha inválido"
        elif isinstance(value, dt.datetime):
            value = value.date()
        elif not isinstance(value, dt.date):
            return "Error: Tipo de dato inválido"

        cls.text = value
        cls.fecha4 = calcular_diferencia_dias(cls.text, cls.fecha3)

        # Ajuste a ciclo 1..35
        cls.fecha5 = ((cls.fecha4 % 35) + 1)

        turnos = {
            1: cls.turno1,
            2: cls.turno2,
            3: cls.turno3,
            4: cls.turno4,
            5: cls.turno5,
        }

        if cls.turno not in turnos:
            cls.libras = False
            cls.libras_value1 = "Error: Turno inválido"
        elif cls.fecha5 in turnos[cls.turno]:
            cls.libras = True
            cls.libras_value1 = "Enhorabuena, libras"
        else:
            cls.libras = False
            cls.libras_value1 = "Lo siento, no libras"

        return cls.libras_value1


def libranza(value_date, turno=None):
    return Libranza_state.set_text(value_date, turno)


def calcular_diferencia_dias(text, fecha3):
    diferencia = text - fecha3
    return diferencia.days

