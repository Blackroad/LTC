from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fixture.ltc_app.background import BackgroundHelper
from fixture.ltc_app.jde_lot_change import Jde_Lot_Change
from fixture.ltc_app.jde_part_change import Jde_Part_Change
from fixture.ltc_app.mes_lot_change import Mes_Lot_Change

class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.wd = webdriver.Chrome(chrome_options=options)
            self.wd.implicitly_wait(5)
        elif browser == "InternetExplorer":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.base_url = config["web"]["baseURL"]
        self.background = BackgroundHelper(self)
        self.jde_lot_change = Jde_Lot_Change(self)
        self.jde_part_change = Jde_Part_Change(self)
        self.mes_lot_change = Mes_Lot_Change(self)
        self.config = config

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def edit_document(self):
        self.wd.find_element_by_xpath("//div[@class='ms-rtestate-field']/a[text()='Edit']").click()
        if self.wd.find_element_by_xpath("//*[@class='section currentItem']").text != 'Background':
            self.wd.find_element_by_xpath("//*[@class='section']/a[text()='Background']").click()

    def save_changes(self):
        self.wd.find_element_by_xpath("//*[@id='menu']//a[@href]").click()

    def publish(self):
        self.wd.find_element_by_xpath("//*[@id='menu']//li[5]/a[@href]").click()
        if self.wd.find_element_by_xpath("//*[@id='ui-id-4' and text()='Notification']").text == 'Notification':
            self.wd.find_element_by_xpath("//*[@class='ui-dialog-buttonset']//span[text()='Continue']").click()
        else:
            pass

    def export_to_word(self):
        self.wd.find_element_by_xpath("//*[@id='menu']//li[4]/a[@href]").click()

    def wait(self, element):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, element)))

    def back_to_sharepoint(self):
        self.wd.find_element_by_xpath("//*[@id='menu']/li/a[text()='Back to SharePoint']").click()

    def navigate_to(self,section_name):
        if self.wd.find_element_by_xpath("//*[@class='section currentItem']").text != section_name:
            self.wd.find_element_by_xpath("//*[@href and text()='%s']" %(section_name)).click()
            if self.wd.find_element_by_xpath("//*[@id='ui-id-4' and text()='Notification']").text == 'Notification':
                self.wd.find_element_by_xpath("//*[@class='ui-dialog-buttonset']//span[text()='Continue']").click()
            pass
        pass


    def error_checker(self, item_name):
        wd = self.wd
        set_of_items = wd.find_elements_by_xpath("//*[@id='leftMenuBar']//div[@class='section']/a")
        item_index = self.get_index(item_name, set_of_items)
        counter = wd.find_element_by_xpath("//*[@id='leftMenuBar']//div[@class='section'][%s]/span"
                                           % (item_index))
        if counter.text == '0':
            return True
        return False

    def get_index(self, item_name, set_of_items):
        item_index = None
        for element in set_of_items:
            if item_name == element.text:
                item_index = int(set_of_items.index(element)) + 1
                break
        return item_index

    def identify_in_current_section(self):
        wd = self.wd
        current_section = wd.find_element_by_xpath("//div[@id='navigationBar']//a[@class='currentItem']").text
        return current_section

    def destroy(self):
        self.wd.quit()

