import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import yfinance as yf
import pyjokes
import webbrowser
import datetime

#opciones de voz de mi dispositivo
id1 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
id2 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'

# escuchar nuestro microfono y devolver el audio comotexto
def transformar_audio_en_texto():
    # almacenar recognizer en variable
    r = sr.Recognizer()
    # configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8
        # informar que comenzo la grabacion
        print("ya puedes hablar")
        # guardar lo que escuche como audio
        audio = r.listen(origen)
        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ar")
            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido
        # en caso de que no comprenda el audio
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("ups, no entendi")
            # devolver error
            return "sigo esperando"
        # en caso de no resolver el pedido
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("ups, no hay servicio")
            # devolver error
            return "sigo esperando"
        # error inesperado
        except:
            # prueba de que no comprendio el audio
            print("ups, algo ha salido mal")
            # devolver error
            return "sigo esperando"


#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id2)
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#Informar el día de la semana
def pedir_dia():
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    #diccionario con los dias de la semana
    calendario = {0:'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'
                  }
    #Dedir dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

#Informar de la hora
def pedir_hora():
    #crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} horas, {hora.minute} minutos and {hora.second} segundos'
    hablar(hora)


def saludo_incial():
    #decir saludo
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 14:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes '
    hablar(f"{momento} Gemma, soy Elena, tu asistente personal. ¿En qué te puedo ayudar?")

#funciona principal
def pedir_cosas():
    saludo_incial()
    #variable de corte
    comenzar = True
    #loop central
    while comenzar:
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Claro! Abriendo Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, te abro Google')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'qué día es' in pedido:
            pedir_dia()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Lo busco, un momento')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente :')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Lo busco enseguida ')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, lo reproduzco')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Tiker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón, pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break



pedir_cosas()