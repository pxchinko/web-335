# ============================================
# ; Title: massie-user-update.py
# ; Author: Sarah Massie
# ; Date: December 12 2020
# ; Modified By: Sarah Massie
# ; Description: UD operations using Python
# ;===========================================

from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335
db.users.update_one(
    {
        "employee_id": "00000008"
    },
    {
        "$set": {
            "email": "smassie@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "00000008"}))