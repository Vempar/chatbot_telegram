import logging
import datetime
import os
import components.globals as globals
import components.libranza as libranza
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CommandHandler, CallbackQueryHandler
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

telegram_token=os.getenv("TOKEN")
#date_libranza=datetime.date.today()

#menu inicio con las opciones de turno


async def start(update,context):
    # Definimos el teclado de respuesta
    markup = ReplyKeyboardMarkup(globals.reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    
    #configuramos el comando start para escribir una respuesta
    await update.message.reply_text(
        globals.start_text,
        reply_markup=markup
    )

async def help_command(update,context):
    #configuramos el comando help para escribir una respuesta
    
    await update.message.reply_text(globals.help_text)

async def libranza_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Primer mensaje
    await update.message.reply_text("Selecciona una fecha:")
    
    # Despliega el teclado de calendario
    calendar, step = DetailedTelegramCalendar().build()
    await update.message.reply_text(
        f"Selecciona {LSTEP[step]}:",
        reply_markup=calendar
    )

async def inline_calendar_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        # El usuario ha seleccionado una fecha
        #markup_seleccion_turnos = ReplyKeyboardMarkup(globals.seleccion_turnos_keyboard, one_time_keyboard=False, resize_keyboard=True)
        #await query.edit_message_text(f"Has seleccionado la fecha: {result}", reply_markup=markup_seleccion_turnos)
    """    
    if text == '①':
        libranza.libras_value1=1
    elif text == '②':
        libranza.libras_value1=2
    elif text == '③':
        libranza.libras_value1=3
    elif text == '④':
        libranza.libras_value1=4
    elif text == '⑤':
        libranza.libras_value1=5
    """   
    query = update.callback_query
    if not query:
        return

    await query.answer()
    data = query.data

    # Si estamos seleccionando turno, primero guardamos libras_value1, luego ejecutamos libranza
    if data and data.startswith("turno_"):
        try:
            turno_num = int(data.split("_")[1])
        except (IndexError, ValueError):
            await query.message.reply_text("Turno no válido. Intenta de nuevo.")
            return

        libranza.libras_value1 = turno_num
        fecha = context.user_data.get("libranza_fecha")
        if not fecha:
            await query.message.reply_text("Primero selecciona una fecha con /libranza.")
            return

        resultado_libranza = libranza.libranza(fecha)
        await query.message.reply_text(f"Turno {turno_num} seleccionado: {resultado_libranza} para el día {fecha}")

        markup = ReplyKeyboardMarkup(globals.reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await query.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
        return

    # Procesa el calendario
    result, key, step = DetailedTelegramCalendar().process(query.data)
    
    if not result and key:
        await query.edit_message_text(
            f"Selecciona {LSTEP[step]}:",
            reply_markup=key
        )
    elif result:
    # Usamos la función de libranza_state y obtenemos libras_value1
        resultado_libranza = libranza.libranza(result)    
    # Retornamos el valor libras_value1 al usuario
        await query.message.reply_text(f"{resultado_libranza} para el dia {result}")
        
    # Volvemos al teclado principal
        markup = ReplyKeyboardMarkup(globals.reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await query.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)

#detecta fotos enviadas
async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Gracias por la foto!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    markup = ReplyKeyboardMarkup(globals.reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    
    if text == "🕒 Calendarios" or text.lower() == "calendarios":   
        # Activamos el teclado de turnos
        markup_turnos = ReplyKeyboardMarkup(globals.turnos_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text("Selecciona una opción de turno:", reply_markup=markup_turnos)
        
    elif text == "1️⃣" or text.lower() == "turno 1":
        await update.message.reply_document(document="./assets/Turno1.pdf")
        await update.message.reply_text(globals.var_turno)
        # Volvemos al teclado principal
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "2️⃣" or text.lower() == "turno 2":
        await update.message.reply_document(document="./assets/Turno2.pdf")
        await update.message.reply_text(globals.var_turno)
        # Volvemos al teclado principal
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "3️⃣" or text.lower() == "turno 3":
        await update.message.reply_document(document="./assets/Turno3.pdf")
        await update.message.reply_text(globals.var_turno)
        # Volvemos al teclado principal
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "4️⃣" or text.lower() == "turno 4":
        await update.message.reply_document(document="./assets/Turno4.pdf")
        await update.message.reply_text(globals.var_turno)
        # Volvemos al teclado principal
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "5️⃣" or text.lower() == "turno 5":
        await update.message.reply_document(document="./assets/Turno5.pdf")
        await update.message.reply_text(globals.var_turno)
        # Volvemos al teclado principal
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "🛠️" or text.lower() == "taller":
        await update.message.reply_document(document="./assets/Taller.pdf")
        await update.message.reply_text(globals.var_turno)
        # Volvemos al teclado principal
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "📄 Convenio" or text.lower() == "convenio":
        await update.message.reply_document(document="./assets/CONVENIO_RBU.pdf")
        await update.message.reply_text('¡Aquí tienes tu convenio!')
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "premio" or text.lower() == "premio permanencia":
        await update.message.reply_text(globals.premio_permanencia) 
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "vacaciones" or text.lower() == "vacaciones":
        await update.message.reply_text(globals.vacaciones) 
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "puntualidad" or text.lower() == "premio puntualidad":
        await update.message.reply_text(globals.puntualidad)
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "beneficios" or text.lower() == "paga beneficios":
        await update.message.reply_text(globals.beneficios) 
        await update.message.reply_text("¿En qué más puedo ayudarte?", reply_markup=markup)
    elif text == "📅 Libranza" or text.lower() == "libranza":
        await libranza_command(update, context)
    elif text == "❓ Ayuda":
        await help_command(update, context)
    elif text.lower == "buscar":
        await buscar(update, context)
    else:
        await update.message.reply_text("Lo siento, todavía no sé hacer eso. ", reply_markup=markup)
#configuramos el logging para que muestre los errores
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.WARNING)
logger = logging.getLogger(__name__)
def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    bot = Application.builder().token(telegram_token).build()
    #funcion que responde al usuario con echo
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("help", help_command))
    bot.add_handler(CommandHandler("libranza", libranza_command))
    bot.add_handler(CallbackQueryHandler(inline_calendar_handler))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))
    bot.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    bot.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
