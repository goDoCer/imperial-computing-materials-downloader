# README

This is an automated downloader for [materials](https://materials.doc.ic.ac.uk/), which is a platform used by the Imperial College London Department of Computing. Since materials is the main source of obtaining lecture slides, tutorial sheets and whatnot, a computing student downloads something or the other from there daily.

This program can be used to avoid the hassle of downloading everything manually.

It downloads all the files from a student's materials page for that year. It also sets up a nice directory structure by year of study and course names.

Whenever the program is run it refreshes all the downloads as quite often professors change the the uploaded materials. If you want to refresh just one course, you can do that as well using the -q (--quick) flag.

## Requirements

1. Login credentials of your materials account.
2. Python3 installed on your machine
3. Google Chrome browser
4. Linux

## How to use it

1. Clone/Download this repository.
2. Make sure you have python3 installed. You can download it using ```sudo apt install python3-pip```. 
3. Open the teminal and go to where you have this repository.
4. Run ```pip3 install -r requirements.txt```
5. Run ```sh get_chromedriver.sh``` to download the latest chromedriver for your linux machine. Alternatively download it from [here](https://chromedriver.chromium.org/downloads).
6. Run the command ```python3 materials-downloader.py -s <your_shortcode> -p <your_password> -d <directory>``` to set your credentials and the relative path of the location where you want to store the downloads. You just have to do this once and can use the same command if your shortcode/password has been changed.

### Optional steps to download materials with just one single command single command

7. Open up your.bashrc file in a text editor using ```vim ~/.bashrc``` or ```nano ~/.bashrc```
8. Paste in the following lines.
```bash
imperial_materials_download() {
        cd ~/imperial/imperial-computing-materials-downloader # path to your repository
        python3 materials-downloader.py "$@"                  # call to script
        cd -                                                  # returning to working directory
}

alias impmat="imperial_materials_download"
```
9. Refresh the your bashrc using the command ```source ~/.bashrc```
10. You can just run ```impmat``` in the terminal to run the python script!


## Optional Flags

1. ```--quick <course_code>``` flag can be used to refresh materials for a particular course only. For example, if you just want to refresh the materials for the course 40009 - Computer Practical 1, you should run ```python3 materials-downloader.py -q 40009```.
2. ```--location <location>``` flag to store the downloaded materials in a place other tha the set directory.
3. ```--real``` flag can be used to run the browser outside of headless mode.
4. ```--shortcode <shortcode>``` flag can be used to set your shortcode.
5. ```--password ``` flag can be used to set the password.
6. ```--dir <dir>``` flag can be used to set where the directory containing all the materials is present.
7. ```--credentials ``` flag to view your credentials.
8. ```--update-chromedriver``` flag to update your chromedriver installation.
9. ```--help``` flag can be used to read about optional flags at anytime.

You can just call the flags using the fist letter of the flag like so ```-r``` where r is the first letter of the real flag.
