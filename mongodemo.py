import pymongoclient = pymongo.MongoClient("use your credential or url")
db = client.virtusa
records=db.superwomen
d={"name":input("enter name"),"ph":int(input("enter phone number")),"mail":input("enter emailid")}
records.insert_one(d)
print("inserted sucessfully")
read=records.find()
for x in read:
    print(x)