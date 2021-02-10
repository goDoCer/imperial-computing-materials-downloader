sudo apt-get install unzip &&
LATEST_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE) &&
wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$LATEST_VERSION/chromedriver_linux64.zip &&
sudo unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/;