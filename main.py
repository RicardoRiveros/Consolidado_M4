from abc import ABC
from io import open
import csv

'''PARTE 1'''

#Creacion de las clases
#Se crea la clase abstracta Vehiculo
class Vehiculo(ABC):
    def __init__(self,marca: str,modelo: str,numero_de_ruedas: int):
        self.marca=marca
        self.modelo=modelo
        self.numero_de_ruedas=numero_de_ruedas

#Se crea la clase Automovil, que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca:str, modelo:str, numero_de_ruedas:int, velocidad :int, cilindrada:int ):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc"


#Menu para realizar las interacciones con el usuario
automoviles=[]
cantidad=int(input('Cuantos Vehiculos desea insertar: '))

#Se ingresan los vehiculos segun la cantidad indicada por el usuario
for i in range(1, cantidad +1):
    print(f'Datos del automovil {i}')
    marca=input('Inserte la marca del automovil: ')
    modelo=input('Inserte el modelo: ')
    numero_de_ruedas=int(input('Inserte el numero de ruedas: '))
    velocidad=int(input('Inserte la velocidad en km/h: '))
    cilindrada=int(input('Inserte el cilindraje en cc: '))
    automoviles.append(Automovil(marca,modelo,numero_de_ruedas, velocidad,cilindrada))

#Se imprime por pantalla los vehiculos ingresados
print('\nImprimiendo por pantalla los vehiculos: ')

#Se genera un for para imprimir cada auto dentro de la lista automoviles, se utiliza el enumerate para inicial el index en 1, asi utilizarilo en al imprimir el automovil indicando su numero identificador
for i, auto in enumerate(automoviles, start=1):
    print(f'\nDatos del automovil {i}: {auto}')



'''PARTE 2'''
#Crear las clases de automovil particular y de carga

class Particular(Automovil):
    def __init__(self, marca: str, modelo: str, numero_de_ruedas: int, velocidad: int, cilindrada: int, numero_puestos:int):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self.numero_puestos=numero_puestos

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc Puestos {self.numero_puestos}"


class Carga(Automovil):
    def __init__(self, marca: str, modelo: str, numero_de_ruedas: int, velocidad: int, cilindrada: int, peso_carga:int):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self.peso_carga=peso_carga

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc Carga: {self.peso_carga} Kg "

#Hereda directamente desde Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, numero_de_ruedas: int, tipo_bicicleta:str):
        super().__init__(marca, modelo, numero_de_ruedas)
        
        #Se valida las opciones de tipo de bicicleta es correcta segun opciones

        if tipo_bicicleta not in ['Urbana', 'Carrera']:
            raise ValueError("El tipo de bicileta debe ser 'Ubana' o 'Carrera")

        self.tipo_bicicleta=tipo_bicicleta

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas  Tipo: {self.tipo_bicicleta}"


class Motocicleta(Bicicleta): 
    def __init__(self, marca: str, modelo: str, numero_de_ruedas: int, tipo_bicicleta: str,motor:str, cuadro:str, nro_radios:int):
        super().__init__(marca, modelo, numero_de_ruedas, tipo_bicicleta)

        if cuadro not in ['doble cuna', 'multitubolar', 'doble viga']:
            raise ValueError("El tipo de cuadro debe ser: doble cuna o multitubolar o doble viga")

        if motor not in ['2T', '4T']:
            raise ValueError("Tipo de motor debe ser: 2T o 4T")

        self.nro_radios=nro_radios
        self.cuadro=cuadro
        self.motor=motor

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas  Tipo: {self.tipo_bicicleta} Motor: {self.motor} Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"


particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
#En la guia se indica primero que la clase bicicleta tiene 2 tipos solente Urbana o Carrera, pero despues se nombre Deportiva en la motocicleta, que es una clase que hereda de bicicleta, por lo tanto la opcion Deportiva no es valida, por lo que se cambia a Carrera
motocicleta = Motocicleta("BMW", "F800s",2,"Carrera","2T","doble viga", 21)

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print('\nMotocicleta es instancia con relacion a Vehiculo:', isinstance(motocicleta, Vehiculo))
print('Motocicleta es instancia con relacion a Automovil:', isinstance(motocicleta, Automovil))
print('Motocicleta es instancia con relacion a Vehiculo Particular:', isinstance(motocicleta, Particular))
print('Motocicleta es instancia con relacion a Vehiculo de Carga:', isinstance(motocicleta, Carga))
print('Motocicleta es instancia con relacion a Bicicleta:', isinstance(motocicleta, Bicicleta))
print('Motocicleta es instancia con relacion a Motocicleta:', isinstance(motocicleta, Motocicleta))

'''PARTE 3'''
    
def crear_archivo():
    try:
        archivo = open('vehiculos.csv', 'x')
        archivo.close()
    except FileExistsError:
        print("El archivo datos.cvs existe o a sido creado previamente")
    except Exception as error:
        print('Se ha generado un error no previsto',
type(error).__name__)


def guardar_datos_csv(*vehiculos):
    archivo = "vehiculos.csv"

    with open(archivo, mode="w", newline="") as file:
        writer = csv.writer(file)
            
        for vehiculo in vehiculos:
            tipo = type(vehiculo).__name__
            datos = str(vehiculo)
            writer.writerow([tipo, datos])

    print(f"Datos guardados en {archivo} correctamente.")

guardar_datos_csv(particular, carga, bicicleta, motocicleta)
    

def leer_datos_csv(archivo):
    try:
        with open(archivo, mode='r') as archivo:
            lector = csv.reader(archivo)
            datos = [fila for fila in lector]
        return datos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{archivo}'.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

archivo = "vehiculos.csv"
filas = leer_datos_csv(archivo)
if filas:
    for fila in filas:
        print(fila)