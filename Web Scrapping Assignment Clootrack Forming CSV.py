#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
url = 'https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/'
HtmlData = requests.get(url).text
data = bs(HtmlData, 'html.parser')


# In[14]:


items = data.find_all('section', class_='categoryItemHolder')
menu3_df = pd.DataFrame(columns=['Name', 'Price'])
for item in items:
    name = item.find('a', class_='itemName').text.strip()
    price_with_currency = item.find('span', class_='itemPrice').text.strip()
    price = price_with_currency.replace('₹', '').strip()
    menu3_df = pd.concat([menu3_df, pd.DataFrame({'Name': [name], 'Price': [price]})], ignore_index=True)
menu3_df.to_csv('menu3_data.csv', index=False, encoding='utf-8')
print("CSV file created successfully!")


# In[ ]:




