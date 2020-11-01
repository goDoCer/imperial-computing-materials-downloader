import datetime as dt
import json 
auth = json.load(open("./lib/auth.json"))

SHORTCODE         = auth["shortcode"]
PASSWORD          = auth["password"]
CHROMEDRIVER_PATH = "./lib/chromedriver"

MATERIALS_URL     = "https://materials.doc.ic.ac.uk/"
YEAR              = dt.datetime.now().year + 1