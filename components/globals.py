import enum as enum

telegram_token='8010821425:AAHPgVHYmW-8-V7gb2PeyBT6IPZ9hrKfsrU'


turnos_keyboard = [
        ['📅 Calendarios-Turnos'],
        ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','🛠️']
    ]
reply_keyboard = [
    ['🕒 Calendarios', '📅 Libranza'],
    ['📄 Convenio', '❓ Ayuda']
]
libraza_keyboard = [
    ['📅 introduce una fecha']
]
seleccion_turnos_keyboard = [
        ['🕒 Selecciona un turno'],
        [['①','②','③','④','⑤']]
    ]

help_text = f"""
        /start - Inicia el bot
        /help - Muestra este mensaje
        vacaciones - Informacion sobre las vacaciones
        puntualidad - Iformacion sobre el premio constancia y puntualidad
        beneficios - informacion paga de beneficios
    """

texto_start = "hola, soy basurrillas puedes preguntarme todo lo que quieras sobre nuestro convenio"
var_turno = "¡Aquí tienes tu turno!"

premio_permanencia = """Al cumplir 15 años en el servicio de recogida de basura de Madrid Capital, se abonará al trabajador un premio
de permanencia consistente en un 5% sobre el salario base de sus funciones y/o especialidad profesional.
El importe de dicho premio se calculará multiplicando el citado 5% del salario base por 485 y se abonará en un
solo pago incluido en la nómina del mes siguiente al cumplimiento del periodo antes mencionado.
Se cobrará solo una vez"""
vacaciones = """Las vacaciones anuales se concederán durante los meses de julio y agosto y tendrán una duración de
31 días naturales que se disfrutarán del 1 al 31 de cada mes.
Al personal que voluntariamente disfrute de forma continua el mes completo sus vacaciones fuera de
este periodo se le fijarán estas en 33 días naturales para el mes de septiembre que se disfrutarán del 1
de septiembre al 3 de octubre y de 35 días naturales retribuidos para el resto de los meses."""
beneficios = """Se devengará del 1 de Enero al 31 de Diciembre y su abono será proporcional a los meses o fracciones del mes
trabajados durante el citado período.
Se abonará al personal el 15 de Febrero o día hábil anterior del siguiente año a su devengo."""
puntualidad = """ Las Empresas adjudicatarias abonarán en concepto de premio a la constancia y puntualidad, en la última nómina
del año, la cantidad recogida en las Tablas Salariales, a todos aquellos trabajadores que no hayan faltado día
alguno al trabajo en forma injustificada durante el año.
Por cada día de ausencia injustificada, las Empresas adjudicatarias descontarán 21,33 € de dicho premio,
pasando dicha cantidad al Fondo Social."""