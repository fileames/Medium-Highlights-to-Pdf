from bs4 import BeautifulSoup

import sys
sys.path.append('/Users/elifs/anaconda3/envs/py64/Lib/site-packages/selenium-3.141.0-py3.8.egg')
sys.path.append('/Users/elifs/anaconda3/envs/py64/Lib/site-packages')



from pageStructure import create_doc 

from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from reportlab.lib.styles import ParagraphStyle

import os.path
from os import path

import reportlab.platypus as platypus





browser = webdriver.Chrome(executable_path=r'/Users/elifs/Desktop/bin/chromedriver.exe')


doc = create_doc(2)


def ask_for_login():
    browser.get("https://medium.com/")
    #Ask if logged in
    inp = input("Logged in?")


import reportlab.lib
posts = []
inch = reportlab.lib.units.inch
style = reportlab.lib.styles.getSampleStyleSheet()

headlineStyle = style["Heading2"]
paraStyle = style["Normal"]
paraStyle.spaceAfter = inch*.04
paraStyle.alignment=reportlab.lib.enums.TA_JUSTIFY

mainHeadlineStyle = style["Heading1"]

def create_posts(url):
    browser.get(url)

    inp = input("Is the loading complete?")

    src = browser.page_source 
    soup = BeautifulSoup(src, 'html.parser')
    y = soup.findAll("mark")

    cl1 = y[0].get("class")
    cl2 = y[-1].get("class")

    dont_look=""

    if cl1 != cl2:
        dont_look = cl1


    header = soup.select('h1')[0].text
    header = '<link href="' + url + '">' + header + '</link>'

    items = []
    mainHeadline = platypus.Paragraph(header, mainHeadlineStyle)
    items.append(mainHeadline)
    posts.append(mainHeadline)
    for m in y:
        if(m.get("class") == dont_look):
            continue

        body = m.text
        parent = m.parent
        if parent.name == 'h1':
            item = platypus.KeepTogether(items)
            items=[]
            headline = platypus.Paragraph(parent.text, headlineStyle)
            posts.append(headline)
            items.append(headline)
        else:
            sib = parent.previous_sibling
            t=False
            if not sib:
                t=True
            else:
            
                while sib.name != 'h1':

                    if  not sib.previous_sibling:
                        sib = sib.parent
                    else:
                        sib = sib.previous_sibling

                    if not sib:
                        t = True
                        break
                
            if(t):
                para = platypus.Paragraph(body, paraStyle)
                posts.append(para)
            else:
                if(sib.text == items[0].text):
                    para = platypus.Paragraph(body, paraStyle)
                    items.append(para)
                    posts.append(para)
                else:
                    item = platypus.KeepTogether(items)
                    items=[]
                    headline = platypus.Paragraph(sib.text, headlineStyle)
                    items.append(headline)
                    posts.append(headline)
                    para = platypus.Paragraph(body, paraStyle)
                    items.append(para)
                    posts.append(para)



ask_for_login()

urlFile = open(sys.argv[1], 'r') 
lines = urlFile.readlines()
for line in lines: 
    create_posts(line)

browser.quit()
doc.build(posts)
