def filter1(**temp):
    print("values  available are ", temp)

    for key, value in temp.items():
        print("{} is {}".format(key,value))

filter1( temprature = 30 , pressure = 10  , country = "India" )
filter1( temprature = 22 , pressure = 8  , country = "Mexico" )