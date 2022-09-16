#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!")


# In[2]:


x = 5
print(x)


# In[6]:


print(type(x))


# In[7]:


preco = 19.99
print(preco, type(preco))


# In[8]:


3 > 2 > 1


# In[12]:


x = 10
y = 2
print(x / y)
print(x // y)
print(x % y)


# In[13]:


tem_cafe = True
print(not tem_cafe) #operadores: or, and, not


# In[14]:


idade = input("Insira a idade")
print(idade, type(idade)) # como no C# o input sempre retorna string


# In[15]:


idade = int(idade)
print(idade, type(idade))


# In[20]:


valor_passagem = 4.3
valor_corrida = input("Qual valor da corrida?")
if float(valor_corrida) <= valor_passagem * 4:
    print("Pague a corrida")
elif float(valor_corrida) <= valor_passagem * 6:
    print("Aguarde um pouco, o valor pode baixar.")
else: print("Pegue o bus")


# In[21]:


contador = 0
while contador < 10:
    contador += 1
    if contador == 1:
        print("Item limpo")
    else:
        print("Itens limpos")
print("Fim da lavação")


# In[ ]:




