# for loop with Break

key_location="chair"
location=["Sofa","garage","chair","table","closet"]

for loc in location:
    if loc == key_location:
      print("Key found at ",loc)
      break
    else:
      print("Key not found at", loc)
print("end")