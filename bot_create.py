import argparse
from FreelancerBot import FreelancerBot
from UpworkBot import UpworkBot
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", help="Specify whether freelancer or upwork.")
args = parser.parse_args()
account_type=args.type
if not isinstance(account_type, str):
    raise TypeError("Missing/Incorrect account_type")
if account_type == "freelancer":
    bot=FreelancerBot()
    bot.create()
if account_type == "upwork":
    bot=UpworkBot()
    bot.create()