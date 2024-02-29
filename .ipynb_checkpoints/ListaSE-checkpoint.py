#!/usr/bin/env python
# coding: utf-8

# In[60]:


class Nodo:
    def __init__(self,valor):
        self.dato = valor
        self.siguiente = None
#Fin de la Clase Nodo


# In[85]:


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
                 if temp.dato == valor:
                     return "Verdadero"
                 temp = temp.siguiente

             return "Falso"

#Fin de la Clase ListaSE
        


# In[86]:


ListaSimple = ListaSE()


# In[87]:


ListaSimple.agregarInicio(1)
print(ListaSimple.cabeza.dato)


# In[88]:


ListaSimple.agregarInicio(2)
print(ListaSimple.cabeza.dato)


# In[89]:


ListaSimple.agregarFinal(3)
ListaSimple.agregarFinal(4)


# In[90]:


print(ListaSimple.cabeza.dato)
print(ListaSimple.cabeza.siguiente.dato)
print(ListaSimple.cabeza.siguiente.siguiente.dato)
print(ListaSimple.cabeza.siguiente.siguiente.siguiente.dato)


# In[ ]:





# In[92]:


print(ListaSimple.cabeza.dato)
print(ListaSimple.cabeza.siguiente.dato)
print(ListaSimple.cabeza.siguiente.siguiente.dato)
print(ListaSimple.cabeza.siguiente.siguiente.siguiente.dato)


# In[95]:


ListaSimple.buscarValor(7)


# In[ ]:




