# import time
# import pytest
# from selenium import webdriver
# from pageObjects.LoginPage import Login
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
# import configparser
# from utilities import ExcelUtils
#
# config=configparser.ConfigParser()
# config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')
# # username = config.get('settings','BaseUrl')
# # print(username)
#
# class Test_001_DDT_Login:
#
#     BaseURL= ReadConfig.getApplicationURL()
#     path=".//TestData/LoginData.xlsx"
#     # username= ReadConfig.getUseremail()
#     # password= ReadConfig.getPassword()
#
#     logger = LogGen.loggen()
#
#     @pytest.mark.sanity
#     def test_login_ddt(self,setup):
#         self.logger.info("********** Test_001_ddt_Login *********")
#         self.logger.info("********** verifying login test *********")
#         self.driver = setup
#         self.driver.get(self.BaseURL)
#
#         self.l=Login(self.driver)
#         self.l.clicksignin()
#
#         self.rows=ExcelUtils.get_row_count(self.path,'LoginTest')
#         print("Number of Rows in a Excel:",self.rows)
#
#         lst_status=[]     #Empty list variable
#
#         for r in range(2,self.rows+1):
#             self.user=ExcelUtils.get_cell_data(self.path,'LoginTest',r,1)
#             self.password = ExcelUtils.get_cell_data(self.path, 'LoginTest', r, 2)
#             self.exp = ExcelUtils.get_cell_data(self.path, 'LoginTest', r, 3)
#
#             self.l.setUserName(self.user)
#             time.sleep(5)
#             self.l.setPassword(self.password)
#             time.sleep(5)
#             self.l.clickLogin()
#             time.sleep(5)
#
#             act_url=self.driver.current_url
#             print(act_url)
#             exp_url="https://www.tickbig.com/home"
#
#             if act_url==exp_url:
#                 if self.exp=="pass":
#                     self.logger.info("**** Passed 1 ***")
#                     time.sleep(5)
#                     self.l.clickLogout()
#                     time.sleep(5)
#                     lst_status.append("pass")
#                 elif self.exp=="fail":
#                     self.logger.info("**** Failed 1 ***")
#                     time.sleep(5)
#                     self.l.clickLogout()
#                     time.sleep(5)
#                     lst_status.append("fail")
#             elif act_url!=exp_url:
#                 if self.exp=="pass":
#                     self.logger.info("***** failed 2 *****")
#                     lst_status.append("fail")
#                 elif self.exp=="fail":
#                     self.logger.info("***** passed 2 *****")
#                     lst_status.append("pass")
#
#
#         if "fail" not in lst_status:
#             self.logger.info("***** Login DDT test passed *****")
#             self.driver.close()
#             assert True
#         else:
#             self.logger.info("***** Login DDT test failed *****")
#             self.driver.close()
#             assert False
#
#         self.logger.info("********** End of Login DDT test *********")
#         self.logger.info("********** Completed TC_LoginDDT_001 *********")
#
#
#
#
