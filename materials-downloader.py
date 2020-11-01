import sys
import os
import json
import argparse
import datetime as dt

sys.path.insert(1, './lib')
from config import *
from helpers import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--real", help="runs the browser outside of headless mode", action="store_true")
    parser.add_argument("-v", "--verbose", help="sets uotput to be verbose", action="store_true")                      

    parser.add_argument("-q", "--quick",  help="gets materials for the provided course_code", 
                                          action="store", type=str)
    try:
        year = YEAR%100 - int(SHORTCODE[-2:])
    except ValueError:
        year = YEAR -1
    parser.add_argument("-d", "--dir",    help="directoty where the materials should be stored", 
                                        action="store",type=str,
                                        default=f"Year {year}", nargs="?")

    parser.add_argument("-s", "--shortcode", help="sets the shortcode", action="store")
    parser.add_argument("-p", "--password",  help="sets the password", action="store")
                                      
    args = parser.parse_args()
    exit = False
    with open("lib/auth.json") as authfile:
        auth = json.load(authfile)
        if args.shortcode:
            auth["shortcode"] = args.shortcode
            exit = True

        if args.password:
            auth["password"] = args.password
            exit = True

    with open("lib/auth.json", "wt") as authfile:
        json.dump(auth, authfile)

    if exit:
        try:
            driver.quit()
        except:
            pass
        finally:    
            quit()

    headless = not args.real
    verbose  = args.verbose
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "./",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
    })
    
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')

    driver = webdriver.Chrome(options=chrome_options, executable_path=CHROMEDRIVER_PATH)
    driver.get(MATERIALS_URL)

    print("authenticating...")
    authenticate(driver)
    
    if args.quick:
        download_course(driver, args.quick, base_dir=args.dir, verbose=verbose)
    else:
        download_courses(driver, headless=headless, base_dir=args.dir, verbose=verbose)
    driver.quit()
