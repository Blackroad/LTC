

class BackgroundHelper:
    def __init__(self,app):
        self.app = app


    def reason_for_change(self,type_of_change=None,reason_for_change = None):
        wd = self.app.wd
        if type_of_change is not None:
            wd.find_element_by_xpath("//select[@id='LotChange']/option[@value='%s']" % type_of_change).click()
            return type_of_change
        if reason_for_change is not None:
            wd.find_element_by_xpath("//*[@id='BriefStatement']/option[@value='%s']" % reason_for_change).click()


    def initial_part_or_lot_upgrade(self, lot_upgrade):
        wd = self.app.wd
        if wd.find_element_by_xpath("//*[@id='LotChange']/option[@value]").text == 'Upgrade':
            if lot_upgrade != 'Select...' and lot_upgrade != 'Select' :
                wd.find_element_by_xpath("//*[@id='InitialUpgrade']/option[@value='%s']" % lot_upgrade).click()
                return True
            elif lot_upgrade == 'Select':
                wd.find_element_by_xpath("//*[@id='InitialUpgrade']/option[text()= 'Select...']").click()
                return False
            self.app.save_changes()
        else:
            pass

    def types_of_Lot_level_change(self, ic_upgrade:bool = False, scsp_upgrade:bool = False, component:bool = False, hybrid_upgrade:bool = False, lot_upgrade=None):
        wd = self.app.wd
        self.initial_part_or_lot_upgrade(lot_upgrade)
        self.set_values(component, hybrid_upgrade, ic_upgrade, scsp_upgrade, lot_upgrade)
        self.app.save_changes()
        if len(wd.find_elements_by_xpath("//*[@id='LotQualUpgradeLevelAndApproversValidationMessage' and text()]")) != 0:
            self.set_values(component, hybrid_upgrade, ic_upgrade, scsp_upgrade, lot_upgrade)
            self.app.save_changes()
        else:
            pass

    def set_values(self,component, hybrid_upgrade, ic_upgrade, scsp_upgrade, lot_upgrade):
        wd = self.app.wd
        if lot_upgrade == 'Yes':
            if ic_upgrade == True:
                wd.find_element_by_xpath(
                    "//*[@id='LotQualUpgradeLevelAndApproversInitial']//tr[1]//input").click()
            if scsp_upgrade == True:
                wd.find_element_by_xpath(
                    "//*[@id='LotQualUpgradeLevelAndApproversInitial']//tr[2]//input").click()
            if component == True:
                wd.find_element_by_xpath(
                    "//*[@id='LotQualUpgradeLevelAndApproversInitial']//tr[3]//input").click()
            if hybrid_upgrade == True:
                wd.find_element_by_xpath(
                    "//*[@id='LotQualUpgradeLevelAndApproversInitial']//tr[4]//input").click()
        elif lot_upgrade == 'No':
            if ic_upgrade == True:
                wd.find_element_by_xpath(
                    "//*[@id='LotQualUpgradeLevelAndApprovers']//tr[1]//input").click()
            if scsp_upgrade == True:
                wd.find_element_by_xpath(
                    "//*[@id='LotQualUpgradeLevelAndApprovers']//tr[2]//input").click()
            if component == True:
                wd.find_element_by_xpath(
                    "//*[@id='LotQualUpgradeLevelAndApprovers']//tr[3]//input").click()
            if hybrid_upgrade == True:
                wd.find_element_by_xpath(
                    "//*[@id='LotQualUpgradeLevelAndApprovers']//tr[4]//input").click()
        else:
            pass

    def questions(self, question1, question2, question3, question4):
        wd = self.app.wd
        if question1 == 'Yes':
            wd.find_element_by_xpath("//table[@class='questions']//tr[1]//input[@value='1']").click()
        elif question1 == 'No':
            wd.find_element_by_xpath("//table[@class='questions']//tr[1]//input[@value='2']").click()
        if question2 == 'Yes':
            wd.find_element_by_xpath("//table[@class='questions']//tr[2]//input[@value='1']").click()
            if question3 == 'Yes':
                wd.find_element_by_xpath("//table[@class='questions']//tr[3]//input[@value='1']").click()
            elif question3 == 'No':
                wd.find_element_by_xpath("//table[@class='questions']//tr[3]//input[@value='2']").click()
            if question4 == 'Yes':
                wd.find_element_by_xpath("//table[@class='questions']//tr[4]//input[@value='1']").click()
            elif question4 == 'No':
                wd.find_element_by_xpath("//table[@class='questions']//tr[4]//input[@value='2']").click()
        elif question2 == 'No':
            wd.find_element_by_xpath("//table[@class='questions']//tr[2]//input[@value='2']").click()

    def add_part(self, part_number, part_revision, part_status):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath("//*[@id='partNumberBindingContainer']//tbody//tr")) == 0:
            wd.find_element_by_xpath("//*[@id='partNumberBindingContainer']//span[text()='Add']").click()
            wd.find_element_by_xpath("//*[@id='partNumberDialog']//input[@data-bind='value: PartNumberControl.partNumbersToEdit']").send_keys(part_number)
            wd.find_element_by_xpath("//*[@id='partNumberDialog']//div[2]//span").click()
            wd.find_element_by_xpath("//*[@id='partNumberDialog']//button//span[text()='OK']").click()
            wd.find_element_by_xpath("//*[@id='messageDialogOkButton']/span").click()
            self.app.back_to_sharepoint()
            self.app.edit_document()
        if len(wd.find_elements_by_xpath("//td[4]//span[text()]")) == True:
            wd.find_element_by_xpath("//input[@data-bind='value: MesPartNumber.Revision']").send_keys(part_revision)
        if len(wd.find_elements_by_xpath("//td[9]//span[text()]")) == True:
            wd.find_element_by_xpath("//select[@id='ProposedPromisLotType']/option[@value='%s']" % part_status).click()
        self.app.save_changes()





















