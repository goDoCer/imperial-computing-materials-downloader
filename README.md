# README

This is an automated downloader for [materials](https://materials.doc.ic.ac.uk/), which is a platform used by the Imperial College London Department of Computing. Since materials is the main source of obtaining lecture slides, tutorial sheets and whatnot, a computing student downloads something or the other from there daily.

This program can be used to avoid the hassle of downloading everything manually.

It downloads all the files from a student's materials page for that year. It also sets up a nice directory structure by year of study and course names.

Whenever the program is run it refreshes all the dowloads as quite often professors change the naming of the uploaded materials. If you want to refresh just one course, you can do that as well.

## Requirements

1. Login credentials of your materials account.
2. Python3 installed on your machine
3 .Google Chrome bowser

## How to use it

1. Download this repository.
2. Make sure you have python3 installed.
3. Open the teminal and go to where you have this repository.
4. Run ```pip3 install -r requirements.txt```
5. Check your chrome version by clicking [here](chrome://version/) or typing "chrome://version/" into Google Chrome.
6. Download a chromedriver for your machine and chrome version from [here](https://chromedriver.chromium.org/downloads) and add it to the lib folder (Make sure to delete any existing chromedrivers that might be there).
7. Run the command ```python3 materials-downloader.py -s <your_shortcode> -p <your_password> -d <directory>``` to set your credentials and the relative path of the location where you want to store the downloads. You just have to do this once and can use the same command if your shortcode/password has been changed.

## Optional Flags

1. ```-q <course_code>``` flag can be used to refresh materials for a particular course only. For example, if you just want to refresh the materials for the course 40009 - Computer Practical 1, you should run ```python3 materials-downloader.py -q 40009```.
2. ```-r``` flag can be used to run the browser outside of headless mode.
3. ```-s <shortcode>``` flag can be used to set your shortcode.
4. ```-p <password>``` flag can be used to set the password.
5. ```-d <dir>``` flag can be used to set where the directory containing all the materials is present.
6. ```-v``` flag can be used for verbosity.
7. ```-h``` flag can be used to read about optional flags at anytime.
