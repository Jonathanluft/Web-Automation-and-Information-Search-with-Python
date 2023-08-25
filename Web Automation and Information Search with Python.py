#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e compramos e vendemos commodities:
# - Soja, Milho, Trigo, Petróleo, etc.
# 
# Precisamos pegar na internet, de forma automática, a cotação de todas as commodites e ver se ela está abaixo do nosso preço ideal de compra. Se tiver, precisamos marcar como uma ação de compra para a equipe de operações.
# 
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=share_link
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# In[50]:


#passo a passo
#passo 1 -> abrir navegador
from selenium import webdriver
navegador=webdriver.Chrome()
navegador.get("https://google.com/")


# In[2]:


#passo 2 -> importar base de dados
import pandas as pd
tabela=pd.read_excel("commodities.xlsx")
display(tabela)


# In[55]:


#passo 3 -> pesquisar o preço
for linha in tabela.index:
    produto=tabela.loc[linha,"Produto"]
    print(produto)
    
    produto=produto.replace("ó","o").replace("ã","a").replace("ú","u").replace("é","e").replace(
    "í","i").replace("ç","c").replace("á","a")

    link= f"https://www.melhorcambio.com/{produto}-hoje"
    navegador.get(link)
    
    preco=navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
    preco=preco.replace(".","").replace(",",".")
    print(preco)
    #passo 4 -> atualizar a base de dado
    tabela.loc[linha,"Preço Atual"]=float(preco)
display(tabela)

#.clicl()->clicar
#.send_keys("texto") -> esrever
#.get_attribute() -> pegar um valor




# In[59]:


#passo 5 -> decidir quais produtos comprar
tabela["Comprar"]=tabela["Preço Atual"] < tabela["Preço Ideal"]
display(tabela)


# In[61]:


tabela.to_excel("Commodities_atualizada.xlsx",index=False)


# In[ ]:


navegador.quit()

