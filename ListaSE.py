#!/usr/bin/env python
# coding: utf-8

# In[176]:


class Nodo:
    def __init__(self,valor):
        self.dato = valor
        self.siguiente = None
#Fin de la Clase Nodo


# In[177]:


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
            while temp.siguiente is not None:
                temp = temp.siguiente
                print(temp.dato)
    def contarLista(self):
        if self.cabeza is None:
            return "La lista se encuentra vacia"
        else:
            count = 0
            temp = self.cabeza
            while temp.siguiente is not None:
                count +=1
                temp = temp.siguiente
            return count
    def listaVacia(self):
        if self.cabeza is None:
            return "Verdadero"
        else:
            return "Falso"
#Fin de la Clase ListaSE


# In[178]:


#Creacion de una lista Simplemente enlazada
ListaSimple = ListaSE()
ListaSimple.listaVacia()


# In[179]:


#Se agrega un valor al inicio y se imprime
ListaSimple.agregarInicio(5)
print(ListaSimple.cabeza.dato)


# In[180]:


#Se agrega otro valor al inicio y se imprime
ListaSimple.agregarInicio(8)
print(ListaSimple.cabeza.dato)


# In[181]:


ListaSimple.agregarFinal(3)
ListaSimple.agregarFinal(4)


# In[182]:


ListaSimple.imprimeLista()


# In[183]:


ListaSimple.contarLista()


# In[184]:


ListaSimple.buscarValor(7)


# In[185]:


ListaSimple.agregarFinal(7)


# In[186]:


ListaSimple.buscarValor(7)


# In[187]:


ListaSimple.imprimeLista()


# In[188]:


ListaSimple.contarLista()


# In[189]:


ListaSimple.listaVacia()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




