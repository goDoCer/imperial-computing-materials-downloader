from config import *
from selenium.common.exceptions import NoSuchElementException
def download(browser, download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def authenticate(driver):
    username_elem = driver.find_element_by_xpath('//*[@id="username"]')
    password_elem = driver.find_element_by_xpath('//*[@id="password"]')

    username_elem.clear()
    password_elem.clear()

    username_elem.send_keys(SHORTCODE)
    password_elem.send_keys(PASSWORD)

    driver.find_element_by_xpath('//*[@id="main"]/div[3]/form/button').click()    

def download_course(driver, course_code, base_dir, verbose=False):
    try:
        driver.get(f"{MATERIALS_URL}resources/{YEAR}/{course_code}")
        course_name = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/span[2]').text
        try:
            authenticate(driver)
        except:
            pass
        try:
            materials_list = driver.find_element_by_xpath('//*[@id="Course Material"]/ul').find_elements_by_tag_name("li")

            for material in materials_list:
                if "\nFile" in material.text:
                    download_dir = f'{base_dir}/{course_code} - {course_name}/'
                    download(driver, download_dir)
                    material.find_element_by_tag_name("div").find_element_by_tag_name("a").click() 
            print(f"Downloaded materials for {course_code} - {course_name}")        
        except:
            if verbose:
                print(f"No materials available for {course_code}{ f' - {course_name}' if course_name != 'None' else '' }")
    except NoSuchElementException:
        print("Something went wrong with your authentication.")
        print(f"Your shortcode is set as {SHORTCODE} and your password is set as {PASSWORD}")
        print("You can reset your credentials using -s <shortcode> and -p <password> flags")
        driver.quit()

def download_courses(driver, headless=True, base_dir="./", verbose=False):
    try:
        courses_list = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/ul').find_elements_by_tag_name("li")
        courses_list = list(map(lambda c: c.text.split(" ")[0], courses_list))

        for course in (courses_list):
            download_course(driver, course, base_dir, verbose=verbose)
    except NoSuchElementException:
        print("Something went wrong with your authentication.")
        print(f"Your shortcode is set as {SHORTCODE} and your password is set as {PASSWORD}")
        print("You can reset your credentials using -s <shortcode> and -p <password> flags")
        driver.quit()


