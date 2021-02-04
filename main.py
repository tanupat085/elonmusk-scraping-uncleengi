from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time 

########################   LINE  ##############################
from songline import Sendline
token = ''
messenger = Sendline(token)
messenger.sendtext('hi')
###############################################################

driverpath = r'path drive chromedriver.exe'
#hidden google chrome
#ถ้าอยากให้มันขึ้น google chrome ให้เอา opt ออก
opt = webdriver.ChromeOptions()
opt.add_argument('headless')
driver = webdriver.Chrome(driverpath,options=opt)

def TwiterPost(twitter_name):
    url = 'https://twitter.com/{}'.format(twitter_name)
    driver.get(url)
    time.sleep(5)
    # pixel = 1000
    # for i in range(3):
    #     driver.execute_script("window.scrollTo(0,{})".format(pixel))
    #     time.sleep(3)
    #     pixel = pixel + 10000

    page_html = driver.page_source #print out html

    data = soup(page_html,'html.parser')
    posts = data.find_all('span',{'class':"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})

    founddot = False
    allpost = []
    for p in posts:
        txt = p.text
        if founddot == True :
            allpost.append(txt)
            founddot = False
        if txt == '·':
            founddot = True
        
 
    return allpost

checktwiter = ['elonmusk','BillGates']
for ct in checktwiter:
    texttoline = ''
    posted = TwiterPost(ct)
    print('-----{}-----'.format(ct))
    texttoline += '-----------{}--------'.format(ct)
    for p in posted:
        print(p)
        texttoline += p + '\n\n'
        print('-*-')
    messenger.sendtext(texttoline)

driver.close()
###########################


