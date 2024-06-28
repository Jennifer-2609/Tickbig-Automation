import time
from telnetlib import EC
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen



class fundraise:

    logger = LogGen.loggen()

    # post fund xpath
    fundraise_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[2]/ul/li[3]/a"
    postfund_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[4]/a/div/p"
    postfundfinal_button_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[13]/button[2]/span[1]"
    fundcompname_input_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/div/input"
    fundcompage_input_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/div/input"
    fundcompvaluation_input_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/input"
    fundcompsizemin_input_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/div/input[1]"
    fundcompsizemax_input_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/div/input[2]"
    fundstage_drpdown_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div/div[1]/div[1]/div[2]"
    fundseed_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div/div[2]/div/div[1]"
    fundseriesA_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div/div[2]/div/div[3]"
    fundseriesD_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div/div[2]/div/div[6]"
    fundsector_drpdown_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div/div/div[1]/div[1]/div[2]"
    fundsectoranimation_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div/div/div[2]/div/div[5]"
    fundshortdesc_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/div/textarea"
    uploaddescdoc_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div/input"
    whocanapplyfund_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[1]/div[1]/div[2]"
    fundpostonbehalf_toggle_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div/label/span[1]/span[1]/input"
    fundonbehalf_chooseone_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div[2]/div"

    # review,save,report,copy link, not interest
    fundthreedots_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[1]/div[3]/div/button/img"
    savefund_button_xpath = "/html/body/div[4]/div[3]/ul/div/li[1]/p"
    # unsavefund_button_xpath="/html/body/div[4]/div[3]/ul/div/li[1]/p"
    fundcopylink_xpath = "/html/body/div[4]/div[3]/ul/div/li[2]/p"
    fundnotinterest_xpath = "/html/body/div[4]/div[3]/ul/div/li[4]/button"
    fundnotinterestYes_xpath = "/html/body/div[5]/div/div/div[2]/section/div/button[1]"

    fundreview_xpath = "/html/body/div[4]/div[3]/ul/div/li[3]/p"
    fundrating_xpath = "/html/body/div[4]/div[3]/span/label[3]"
    fundreviewtxt_xpath = "/html/body/div[4]/div[3]/textarea"
    fundreviewsubmit_xpath = "/html/body/div[4]/div[3]/div/button[2]"

    fundreport_xpath = "/html/body/div[4]/div[3]/ul/div/li[5]/p"
    fundreporttxt_xpath = "/html/body/div[4]/div[3]/textarea"
    fundreportsubmit_xpath = "/html/body/div[4]/div[3]/div/button[2]"
    fundlike_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[6]/div/button[1]/img"
    fundsuperlike_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[6]/div/button[2]/img"


    # open,close,save fundraise
    funddownarrow_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[4]/h2/button"
    openfund_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[4]/div/p[2]"
    openfund3dots_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[1]/div[3]/div/button/img"
    openfundclose_xpath = "/html/body/div[3]/div[3]/ul/div/li[2]/p"
    closedfund_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/div[2]/a[2]"
    closedfundrepost_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[6]/div/button[3]"
    fundrepost_button_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/main/section/form/div/div[2]/div[13]/button[2]/span[1]"
    savedfund_button_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[4]/div/p[4]"


    def __init__(self, driver):
        self.driver = driver

    def clickfundraise(self):
        self.driver.find_element(By.XPATH, self.fundraise_button_xpath).click()

    def clickpostfund(self):
        self.driver.find_element(By.XPATH, self.postfund_button_xpath).click()

    def scrollpostfundfinal(self):
        Button = self.driver.find_element(By.XPATH, self.postfundfinal_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickpostfundfinal(self):
        self.driver.find_element(By.XPATH, self.postfundfinal_button_xpath).click()

    def clickfundcompname(self):
        self.driver.find_element(By.XPATH, self.fundcompname_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundcompname_input_xpath).send_keys("DSP Mutual Fund")

    def clickfundcompage(self):
        self.driver.find_element(By.XPATH, self.fundcompage_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundcompage_input_xpath).send_keys("3")

    def clickfundcompvaluation(self):
        self.driver.find_element(By.XPATH, self.fundcompvaluation_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundcompvaluation_input_xpath).send_keys("3000000")

    def clickfundcompsizemin(self):
        self.driver.find_element(By.XPATH, self.fundcompsizemin_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundcompsizemin_input_xpath).send_keys("50")

    def clickfundcompsizemax(self):
        self.driver.find_element(By.XPATH, self.fundcompsizemax_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundcompsizemax_input_xpath).send_keys("90")

    def clickfundstage(self):
        self.driver.find_element(By.XPATH, self.fundstage_drpdown_xpath).click()

    def clickfundstagedetails(self):
        self.driver.find_element(By.XPATH, self.fundseed_xpath).click()
        # time.sleep(1)
        # self.driver.find_element(By.XPATH, self.fundseriesA_xpath).click()
        # time.sleep(1)
        # self.driver.find_element(By.XPATH, self.fundseriesD_xpath).click()

    def clickfundsector(self):
        self.driver.find_element(By.XPATH, self.fundsector_drpdown_xpath).click()

    def clickfundsectoranimation(self):
        self.driver.find_element(By.XPATH, self.fundsectoranimation_xpath).click()

    def clickfundshortdesc(self):
        self.driver.find_element(By.XPATH, self.fundshortdesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundshortdesc_xpath).send_keys("As such, dummy content is an essential tool for developers because it allows them to showcase what real content will look like on their website.")

    def uploadfunddescdoc(self):
        self.driver.find_element(By.XPATH, self.uploaddescdoc_xpath).send_keys("D://Python/S3details.pdf")

    def clickwhocanapplyfund(self):
        self.driver.find_element(By.XPATH, self.whocanapplyfund_xpath).click()

    def clickfundpostonbehalf(self):
        self.driver.find_element(By.XPATH, self.fundpostonbehalf_toggle_xpath).click()

    def clickfundonbehalfchooseone(self):
        self.driver.find_element(By.XPATH, self.fundonbehalf_chooseone_xpath).click()


    # negative testcase

    def clickfundcompnameneg1(self):
        self.driver.find_element(By.XPATH, self.fundcompname_input_xpath).send_keys("  ")
    def clickfundcompnameneg2(self):
        self.driver.find_element(By.XPATH, self.fundcompname_input_xpath).send_keys(" !!)(*&%&23 ")
    def clickfundcompageneg(self):
        self.driver.find_element(By.XPATH, self.fundcompage_input_xpath).send_keys(" !#$%6876")
    def clickfundcompvaluationneg(self):
        self.driver.find_element(By.XPATH, self.fundcompvaluation_input_xpath).send_keys("  !#%^^^&576")

    def clickfundcompsizeminneg1(self):
        self.driver.find_element(By.XPATH, self.fundcompsizemin_input_xpath).send_keys(" )(*47347")

    def clickfundcompsizemaxneg1(self):
        self.driver.find_element(By.XPATH, self.fundcompsizemax_input_xpath).send_keys(" )(*47347")
    def clickfundcompsizeminneg2(self):
        self.driver.find_element(By.XPATH, self.fundcompsizemin_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundcompsizemin_input_xpath).send_keys("100")
    def clickfundcompsizemaxneg2(self):
        self.driver.find_element(By.XPATH, self.fundcompsizemax_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundcompsizemax_input_xpath).send_keys("50")
    def clickfundshortdescneg1(self):
        self.driver.find_element(By.XPATH, self.fundshortdesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundshortdesc_xpath).send_keys("  ")
    def clickfundshortdescneg2(self):
        self.driver.find_element(By.XPATH, self.fundshortdesc_xpath).clear()
        self.driver.find_element(By.XPATH, self.fundshortdesc_xpath).send_keys("As such, dummy content is an essential tool for developers because it allows them to showcase what real content will look like on their website.As such, dummy content is an essential tool for developers")


    # review,save,report,copy link, not interest
    def clickFundthreedots(self):
        self.driver.find_element(By.XPATH, self.fundthreedots_xpath).click()

    def clickFundcopylink(self):
        self.driver.find_element(By.XPATH, self.fundcopylink_xpath).click()

    def clickFundreview(self):
        self.driver.find_element(By.XPATH, self.fundreview_xpath).click()

    def clickFundreviewsubmit(self):
        self.driver.find_element(By.XPATH, self.fundreviewsubmit_xpath).click()

    def clickFundrating(self):
        self.driver.find_element(By.XPATH, self.fundrating_xpath).click()

    def clickFundreviewtext(self):
        self.driver.find_element(By.XPATH, self.fundreviewtxt_xpath).send_keys("automation testing review")

    def clickFundnotinterest(self):
        self.driver.find_element(By.XPATH,self.fundnotinterest_xpath).click()

    def clickFundnotinterestyes(self):
        self.driver.find_element(By.XPATH, self.fundnotinterestYes_xpath).click()

    def clickFundreport(self):
        self.driver.find_element(By.XPATH,self.fundreport_xpath).click()

    def clickFundreportsubmit(self):
        self.driver.find_element(By.XPATH, self.fundreportsubmit_xpath).click()

    def clickFundreporttext(self):
        self.driver.find_element(By.XPATH, self.fundreporttxt_xpath).send_keys("automation testing report")

    def clickFundlike(self):
        self.driver.find_element(By.XPATH,self.fundlike_xpath).click()

    def clickFundsuperlike(self):
        self.driver.find_element(By.XPATH, self.fundsuperlike_xpath).click()

    def clickFundsave(self):
        self.driver.find_element(By.XPATH, self.savefund_button_xpath).click()

    # Open, Close, Saved Fund

    def clickfunddownarrow(self):
        self.driver.find_element(By.XPATH, self.funddownarrow_xpath).click()

    def clickopenfund(self):
        self.driver.find_element(By.XPATH, self.openfund_xpath).click()

    def clickopenfund3dots(self):
        self.driver.find_element(By.XPATH, self.openfund3dots_xpath).click()

    def clickopenfundclose(self):
        self.driver.find_element(By.XPATH, self. openfundclose_xpath).click()

    def clickclosedfund(self):
        self.driver.find_element(By.XPATH, self.closedfund_button_xpath).click()

    def clickclosedfundrepost(self):
        self.driver.find_element(By.XPATH, self.closedfundrepost_xpath).click()

    def scrollfundrepostbutton(self):
        Button = self.driver.find_element(By.XPATH, self.fundrepost_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickfundrepostbutton(self):
        self.driver.find_element(By.XPATH, self.fundrepost_button_xpath).click()

    def clicksavedfund(self):
        self.driver.find_element(By.XPATH, self.savedfund_button_xpath).click()