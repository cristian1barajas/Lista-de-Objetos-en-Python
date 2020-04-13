class Galleta(object):
    def __init__(self):
        self.chipChocolate = 0
        self.sabor = ""
        self.forma = ""
        self.crema = ""
        self.porciones = 0
    def entregar(self):
        print("Chips de chocolate: {}".format(self.chipChocolate))
        print("Sabor: {}".format(self.sabor))
        print("Forma: {}".format(self.forma))
        print("Crema: {}".format(self.crema))
        print("Porciones: {}".format(self.porciones))

listaGalletas = []
n = 1

def solicitar():
        objGalleta = Galleta()
        objGalleta.chipChocolate = int(raw_input("Numero de chips de chocolate: "))
        objGalleta.sabor = raw_input("Que sabor desea: ")
        objGalleta.forma = raw_input("Que forma geometrica prefiere: ")
        objGalleta.crema = int(raw_input("Con crema = 1, sin crema = 0: "))
        objGalleta.porciones = int(raw_input("Indique el numero de porciones: "))
        listaGalletas.append(objGalleta)

def main():
    while True:
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Recetar Galleta")
        print("2.- Entregar Galleta")
        print("3.- Salir")

        opcion = int(raw_input("Opcion: "))

        if opcion == 1:
            solicitar()
        elif opcion == 2:
            print("Galleta: {}".format(n))
            listaGalletas[n].entregar()
        elif opcion == 3:
            print("Salida")
        else:
            print("Digite una opcion valida!")

if __name__ == '__main__':
    main()