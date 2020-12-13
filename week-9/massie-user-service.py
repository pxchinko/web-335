# ============================================
# ; Title: massie-user-service.py
# ; Author: Sarah Massie
# ; Date: December 12 2020
# ; Modified By: Sarah Massie
# ; Description: CR operations using Python
# ;===========================================

from pymongo import MongoClient

import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335

user = {
    "first_name": "Josuke",
    "last_name": "Kujo",
    "email": "josukekujo@gmail.com",
    "employee_id": "00000008",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id
print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "00000008"}))