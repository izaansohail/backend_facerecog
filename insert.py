import pymongo
import gridfs
def Insert(name , age , cnic , address , phone_number , gender , carreg, email, image1_name , image2_name , image3_name):
 client = pymongo.MongoClient('mongodb://localhost:27017/')
 db = client.Citizen
 fs = gridfs.GridFS(db)
 collection = db.get_collection('CitizenData')
 datafile1 = open(image1_name,'rb').read()
 datafile2 = open(image2_name , 'rb').read()
 datafile3 = open(image3_name , 'rb').read()
 image1_id = fs.put(datafile1 , filename = name)
 image2_id = fs.put(datafile2 , filename = name)
 image3_id = fs.put(datafile3 , filename = name)
 collection.insert_one({'Name' : name , 'Age' : age , 'Cnic': cnic , 'Address': address , 'Phone_number':phone_number , 'gender':gender ,'carreg':carreg , 'email':email , 'Image1_id':image1_id, 'Image2_id':image2_id, 'Image3_id': image3_id})
def main():
 number=int(input("How many records would you like to enter : "))
 print(number)
 for x in range(number):
  name = input("Enter the name : ")
  age = input("Enter the age : ")
  cnic = input("Enter the cnic : ")
  address = input("Enter the address : ")
  phone_number = input("Enter the phone_number : ")
  gender =  input("Enter the gender : ")
  carreg = input("Enter car registeration number : ")
  email = input("Enter Email id : ")
  image1_name = input("Enter the image1 name : ")
  image2_name = input("Enter the image2 name : ")
  image3_name = input("Enter the image3 name : ")
  Insert(name , age , cnic , address , phone_number , gender , carreg, email, image1_name , image2_name , image3_name)


main()