import ast
import datetime
import os
import random
import webbrowser  # Módulo para abrir páginas web

# Base de datos simulada en memoria para usuarios
usuarios_db = {}


def cargar_usuario(usuario):
    """Simula la carga de datos del usuario desde la memoria."""
    return usuarios_db.get(usuario, None)


def guardar_usuario(datos):
    """Guarda los datos del usuario en la base de datos simulada."""
    usuarios_db[datos["usuario"]] = datos


# ==========================================
# FUNCIONES CLÁSICAS (Versiones 2.2 a 2.8)
# ==========================================
def hola():
    """Saludo clásico de Hana."""
    print("¡Hola! Soy Hana, tu asistente personal y de desarrollo 😄")


def chiste():
    """Cuenta un chiste aleatorio."""
    chistes = [
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        (
            "¿Por qué los pájaros no usan Facebook? Porque ya tienen"
            " Twitter."
        ),
    ]
    print(f"\n🌸 Hana: {random.choice(chistes)}")


def adivinanza():
    """Juego rápido de adivinanza."""
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
    print(f"\n🧩 {pregunta}")
    intento = input("Tu respuesta: ").lower().strip()
    if intento == respuesta:
        print("✨ ¡Correcto, muy bien!")
    else:
        print(f"❌ Ups, la respuesta correcta era: {respuesta}")


def hora():
    """Muestra la hora actual."""
    ahora = datetime.datetime.now()
    print(f"\n⏰ Son las {ahora.strftime('%H:%M')} en tu PC")


def fecha():
    """Muestra la fecha actual."""
    hoy = datetime.date.today()
    print(f"\n📅 Hoy es {hoy.strftime('%d/%m/%Y')}")


def juego_adivinar_numero():
    """Juego de adivinar un número del 1 al 10."""
    print("\n🎲 Adivina un número del 1 al 10.")
    numero = random.randint(1, 10)
    intento = None
    while intento != numero:
        try:
            intento = int(input("Ingresa tu número: "))
            if intento < numero:
                print("📈 Más alto...")
            elif intento > numero:
                print("📉 Más bajo...")
            else:
                print("🎉 ¡Felicidades! ¡Adivinaste el número!")
        except ValueError:
            print("❌ Ingresa un número válido por favor.")


def moneda():
    """Lanzamiento de moneda (Cara o Cruz)."""
    resultado = random.choice(["Cara", "Cruz"])
    print(f"\n🪙 La moneda giró y salió: **{resultado}**!")


def bateria():
    """Simulador de nivel de batería."""
    nivel = random.randint(5, 100)
    print(f"\n🔋 Batería simulada: {nivel}%")
    if nivel < 20:
        print("⚠️ ¡Batería baja, enchufá la compu!")
    elif nivel > 80:
        print("✅ Batería full y en buen estado.")


def estado():
    """Muestra el estado del sistema según la hora del día."""
    hora_actual = datetime.datetime.now()
    h = hora_actual.hour
    if 5 <= h < 12:
        saludo_est = "Buenos días"
    elif 12 <= h < 20:
        saludo_est = "Buenas tardes"
    else:
        saludo_est = "Buenas noches"
    print(
        f"\n📊 {saludo_est}! Son las {hora_actual.strftime('%H:%M')} del"
        f" {hora_actual.strftime('%d/%m/%Y')}"
    )


# ==========================================
# FUNCIONES WEB Y DE CÁLCULO (Versiones 3.0+)
# ==========================================
def abrir_web(url):
    """Abre un sitio web intentando usar Microsoft Edge."""
    try:
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        if os.path.exists(edge_path):
            webbrowser.register(
                "edge", None, webbrowser.BackgroundBrowser(edge_path)
            )
            webbrowser.get("edge").open(url)
        else:
            webbrowser.open(url)
    except Exception:
        webbrowser.open(url)


