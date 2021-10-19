from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars" 
browser = webdriver.Chrome("/Users/Tapas/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    Star_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs = {"class","exoplanets"}):
            li_tag = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tag):
                if index == 0 :
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except: 
                        temp_list.append("")
            Star_data.append(temp_list)
        browser.find_element_by_xpath("//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a").click()
        with open("scraper_2.csv","w")as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(Star_data)
scrape()