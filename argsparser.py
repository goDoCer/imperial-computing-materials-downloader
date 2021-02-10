import argparse


def get_args():
    """Uses the argparse package to define the command line flags

    Returns:
      dict: Return a dictionary that maps from flag name to flag value
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-r", "--real", help="runs the browser outside of headless mode", action="store_true")
    parser.add_argument("-v", "--verbose",
                        help="sets uotput to be verbose", action="store_true")
    parser.add_argument("-c", "--credentials",
                        help="shows the credentials", action="store_true")

    parser.add_argument("-u", "--update-chromedriver",
                        help="Updates the chromedriver installation", action="store_true")

    parser.add_argument(
        "-d", "--dir", help="sets the directory where the materials should be stored", action="store")
    parser.add_argument("-s", "--shortcode",
                        help="sets the shortcode", action="store")
    parser.add_argument("-p", "--password",
                        help="sets the password", action="store_true")

    return parser.parse_args()
