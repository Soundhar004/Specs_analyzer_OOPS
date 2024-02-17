import colorama
from colorama import Back,Fore,Style
class automotives:

    def __init__(self,make,model,color):
        self.car_make=make
        self.car_model=model
        self.car_color=color
        #self.batteries=0


    def soundhar(self):
        print("The Ultimate Machine {} {} {} is ready to Race "\
            .format(self.car_color,self.car_make,self.car_model))
        

    def cars_list():
        cars_name=["   --> BMW ","   --> AUDI","   --> volkswagen",
        "   --> Hyundai","   --> Maruthi Suzuki","   --> Mahindra",
        "   --> TATA","   --> Toyota"
        ]
        for i in cars_name:
            print(Fore.LIGHTBLACK_EX+i)   

    def bikes_list():
        bikes_name=["   --> Yamaha","   --> KTM","   --> Royal Enfield",
        "   --> Suzuki","   --> Kawasaki","   --> TVS ","   --> Bajaj"]   
        for i in bikes_name:
            print(Fore.LIGHTBLACK_EX+i)
            