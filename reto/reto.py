import csv
import matplotlib.pyplot as plt
import os


def listar_txt_csv():
    ruta = os.path.join(os.getcwd(), "usoarchivos")  
    archivos = os.listdir(ruta)
    archivos_filtrados = []

    for archivo in archivos:
        if archivo.endswith('.txt') or archivo.endswith('.csv'):
            archivos_filtrados.append(archivo)

    print("\nArchivos .txt y .csv encontrados en el directorio actual:")
    for archivo in archivos_filtrados:
        print(archivo)

    return archivos_filtrados



def seleccionar_archivo():
    ruta = input("Ingrese la ruta completa del archivo: ")
    try:
        with open(ruta, 'r', encoding="utf-8") as file:
            pass
        return ruta
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None


def mostrar_15_filas(ruta):
    print("\nMostrando las primeras 15 filas del archivo:")
    with open(ruta, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i < 15:
                print(row)
            else:
                break


def calcular_estadisticas(ruta, columna):
    datos = []
    with open(ruta, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                datos.append(float(row[columna]))
            except ValueError:
                continue
            except KeyError:
                print(f"La columna '{columna}' no existe.")
                return

    if datos:
        print(f"\nEstadísticas de la columna '{columna}':")
        print(f"Número de datos: {len(datos)}")
        print(f"Promedio: {sum(datos) / len(datos)}")
        print(f"Máximo: {max(datos)}")
        print(f"Mínimo: {min(datos)}")
        datos.sort()
        mediana = datos[len(datos) // 2] if len(datos) % 2 != 0 else \
            (datos[len(datos) // 2 - 1] + datos[len(datos) // 2]) / 2
        print(f"Mediana: {mediana}")
    else:
        print("Columna no encontrada o sin datos numéricos.")


def graficar_columna(ruta, columna):
    datos = []
    with open(ruta, 'r',  encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                datos.append(float(row[columna]))
            except ValueError:
                continue
            except KeyError:
                print(f"La columna '{columna}' no existe.")
                return

    if datos:
        plt.plot(datos, label=columna)
        plt.title(f"Gráfica de la columna '{columna}'")
        plt.xlabel("Índice")
        plt.ylabel(columna)
        plt.legend()
        plt.show()
    else:
        print("Columna no encontrada o sin datos numéricos.")


def contar_palabras_y_caracteres(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        palabras = file.read()
    
        num_palabras = len(palabras.split())
        num_caracteres_con_espacios = len(palabras)
        num_caracteres_sin_espacios = len(palabras.replace(" ", "").replace("\n", "").replace("\t", ""))
            
        print(f"Número de palabras: {num_palabras}")
        print(f"Número de caracteres (con espacios): {num_caracteres_con_espacios}")
        print(f"Número de caracteres (sin espacios): {num_caracteres_sin_espacios}")
    

    
def reemplazar_palabra(ruta, palabra_buscar, palabra_reemplazar):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            contenido = file.read()
        
        nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazar)

        with open(ruta, 'w', encoding='utf-8') as file:
            file.write(nuevo_contenido)

        print(f"Se reemplazó '{palabra_buscar}' por '{palabra_reemplazar}' en el archivo.")
    except Exception:
        print("Ocurrió un error al procesar el archivo")
    
    
def histograma_vocales(ruta):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            texto = file.read().lower()
            for letra in texto:
                if letra in vocales:
                    vocales[letra] += 1

        print("\nFrecuencia de vocales:")
        for vocal, cantidad in vocales.items():
            print(f"{vocal.upper()}: {cantidad}")

     
        plt.bar(vocales.keys(), vocales.values())
        plt.title("Histograma de Vocales")
        plt.xlabel("Vocal")
        plt.ylabel("Frecuencia")
        plt.show()
    except Exception:
        print("Ocurrió un error al procesar el archivo")



def main():
    ruta = None
    while True:
        print("\nMenú Principal:")
        print("1. Listar archivos .txt y .csv ")
        print("2. Seleccionar archivo .csv o .txt")
        print("3. Mostrar las primeras 15 filas del archivo .csv")
        print("4. Calcular estadísticas de una columna en el archivo .csv")
        print("5. Graficar una columna en el archivo .csv")
        print("6. Contar número de palabras y caracteres")
        print("7. Reemplazar una palabra por otra")
        print("8. Histograma de ocurrencia de las vocales")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            listar_txt_csv()
        elif opcion == '2':
            ruta = seleccionar_archivo()
        elif opcion == '3':
            if ruta:
                mostrar_15_filas(ruta)
            else:
                print("Primero seleccione un archivo.")
        elif opcion == '4':
            if ruta:
                columna = input("Ingrese el nombre de la columna: ")
                calcular_estadisticas(ruta, columna)
            else:
                print("Primero seleccione un archivo.")
        elif opcion == '5':
            if ruta:
                columna = input("Ingrese el nombre de la columna: ")
                graficar_columna(ruta, columna)
            else:
                print("Primero seleccione un archivo.")
        elif opcion == '6':
            if ruta:
                contar_palabras_y_caracteres(ruta)
            else:
                print("Primero seleccione un archivo.")
        elif opcion == '7':
            if ruta:
                palabra_buscar = input("Ingrese la palabra a buscar: ")
                palabra_reemplazar = input("Ingrese la palabra a reemplazar: ")
                reemplazar_palabra(ruta, palabra_buscar, palabra_reemplazar)
            else:
                print("Primero seleccione un archivo.")
        elif opcion == '8':
            if ruta:
                histograma_vocales(ruta)
            else:
                print("Primero seleccione un archivo.")
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")



if __name__ == "__main__":
    main()
