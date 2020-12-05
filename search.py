import pymongo
import gridfs
def Search_by_cnic(cnic):
 client = pymongo.MongoClient('mongodb://localhost:27017/')
 db = client.Citizen
 fs = gridfs.GridFS(db)
 collection = db.get_collection('CitizenData')
 Data = collection.find_one({'Cnic': cnic})
 imageid = collection.find_one({'Cnic': cnic} , {"Image1_id":1 , "_id":0} )
 print(Data)
def Search_by_CarRegisteration(number):
 client = pymongo.MongoClient('mongodb://localhost:27017/')
 db = client.Citizen
 fs = gridfs.GridFS(db)
 collection = db.get_collection('CitizenData')
 Data = collection.find_one({'carreg': number})
 imageid = collection.find_one({'carreg': number} , {"Image1_id":1 , "_id":0} )
 print(Data)
def main():
   choice = int(input("Enter\n1. to search by cnic:\n2. to search by car registeration number:\n"))
   if choice == 1 :
      cnic = input("Enter the cnic: ")
      Search_by_cnic(cnic)
   elif choice == 2:
      car_registeration_number = input("Enter the car registeration number: ")
      Search_by_CarRegisteration(car_registeration_number)
   else:
      print("wrong choice entered")
  

main()