def calcular():
    """Calculadora inteligente y segura con soporte de palabras en español."""
    print("\n🧮 ================================= 🧮")
    print("          CALCULADORA DE HANA        ")
    print("🧮 ================================= 🧮")
    print("💡 Ejemplos:")
    print("   • Con símbolos: 5 * 4  |  10 / 2  |  2 ^ 3")
    print("   • Con palabras: 5 por 4 | 10 entre 2 | 8 mas 2")

    expresion = input("\n👉 Ingresa la operación a realizar: ").strip().lower()

    if not expresion:
        print("❌ Operación vacía.")
        return

    reemplazos = {
        "mas": "+",
        "más": "+",
        "sumado a": "+",
        "sumado con": "+",
        "menos": "-",
        "multiplicado por": "*",
        "por": "*",
        "x": "*",
        "dividido por": "/",
        "dividido entre": "/",
        "dividido": "/",
        "entre": "/",
        "elevado a la": "**",
        "elevado a": "**",
        "elevado": "**",
        "^": "**",
    }

    for palabra, simbolo in reemplazos.items():
        expresion = expresion.replace(palabra, simbolo)

    try:
        nodo = ast.parse(expresion, mode="eval")

        def evaluar_nodo(node):
            if isinstance(node, ast.Expression):
                return evaluar_nodo(node.body)
            elif isinstance(node, ast.Constant):
                return node.value
            elif isinstance(node, ast.BinOp):
                izq = evaluar_nodo(node.left)
                der = evaluar_nodo(node.right)

                if isinstance(node.op, ast.Add):
                    return izq + der
                elif isinstance(node.op, ast.Sub):
                    return izq - der
                elif isinstance(node.op, ast.Mult):
                    return izq * der
                elif isinstance(node.op, ast.Div):
                    if der == 0:
                        raise ZeroDivisionError("División por cero")
                    return izq / der
                elif isinstance(node.op, ast.Pow):
                    return izq**der
                elif isinstance(node.op, ast.Mod):
                    return izq % der
                else:
                    raise ValueError("Operador no soportado")
            elif isinstance(node, ast.UnaryOp):
                operand = evaluar_nodo(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                elif isinstance(node.op, ast.UAdd):
                    return +operand
                else:
                    raise ValueError("Operador unario no soportado")
            else:
                raise ValueError("Estructura no permitida por seguridad")

        resultado = evaluar_nodo(nodo)

        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)

        print(f"\n✨ Resultado de Hana: {resultado}")

    except ZeroDivisionError:
        print("\n❌ Error: No se puede dividir ningún número entre cero.")
    except Exception:
        print(
            "\n❌ Operación inválida. Asegúrate de usar números y operadores"
            " claros."
        )


def menu_inteligencias_artificiales():
    """Submenú interactivo para herramientas de IA."""
    while True:
        print("\n🤖 ================================= 🤖")
        print("  MENÚ DE INTELIGENCIAS ARTIFICIALES")
        print("🤖 ================================= 🤖")
        print("1. 🌐 Gemini")
        print("2. 🚀 Grok")
        print("3. 💬 ChatGPT")
        print("4. ♾️ Meta AI")
        print("5. 🧠 Claude")
        print("6. 🤖 Copilot")
        print("7. 🔍 Perplexity AI")
        print("8. 🐱 Le Chat (Mistral)")
        print("9. 🐬 DeepSeek")
        print("0. 🔙 Volver al menú principal")

        opcion = input("\n👉 Elige una opción de IA (0-9): ").strip()

        if opcion == "1":
            abrir_web("https://gemini.google.com")
        elif opcion == "2":
            abrir_web("https://grok.x.ai")
        elif opcion == "3":
            abrir_web("https://chatgpt.com")
        elif opcion == "4":
            abrir_web("https://www.meta.ai")
        elif opcion == "5":
            abrir_web("https://claude.ai")
        elif opcion == "6":
            abrir_web("https://copilot.microsoft.com")
        elif opcion == "7":
            abrir_web("https://www.perplexity.ai")
        elif opcion == "8":
            abrir_web("https://chat.mistral.ai")
        elif opcion == "9":
            abrir_web("https://chat.deepseek.com")
        elif opcion == "0":
            print("\n🌸 Hana: Volviendo al menú principal...")
            break
        else:
            print("\n❌ Opción inválida. Elige un número del 0 al 9.")


