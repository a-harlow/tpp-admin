#to run: python load.py env users request_num
import tpp_test_scripts as t
import time
import sys

CLEANUP = False
HUNDRED = False
users = 1
request_num = 50

args = sys.argv
url = t.qa_url
if len(args) > 1:
    if args[1] == "uat":
        url =t.uat_url
    if args[1] == "dev":
        url = t.dev_url
    if len(args) > 2:
        users = int(args[2])
    if len(args) > 3:
        request_num = int(args[3])


driver_list = []

for u in range(users):
    driver = t.init_driver()
    driver_list.append(driver)

for driver in driver_list:
    t.login_tpp(driver,url)
    if HUNDRED:
        dropdown = driver.find_element_by_xpath('//div[@class="MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-1cccqvr"]')
        num_entries_dropdown_id = dropdown.get_attribute('id')
        t.dropdown_handler(driver,num_entries_dropdown_id,5,'//div[@id="'+num_entries_dropdown_id+'"]')

time.sleep(5)


to_search = "transpo"
end = len(to_search)
down = True
for r in range(request_num):
    current_search = to_search[0:end]
    if down:
        if end > 1:
            end-=1
        else:
            down = False
            end+=1
    else:
        if end < len(to_search):
            end+= 1
        else:
            down = True
            end-=1
    time.sleep(0.26)
    for driver in driver_list:
        t.text_to_search(driver,current_search,t.NAME_SEARCH_KEY,False)

if CLEANUP:
    for driver in driver_list:
        driver.close()
        driver.quit()   