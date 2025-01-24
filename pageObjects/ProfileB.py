from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen

class profileB:

    logger = LogGen.loggen()

    # path to Pjts & Links
    btn_pjtslinks_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[6]/section/div[2]/div"
    txt_pjtname_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[1]/input"
    txt_compnamepjts_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[2]/input"
    txt_pjtlinks_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[3]/input"
    txt_responsibility_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[4]/div/div[2]/div[1]"
    txt_pjtsdescription_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[1]/div[5]/div/div/textarea[1]"
    btn_savepjt_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/button"
    mousehover_pjtcard_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[6]/section/main/div/div/div/div[1]/main/div[2]/section"
    btn_delpjts_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[6]/section/main/div/div/div/div[1]/main/div[1]/div/button[1]/span/i"
    btn_editpjts_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[6]/section/main/div/div/div/div[1]/main/div[1]/div/button[2]/span/i"
    btn_editsavepjt_xpath="/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/button"
    btn_pjtweblink_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[6]/section/main/div/div/div/div/main/div[2]/section/div[1]/div/img"

    def __init__(self, driver):
        self.driver = driver

    def scrollPjtslinks(self):
        Button = self.driver.find_element(By.XPATH, self.btn_pjtslinks_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def scrollSavepjtslinks(self):
        Button = self.driver.find_element(By.XPATH, self.btn_savepjt_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickPjtslinks(self):
        self.driver.find_element(By.XPATH, self.btn_pjtslinks_xpath).click()

    def mousehoverpjtlinkcardEdit(self):
        # self.driver.find_element(By.XPATH, self.mousehover_pjtcard_xpath).click()

        # Find the element to hover over
        element_to_hover_over = self.driver.find_element(By.XPATH, self.mousehover_pjtcard_xpath)

        # Create an ActionChains object
        action_chains = ActionChains(self.driver)

        # Perform the mouse hover action
        action_chains.move_to_element(element_to_hover_over).perform()

        # After performing the hover action, you can interact with the elements that appear after the hover
        # For example, you can click on an element that appears after the hover
        element_to_click = self.driver.find_element(By.XPATH, self.btn_editpjts_xpath)
        element_to_click.click()
        # self.logger.info("********** Edit pjts clicked successfully *********")


    def textPjtName(self,projectname):
        self.driver.find_element(By.XPATH, self.txt_pjtname_xpath).send_keys(projectname)

    def textPjtCompName(self,projectcompanyname):
        self.driver.find_element(By.XPATH, self.txt_compnamepjts_xpath).send_keys(projectcompanyname)

    def textPjtlinks(self,projectlinks):
        self.driver.find_element(By.XPATH, self.txt_pjtlinks_xpath).send_keys(projectlinks)

    def textPjtresponsibility(self,projectresponsibility):
        self.driver.find_element(By.XPATH, self.txt_responsibility_xpath).send_keys(projectresponsibility)

    def textPjtdescription(self,projectdescription):
        self.driver.find_element(By.XPATH, self.txt_pjtsdescription_xpath).send_keys(projectdescription)

    def clickSavePjtslinks(self):
        self.driver.find_element(By.XPATH, self.btn_savepjt_xpath).click()

    def mousehoverpjtlinkcardDel(self):
        # self.driver.find_element(By.XPATH, self.mousehover_pjtcard_xpath).click()

        # Find the element to hover over
        element_to_hover_over = self.driver.find_element(By.XPATH, self.mousehover_pjtcard_xpath)

        # Create an ActionChains object
        action_chains = ActionChains(self.driver)

        # Perform the mouse hover action
        action_chains.move_to_element(element_to_hover_over).perform()

        # After performing the hover action, you can interact with the elements that appear after the hover
        # For example, you can click on an element that appears after the hover
        element_to_click = self.driver.find_element(By.XPATH, self.btn_delpjts_xpath)
        element_to_click.click()
        # self.logger.info("********** Edit pjts clicked successfully *********")

    def clickeditSavePjtslinks(self):
        self.driver.find_element(By.XPATH, self.btn_editsavepjt_xpath).click()

    def clickpjtweblink(self):
        self.driver.find_element(By.XPATH, self.btn_pjtweblink_xpath).click()
        # Wait for the new window to open
        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Now you can perform actions on the new window
        # For example, get the current URL
        # print("Current URL of the new window:", self.driver.current_url)
        self.logger.info("Project Link is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "ProjectLink.png")
        # Close the new window
        self.driver.close()
        # Switch back to the original window
        self.driver.switch_to.window(self.driver.window_handles[0])

    # def clickeditPjtslinks(self):
    #     self.driver.find_element(By.XPATH, self.btn_editpjts_xpath).click()

    def textPjtdescriptionmin(self, projectdescriptionmin):
        self.driver.find_element(By.XPATH, self.txt_pjtsdescription_xpath).send_keys(projectdescriptionmin)

    def textPjtdescriptionmax(self, projectdescriptionmax):
        self.driver.find_element(By.XPATH, self.txt_pjtsdescription_xpath).send_keys(projectdescriptionmax)