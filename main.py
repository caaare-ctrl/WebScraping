from selenium import webdriver
import csv
import pandas as pd
#contain a bunch of constant
# it is shorter than using bs4 from import request -> make soup
# bs4 is good for scraping html website but not good for site with js angular react...

# webdriver can drive the chrome browser or other browswe like firefox
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

scrap_url = "https://steamdb.info/"
driver.get(scrap_url)

tables = driver.find_elements_by_tag_name("table")
for i in range(len(tables)):
    all_data = []
    files_name = ["most_played.csv","trending.csv","popular_releases.csv","hot_release.csv"]
    names = tables[i].find_elements_by_tag_name("thead tr th")
    column_name = [name.text for name in names]
    print(column_name)
    rows = tables[i].find_elements_by_tag_name("tr")

    for row in rows:
        columns = row.find_elements_by_tag_name("td")
        steam_row = [data.text for data in columns if data.text]
        if steam_row:
            all_data.append(steam_row)
        with open(files_name[i], "w",newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(column_name)
            writer.writerows(all_data)

driver.close()


#
df = pd.read_csv("steam_most_played.csv")
print(df)