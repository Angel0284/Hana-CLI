import datetime
import random
import sys
import webbrowser  # Módulo para abrir páginas web

# Configuración para permitir emojis en la consola de comandos
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def hola():
    print("¡Hola! Soy Hana, tu asistente personal 😄")


def chiste():
    chistes = [
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
    ]
    print(random.choice(chistes))


def adivinanza():
    adivinanzas = [
        (
            "¿Qué tiene una cara y dos manos pero no tiene brazos ni piernas?",
            "un reloj",
        ),
        (
            "¿Qué sube y baja pero siempre se queda en el mismo lugar?",
            "una escalera",
        ),
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


def calcular():
    try:
        expresion = input("Ingresa una operación (ej: 2 + 2): ")
        resultado = eval(expresion)
        print(f"Resultado: {resultado}")
    except:
        print("Expresión inválida. Usa solo números y + - * /")


def juego():
    numero = random.randint(1, 10)
    intento = None
    while intento != numero:
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
        "La miel nunca se echa a perder",
    ]
    print(random.choice(datos))


def suerte():
    consejos = [
        "Hoy es buen día para aprender algo nuevo",
        "Un amigo te va a sorprender hoy",
        "Confía en tu intuición hoy",
    ]
    print(f"Tu suerte del día: {random.choice(consejos)}")


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

    print(
        f"{saludo}! Son las {hora_actual.strftime('%H:%M')} del {hora_actual.strftime('%d/%m/%Y')}"
    )


# --- FUNCIONES PARA ABRIR WEBS CON EL NAVEGADOR PREDETERMINADO ---
def abrir_en_navegador(url):
    try:
        webbrowser.open(url)
    except:
        print("No se pudo abrir el navegador automáticamente.")


def abrir_youtube():
    print("Abriendo YouTube en tu navegador predeterminado...")
    abrir_en_navegador("https://www.youtube.com")


def abrir_tiktok():
    print("Abriendo TikTok en tu navegador predeterminado...")
    abrir_en_navegador("https://www.tiktok.com")


def abrir_discord():
    print("Abriendo Discord en tu navegador predeterminado...")
    abrir_en_navegador("https://discord.com/app")


def abrir_youtubemusic():
    print("Abriendo YouTube Music en tu navegador predeterminado...")
    abrir_en_navegador("https://music.youtube.com")


def abrir_twitch():
    print("Abriendo Twitch en tu navegador predeterminado...")
    abrir_en_navegador("https://www.twitch.tv")


def abrir_pinterest():
    print("Abriendo Pinterest en tu navegador predeterminado...")
    abrir_en_navegador("https://www.pinterest.com")


# --- FUNCIONES PARA INTELIGENCIAS ARTIFICIALES ---
def abrir_gemini():
    print("Abriendo Gemini...")
    abrir_en_navegador("https://gemini.google.com")


def abrir_grok():
    print("Abriendo Grok...")
    abrir_en_navegador("https://x.ai")


def abrir_chatgpt():
    print("Abriendo ChatGPT...")
    abrir_en_navegador("https://chatgpt.com")


def abrir_metaai():
    print("Abriendo Meta AI...")
    abrir_en_navegador("https://www.meta.ai")


def abrir_claude():
    print("Abriendo Claude...")
    abrir_en_navegador("https://claude.ai")


def abrir_copilot():
    print("Abriendo Copilot...")
    abrir_en_navegador("https://copilot.microsoft.com")


def abrir_perplexity():
    print("Abriendo Perplexity AI...")
    abrir_en_navegador("https://www.perplexity.ai")


def abrir_lechat():
    print("Abriendo Le Chat de Mistral AI...")
    abrir_en_navegador("https://chat.mistral.ai")


def abrir_deepseek():
    print("Abriendo DeepSeek...")
    abrir_en_navegador("https://chat.deepseek.com")


def menu_inteligencias_artificiales():
    while True:
        print("\n" + "=" * 35)
        print("  MENÚ DE INTELIGENCIAS ARTIFICIALES")
        print("=" * 35)
        print("1. Gemini")
        print("2. Grok")
        print("3. ChatGPT")
        print("4. Meta AI")
        print("5. Claude")
        print("6. Copilot")
        print("7. Perplexity AI")
        print("8. Le Chat (Mistral)")
        print("9. DeepSeek")
        print("0. Volver al menú principal")

        opcion = input("\nElige una opción de IA (0-9): ").strip()

        if opcion == "1":
            abrir_gemini()
        elif opcion == "2":
            abrir_grok()
        elif opcion == "3":
            abrir_chatgpt()
        elif opcion == "4":
            abrir_metaai()
        elif opcion == "5":
            abrir_claude()
        elif opcion == "6":
            abrir_copilot()
        elif opcion == "7":
            abrir_perplexity()
        elif opcion == "8":
            abrir_lechat()
        elif opcion == "9":
            abrir_deepseek()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida. Elige un número del 0 al 9.")


def main():
    nombre = input("¿Cómo te llamas? ")
    print(f"Mucho gusto {nombre}! Ya me acuerdo de vos 😄")

    while True:
        comando = (
            input(
                "\nComando (hola, chiste, adivinanza, hora, fecha, calcular, juego, moneda, dato, suerte, bateria, estado, youtube, tiktok, discord, youtubemusic, twitch, pinterest, ia, salir): "
            )
            .lower()
            .strip()
        )

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
        elif comando == "bateria":
            bateria()
        elif comando == "estado":
            estado()
        # --- COMANDOS WEB ---
        elif comando == "youtube":
            abrir_youtube()
        elif comando == "tiktok":
            abrir_tiktok()
        elif comando == "discord":
            abrir_discord()
        elif comando == "youtubemusic":
            abrir_youtubemusic()
        elif comando == "twitch":
            abrir_twitch()
        elif comando == "pinterest":
            abrir_pinterest()
        # --- COMANDO MODO INTELIGENCIA ARTIFICIAL ---
        elif comando == "ia" or comando == "modo inteligencia artificial":
            menu_inteligencias_artificiales()
        elif comando == "salir":
            print("¡Chau! Fue un gusto charlar con vos")
            break
        elif comando == "":
            print("No ingresaste ningún comando")
        else:
            print("Comando no reconocido. Prueba otra vez.")


if __name__ == "__main__":
    print("=" * 45)
    print("        A S I S T E N T E   H A N A        ")
    print("  Versión 2.8 - Soporte Emojis Integrado   ")
    print("=" * 45)
    main()