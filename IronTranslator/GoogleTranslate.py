# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 21:05:39 2021

@author: M.ABDELMOULA
"""



from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import JavascriptException 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import TimeoutException


from tqdm import tqdm
from IronTranslator.constants import LANGUAGES_CODES, LANGUAGES_NAMES, MAIN_LINK


class Translator:
    def __init__(self,ChromeDriverPath):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless') 
            self.browser = webdriver.Chrome(executable_path=ChromeDriverPath,options=options)
        except Exception as e:
            print(e.args)
            
    def GetUrl(self, src, dest, text):
        newurl = ""
        url = "https://translate.google.com/?sl={}&tl={}&text=".format(src,dest)
        for word in text.split(" "):
            newurl = newurl + word +"%20"
        return url + newurl
        
    def translate(self, texts, dest='en', src='auto', TimeLimit = 360, **kwargs):
        
        dest = dest.lower()
        src = src.lower()
        text_translated = []

        
        if src != 'auto' and src not in LANGUAGES_CODES:
            if src in LANGUAGES_NAMES:
                src = LANGUAGES_NAMES[src]
            else:
                raise ValueError('Invalid source language')
                
        if dest not in LANGUAGES_CODES:
            if dest in LANGUAGES_NAMES:
                dest = LANGUAGES_NAMES[dest]
            else:
                raise ValueError('Invalid destination language')
                
        if type(texts) != list :
            raise ValueError('Texts input must be a list')
        
        if type(texts) == list :
            texts = [str(t) for t in texts]
        
        for text in tqdm(texts, bar_format='{l_bar}{bar:50}{r_bar}{bar:-50b}'):
            sub_text = ""
            link = self.GetUrl(src, dest, text)
            try: 
                self.browser.get(link)
                WebDriverWait(self.browser, TimeLimit).until(EC.presence_of_element_located(
                    (By.XPATH, './/span[@data-language-for-alternatives = "{}"]'.format(dest))))
                for elem in self.browser.find_elements_by_xpath('.//span[@data-language-for-alternatives = "{}"]'.format(dest)):
                    sub_text = sub_text + elem.text
                text_translated.append(sub_text) 
            except :
                raise ValueError('TimeoutException')
                
        self.browser.quit()
                    
        return text_translated
    




































