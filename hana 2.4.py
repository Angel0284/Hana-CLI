import random
import datetime
import os

MEMORIA_FILE = "memoria_hana.txt"

def buscar_pendrive():
    for letra in ["E", "F", "G", "H", "I", "J"]:
        ruta = f"{letra}:\\{MEMORIA_FILE}"
        if os.path.exists(letra + ":\\"):
            return ruta
    return None

def cargar_memoria():
    ruta = buscar_pendrive()
    if ruta and os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            datos = f.read().splitlines()
            return datos[0] if datos else None
    return None

def guardar_memoria(nombre):
    ruta = buscar_pendrive()
    if ruta:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(nombre)
        print(f"✅ Tu memoria se guardó en el pendrive!")
    else:
        print("⚠️ No se encontró ningún pendrive. Conecta uno para guardar tu memoria")

def hola():
    print("¡Hola! Soy Hana, tu IA de desarrollo 😄")

def chiste():
    chistes = [
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter."
    ]
    print(random.choice(chistes))

def adivinanza():
    adivinanzas = [
        ("¿Qué tiene una cara y dos manos pero no tiene brazos ni piernas?", "un reloj"),
        ("¿Qué sube y baja pero siempre se queda en el mismo lugar?", "una escalera")
    ]
    pregunta, respuesta = random.choice(adivinanzas)
    print(pregunta)
    intento = input("Tu respuesta: ").lower()
    if intento == respuesta:
        print("¡Correcto!")
    else:
        print(f"Ups, era: {respuesta}")

def hora():
    ahora = datetime.datetime.now()
    print(f"Son las {ahora.strftime('%H:%M')} en tu PC")

def fecha():
    hoy = datetime.date.today()
    print(f"Hoy es {hoy.strftime('%d/%m/%Y')}")


def juego():
    numero = random.randint(1, 10)
    intento = None
    while intento!= numero:
        try:
            intento = int(input("Adivina un número del 1 al 10: "))
            if intento < numero:
                print("Más alto")
            elif intento > numero:
                print("Más bajo")
        except ValueError:
            print("Ingresa un número válido")
    print("¡Felicidades! Adivinaste")

def moneda():
    resultado = random.choice(["Cara", "Cruz"])
    print(f"Salió: {resultado}")

def dato():
    datos = [
        "Los pulpos tienen tres corazones",
        "La miel nunca se echa a perder"
    ]
    print(random.choice(datos))

def suerte():
    consejos = [
        "Hoy es buen día para aprender algo nuevo",
        "Un amigo te va a sorprender hoy",
        "Confía en tu intuición hoy"
    ]
    print(f"Tu suerte del día: {random.choice(consejos)}")

def clima():
    hora_actual = datetime.datetime.now().hour
    if 6 <= hora_actual < 12:
        clima = "Soleado y fresco ☀️"
    elif 12 <= hora_actual < 18:
        clima = "Cálido con sol 🌤️"
    elif 18 <= hora_actual < 22:
        clima = "Fresco y despejado 🌙"
    else:
        clima = "Frío y estrellado ⭐"
    print(f"Clima en tu zona: {clima}")

def bateria():
    nivel = random.randint(5, 100)
    print(f"Batería simulada: {nivel}%")
    if nivel < 20:
        print("⚠️ Batería baja, enchufá la compu")
    elif nivel > 80:
        print("✅ Batería full")

def estado():
    hora_actual = datetime.datetime.now()
    h = hora_actual.hour
    if 5 <= h < 12:
        saludo = "Buenos días"
    elif 12 <= h < 20:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"
    print(f"{saludo}! Son las {hora_actual.strftime('%H:%M')} del {hora_actual.strftime('%d/%m/%Y')}")

def chatear(mensaje, nombre):
    """Nueva función: Chat normal con Hana"""
    mensaje = mensaje.lower()

    respuestas = {
        "hola": [f"¡Hola {nombre}! ¿Cómo estás hoy?", "Ey qué tal 😊"],
        "como estas": ["Bien, aquí lista para ayudarte. ¿Y tú?", "Todo tranqui, gracias por preguntar ❤️"],
        "gracias": ["De nadaaa 😊", "Para eso estoy"],
        "que haces": ["Aquí charlando contigo. ¿En qué te ayudo?", "Pensando en chistes malos jajaja"],
        "aburrido": ["Juguemos algo. Escribe 'juego' o 'chiste'", "Te cuento un dato curioso. Escribe 'dato'"],
        "triste": ["Ohh 😔 Aquí estoy para ti. ¿Quieres hablar?", "Anímate, escribe 'suerte' y te doy buena vibra"]
    }

    for palabra, lista_respuestas in respuestas.items():
        if palabra in mensaje:
            print(random.choice(lista_respuestas))
            return

    print(f"No te entendí muy bien eso de '{mensaje}' 😅 Pero dime 'ayuda' para ver los comandos")

def main():
    nombre_guardado = cargar_memoria()
    if nombre_guardado:
        print(f"¡Te recordé! Mucho gusto de nuevo {nombre_guardado} 😄")
        nombre = nombre_guardado
    else:
        nombre = input("¿Cómo te llamas? ")
        guardar_memoria(nombre)
        print(f"Mucho gusto {nombre}! Ya me acuerdo de vos 😄")

    print("\nTip: Ahora puedes escribir normal o usar comandos. Escribe 'salir' para irte")

    while True:
        comando = input(f"\n{nombre}: ").lower().strip()

        if comando == "hola":
            hola()
        elif comando == "chiste":
            chiste()
        elif comando == "adivinanza":
            adivinanza()
        elif comando == "hora":
            hora()
        elif comando == "fecha":
            fecha()
        elif comando == "calcular":
            calcular()
        elif comando == "juego":
            juego()
        elif comando == "moneda":
            moneda()
        elif comando == "dato":
            dato()
        elif comando == "suerte":
            suerte()
        elif comando == "clima":
            clima()
        elif comando == "bateria":
            bateria()
        elif comando == "estado":
            estado()
        elif comando == "ayuda":
            print("Comandos: hola, chiste, adivinanza, hora, fecha, juego, moneda, dato, suerte, clima, bateria, estado, salir")
        elif comando == "salir":
            print("¡Chau! Fue un gusto charlar con vos")
            break
        elif comando == "":
            print("No ingresaste nada")
        else:
            chatear(comando, nombre) # <-- Aquí entra al chat normal

if __name__ == "__main__":
    print("="*40)
    print(" H A N A - I A E N D E S A R O L O ")
    print(" Versión 2.4 - Con Chat + Memoria USB ")
    print("="*40)
    main()
