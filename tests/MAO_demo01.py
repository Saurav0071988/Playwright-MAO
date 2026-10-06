from playwright.sync_api import playwright,Page
from playwright.sync_api import expect
import playwright
import re
import pytest
import openpyxl
from openpyxl import load_workbook
from utils.MAO_excel_utils import read_testdata
from utils.MAO_excel_utils import write_data


URL = "https://lesls-auth.omni.manh.com/auth/realms/maactive/protocol/openid-connect/auth?scope=openid&client_id=zuulserver.1.0.0&redirect_uri=https://lesls.omni.manh.com/login&response_type=code&state=WBH2mm"

@pytest.mark.parametrize("row_num, username, password, ordervalue", read_testdata())
def test_search_item(page: Page, row_num, username, password, ordervalue):
    page.goto(URL)
    page.locator("//*[@id='username']").fill(username)
    page.wait_for_timeout(2000)
    page.locator("//*[@id='password']").fill(password)
    page.wait_for_timeout(2000)
    page.locator("//input[@name='login']").click()
    page.wait_for_selector("//*[@id='User']", timeout=20000)
    User_icon = page.locator("//*[@id='User']")
    expect(User_icon).to_be_visible()
    
    # Search for the Order from MAO and retrieve the order details
    
    print(" Order Search Begins ... ")
    page.wait_for_timeout(10000)
    page.locator("(//*[@svgicon='menu']/..)[1]").click()
    page.wait_for_timeout(5000)
    page.get_by_text("Orders", exact=True).click()
    page.wait_for_timeout(5000)
    page.get_by_role("listitem").filter(has_text="Order Number").get_by_role("textbox").click()
    page.wait_for_timeout(5000)
    page.get_by_role("listitem").filter(has_text="Order Number").get_by_role("textbox").fill(str(ordervalue))
    page.wait_for_timeout(2000)
    page.locator("(//*[@id='btnApply'])[1]").click()
    page.wait_for_timeout(5000)
    
    ordertotal = page.locator("(//*[@class='datatable-body-cell sort-active'])[7]/div/span").text_content()
    status = page.locator("(//*[@class='datatable-body-cell sort-active'])[9]/div/span").text_content()
    
    print(" The validation Passed for -", ordervalue)
    write_data(row_num, status, ordertotal, "PASS")



    



