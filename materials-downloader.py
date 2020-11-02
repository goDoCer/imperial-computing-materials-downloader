import sys
import os
import json
import argparse
import datetime as dt

sys.path.insert(1, './lib')
from config import *
from helpers import *

from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--real", help="runs the browser outside of headless mode", action="store_true")
    parser.add_argument("-v", "--verbose", help="sets uotput to be verbose", action="store_true")                      
    parser.add_argument("-c", "--credentials", help="shows the credentials", action="store_true")

    parser.add_argument("-q", "--quick", help="gets materials for the provided course_code", 
                                          action="store", type=str)
    parser.add_argument("-l", "--location", help="stores downloads in specified location", 
                                          action="store", type=str)
    
    
    parser.add_argument("-d", "--dir", help="sets the directory where the materials should be stored", action="store")
    parser.add_argument("-s", "--shortcode", help="sets the shortcode", action="store")
    parser.add_argument("-p", "--password",  help="sets the password", action="store")
                                      
    args = parser.parse_args()
    exit = False

    
    with open("lib/auth.json") as authfile:
        auth = json.load(authfile)
        if args.credentials:
            [print(f"Your {key} is set as {auth[key]}") for key in auth.keys()]
            quit()

        if args.shortcode:
            auth["shortcode"] = args.shortcode
            print(f"Shortcode set to {args.shortcode}")
            exit = True

        if args.password:
            auth["password"] = args.password
            print(f"Password set to {args.password}")
            exit = True

        if args.dir:
            if os.path.isdir(args.dir):
                auth["directory"] = args.dir
                print(f"Directory set to {args.dir}")
            else:
                print(f"{args.dir} is not a valid directory!!!")
                print(f"Please pass in a valid directory")

            exit = True
            
    with open("lib/auth.json", "wt") as authfile:
        json.dump(auth, authfile)

    if exit:    
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

    base_dir = args.location if arg.location else "downloads"
    if args.quick:
        download_course(driver, args.quick, base_dir=base_dir, verbose=verbose)
    else:
        download_courses(driver, headless=headless, base_dir=base_dir, verbose=verbose)

    driver.quit()
    print("Finishing...")
    copy_tree(base_dir, DIRECTORY)
    remove_tree(base_dir)
    print("DONE!!!")