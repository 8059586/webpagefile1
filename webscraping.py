from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

startURL="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe")
browser.get(startURL)
time.sleep(10)

def scrape():
    headers = ["name","Lightyears from Earth","Planet Mass", "Stellar Magnitude", "Discovery Date"]
    planet_data = []

    for i in range(0,448):
        Soup = BeautifulSoup(browser.page_source,"html.parser")
        
        for ultag in Soup.find_all("ul",attrs={"class","exoplanet"}):
            litags = ultag.find_all("li")
            templist = []
            for index,litag in enumerate(litags):
                if index == 0:
                    templist.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(litag.contents[0])
                    except:
                        templist.append("")
            planet_data.append(templist)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper1.csv","w")as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()