from playwright.sync_api import playwright
from playwright.sync_api import expect
import playwright
import re
import pytest
import openpyxl
from openpyxl import load_workbook
from utils.excel_utils import read_testdata
from utils.excel_utils import write_data



@pytest.mark.parametrize("row_num, search_item", read_testdata())
def test_search_item(page: Page, row_num, search_item):
    page.goto("https://www.flipkart.com/")
    page.locator("//span[@class='b3wTlE']").click()
    page.wait_for_timeout(2000)
    page.locator("(//input[@title='Search for Products, Brands and More'])[1]").clear()
    page.wait_for_timeout(2000)
    print(" Search begins for the item -", search_item)
    page.locator("(//input[@title='Search for Products, Brands and More'])[1]").fill(search_item)
    page.wait_for_timeout(2000)
    page.locator("(//button[@title='Search for Products, Brands and More'])[1]").click()
    page.wait_for_timeout(2000)
    showing_text = page.locator("//*[@class='_Omnvo']").text_content()
    print(" Visible Text -", showing_text)
    
    expect(page.locator("//*[text()='Login']")).to_be_visible()
    print(" The validation Passed for -", search_item)
    write_data(row_num, "PASS")



    