# ==========================================
# REGISTRO Y SESIONES
# ==========================================
def registrar_cuenta():
    """Permite registrar un nuevo usuario incluyendo contraseña, edad y género."""
    print("\n✨ ================================= ✨")
    print("      🌸 REGISTRO DE CUENTA EN HANA 🌸")
    print("✨ ================================= ✨")

    usuario = input("👤 Ingresa tu nombre de usuario: ").strip()
    if not usuario:
        print("❌ ¡Ojo! El nombre de usuario no puede estar vacío.")
        return

    if cargar_usuario(usuario):
        print("⚠️ ¡Ese usuario ya existe, elige otro nombre!")
        return

    clave = input("🔑 Ingresa tu contraseña secreta: ").strip()

    try:
        edad = int(input("🎂 Ingresa tu edad: ").strip())
    except ValueError:
        print("⚠️ Edad no válida, se asignará 0 por defecto.")
        edad = 0

    print("\n🎭 Selecciona tu género para personalizar la experiencia:")
    print("1. 👦 Hombre")
    print("2. 👧 Mujer")
    print("3. 🤫 No quiero decirlo")
    opcion_genero = input("👉 Elige una opción (1-3): ").strip()

    if opcion_genero == "1":
        genero = "hombre"
    elif opcion_genero == "2":
        genero = "mujer"
    else:
        genero = "no_decir"

    datos = {
        "usuario": usuario,
        "clave": clave,
        "edad": edad,
        "genero": genero,
    }

    guardar_usuario(datos)
    print(
        f"\n🎉 ¡Súper! La cuenta de {usuario} (Edad: {edad} años) fue creada con"
        " éxito. 🚀"
    )


def obtener_saludo(datos_usuario):
    """Adapta el saludo inicial según el género con mucha personalidad."""
    genero = datos_usuario.get("genero", "no_decir")
    nombre = datos_usuario["usuario"]
    edad = datos_usuario.get("edad", 0)

    if genero == "hombre":
        return f"🔓 ¡Acceso concedido! 👑 ¡Qué grande, {nombre} ({edad} años)! Mucho gusto en verte de nuevo, amigo. 🚀"
    elif genero == "mujer":
        return (
            f"🔓 ¡Acceso concedido! ✨ ¡Hola, {nombre} ({edad} años)! Qué genial"
            " tenerte de vuelta, amiga. 🌸"
        )
    else:
        return (
            f"🔓 ¡Acceso concedido! 🎉 ¡Bienvenido/a {nombre} ({edad} años)!"
            " Todo listo para arrancar hoy. ⚡"
        )


