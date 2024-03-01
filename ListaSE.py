class Nodo:
    def __init__(self,valor):
        self.dato = valor
        self.siguiente = None
#Fin de la Clase Nodo


class ListaSE:
    def __init__(self):
        self.cabeza = None
        
    def agregarInicio(self,valor):
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza is None: 
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
    
    def agregarFinal(self,valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return 
        else:
            temp = self.cabeza
            while temp.siguiente is not None:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            
    def eliminarPrimero(self):
        if self.cabeza is None:
            return
        else:
            self.cabeza = self.cabeza.siguiente
            
    def eliminarUltimo(self):
        if self.cabeza is None:
            return
        else:
            if self.cabeza.siguiente is None:
                self.cabeza = None
            else:
                temp = self.cabeza
                while temp.siguiente is not None:
                    if temp.siguiente.siguiente is None:
                        temp.siguiente = None
                        return
                    temp = temp.siguiente
                    
    def buscarValor(self,valor):
         if self.cabeza is None:
             return "Falso"
         else:
             temp = self.cabeza
             while temp.siguiente is not None:
                 temp = temp.siguiente
                 if temp.dato == valor:
                     return "Verdadero"

             return "Falso"
    def imprimeLista(self):
        if self.cabeza is None:
            return
        else:
            temp = self.cabeza
            while temp is not None:
                print(temp.dato)
                temp = temp.siguiente
                
    def contarLista(self):
        if self.cabeza is None:
            return "La lista se encuentra vacia"
        else:
            count = 0
            temp = self.cabeza
            while temp is not None:
                temp = temp.siguiente
                count +=1
                
            return count
    def listaVacia(self):
        if self.cabeza is None:
            return "Verdadero"
        else:
            return "Falso"
#Fin de la Clase ListaSE


#Creacion de una lista Simplemente enlazada
ListaSimple = ListaSE()
print(f"La lista está vacia?: {ListaSimple.listaVacia()}")


#Se agrega un valor al inicio y se imprime
ListaSimple.agregarInicio(5)
print(f"Valor agregado :{ListaSimple.cabeza.dato}")


#Se agrega otro valor al inicio y se imprime
ListaSimple.agregarInicio(8)
print(f"Valor agregado :{ListaSimple.cabeza.dato}")


#Agregar al final
ListaSimple.agregarFinal(3)
ListaSimple.agregarFinal(4)
print("Agregados los numeros 3 y 4 al final de la lista")



#Cuenta los elementos de la lista
print(f"Cantidad de elementos en la lista {ListaSimple.contarLista()}")

#Busca en la lista por valor
print(f"Está el 7 en la lista: {ListaSimple.buscarValor(7)}")


ListaSimple.agregarFinal(7)
print("Agregado el numero 7 al final de la lista")

print(f"Está el 7 en la lista: {ListaSimple.buscarValor(7)}")


#Imprime la lista
ListaSimple.imprimeLista()


print(f"Cantidad de elementos en la lista {ListaSimple.contarLista()}")


print(f"La lista está vacia?: {ListaSimple.listaVacia()}")

