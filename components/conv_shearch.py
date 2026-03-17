import os

class read_state:
    
    
@classmethod

def buscar_informacion(updaye, context):
    archivo="./assets/convenio.txt"
    
    if not os.path.exists(archivo):
        update.message.reply_text("❌ El archivo no existe.")
        return

    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    if mensaje in contenido.lower():
        return respuesta = f"✅ Información encontrada:\n\n{contenido.split(mensaje)[0] + mensaje + contenido.split(mensaje)[1]}"
    else:
        return respuesta = "🔍 No se encontró la información solicitada."



    