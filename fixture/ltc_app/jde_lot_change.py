class Jde_Lot_Change:
    def __init__(self,app):
        self.app = app

    def fetch_lot_id(self):
        wd = self.app.wd
        wd.find_elemetn_by_xpath("//*//span[text()='Fetch Lot ID’s using Part Number and Lot Type']").click()






