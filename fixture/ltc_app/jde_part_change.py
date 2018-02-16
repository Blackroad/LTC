class Jde_Part_Change:
    def __init__(self,app):
        self.app = app

    def fetch_JDE_status(self,lot_type):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath("//tbody[@data-bind='foreach: JdePartChanges']//tr")) == 0:
            wd.find_element_by_xpath("//*//span[text()='Fetch JDE Part Status']").click()
            wd.find_element_by_xpath("//select/option[@value='%s']" % lot_type).click()
        pass