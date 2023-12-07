#!/usr/bin/env python
# coding: utf-8

# In[76]:


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# In[77]:


driver = webdriver.Chrome(executable_path=r"C:\Users\is038\anaconda3\chromedriver-win64\chromedriver.exe")


# In[79]:


driver.get('https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/')


# In[80]:


add_to_cart_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'countCta')))
ActionChains(driver).move_to_element(add_to_cart_button).click().perform()


# In[83]:


add_button_in_popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'addCTA')))


# In[84]:


ActionChains(driver).move_to_element(add_button_in_popup).click().perform()


# In[85]:


final_price_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'finalPrice')))
final_price = final_price_element.text
print(f"Final Price: {final_price}")


# In[86]:


driver.quit()


# In[ ]:




