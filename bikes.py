from machine import automotives
from colorama import Back,Fore,Style

class bike(automotives):
    type="Sports"
    type1="Naked"

    def __init__(self, make, model, color):
        super().__init__(make, model, color)

    def start_bike(self):
        print("My attitude {} {} {} is take to Revenge"\
            .format(self.car_color,self.car_make,self.car_model))    
   
    # def bikes_battery(self):
    #     print("{}s battey level is now {}%"\
    #         .format(self.car_make,self.batteries))

    def bike_spec(self):
        bike_details={
            "Make         : ":'YAMAHA',"Model        : ":'R15',"color        : ":'Racing Blue',
            "Indian cost  : ":'Rupees 1.41lakhs - 1.95lakhs', 
            "EmissionType : ":'BS6',"Engine(CC)   : ":'155cc',"Mileage      : ":'40 km/l',
            "Max Power    : ":'18.4PS@ 10000RPM',"Max Torque   : ":'14.2Nm@7500rpm',
            "Kerb Weight  : ":'142kg',"Fuel Tank    : ":'11 Litres'
        }

        for x,y in bike_details.items():
            print(x,Fore.CYAN+y)

        print("Key Features of YAMAHA R15") 
        bike_feature=["   --> Anti-Lock Braking System","   --> Traction Control",
        '   --> Quick Shifter',"   --> Tubeless Tyre","   --> Alloy Wheel",
        "   --> Digital Fuel Indicator"]
        for i in bike_feature:
            print(Fore.GREEN+i)
        
        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.yamaha-motor-india.com/yamaha-r15v4.html")

    def bike1_spec(self):
        bike_details={
            "Make         : ":'KTM',"Model        : ":'DUKE 390',"color        : ":'Green',
            "Indian cost  : ":'Rupees 2.96lakhs - 3.00lakhs',
            "EmissionType : ":'BS6',"Engine(CC)   : ":'373.2cc',"Mileage      : ":'28.9 km/l',
            "Max Power    : ":'43.5 PS@9000 rpm',"Max Torque   : ":'37 Nm@7000rpm',
            "Kerb Weight  : ":'171kg',"Fuel Tank    : ":'13.4 Litres'
        }        
        for a,b in bike_details.items():
            print(a,Fore.CYAN+b)
        print("Key Feature of KTM DUKE")
        bike_feature=["   --> Anti Braking System","   --> Quick Shifter",
        "   --> Digital Tripmeter","    --> Digital Tachometer","   --> Full control over Incoming calls",
        "   --> And Audio Player"]
        for w in bike_feature:
            print(Fore.GREEN+w)

        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.ktmindia.com/ktm-bikes/naked-bike/ktm-390-duke")     

    def bike2_spec(self):
        bike_details={
                "Make         : ":'Royal Enfield',"Model        : ":'Classic 350',"color        : ":'Red Varient',
                 "Indian cost  : ":'Rupees 1.90lakhs - 2.21lakhs',
                "EmissionType : ":'BS6',"Engine(CC)   : ":'349.34cc',"Mileage      : ":'41.55 km/l',
                "Max Power    : ":'20.21 PS @ 6100rpm',"Max Torque   : ":'27 Nm @ 4000rpm',
                "Kerb Weight  : ":'195 kg',"Fuel Tank    : ":'13 Litres',"Battery      : ":'12 V/8Ah Capacity'
                }
        for i,v in bike_details.items():
            print(i,Fore.CYAN+v)
   
        print("Key Features of Royal Enfield Classic 350")
        bike_features=["   -->ABS Dual Channel ","   --> Electronic Fuel Injection",
        "   --> Air Cleaner - Paper element","   --> Lubrication - Wet sump forced lubrication",
        "   --> 0-100kmph - 16.30s","   --> Absorbers with 6-Step Adujstable Preload"]

        for i in bike_features:
            print(Fore.GREEN+i)

        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.royalenfield.com")               
            
    def bike3_spec(self):
        bike_details={
            "Make         : ":'Suzuki',"Model        : ":'Gixxer 250',"color        : ":'Black Varient',
            "Indian cost  : ":'Rupees 1.81lakhs - 1.98lakhs',
            "EmissionType : ":'BS6',"Engine(CC)   : ":'249cc',"Mileage      : ":'38.5 km/l',
            "Max Power    : ":'26.5 PS @ 9300rpm',"Max Torque   : ":'22.2 Nm @ 7300rpm',
            "Kerb Weight  : ":'156 kg',"Fuel Tank    : ":'12 Litres',"Battery      : ":'12 V/6 Ah Capacity'

        } 
        for a,b in bike_details.items():
            print(a,Fore.CYAN+b)

        print("Key Features of SUZUKI Gixxer 250")

        bike_features=["   --> Wet Multi-Plate Clutch Type","   --> Twin Muffler Varient",
        "   --> Low Fuel Indicator","   --> With Body Graphics","   --> Swing Arm Suspension"
        ]   
        for a in bike_features:
            print(Fore.GREEN+a)        
        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.suzukimotorcycle.co.in/product-details/gixxer-250")

    def bike4_spec(self):
        bike_details={
            "Make         : ":'Kawasaki',"Model        : ":'Ninja H2 R',"color        : ":'Black With Green',
             "Indian cost  : ":'Rupees 79.90lakhs - 81.10lakhs',
            "EmissionType : ":'BS6',"Engine(CC)   : ":'998cc',"Mileage      : ":'14 km/l',
            "Max Power    : ":'310PS@ 14000rpm',"Max Torque   : ":'165 Nm @12500rpm',
            "Kerb Weight  : ":'216 kg',"Fuel Tank    : ":'17 Litres',"Battery      : ":'12 V 8.6 Ah Capacity'

        }     
        for a,b in bike_details.items():
            print(a,Fore.CYAN+b)
        print("Key Features of Kwasaki Ninja H2 R ")

        bike_features=["   --> Hydraulic Clutch Type","   --> ALL TItanium Exhaust System",
        "   --> Wheelie and Sliding ControlOctane Rating - Unleaded Petrol",
        "   --> Cornering Management Function","   --> Electronic Throttle Valves",
        "   --> Spring Preload Adjustability Top-out Spring","   --> Compression and Rebound Damping"

        ]    
        for a in bike_features:
            print(Fore.GREEN+a)        
        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://kawasaki-india.com/bikes/ninja-h2")
    

    def bike5_spec(self):
        bike_details={
            "Make         : ":'TVS',"Model        : ":'Apache RTR 160',"color        : ":'Blue varient',
            "Indian cost  : ":'Rupees 1.25lakhs - 1.50lakhs',
            "EmissionType : ":'BS6',"Engine(CC)   : ":'159.77cc',"Mileage      : ":'40 to 50 km/l',
            "Max Power    : ":'16.04 PS @ 8750rpm',"Max Torque   : ":'13.85 Nm @ 7000rpm',
            "Kerb Weight  : ":'138 kg',"Fuel Tank    : ":'12 Litres',"Battery      : ":'12 V/6 Ah Capacity'

        }     
        for a,b in bike_details.items():
            print(a,Fore.CYAN+b)
        print("Key Features of TVS Apache RTR 160 ")

        bike_features=["   --> SOHC Fuel Injection","   --> Slipper Clutch Type",
        "   --> Muffler - Conventional Design","   --> TVS SmartXonnect",
        "   --> Glide Through Technology","   --> Roto Petal Disc Brake",
        "   --> Suspension - Gs Filled shox(MIG) with Spring Aid "
        ]    
        for a in bike_features:
            print(Fore.GREEN+a)        
        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.tvsmotor.com/tvs-apache/Apache-RTR-160-2V")

    def bike6_spec(self):
        bike_details={
            "Make         : ":'Bajaj',"Model        : ":'Pulsar RS 200',"color        : ":'White varient',
             "Indian cost  : ":'Rupees 1.43lakhs - 1.77lakhs',
            "EmissionType : ":'BS6',"Engine(CC)   : ":'199.5cc',"Mileage      : ":'35 km/l',
            "Max Power    : ":'24.5 PS @ 9750rpm',"Max Torque   : ":'18.7 Nm @ 8000rpm',
            "Kerb Weight  : ":'166 kg',"Fuel Tank    : ":'13 Litres',"Battery      : ":'12 V/8 Ah Capacity'

        }     
        for a,b in bike_details.items():
            print(a,Fore.CYAN+b)
        print("Key Features of ")

        bike_features=["   --> Anti Braking System Dual Channel","   --> Telescopic with Anti-Friction Bush",
        "   --> Nitrox mono shock Absorber with Canister","   --> Dual Wheel Disc Brake",
        "   --> With Engine Kill Switch "
        ]    
        for a in bike_features:
            print(Fore.GREEN+a)        
        print("IF you want more details to buy: Click The Link is Below")
        print(Fore.CYAN+"https://www.bajajauto.com/bikes/pulsar/pulsar-rs200")
        
    
        

        
