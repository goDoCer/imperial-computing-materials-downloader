import datetime as dt
import json 
auth = json.load(open("./lib/auth.json"))

SHORTCODE         = auth["shortcode"]
PASSWORD          = auth["password"]
DIRECTORY         = auth["directory"]
CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"

MATERIALS_URL     = "https://materials.doc.ic.ac.uk/"
YEAR              = 2021