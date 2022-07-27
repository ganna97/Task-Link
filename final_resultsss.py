#!/usr/bin/env python
# coding: utf-8

# In[16]:


import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from tqdm import tqdm_notebook
#from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:\\Users\\Admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://www.amazon.de/dp/000101742X"
driver.get(url)
#driver.find_element_by_xpath("//input[@class='a-button-input celwidget']").click()
driver.find_element('xpath', "//input[@class='a-button-input celwidget']").click()


#user_name=driver.find_element_by_xpath('//*[@id="username"]')
#user_name.send_keys("sureshkumarbevara1527@gmail.com")
#pass_word=driver.find_element_by_xpath('//*[@id="password"]')
#pass_word.send_keys("Rams@1227")
#driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()


# In[3]:


driver.


# In[17]:


import time
import pandas as pd
url_data=pd.read_csv("C:\\Users\\Admin\\Downloads\\res_link.csv")
url=url_data.links
url


# In[18]:


from tqdm.notebook import tqdm


# In[19]:


link=[]
name=[]
logo=[]
pr=[]
de=[]


for i in tqdm(range(0,len(url))):
    driver.get(url[i])
    time.sleep(3)
    print(i)
    
    #url
    link.append(url[i])
    try:
        #driver.find_element_by_xpath("//input[@class='a-button-input celwidget']").click()
        driver.find_element('xpath', "//input[@class='a-button-input celwidget']").click()

    except NoSuchElementException:
        pass
    
    #//span[@dir='ltr'][1]
    #name of the url
    try:
        #na=driver.find_element_by_xpath("//span[@class='a-size-extra-large']")
        na=driver.find_element('xpath', "//span[@class='a-size-extra-large']")

        #na=driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/h1")
        print(na.text)
        #print(len(k.text))
        name.append(na.text)
    except NoSuchElementException:
        print("none")
        name.append("none")
            
        #if k.text in name:
            #print(k.text)
        #else:
            #name.append("NaN")
            #print(name)

    #product image url
    try:
        #indu=driver.find_element_by_xpath("//div[@class='maintain-height  image-2d']//img").get_attribute("src")
        indu=driver.find_element('xpath', "//div[@class='maintain-height  image-2d']//img").get_attribute("src")

        print(indu)
        #print(len(k.text))
        logo.append(indu)
    except NoSuchElementException:
        print("none")
        logo.append("none")
        
        #if k.text in ind:
            #print(k.text)
        #else:
            #ind.append("NaN")
            #print(ind)
    

    #price of the product
    try:
        #he=driver.find_element_by_xpath("//span[@class='a-size-base a-color-price a-color-price']")
        he=driver.find_element('xpath', "//span[@class='a-size-base a-color-price a-color-price']")

        print(he.text)
        #print(len(k.text))
        pr.append(he.text)
    except NoSuchElementException:
        print("none")
        pr.append("none")
        
        #if k.text in head:
            #print(k.text)
        #else:
            #ind.append("NaN")
            #print(head)
   
    #product details
    try:
        #fol=driver.find_element_by_xpath("//ul[@class='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']")
        fol=driver.find_element('xpath', "//ul[@class='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list']")

        print(fol.text)
        #print(len(k.text))
        de.append(fol.text)
    except NoSuchElementException:
        print("none")
        de.append("none")
        
        #if k.text in foll:
            #print(k.text)
        #else:
            #foll.append("NaN")
            #print(foll)

    


# In[20]:


print(len(link));print(len(name));print(len(logo));print(len(pr));print(len(de))


# In[21]:


df=pd.DataFrame()
df["link"]=link
df["Product_name"]=name
df["Product_image_url"]=logo
df["Price_of_the_product"]=pr
df["Product_details"]=de


# In[22]:


df


# In[31]:


df.loc[df["Product_name"]!="none",]


# In[26]:


df.to_csv("final_res.csv",index=False)


# In[35]:


pwd


# In[34]:


df.to_json("“Task_results")


# In[ ]:




