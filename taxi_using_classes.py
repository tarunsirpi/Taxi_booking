# TAXI BOOKING USING CLASSES

# locations, distance & amount
locations={'A':1,'B':2,'C':3,'D':4,'E':5}
booked_count =[0]
def calculate_distance(loc1,loc2):
    return abs(locations[loc1]-locations[loc2]) * 15

def calculate_amount(distance):
    return distance *10

# taxi initialization

taxi_list=[]

class Taxi:
    def __init__(self, name, location, amount, drop_time):
        self.name= name
        self.location= location
        self.amount= amount
        self.drop_time= drop_time
        self.booking_dict = {}

    def add_taxi(self):
        taxi_list.append(self)

    def get_booking_history(self):

        print('Booking History of ', self.name)
        count = 0
        for id in self.booking_dict:
            count += 1
            print(count)
            print('Customer ID: ', self.booking_dict[id]['Customer ID'])
            print('From: ', self.booking_dict[id]['From'])
            print('To: ', self.booking_dict[id]['To'])
            print('Pickup Time:{}.{} '.format(self.booking_dict[id]['Pickup Time'] // 60,self.booking_dict[id]['Pickup Time'] % 60))
            print('Drop Time:{}.{} '.format(self.booking_dict[id]['Drop Time'] // 60, self.booking_dict[id]['Drop Time'] % 60))
            print('Amount Charged: ', self.booking_dict[id]['Amount Charged'])
        print("Total amount received: ", self.amount)

# Booking taxi

class booking:
    def __init__(self, from_loc, to_loc, pickup_time):
        self.from_loc = from_loc
        self.to_loc = to_loc
        self.pickup_time = pickup_time

    def book_taxi(self):
        min_distance = -1
        available_taxis = []

        if self.from_loc != self.to_loc:
            for taxi in taxi_list:

                if taxi.drop_time <= self.pickup_time:
                    distance = calculate_distance(self.from_loc, taxi.location)

                    if min_distance == -1:
                        available_taxis.append(taxi)
                        min_distance = distance

                    elif distance < min_distance:
                        available_taxis.clear()
                        available_taxis.append(taxi)
                        min_distance = distance

                    elif distance == min_distance:
                        available_taxis.append(taxi)

            selected_taxi = available_taxis[0]
            min_amount = selected_taxi.amount
            for i in available_taxis:
                if i.amount < min_amount:
                    min_amount = i.amount
                    selected_taxi = i

            taxi_booked = selected_taxi

            booked_count[0] += 1

            booking_id = str(booked_count[0])
            customer_id = str(booked_count[0])

            distance = calculate_distance(self.from_loc, self.to_loc)
            fare = calculate_amount(distance)
            drop_time = self.pickup_time + distance

            taxi_booked.location = self.to_loc
            taxi_booked.drop_time = drop_time
            taxi_booked.amount += fare

            taxi_booked.booking_dict[booking_id] = {'Customer ID': customer_id,
                                                    'From': self.from_loc,
                                                    'To': self.to_loc,
                                                    'Pickup Time': self.pickup_time,
                                                    'Drop Time': drop_time,
                                                    'Amount Charged': fare}
            print("Taxi booked...")
            print("Booking ID : ", booking_id)
            print("Allotted Taxi : ", taxi_booked.name)

        else:
            print("Cannot book taxi if start and end location are same...")

###############################################


Taxi('taxi1','A',0,-1).add_taxi()
Taxi('taxi2','A',0,-1).add_taxi()
Taxi('taxi3','A',0,-1).add_taxi()
Taxi('taxi4','A',0,-1).add_taxi()
Taxi('taxi5','A',0,-1).add_taxi()

booking('B','C',2*60).book_taxi()
booking('E','C',3*60).book_taxi()
booking('A','E',3*60).book_taxi()
booking('A','B',4*60).book_taxi()
booking('E','B',4*60).book_taxi()
booking('D','E',4*60).book_taxi()
booking('A','C',4*60).book_taxi()
booking('A','D',4*60).book_taxi()

history = 'taxi1'
for t in taxi_list:
    if t.name == history:
        print(t.get_booking_history())

loop = '0'
print(loop)
while loop != '3':
    loop = input("\nTo book a taxi press 1\nTo view history of taxi press 2\nTo exit press 3\n")

    if loop == '1':
        print("Taxi locations available: ", locations.keys())
        start = input("Enter starting location: ")
        end = input("Enter ending location: ")
        pickup = int(input("Enter pickup time: "))

        booking(start, end, pickup).book_taxi()

    elif loop == '2':
        print("Taxis available for history...")
        for t in taxi_list:
            print(t.name)
        history = input("Enter taxi for history: ")
        for t in taxi_list:
            if t.name == history:
                print(t.get_booking_history())
    elif loop != '3':
        print("\nInvalid input")


