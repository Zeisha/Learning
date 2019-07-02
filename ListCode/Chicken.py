class Chicken:
    total_egg = 0
    def __init__(self, name , species , eggs = 0):
        self.name = name
        self.species = species
        self.eggs = eggs


    def lay_egg(self):
        self.eggs +=1
        print("Number of Eggs are for " + self.name + " is " + str(self.eggs))
        Chicken.total_egg +=1



c1 = Chicken("Alice" ,  "Patridge")
c2 = Chicken("Amelia" , "Speckled")

print("Total Eggs are " + str(Chicken.total_egg))
c1.lay_egg()
print("Total Eggs are " + str(Chicken.total_egg))
c2.lay_egg()
c2.lay_egg()

print("Total Eggs are " + str(Chicken.total_egg))



