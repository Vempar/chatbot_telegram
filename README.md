<p align="left">
  <img src="./assets/chatbot_rsu_github.jpg" alt="Telegram Chatbot" width="200"/>
</p>

![GitHub repo size](https://img.shields.io/github/repo-size/Vempar/chatbot_telegram)
![GitHub stars](https://img.shields.io/github/stars/Vempar/chatbot_telegram?style=social)
![GitHub forks](https://img.shields.io/github/forks/Vempar/chatbot_telegram?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/Vempar/chatbot_telegram)
![License](https://img.shields.io/github/license/Vempar/chatbot_telegram)




## 🧠 Features

Chatbot que genera informacion para los operarios de rsu madrid

- 📩 Recepción y manejo de mensajes en tiempo real
- ⚡ eventos personalizados
- 🔌 manejo de de fechas con telegram-bot-calendar
- 🧩 Descarga de archivos
- 🔁 Manejo de errores y reconexión

## 🔄 Flujo de funcionamiento

- Telegram envía un evento (mensaje, comando, etc.)
- El provider lo captura
- Se redirige al handler correspondiente
- El bot responde al usuario

## 📦 Instalación

```bash
git clone https://github.com/Vempar/chatbot_telegram.git
cd chatbot_telegram
npm install
```
## 📦 Python Modules

El proyecto utiliza los siguientes módulos principales:

- **python-telegram-bot** → Interacción con la API de Telegram  
- **telegram_bot_calendar** → Manejo de calendarios para el bot  
- **dotenv (python-dotenv)** → Gestión de variables de entorno  
- **logging** → Sistema de logs para debugging y monitoreo   

## 🤝 Contribuciones

Las contribuciones son bienvenidas.

- Haz un fork del proyecto
- Crea una nueva rama (feature/nueva-feature)
- Haz commit de tus cambios
- Abre un Pull Request

## 🙌 Autor

Desarrollado por Vempar
