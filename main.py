import os
from datetime import *
import platform

while True:
    com = input("-: ")
    if com == "pwd":
        print(os.getcwd())
    elif com == "date":
        print(date.today())
    elif com == "time":
        print(datetime.now().time())
    elif com == "exit":
        exit()
    elif com == "clear":
        os.system("cls")
    elif com == "man":
        print("Comandos permitidos:")
        print("1. pwd")
        print("2. date")
        print("3. time")
        print("4. exit")
        print("5. clear")
        print("6. man")
        print("7. uname -a")
        print("8. cd [directorio]")
        print("9. ls [opciones][dir]")
        print("10. rm [archivos]")
        print("11. mkdir [directorio]")
        print("12. rmdir [directorio]")
    elif com == "uname -a":
        system_info = platform.uname()
        print("Sistema operativo:", system_info.system)
    elif com.startswith("cd"):
        ruta = com.split(" ")
        if len(ruta) == 1:
            os.chdir(os.path.expanduser("~"))
        elif len(ruta) == 2:
            try:
                os.chdir(ruta[1])
            except FileNotFoundError:
                print("No existe el directorio")
        else:
            print("Coloque la directorio correcto")
    elif com.startswith("ls"):
        partes = com.split(" ")
        opciones = ""
        directorio = os.getcwd()
        if len(partes) > 1:
            opciones = partes[1]
            directorio = os.getcwd() if len(partes) == 2 else partes[2]
        try:
            with os.scandir(directorio) as archivos:
                for archivo in archivos:
                    if opciones == "-a" or not archivo.name.startswith("."):
                        if opciones == "-l":
                            print(archivo.name, archivo.stat())
                        else:
                            print(archivo.name)
        except FileNotFoundError:
            print("No existe el directorio")
    elif com.startswith("rm "):
        partes = com.split(" ")
        if len(partes) > 1:
            archivos = partes[1:]
            for archivo in archivos:
                try:
                    os.remove(archivo)
                    print(f"Archivo borrado")
                except FileNotFoundError:
                    print(f"No existe el archivo")
        else:
            print("Uso incorrecto de rm. Uso: rm [archivo]")
    elif com.startswith("mkdir "):
        partes = com.split(" ")
        if len(partes) == 2:
            try:
                os.mkdir(partes[1])
                print(f"Directorio creado")
            except FileExistsError:
                print("Existe el directorio")
        else:
            print("Coloque la directorio correcto")
    elif com.startswith("rmdir "):
        partes = com.split(" ")
        if len(partes) == 2:
            try:
                os.rmdir(partes[1])
                print(f"Directorio borrado")
            except FileNotFoundError:
                print("No existe el directorio")
        else:
            print("Coloque la directorio correcto")
    else:
        print("Comando no permitido")
