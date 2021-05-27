# for loop with Break
# after for loop ypu have to learn all lops & structure of the program


key_location="chair"
location=["Sofa","garage","chair","table","closet"]

for loc in location:
    if loc == key_location:
      print("Key found at ",loc)
      break
    else:
      print("Key not found at", loc)
print("end")