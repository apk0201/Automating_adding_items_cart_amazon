from selenium import webdriver
from os.path import expanduser

home = expanduser("~")
driver = webdriver.Chrome(executable_path=home+r"\PycharmProjects\Selenium\AutomateAddingItemsToCart\driver"
                                               r"\\chromedriver.exe")
driver.implicitly_wait(15)
driver.maximize_window()
driver.get("https://www.amazon.com")
select_books= driver.find_element_by_link_text("Books")
select_books.click()
select_children_books = driver.find_element_by_xpath("//a[@href = '/Childrens-Books/b/?ie=UTF8&node=4&ref_=sv_b_4']")
select_children_books.click()
select_education_ref_books = driver.find_element_by_xpath("//a[@title = 'Education & Reference']")
select_education_ref_books.click()
enter_txt = driver.find_element_by_id("twotabsearchtextbox")
enter_txt.send_keys("Peppa Pig")
click_go = driver.find_element_by_xpath("//input[@value = 'Go']")
click_go.click()
select_book = driver.find_element_by_xpath("//div/img[@data-image-index='3']")
select_book.click()
add_to_cart = driver.find_element_by_id("add-to-cart-button")
add_to_cart.click()
count_cart_items = driver.find_element_by_id("nav-cart-count")
txt = count_cart_items.text
if int(txt) >= 1:
    count_cart_items.click()
else:
    print("Item not added to cart. Please add again")
    add_to_cart.click()
driver.get_screenshot_as_file("screenshot.png")
driver.close()
