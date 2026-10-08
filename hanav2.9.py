import os
import json
import zipfile
import webbrowser

# Nombre del archivo ZIP donde se guardan las cuentas de usuario
DATOS_ZIP = "cuentas.zip"

def cargar_usuario(usuario):
    """Carga los datos de un usuario desde el archivo ZIP."""
    if not os.path.exists(DATOS_ZIP):
        return None
    try:
        with zipfile.ZipFile(DATOS_ZIP, 'r') as zf:
            nombre_archivo = f"{usuario}.json"
            if nombre_archivo in zf.namelist():
                with zf.open(nombre_archivo) as f:
                    return json.load(f)
    except Exception:
        pass
    return None

def guardar_usuario(datos_usuario):
    """Guarda los datos del usuario dentro del archivo ZIP."""
    usuario = datos_usuario["usuario"]
    nombre_archivo = f"{usuario}.json"
    
    archivos_existentes = {}
    if os.path.exists(DATOS_ZIP):
        try:
            with zipfile.ZipFile(DATOS_ZIP, 'r') as zf:
                for item in zf.namelist():
                    archivos_existentes[item] = zf.read(item)
        except Exception:
            pass

    archivos_existentes[nombre_archivo] = json.dumps(datos_usuario, indent=4).encode('utf-8')

    with zipfile.ZipFile(DATOS_ZIP, 'w', zipfile.ZIP_DEFLATED) as zf:
        for nombre, contenido in archivos_existentes.items():
            zf.writestr(nombre, contenido)

def registrar_cuenta():
    print("\n✨ ================================= ✨")
    print("      🌸 REGISTRO DE CUENTA EN HANA 🌸")
    print("✨ ================================= ✨")
    
    usuario = input("👤 Ingresa tu nombre de usuario: ").strip()
    if not usuario:
        print("❌ ¡Ojo! El nombre de usuario no puede estar vacío.")
        return

    if cargar_usuario(usuario):
        print("⚠️ ¡Uso de nombre duplicado! Ese usuario ya existe, elegí otro.")
        return

    clave = input("🔑 Ingresa tu contraseña secreta: ").strip()
    
    try:
        edad = int(input("🎂 Ingresa tu edad: ").strip())
    except ValueError:
        print("⚠️ Edad no válida, pero tranqui, te asignaré 0 por mientras.")
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
        "genero": genero
    }

    guardar_usuario(datos)
    print(f"\n🎉 ¡Súper! La cuenta de {usuario} fue creada con éxito. 🚀")

def abrir_web(url):
    """Abre un sitio web intentando usar Microsoft Edge."""
    try:
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        if os.path.exists(edge_path):
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open(url)
        else:
            webbrowser.open(url)
    except Exception:
        webbrowser.open(url)

def obtener_saludo(datos_usuario):
    """Adapta el saludo inicial según el género con mucha personalidad."""
    genero = datos_usuario.get("genero", "no_decir")
    nombre = datos_usuario["usuario"]

    if genero == "hombre":
        return f"🔓 ¡Acceso concedido! 👑 ¡Qué grande, {nombre}! Mucho gusto en verte de nuevo, amigo. 🚀"
    elif genero == "mujer":
        return f"🔓 ¡Acceso concedido! ✨ ¡Hola, {nombre}! Qué genial tenerte de vuelta, amiga. 🌸"
    else:
        return f"🔓 ¡Acceso concedido! 🎉 ¡Bienvenido/a {nombre}! Todo listo para arrancar hoy. ⚡"

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
        print("8. 🚪 Cerrar Sesión")
        
        opcion = input("\n👉 Elige una opción: ").strip()
        
        if opcion == "1":
            if genero == "hombre":
                print("\n🌸 Hana: ¡Con toda la energía, campeón! 🚀 ¿En qué te puedo ayudar hoy?")
            elif genero == "mujer":
                print("\n🌸 Hana: ¡Súper bien y lista para dar lo mejor! ✨ ¿Qué hacemos hoy, amiga?")
            else:
                print("\n🌸 Hana: ¡Excelente de energía y a pleno! ⚡ Contame, ¿qué querés hacer?")

        elif opcion == "2":
            print("\n🌸 Hana: ¡A disfrutar de unos buenos videos! Abriendo YouTube... 🎬🍿")
            abrir_web("https://www.youtube.com")

        elif opcion == "3":
            print("\n🌸 Hana: ¡Hora de scrollear un rato! Abriendo TikTok... 🎵📱")
            abrir_web("https://www.tiktok.com")

        elif opcion == "4":
            print("\n🌸 Hana: ¡Conectando con la comunidad! Abriendo Discord... 🎧💬")
            abrir_web("https://discord.com/app")

        elif opcion == "5":
            print("\n🌸 Hana: ¡A poner buena música! Abriendo YouTube Music... 🎶🎧")
            abrir_web("https://music.youtube.com")

        elif opcion == "6":
            print("\n🌸 Hana: ¡A ver esos streams en vivo! Abriendo Twitch... 🎮🟣")
            abrir_web("https://www.twitch.tv")

        elif opcion == "7":
            print("\n🌸 Hana: ¡Buscando inspiración e ideas! Abriendo Pinterest... 🎨📌")
            abrir_web("https://www.pinterest.com")

        elif opcion == "8":
            print(f"\n🌸 Hana: Guardando todo y cerrando la sesión de {nombre}... ¡Nos vemos pronto! 👋✨")
            break

        else:
            print("\n❌ Opción inválida, prueba elegir un número del menú.")

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
        print("     ✨ ASISTENTE HANA - VERSIÓN 2.9 ✨ ")
        print("          Sistema con Personalidad")
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
            print("\n🌸 Hana: ¡Un gusto ayudarte! Nos vemos la próxima. Bye bye! 👋✨")
            break
        else:
            print("\n❌ Opción no válida, intenta otra vez.")

if __name__ == "__main__":
    main()