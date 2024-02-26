import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tabulate import tabulate
import pandas as pd
import time
import numpy as np

headers = ['Date','Race', "Location", "Distance", "Course", "Track", "Going"]
df = pd.DataFrame(columns=headers)
date_list= np.loadtxt(r"/Users/kevinliu/Desktop/RaceDateList.csv",
                 delimiter=",", dtype=str)
# create a new Chrome driver
#PATH = r""
#driver = webdriver.Chrome(PATH)
for date in date_list:
    print(date)
    for i in range(1, 12):
        try:
            url = f"https://racing.hkjc.com/racing/information/English/Racing/LocalResults.aspx?RaceDate={date}&RaceNo={i}"
            driver.get(url)
            # Find the table containing the race results
            table = driver.find_element(By.CLASS_NAME, "performance")
            location = driver.find_element(By.CSS_SELECTOR, "span[style*='color:#666666'][style*='font-size:12px'][style*='font-weight:700'][style*='font-family:Arial'], span[style*='color:#666666'][style*='font-size:12px'][style*='font-weight:700'][style*='font-family:Verdana'], span[style*='color:#666666'][style*='font-size:12px'][style*='font-weight:700'][style*='font-family:Helvetica'], span[style*='color:#666666'][style*='font-size:12px'][style*='font-weight:700'][style*='font-family:sans-serif']").text.replace(":", "")

            x = race_information_rows[1][0].split("-")
            y = race_information_rows[2][2].split("-")
            rank = x[0]
            distance = x[1]
            track = y[0]

            df_data = [date, race_num,location, distance, rank, track, going]

            df.loc[len(df)] = df_data
            
        except Exception as e:
            print(e)
            pass
