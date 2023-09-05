class pizza:
    radius =0
    area=0
    cost=0
    cheez=0
    def __init__(self,radius):
        self.radius=radius
    def display(self):
        print("area: ",self.area)
        print("price: ",self.cost)

class veg_pizza(pizza):
    def __init__(self,radius,cheez):
        self.area = 3.14*(radius**2)
        self.cheez=cheez
        self.cost=self.area*20
        if(sel.area<15):
            print("small")
        elif(sel.price>15 && sel.price
             h<75)
            
        
        if(cheez==1):
            self.cost+=(self.cost)*0.1
            print("extra price: ",(self.cost)*0.1)

class non_veg_pizza(pizza):
    def __init__(self,radius,cheez):
        self.area=3.14*(radius**2)
        self.cheez=cheez
        self.cost=self.area*15
        if(cheez==1):
            self.cost+=(self.cost)*0.1
            print("extra price: ",(self.cost)*0.1)

r=int(input("rnter radius: "))
ch= int(input("enter choice 1/0: "))
print("\n veg pizza price: ")
veg=veg_pizza(r,ch)
veg.display()

print("\n non veg pizza price: ")
nveg=non_veg_pizza(r,ch)
nveg.display()
        

    
        
        