def menu_principal_hana(datos_usuario):
    genero = datos_usuario.get("genero", "no_decir")
    nombre = datos_usuario["usuario"]

    print("\n" + obtener_saludo(datos_usuario))

    while True:
        print(f"\n⚡ --- MENÚ PRINCIPAL DE HANA (Sesión: {nombre}) --- ⚡")

        if genero == "hombre":
            print("1. 💬 ¿Cómo estás, amigo?")
        elif genero == "mujer":
            print("1. 💬 ¿Cómo estás, amiga?")
        else:
            print("1. 💬 ¿Cómo estás?")

        print("2. ▶️ Abrir YouTube")
        print("3. 🎵 Abrir TikTok")
        print("4. 💬 Abrir Discord")
        print("5. 🎧 Abrir YouTube Music")
        print("6. 🎮 Abrir Twitch")
        print("7. 📌 Abrir Pinterest")
        print("8. 🤖 Menú de Inteligencias Artificiales")
        print("9. 🧮 Calcular (¡Función inteligente! ✨)")
        print("10. 🎲 Jugar a adivinar el número")
        print("11. 🧩 Adivinanza rápida")
        print("12. 😂 Contar un chiste")
        print("13. ⏰ Ver la hora actual")
        print("14. 📅 Ver la fecha de hoy")
        print("15. 🪙 Lanzar moneda")
        print("16. 🔋 Simular estado de batería")
        print("17. 📊 Ver estado del sistema")
        print("18. 🚪 Cerrar Sesión")

        opcion = input("\n👉 Elige una opción (1-18): ").strip()

        if opcion == "1":
            if genero == "hombre":
                print(
                    "\n🌸 Hana: ¡Con toda la energía, campeón! 🚀 ¿En qué te"
                    " puedo ayudar hoy?"
                )
            elif genero == "mujer":
                print(
                    "\n🌸 Hana: ¡Súper bien y lista para dar lo mejor! ✨ ¿Qué"
                    " hacemos hoy, amiga?"
                )
            else:
                print(
                    "\n🌸 Hana: ¡Excelente de energía y a pleno! ⚡ Contame,"
                    " ¿qué querés hacer?"
                )

        elif opcion == "2":
            print(
                "\n🌸 Hana: ¡A disfrutar de unos buenos videos! Abriendo"
                " YouTube... 🎬🍿"
            )
            abrir_web("https://www.youtube.com")

        elif opcion == "3":
            print(
                "\n🌸 Hana: ¡Hora de scrollear un rato! Abriendo TikTok..."
                " 🎵📱"
            )
            abrir_web("https://www.tiktok.com")

        elif opcion == "4":
            print(
                "\n🌸 Hana: ¡Conectando con la comunidad! Abriendo Discord..."
                " 🎧💬"
            )
            abrir_web("https://discord.com/app")

        elif opcion == "5":
            print(
                "\n🌸 Hana: ¡A poner buena música! Abriendo YouTube Music..."
                " 🎶🎧"
            )
            abrir_web("https://music.youtube.com")

        elif opcion == "6":
            print(
                "\n🌸 Hana: ¡A ver esos streams en vivo! Abriendo Twitch... 🎮🟣"
            )
            abrir_web("https://www.twitch.tv")

        elif opcion == "7":
            print(
                "\n🌸 Hana: ¡Buscando inspiración e ideas! Abriendo Pinterest..."
                " 🎨📌"
            )
            abrir_web("https://www.pinterest.com")

        elif opcion == "8":
            menu_inteligencias_artificiales()

        elif opcion == "9":
            calcular()

        elif opcion == "10":
            juego_adivinar_numero()

        elif opcion == "11":
            adivinanza()

        elif opcion == "12":
            chiste()

        elif opcion == "13":
            hora()

        elif opcion == "14":
            fecha()

        elif opcion == "15":
            moneda()

        elif opcion == "16":
            bateria()

        elif opcion == "17":
            estado()

        elif opcion == "18":
            print(
                f"\n🌸 Hana: Guardando todo y cerrando la sesión de {nombre}..."
                " ¡Nos vemos pronto! 👋✨"
            )
            break

        else:
            print(
                "\n❌ Opción inválida, prueba elegir un número válido del menú."
            )


def iniciar_sesion():
    print("\n🔐 ================================= 🔐")
    print("         INICIAR SESIÓN EN HANA        ")
    print("🔐 ================================= 🔐")
    usuario = input("👤 Usuario: ").strip()
    clave = input("🔑 Contraseña: ").strip()

    datos = cargar_usuario(usuario)

    if datos and datos["clave"] == clave:
        menu_principal_hana(datos)
    else:
        print("\n❌ Ups, usuario o contraseña incorrectos. ¡Intenta de nuevo!")


def main():
    while True:
        print("\n🤖 ================================= 🤖")
        print("     ✨ ASISTENTE HANA - VERSIÓN 3.2 ✨ ")
        print("   Fusión Total (Sin TXT, Con Todo lo Demás)")
        print("🤖 ================================= 🤖")
        print("1. 🔑 Iniciar sesión")
        print("2. 📝 Crear cuenta")
        print("3. ❌ Salir")

        opcion = input("\n👉 Selecciona una opción: ").strip()

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_cuenta()
        elif opcion == "3":
            print(
                "\n🌸 Hana: ¡Un gusto ayudarte! Nos vemos la próxima. Bye bye!"
                " 👋✨"
            )
            break
        else:
            print("\n❌ Opción no válida, intenta otra vez.")


if __name__ == "__main__":
  main()