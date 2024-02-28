#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Nodo:
    def __init__(self,valor):
        self.dato = valor
        self.siguiente = None
#Fin de la Clase Nodo


# In[29]:


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

#Fin de la Clase ListaSE
        


# In[33]:


ListaSimple = ListaSE()


# In[34]:


ListaSimple.agregarInicio(5)
print(ListaSimple.cabeza.dato)


# In[35]:


ListaSimple.agregarInicio(8)
print(ListaSimple.cabeza.dato)

