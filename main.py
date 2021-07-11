import csv, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
import xlsxwriter
import argparse
parser = argparse.ArgumentParser(description="A argument is required: start_idx")
parser.add_argument("-o", "--outfilename", help="out file name")
parser.add_argument("-s", "--start_idx", type=int, help="'start index' counting from 1")
parser.add_argument("-e", "--end_idx", type=int, help="'end index'")
args = parser.parse_args()
if not args.start_idx:
    args.start_idx = 1
if not args.end_idx:
    args.end_idx = args.start_idx + 10
if not args.outfilename:
    args.outfilename = "result(" + str(args.start_idx) + "-" + str(args.end_idx) + ").txt"

f = open(args.outfilename,'w',encoding = 'utf-8')
# workbook = xlsxwriter.Workbook('scrapResult.xlsx')
# worksheet = workbook.add_worksheet("post_code")
today = datetime.today().strftime('%A %d %b, %Y')
driver = webdriver.Chrome()
row = 0
## ---------------------------------
driver.get("https://www.childcarefinder.gov.au/search/nsw/2127/sydney+olympic+park?geo=-33.8481431%2C151.0723825&sortOrder=order-tier&service_type=ZCDC,ZFDC,ZOSH")

for x in range(args.start_idx,args.end_idx): # To set range(1, 10000)
    print('input' + str(x))
    driver.find_element_by_id("main_search").clear()
    driver.find_element_by_id("main_search").send_keys(x)
    time.sleep(2)
    pac_container = driver.find_element_by_class_name("pac-container")
    pac_items = pac_container.find_elements_by_tag_name("div")
    print('output ' + str(len(pac_items)))
    if(len(pac_items)>0):
        
        for items in pac_items:
            txt = ""
            # row += 1
            # print(row)
            for item in items.find_elements_by_tag_name("span"):
                txt +=item.text
            # worksheet.write(row, 0, txt)
            f.write(txt + "\n")
        
        
driver.close()
# workbook.close()




