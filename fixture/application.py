from selenium import webdriver


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def edit_document(self):
        self.wd.find_element_by_xpath("//div[@class = 'ms-rtestate-field']/a").click()
        self.wd.find_element_by_xpath("//ul[@id='menu']//a[@class='editDocument']").click()

    def error_checker(self,section, item_name):
        wd = self.wd
        set_of_items = wd.find_elements_by_xpath("//div[@id='leftMenuBar']//li[@class='node']/a")
        item_index = self.get_index(item_name, set_of_items)
        counter = wd.find_element_by_xpath("//div[@id='leftMenuBar']//ul[%s]//li[%s]/span[@class='errorsCount']"
                                           % (section,item_index))
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

