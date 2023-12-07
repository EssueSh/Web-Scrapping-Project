#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
from bs4 import BeautifulSoup as bs
url = 'https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/'
HtmlData = requests.get(url).text
data = bs(HtmlData, 'html.parser')


# In[46]:


items = data.find_all('section', class_='categoryItemHolder')

for item in items:
    name = item.find('a', class_='itemName').text.strip()
    price = item.find('span', class_='itemPrice').text.strip()
    print(f"{name} , Price= {price}")


# In[ ]:




