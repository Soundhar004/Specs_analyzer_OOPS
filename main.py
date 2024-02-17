from machine import automotives as a 
from cars import car as soundhar
from bikes import bike as tharun
from trucks import truck as karthi

print("NOTE : In giving brand name It will give under the Filtration of best Cars or Bikes or Trucks ")
Option1=input("Please enter the Automotive that you want : ")

if Option1=="car":
      print("Please Select The Brand Name in the List of Cars ")
      a.cars_list()
      Option2=input("By entering The Brand Name It Shows the Top and Best CAR :")
      if Option2=="BMW"or Option2=="bmw"or Option2=="Bmw":
            b=soundhar("BMW","M4","Black")  
            print(">>>Car that it is {} type"\
              .format(soundhar.type))
            b.start_car()
            b.car_spec()
            
      elif Option2=="AUDI"or Option2=="audi"or Option2=="Audi":
            c=soundhar("Audi","RS7","Yellow")
            print(">>>Car that it is {} type"\
              .format(soundhar.type))
            c.start_car()
            c.car1_spec()
      elif Option2=="Volkswagen"or Option2=="volkswagen":
            d=soundhar("Volkswagen","Polo","Red")
            print(">>>Car that it is {} type"\
              .format(soundhar.type))
            d.start_car()
            d.car2_spec()
      elif Option2=="Hyundai"or Option2=="hyundai":
            e=soundhar("Hyundai","Santa Fe","White")
            print(">>>Car that it is {} type"\
              .format(soundhar.type_1))
            e.start_car()
            e.car3_spec()
      elif Option2=="Maruthi suzuki"or Option2=="maruthi suzuki":
            f=soundhar("Maruthi Suzuki","Grand Vitara","Blue")
            print(">>>Car that it is {} type"\
              .format(soundhar.type_1))
            f.start_car()
            f.car4_spec() 
      elif Option2=="Mahindra"or Option2=="mahindra":
            g=soundhar("Mahindra","XUV700","Voilet")
            print(">>>Car that it is {} type"\
              .format(soundhar.type_1))
            g.start_car()  
            g.car5_spec()
      elif Option2=="TATA"or Option2=="tata"or Option2=="Tata":
            h=soundhar("TATA","Safari","Black")
            print(">>>Car that it is {} type"\
              .format(soundhar.type_1))
            h.start_car()  
            h.car6_spec()  
      elif Option2=="Toyota"or Option2=="toyota":
            i=soundhar("Toyota","Fortuner","White")
            print(">>>Car that it is {} type"\
              .format(soundhar.type_1))
            i.start_car()
            i.car7_spec()   
      else:
            print("Enter correct word")                



elif Option1 =="bike":
      print("Please Select The Brand Name in the List of Bikes ")
      a.bikes_list()
      Option2=input("By entering The Brand Name It Shows the Top and Best Bike :")
      if Option2=="YAMAHA"or Option2=="yamaha"or Option2=="Yamaha":
            x=tharun("YAMAHA","R15","RACING BLUE")
            print(">>>Bike that it is {} type"\
               .format(tharun.type))
            x.start_bike()
            x.bike_spec()
      elif Option2=="KTM"or Option2=="ktm"or Option2=="Ktm":
            y=tharun("KTM","DUKE 390","Green")
            print(">>>Bike that it is {} type"\
               .format(tharun.type))
            y.start_bike()
            y.bike1_spec() 
      elif Option2=="Royal Enfield"or Option2=="royal enfield":
            z=tharun("Royal Enfield","Classic 350","RED")
            print(">>>Bike that it is {} type"\
               .format(tharun.type1))
            z.start_bike()
            z.bike2_spec()   
      elif Option2=="SUZUKI"or Option2=="Suzuki"or Option2=="suzuki":
            l=tharun("Suzuki","Gixxer 250","Black")
            print(">>>Bike that it is {} type"\
               .format(tharun.type1))
            l.start_bike()
            l.bike3_spec()
      elif Option2=="Kawasaki"or Option2=="kawasaki":
            m=tharun("Kawasaki","H2 R","Black with Green")
            print(">>>Bike that it is {} type"\
               .format(tharun.type1))
            m.start_bike()
            m.bike4_spec() 
      elif Option2=="TVS"or Option2=="tvs"or Option2=="Tvs":
            n=tharun("TVS","Apache RTR 160","Black")
            print(">>>Bike that it is {} type"\
               .format(tharun.type1))
            n.start_bike()
            n.bike5_spec()
      elif Option2=="Bajaj"or Option2=="bajaj":
            o=tharun("Bajaj","Pulsar RS 200","White")
            print(">>>Bike that it is {} type"\
               .format(tharun.type1))
            o.start_bike()
            o.bike6_spec()     
      else:
            print("Enter correct word")
                     
   
              









            
elif Option1=="truck":
      
      z=karthi("VOLVO","FH16","WHITE")
      print(">>>Truck that it is {}"\
        .format(karthi.type))
      z.start_truck()
      z.batteries=89
      z.trucks_battery() 



