# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:16:02 2020

@author: hsola
"""
from selenium import webdriver
#from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd

BSE_List = pd.read_csv("Delistedstocks.csv")
BSE_Codes = BSE_List.BSE_code
 
Delisted_Stocks = {}
for stock_name in BSE_Codes:
    Delisted_Stocks[stock_name] = pd.DataFrame()

for i in range(1,len(BSE_List)):
    i = 12
    Code = str(BSE_List.Code[i])
    Company = BSE_List.Company[i]
    qtrid = str(65.50)
    url = "https://www.bseindia.com/corporates/results.aspx?Code="+Code+ "&Company="+Company+"&qtr="+qtrid+"&RType="

    driver = webdriver.Chrome()
    driver.get(url)
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    Type= bs.find(id = "ContentPlaceHolder1_lblresulttype")
    #Type = driver.find_element_by_id('ContentPlaceHolder1_lblresulttype')
    driver.find_element_by_id('ContentPlaceHolder1_lnkDetailed').click()
    # select = driver.find_element_by_id('ContentPlaceHolder1_lnkDetailed')
    # select = select.click()
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    table = bs.find_all('table')[3]

    table_rows = table.find_all('tr')

    res = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        if row:
            res.append(row)

    df = pd.DataFrame(res, columns=["A", "B"])
    Delisted_Stocks[BSE_Codes[i]] = df 
    driver.close()