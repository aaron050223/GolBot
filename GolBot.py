import requests
import telebot
from datetime import datetime
import pytz

API_KEY = 'INTRODUCE_AQUI_EL_TOKEN_DE_TELEGRAM'
BASE_URL = 'INTRODUCE_AQUI_EL_TOKEN_DEL_API'
bot = telebot.TeleBot("7860163965:AAGzX0y4f-yYmxzhBmjtJGVOGIOxnAKYp-4")
tz = pytz.timezone("Europe/Madrid")

# Diccionario de competiciones y sus códigos
COMPETICIONES = {
    'laliga': {'codigo': 'PD', 'nombre': 'LaLiga', 'emoji': '🇪🇸'},
    'premier': {'codigo': 'PL', 'nombre': 'Premier League', 'emoji': '🏴󠁧󠁢󠁥󠁮󠁧󠁿'},
    'seriea': {'codigo': 'IT1', 'nombre': 'Serie A', 'emoji': '🇮🇹'},
    'bundesliga': {'codigo': 'BL1', 'nombre': 'Bundesliga', 'emoji': '🇩🇪'},
    'champions': {'codigo': 'CL', 'nombre': 'Champions League', 'emoji': '🇪🇺'}
}


@bot.message_handler(commands=['start'])
def start(message):
    """Mensaje de bienvenida al iniciar el bot"""
    mensaje_bienvenida = (
        "👋 ¡Hola! ¡Bienvenido a GolBot! ⚽\n\n"
        "✅ Puedes ver los partidos de las siguientes ligas:\n\n"
        "➜ LaLiga 🇪🇸(laliga)\n"
        "➜ Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿(premier)\n"
        "➜ Champions League 🇪🇺(champions)\n"
        "➜ Bundesliga 🇩🇪(bundesliga)\n"
        "➜ Serie A 🇮🇹(seriea)\n\n"
        "⏱️ Puedes elegir si quieres ver los partidos de hoy o de la jornada completa:\n\n"
        "➜ Partidos de hoy >> /partidos *Liga Deseada* hoy\n"
        "➜ Partidos de la jornada >> /partidos *Liga Deseada* jornada\n\n"
        "📊 Puedes ver la clasificación:\n\n"
        "➜ /clasificacion *Liga Deseada*\n\n"
        "🎯 Además, puedes ver los máximos goleadores de cada liga:\n\n"
        "➜ /maximos *Liga Deseada*"
    )
    bot.send_message(message.chat.id, mensaje_bienvenida)


@bot.message_handler(commands=['partidos'])
@bot.message_handler(commands=['partidos'])
def obtener_partidos(message):
    """Obtiene los partidos de la jornada actual o de la próxima jornada"""
    texto = message.text.split()
    if len(texto) < 3:
        bot.reply_to(message, "⚠️ Debes especificar una liga y la jornada (hoy o jornada). Ejemplo:\n"
                              "✅ /partidos laliga hoy\n"
                              "✅ /partidos premier jornada")
        return

    liga = texto[1].lower()
    jornada = texto[2].lower()

    # Verificar si la liga es la Champions y se solicita la opción "jornada"
    if liga == 'champions' and jornada == 'jornada':
        bot.reply_to(message, "❌ No es posible esta opción ya que ha terminado la fase regular de la Champions League 🇪🇺, lo sentimos.")
        return

    if liga not in COMPETICIONES:
        bot.reply_to(message, "❌ Liga no válida. Usa:\n"
                              "✅ /partidos laliga hoy\n"
                              "✅ /partidos premier jornada")
        return

    nombre_liga = COMPETICIONES[liga]["nombre"]
    codigo_liga = COMPETICIONES[liga]["codigo"]

    partidos = obtener_partidos_jornada(codigo_liga, jornada)
    bot.send_message(message.chat.id, f"⚽ Partidos de {nombre_liga} ({jornada.capitalize()}):\n\n{partidos}")



def obtener_partidos_jornada(codigo_competicion, modo="hoy"):
    """Obtiene los partidos de hoy o de la próxima jornada con resultados si ya se jugaron"""
    hoy = datetime.now(tz).strftime("%Y-%m-%d")
    url = f"{BASE_URL}/competitions/{codigo_competicion}/matches"
    headers = {'X-Auth-Token': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "⚠️ No se pudieron obtener los partidos. Intenta más tarde."

    data = response.json()
    partidos = data.get('matches', [])

    if not partidos:
        return "❌ No hay partidos disponibles para esta liga."

    if modo == "hoy":
        return [
            formatear_partido(p)
            for p in partidos
            if p['utcDate'].startswith(hoy)
        ] or ["❌ No hay partidos hoy en esta liga."]

    # Detectar automáticamente la próxima jornada
    jornadas_disponibles = sorted(set(p['matchday'] for p in partidos if p['status'] != "FINISHED"))

    if not jornadas_disponibles:
        return "❌ No hay más jornadas pendientes."

    siguiente_jornada = jornadas_disponibles[0]  # La más próxima

    return [
        formatear_partido(p)
        for p in partidos
        if p['matchday'] == siguiente_jornada
    ]


def formatear_partido(partido):
    """Formatea la información de un partido con mejor presentación visual"""
    equipo_local = partido['homeTeam']['name']
    equipo_visitante = partido['awayTeam']['name']
    estado = partido['status']
    fecha_utc = partido['utcDate']
    fecha = datetime.strptime(fecha_utc, "%Y-%m-%dT%H:%M:%SZ").astimezone(tz)
    fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M")  # Cambié a un formato más amigable

    if estado == "FINISHED":
        goles_local = partido['score']['fullTime'].get('home', 0)
        goles_visitante = partido['score']['fullTime'].get('away', 0)
        marcador = f"🏆 {goles_local} - {goles_visitante}"
    elif estado in ["IN_PLAY", "PAUSED"]:
        marcador = "🟢 En juego"
    else:
        marcador = "⚽"

    # Agregar algunos separadores visuales y mejorar la claridad
    partido_formateado = (
        f"📅 {fecha_formateada} - {equipo_local} 🆚 {equipo_visitante}\n"
        f"→ {marcador}\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
    )
    return partido_formateado


def obtener_partidos_jornada(codigo_competicion, modo="hoy"):
    """Obtiene los partidos de hoy o de la próxima jornada con resultados si ya se jugaron"""
    hoy = datetime.now(tz).strftime("%Y-%m-%d")
    url = f"{BASE_URL}/competitions/{codigo_competicion}/matches"
    headers = {'X-Auth-Token': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "⚠️ No se pudieron obtener los partidos. Intenta más tarde."

    data = response.json()
    partidos = data.get('matches', [])

    if not partidos:
        return "❌ No hay partidos disponibles para esta liga."

    if modo == "hoy":
        partidos_hoy = [
            formatear_partido(p)
            for p in partidos
            if p['utcDate'].startswith(hoy)
        ]
        if partidos_hoy:
            return "\n".join(partidos_hoy)
        else:
            return "❌ No hay partidos hoy en esta liga."

    # Detectar automáticamente la próxima jornada
    jornadas_disponibles = sorted(set(p['matchday'] for p in partidos if p['status'] != "FINISHED"))

    if not jornadas_disponibles:
        return "❌ No hay más jornadas pendientes."

    siguiente_jornada = jornadas_disponibles[0]  # La más próxima

    partidos_jornada = [
        formatear_partido(p)
        for p in partidos
        if p['matchday'] == siguiente_jornada
    ]

    return "\n".join(partidos_jornada)


@bot.message_handler(commands=['partidos'])
def obtener_partidos(message):
    """Obtiene los partidos de la jornada actual o de la próxima jornada"""
    texto = message.text.split()
    if len(texto) < 3:
        bot.reply_to(message, "⚠️ Debes especificar una liga y la jornada (hoy o jornada). Ejemplo:\n"
                              "✅ /partidos laliga hoy\n"
                              "✅ /partidos premier jornada")
        return

    liga = texto[1].lower()
    jornada = texto[2].lower()

    if liga not in COMPETICIONES:
        bot.reply_to(message, "❌ Liga no válida. Usa:\n"
                              "✅ /partidos laliga hoy\n"
                              "✅ /partidos premier jornada")
        return

    nombre_liga = COMPETICIONES[liga]["nombre"]
    codigo_liga = COMPETICIONES[liga]["codigo"]

    partidos = obtener_partidos_jornada(codigo_liga, jornada)
    bot.send_message(message.chat.id, f"⚽ **Partidos de {nombre_liga}** ({jornada.capitalize()}):\n\n{partidos}")


@bot.message_handler(commands=['clasificacion'])
def obtener_clasificacion(message):
    """Obtiene la clasificación de una liga"""
    texto = message.text.split()
    if len(texto) < 2:
        bot.reply_to(message, "⚠️ Debes especificar una liga. Ejemplo:\n"
                              "✅ /clasificacion laliga\n"
                              "✅ /clasificacion premier")
        return

    liga = texto[1].lower()

    if liga not in COMPETICIONES:
        bot.reply_to(message, "❌ Liga no válida. Usa:\n"
                              "✅ /clasificacion laliga\n"
                              "✅ /clasificacion premier")
        return

    nombre_liga = COMPETICIONES[liga]["nombre"]
    codigo_liga = COMPETICIONES[liga]["codigo"]

    clasificacion = obtener_clasificacion_liga(codigo_liga)
    bot.send_message(message.chat.id, f"🏆 Clasificación de {nombre_liga}:\n\n{clasificacion}")


def obtener_clasificacion_liga(codigo_competicion):
    """Obtiene la clasificación de la liga seleccionada"""
    url = f"{BASE_URL}/competitions/{codigo_competicion}/standings"
    headers = {'X-Auth-Token': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "⚠️ No se pudieron obtener los datos de clasificación. Intenta más tarde."

    data = response.json()
    clasificacion = data['standings'][0]['table']

    clasificacion_str = ""
    for i, equipo in enumerate(clasificacion, 1):
        posicion = emoji_posicion(i)
        equipo_nombre = equipo['team']['name']
        puntos = equipo['points']
        clasificacion_str += f"{posicion} {equipo_nombre} → {puntos} puntos\n"

    return clasificacion_str


def emoji_posicion(posicion):
    """Devuelve el emoji correspondiente a la posición"""
    if posicion == 1:
        return "🥇"
    elif posicion == 2:
        return "🥈"
    elif posicion == 3:
        return "🥉"
    elif posicion == 4:
        return "4️⃣"
    elif posicion == 5:
        return "5️⃣"
    elif posicion == 6:
        return "6️⃣"
    elif posicion == 7:
        return "7️⃣"
    elif posicion == 8:
        return "8️⃣"
    elif posicion == 9:
        return "9️⃣"
    elif posicion == 10:
        return "🔟"
    elif posicion == 11:
        return "1️⃣1️⃣"
    elif posicion == 12:
        return "1️⃣2️⃣"
    elif posicion == 13:
        return "1️⃣3️⃣"
    elif posicion == 14:
        return "1️⃣4️⃣"
    elif posicion == 15:
        return "1️⃣5️⃣"
    elif posicion == 16:
        return "1️⃣6️⃣"
    elif posicion == 17:
        return "1️⃣7️⃣"
    elif posicion == 18:
        return "1️⃣8️⃣"
    elif posicion == 19:
        return "1️⃣9️⃣"
    elif posicion == 20:
        return "2️⃣0️⃣"
    elif posicion == 21:
        return "2️⃣1️⃣"
    elif posicion == 22:
        return "2️⃣2️⃣"
    elif posicion == 23:
        return "2️⃣3️⃣"
    elif posicion == 24:
        return "2️⃣4️⃣"
    elif posicion == 25:
        return "2️⃣5️⃣"
    elif posicion == 26:
        return "2️⃣6️⃣"
    elif posicion == 27:
        return "2️⃣7️⃣"
    elif posicion == 28:
        return "2️⃣8️⃣"
    elif posicion == 29:
        return "2️⃣9️⃣"
    elif posicion == 30:
        return "3️⃣0️⃣"
    elif posicion == 31:
        return "3️⃣1️⃣"
    elif posicion == 32:
        return "3️⃣2️⃣"
    elif posicion == 33:
        return "3️⃣3️⃣"
    elif posicion == 34:
        return "3️⃣4️⃣"
    elif posicion == 35:
        return "3️⃣5️⃣"
    elif posicion == 36:
        return "3️⃣6️⃣"
    else:
        return str(posicion)

@bot.message_handler(commands=['maximos'])
def maximos(message):
    """Muestra los máximos goleadores y asistentes de la liga solicitada"""
    texto = message.text.split()
    if len(texto) < 2:
        bot.reply_to(message, "⚠️ Debes especificar una liga. Ejemplo:\n"
                              "✅ /maximos laliga\n"
                              "✅ /maximos premier")
        return

    liga = texto[1].lower()

    if liga not in COMPETICIONES:
        bot.reply_to(message, "❌ Liga no válida. Usa:\n"
                              "✅ /maximos laliga\n"
                              "✅ /maximos premier")
        return

    nombre_liga = COMPETICIONES[liga]["nombre"]
    maximos = obtener_maximos(COMPETICIONES[liga]["codigo"])

    bot.send_message(message.chat.id, f"⚽ Máximos goleadores de {nombre_liga}:\n\n{maximos}")


def obtener_maximos(codigo_competicion):
    """Obtiene los máximos goleadores de la liga"""
    url = f"{BASE_URL}/competitions/{codigo_competicion}/scorers"
    headers = {'X-Auth-Token': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "⚠️ No se pudieron obtener los máximos goleadores. Intenta más tarde."

    data = response.json()

    # 🔍 Depuración: Imprimimos la estructura de los datos
    print("📊 JSON devuelto por la API:", data)

    goleadores = data.get('scorers', [])

    if not goleadores:
        return "❌ No se encontraron máximos goleadores para esta liga."

    maximos = "🎯 Máximos Goleadores:\n"
    for i, jugador in enumerate(goleadores[:5], 1):
        nombre = jugador.get('player', {}).get('name', 'Desconocido')  # Verifica que 'player' existe
        goles = jugador.get('numberOfGoals')  # Sin valor por defecto para ver si falla

        if goles is None:
            goles = jugador.get('goals', 0)  # Intenta con otro nombre de campo si 'numberOfGoals' no existe

        maximos += f"{i}. {nombre} → {goles} goles\n"

    return maximos

    # Obtener los máximos asistentes
    url_asistentes = f"{BASE_URL}/compet"
    bot.remove_webhook()
    bot.polling(none_stop=True)
if __name__ == "__main__":
    bot.remove_webhook()
    bot.polling(none_stop=True)