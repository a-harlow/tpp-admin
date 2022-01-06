from selenium import webdriver
import vehicles_detail
import time
import helpers as h

class VehiclesHome:
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.vehicle_link_xpath = '//a[@href="#"]'
        self.num_vehicles = len(self.driver.find_elements_by_xpath(self.vehicle_link_xpath))
        self.result_numbers_xpath = '//div[@class="MuiToolbar-root MuiToolbar-gutters MuiToolbar-regular MuiTablePagination-toolbar css-1wif0xq"]/p[2]'

        self.refresh()

    def search(self,search_text):
        self.search_field.send_keys(search_text)
        time.sleep(3)
    
    def clear_search(self):
        self.refresh()
        self.clear_search_button.click()
        self.refresh()

    def refresh(self):
        if len(self.driver.find_elements_by_xpath(self.vehicle_link_xpath)) > 0:
            self.num_providers = len(self.driver.find_elements_by_xpath(self.vehicle_link_xpath))
        else: 
            self.num_providers = 0
        self.search_field = self.driver.find_element_by_xpath('//input[@placeholder="Search for a Vehicle"]')
        self.clear_search_button = self.driver.find_element_by_xpath('//input[@placeholder="Search for a Vehicle"]//ancestor::div[1]/div/button')
        self.rows_per_page_dropdown = self.driver.find_element_by_xpath('//div[@class="MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-1cccqvr"]')
        self.next_page_button = self.driver.find_element_by_xpath('//button[@title="Go to next page"]')
        self.previous_page_button = self.driver.find_element_by_xpath('//button[@title="Go to previous page"]')
        self.sort_buttons = self.driver.find_elements_by_xpath('//div[@class="MuiDataGrid-columnHeader MuiDataGrid-columnHeader--sortable"]')
        self.delete_buttons = self.driver.find_elements_by_xpath('//button[@data-testid="delete"]')
        self.providers_button = self.driver.find_element_by_xpath('//a[contains(text(),"Transportation Providers")]')
        self.drivers_button = self.driver.find_element_by_xpath('//a[contains(text(),"Drivers")]')
    
    def get_fresh_provider_links(self):
        return self.driver.find_elements_by_xpath(self.vehicle_link_xpath)
    
    def open_vehicle_detail(self,entry_index = 0) -> vehicles_detail.VehicleDetail:
        links = self.get_fresh_provider_links()
        links[entry_index].click()
        time.sleep(1)
        this_vehicle = vehicles_detail.VehicleDetail(self.driver)
        return this_vehicle