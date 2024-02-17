from machine import automotives
import colorama
from colorama import Back,Fore,Style 
colorama.init(autoreset=True)

class car(automotives):
    type="Sedan"
    type_1="Hatchback"

    def __init__(self,make,model,color):
        super().__init__(make,model,color)

    def start_car(self):
        print("Your {} {} {} is get ready for Action"\
            .format(self.car_color,self.car_make,self.car_model))
        
    # def cars_battery(self):
    #     print("Your {}s battery level is now {}%"\
    #         .format(self.car_make,self.batteries))

    def car_spec(self):
        car_details={
            "Make        : ":'BMW',"Model       : ":'M4 COMPETITION',"Color       : ":'Black',
            "Price       : ":'$73.556 - $75.674',"Indian cost : ":'Rupees1.59crore', 
            "Fueltype    : ":'Petrol',"Engine(CC)  : ":'3000cc',
            "Mileage     : ":'10.75 km/litre',"ABS         : ":'Yes',
            "Max Power   : ":'502.88bhp@6250rpm',"Max Torque  : ":'650Nm@2750-5500rpm',
            "SeatCapacity: ":'5',"AirBags     : ":'Frontal,Side,Knee AirBags'
        }
        for x,y in car_details.items():
            print(x ,Fore.CYAN + y)    

        print("Key Features of BMW M4")

        car_feature=["  --> M sports Exhaust","  --> Multi Steering system",
        "  --> Alloy Wheel","  --> Power Steering","  --> Electronic brake Assist"]
        for x in car_feature:
            print(Fore.GREEN+x)            
        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.bmw.in/en/all-models/m-series/m4-coupe/2020/bmw-4-series...")

    def car1_spec(self):
        car_details={
            "Make        : ":'AUDI',"Model       : ":'RS7',"Color       : ":'Yellow',
            "Price       : ":'$120,900 - $122,600',"Indian cost : ":'Rupees 2.24crore', 
            "Fueltype    : ":'Petrol',"Engine(CC)  : ":'3993cc',
            "Mileage     : ":'9.8 km/litre',"ABS         : ":'YES',
            "Max Power   : ":'560PS@6600rpm',"Max Torque  : ":'700Nm@1750-5500rpm',
            "SeatCapacity: ":'4',"AirBags     : ":'Frontal,Side,Knee AirBags'
        }
        for q,w in car_details.items():
            print(q,Fore.CYAN+w)

        print("Key Feature of AUDI RS7")
        car_feature=["   --> Multi Function Steering","   --> Fog Lights",
        "   --> Find Car Location","   --> Drive Mode 2"] 
        for q in car_feature:
            print(Fore.GREEN+q)

        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.audi.in/in/web/en/models/rs/rs-7-sportback-2020.html")


    def car2_spec(self):
        car_details={
            
            "Make        : ":'Volkswagen',"Model       : ":'Polo',"Color       : ":'Red',
            "Price       : ":'$18,600 - $25,960',"Indian cost : ":'Rupees6.74lakh - 12.44lakh', 
            "Fueltype    : ":'Petrol',"Engine(CC)  : ":'999cc',
            "Mileage     : ":'17.74 km/litre',"ABS         : ":'Yes',
            "Max Power   : ":'75.10bhp@6200rpm',"Max Torque  : ":'95Nm@2950-3800rpm',
            "SeatCapacity: ":'5',"AirBags     : ":'Frontal AirBags'
        }
        for a,b in car_details.items():
            print(a,Fore.CYAN+b)

        print("Ky Features of Volkswagen Polo") 
        car_feature=["   --> Anti Lock Braking System","   --> Power Windows Front",
        "   --> MPI Fuel Supply System","   --> Tilt & Telescopic Steering",
        "   --> Rack & Pinion Gear Type"]

        for q in car_feature:
            print(Fore.GREEN+q)

        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.volkswagen.co.in/en/models/polo.html")    

    def car3_spec(self):
        car_details={
            
            "Make        : ":'Hyundai',"Model       : ":'Santa Fe',"Color       : ":'White',
            "Price       : ":'$28,200 - $29,300',"Indian cost : ":'Rupees28.32lakh - 31.74lakh', 
            "Fueltype    : ":'Diesel',"Engine(CC)  : ":'2199cc',
            "Mileage     : ":'14.74 km/litre',"ABS         : ":'Yes',
            "Max Power   : ":'194.3BHP@3800rpm',"Max Torque  : ":'420.7Nm@1800-2500rpm',
            "SeatCapacity: ":'7',"AirBags     : ":'Frontal,Driver and Passengers Airbags'
        }
        for x,y in car_details.items():
            print(x,Fore.CYAN+y)
        print("Key Features Of Hyundai Santa Fe")
        car_feature=["   --> Adjustable Headlights","   --> Leather Steering Wheel",
        "   --> Electronic Multi Tripmeter","   --> Cruise Control","   --> MacPherson Strut Suspension",
        "   --> Ventilated Disc Brake"]
        for x in car_feature:
            print(Fore.GREEN+ x)
     
        print("If you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.hyundai.com/in")

    def car4_spec(self):
        car_details={
            "Make        : ":'Maruthi Suzuki',"Model       : ":'Grand Vitara Alpha',"Color       : ":'Blue Varient',
            "Indian cost : ":'Rupees7.99lakh - 13.96lakh', 
            "Fueltype    : ":'Petrol',"Engine(CC)  : ":'1490cc',
            "Mileage     : ":'27.97 km/litre',"ABS         : ":'Yes',
            "Max Power   : ":'91.18bhp@5500rpm',"Max Torque  : ":'122Nm@4400-4800rpm',
            "SeatCapacity: ":'5',"AirBags     : ":'Frontal,Side,Driver and Passengers Airbags'
        }

        for a,b in car_details.items():
            print(a, Fore.CYAN+b)

        print("Key Features of Maruthi Grand Vitara")

        car_feature=["   --> Torsion Rear Suspension","   --> Ventilted Disc Brake",
        "   --> Panoramic Sunroof","   --> Dual Tone Precision Cut Alloy Wheel",
        "   --> ALEXA Skill Connectivity","   --> Premium Sound System"
        ]
        for x in car_feature:
            print(Fore.GREEN+x)
     
        print( "If you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.nexaexperience.com/grand-vitara")

    def car5_spec(self):
        car_details={
            "Make        : ":'Mahindra',"Model       : ":'XUV700',"Color       : ":'Voilet Varient',
            "Indian cost : ":'Rupees13.45lakh - 24.95lakh', 
            "Fueltype    : ":'Diesel',"Engine(CC)  : ":'2198cc',
            "Mileage     : ":'17.19 km/litre',"ABS         : ":'Yes',
            "Max Power   : ":'182.38bhp@3500rpm',"Max Torque  : ":'450Nm@1750-2800rpm',
            "SeatCapacity: ":'5,7',"AirBags     : ":'Frontal,Side,Driver and Passengers Airbags'
        }
        for i,v in car_details.items():
            print(i,Fore.CYAN+v)

        print("Key Feature of Mahindra XUV700")
        car_feature=["   --> McPherson Suspension with FSD and Stabilizer Bar ",
        "   --> Adaptive Cruise Control with Start and Go","   --> Vanity Mirror Illumination",
        "   --> Day Time Running Lights","   --> Micro Hybrid Technology",
        "   --> Personalized Safety Alerts","   --> Electronic Park Brake"
        ]   
        for i in car_feature:
            print(Fore.GREEN+i)

        print( "If you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://auto.mahindra.com/suv/xuv700")

    def car6_spec(self):
        cars_detail={
            "Make        : ":'TATA',"Model       : ":'Safari',"Color       : ":'Black Varient',
            "Indian cost : ":'Rupees15.45lakh - 23.76lakh', 
            "Fueltype    : ":'Diesel',"Engine(CC)  : ":'1956cc',
            "Mileage     : ":'14.08 km/litre',"ABS         : ":'Yes',
            "Max Power   : ":'167.67bhp@3750rpm',"Max Torque  : ":'350nm@1750-2500rpm',
            "SeatCapacity: ":'6,7 Seaters',"AirBags     : ":'Frontal,Side,Driver and Passengers Airbags'
        }

        for o,p in cars_detail.items():
            print(o,Fore.CYAN+p)
 
        cars_feature=["   --> Kryotec2.0 L Turbocharged Engine","   --> Multi Drive Modes 2.0",
        "   --> Electronic Parking Brake(EPB)","   --> Colour TFT Display",
        "   --> Brake Disc Wiping","   --> Modes-Normal,Rough,Wet Airbags",
        "   --> 4 Tweeters,9 JBL Speakers over Wifi"

        ]
        for i in cars_feature:
            print(Fore.GREEN+i)

        print( "If you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://cars.tatamotors.com/suv/safari")

    def car7_spec(self):
        car_details={
            "Make        : ":'Toyota',"Model       : ":'Fortuner',"Color       : ":'White Varient',
            "Indian cost : ":'Rupees32.58lakh - 50.34lakh', 
            "Fueltype    : ":'Diesel',"Engine(CC)  : ":'2755cc',
            "Mileage     : ":'8.0 km/litre',"ABS         : ":'Yes',
            "Max Power   : ":'201.15bhp@3000-3400rpm',"Max Torque  : ":'500Nm@1600-2800rpm',
            "SeatCapacity: ":'7 Seaters',"AirBags     : ":'Frontal,Side,Driver and Passengers Airbags'
        }
        for i,v in car_details.items():
            print(i,Fore.CYAN+v)

        print("Key Features of Toyota Fortuner")
        car_features=["   --> Driving modes:Eco/Sport/Normal with VFC Steering","   --> Aero Stabilising Fins On ORVM",
        "   --> A-TRC[Active Traction Control]","   --> Pitch & Bounce Control",
        "   --> DAC [Downhill Assist Control","   --> WIL [Whiplash Injury Lessening]",
        "   --> ISOFIX Child Seats Mounts"
        ]    
        for i in car_features:
            print(Fore.GREEN+i)

        print( "If you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.toyotabharat.com/showroom/fortuner/index-fortuner.html")    




        


        



