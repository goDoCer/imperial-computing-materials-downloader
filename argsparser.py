import argparse

def get_args():
  parser = argparse.ArgumentParser()                                  

  parser.add_argument("-r", "--real", help="runs the browser outside of headless mode", action="store_true")
  parser.add_argument("-v", "--verbose", help="sets uotput to be verbose", action="store_true")                      
  parser.add_argument("-c", "--credentials", help="shows the credentials", action="store_true")

  parser.add_argument("-e", "--easymarking", help="gets feedback from E(asy) marking platform", action="store_true")

  parser.add_argument("-q", "--quick", help="gets materials for the provided course_code", 
                                        action="store", type=str)
  parser.add_argument("-l", "--location", help="stores downloads in specified location", 
                                        action="store", type=str)

  parser.add_argument("-d", "--dir", help="sets the directory where the materials should be stored", action="store")
  parser.add_argument("-s", "--shortcode", help="sets the shortcode", action="store")
  parser.add_argument("-p", "--password",  help="sets the password", action="store")

  return parser.parse_args()