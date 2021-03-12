
#pitch=teeth/diameter
#pitch*diameter=teeth

class gear:
    def __init__(self,name,radius,teeth):


        self.name=name
        self.radius=radius
        self.teeth=teeth
        self.diameter=radius*2
        self.pitch=teeth/self.diameter


    def gear_print(self):

        
        print('Gear name: ' , self.name)
        print('Radius: ' , self.radius)
        print('Diameter: ' , self.diameter)
        print('Teeth: ' , self.teeth)
        print('Pitch: ' , self.pitch)
        print('~~~','\n'*2)



gear3v=False
gear4v=False
gear5v=False



gearsnum=int(input('how many gears do you want?:'))

#change this variables
gear1_radius=float(input('enter radius for gear 1: '))
gear1_teeth=float(input('enter teeth number for gear 1: '))

gear2_radius=float(input('enter radius for gear 2: '))

if gearsnum==3: 
    gear3v=True
    gear3_radius=float(input('enter radius for gear 3: '))

elif gearsnum==4: 
    gear4v=True
    gear4_radius=float(input('enter radius for gear 4: '))
    
elif gearsnum==5:
    gear5_radius=float(input('enter radius for gear 5: '))
    gear5v=True    




print('~~~','\n'*2)


gear1=gear('gear1',gear1_radius,gear1_teeth)
gear1.gear_print()




gear2=gear('gear2',gear2_radius,gear1.pitch*gear2_radius*2)
gear2.gear_print()


if gear3v:
    gear3 = gear('gear3', gear3_radius, gear1.pitch * gear3_radius * 2)
    gear3.gear_print()


if gear4v:
    gear4 = gear('gear4', gear4_radius, gear1.pitch * gear4_radius * 2)
    gear4.gear_print()

if gear5v:
    gear5 = gear('gear5', gear5_radius, gear1.pitch * gear5_radius * 2)
    gear5.gear_print()






xtemp=input('click enter to close')
