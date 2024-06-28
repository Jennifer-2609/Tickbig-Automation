# from lib2to3.pgen2 import driver
# from pydoc import html
# from _pytest.hookspec import hookspec
import pytest_html
from selenium import webdriver
import pytest
# from datetime import datetime


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    return driver

def pytest_addoption(parser):  #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")


#  *********************************************************************************************************************


##### Pytest HTML Report #####

#It is hook for adding environment info to HTML report

# def pytest_configure(config):
#     config._metadata = {}
#     config._metadata['Project Name'] = 'Tick Big'
#     config._metadata['Module Name'] = 'Login'
#     config._metadata['Tester'] = 'Jennifer'

# def pytest_configure(config):
#     config.custom_ini = {}
#     config.custom_ini['Project Name'] = 'Tick Big'
#     config.custom_ini['Module Name'] = 'Login'
#     config.custom_ini['Tester'] = 'Jennifer'

#It is hook for delete/modify environment info to HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


# **********************************************************************************************************************

# @pytest.fixture(scope='session')
# def pytest_html_results_table_header(request, table):
#     # Add custom columns to the HTML report table header
#     table.extend([
#         html.th('Time', class_='sortable time', col='time', row=1),
#         html.th('Browser', class_='sortable', col='browser', row=1),
#     ])
#
# @pytest.fixture(scope='session')
# def pytest_html_results_table_row(report, cells):
#     # Add custom data to each test result row in the HTML report
#     cells.insert(2, html.td(datetime.utcnow(), class_='col-time'))
#     cells.insert(3, html.td(report.user_properties['browser']))
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_html_results_table_header(prefix, table):
#     # Add custom columns to the HTML report table header
#     prefix.append('<div class="text-center">Additional Info</div>')
#     table.append(pytest_html.results.KnownColumns.Result)
#
# def pytest_configure(config):
#     # Add custom metadata to the HTML report
#     config._metadata['Project Name'] = 'Your Project Name'
#     config._metadata['Test Environment'] = 'Production'
#
# def _capture_screenshot(name):
#      driver.get_screenshot_as_file(name)
#
# def pytest_html_report_title(report):
#     # Set the title of the HTML report
#     report.title = "Automation Report"
#
# def pytest_html_results_summary(prefix, summary, postfix):
#     # Add additional information to the summary section of the HTML report
#     prefix.extend([html.p("Custom summary paragraph")])

#  *********************************************************************************************************************

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#
#     if report.when == "call" or report.when == "setup":
#         # # always add url to report
#         # extras.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file = "failed_screenshot.png"
#             driver.get_screenshot_as_file(file)
#             extra_html = '<div><img src="%s" style="width:250px;height:200px;" ' \
#                    'onclick="window.open(this.src)" align="right"/></div>' % file
#             # only add additional html on failure
#             extras.append(pytest_html.extras.html(extra_html))
#         report.extras = extras
#
# @pytest.fixture()
# def driverChrome():
#     global driver
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.implicitly_wait(20)
#     return driver