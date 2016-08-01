
from pymongo import *
from bson.son import SON
c=MongoClient()
db=c.test
collection=db.items

def insert():
    item={
          "Type":"Laptop",
          "ItemNumber":"2345FDX",
          "Status":"Not used",
          "Location":{
                      "Department":"Storage",
                      "Building":"1A"
            },
          "Tags":["Not used","Laptop","Storage"]
    }
    collection.insert(item)
    
def insertTwo():
    two=[{
          "Type":"Laptop",
          "ItemNumber":"1234EXD",
          "Status":"In use",
          "Location":{
                      "Department":"Development",
                      "Building":"2B",
                      "Floor":12,
                      "Desk":120101,
                      "Owner":"Anderson,Thomas"
            },
          "Tags":["Laptop","Development","In Use"]
          },
         {"Type":"Laptop",
          "ItemNumber":"3456TFS",
          "Status":"In use",
          "Location":{
                      "Department":"Development",
                      "Building":"2B",
                      "Floor":12,
                      "Desk":120103,
                      "Owner":"Walker,Jan"
            },
          "Tags":["Laptop","Development","In Use"]
          }]
    collection.insert(two)
    
if __name__ == '__main__':
    #collection.create_index([("ItemNumber",ASCENDING)])
    for doc in collection.find({"Location.Owner":"Walker,Jan"}).hint([("ItemNumber",ASCENDING)]):
        print(doc["ItemNumber"])