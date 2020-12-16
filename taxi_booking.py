## CALL TAXI BOOKING

# locations, distance & amount
locations={'A':1,'B':2,'C':3,'D':4,'E':5}

def calculate_distance(loc1,loc2):
    return abs(locations[loc1]-locations[loc2]) * 15

def calculate_amount(distance):
    return distance *10

# taxi initialization
taxi_dict={}
def taxi (name,location,amount,drop_time):
    taxi_dict[name]={'name':name,
                     'location':location,
                     'amount':amount,
                     'drop_time':drop_time}

taxi('taxi1','A',0,-1)
taxi('taxi2','A',0,-1)
taxi('taxi3','A',0,-1)
taxi('taxi4','A',0,-1)
taxi('taxi5','A',0,-1)

# taxi finding

def find_taxi(from_location,pickup_time):
    min_distance=-1
    available_taxis=[]

    for i in taxi_dict:
        taxi=taxi_dict[i]

        if taxi['drop_time'] <= pickup_time :
            distance=calculate_distance(from_location,taxi['location'])

            if min_distance == -1 :
                available_taxis.append(i)
                min_distance=distance

            elif distance < min_distance :
                available_taxis.clear()
                available_taxis.append(i)
                min_distance=distance

            elif distance == min_distance:
                available_taxis.append(i)

    selected_taxi=available_taxis[0]
    min_amount=taxi_dict[selected_taxi]['amount']
    for i in available_taxis:
        if taxi_dict[i]['amount'] < min_amount :
            min_amount = taxi_dict[i]['amount']
            selected_taxi = i

    return selected_taxi

# booking a taxi
booking_dict = {}

def book_taxi(from_loc,to_loc,pickup_time):
    taxi_booked = find_taxi(from_loc,pickup_time)
    booking_id= str(len(booking_dict) +1)
    customer_id = str(len(booking_dict) + 1)

    distance=calculate_distance(from_loc,to_loc)
    fare=calculate_amount(distance)
    drop_time = pickup_time + distance

    taxi_dict[taxi_booked]['location'] = to_loc
    taxi_dict[taxi_booked]['drop_time'] = drop_time
    taxi_dict[taxi_booked]['amount'] += fare

    booking_dict[booking_id] = {'Customer ID':customer_id,
                                'From':from_loc,
                                'To':to_loc,
                                'Pickup Time':pickup_time,
                                'Drop Time':drop_time,
                                'Amount Charged':fare,
                                'Taxi Name':taxi_booked}
    print("Taxi booked...")
    print("Booking ID : ",booking_id)
    print("Allotted Taxi : ",taxi_booked)

# Booking history

def booking_history(taxi):
    print('Booking History of ',taxi)
    count=0
    for id in booking_dict:
        if booking_dict[id]['Taxi Name'] == taxi :
            count+=1
            print(count)
            print('Customer ID: ',booking_dict[id]['Customer ID'])
            print('From: ',booking_dict[id]['From'])
            print('To: ',booking_dict[id]['To'])
            print('Pickup Time:{}.{} '.format(booking_dict[id]['Pickup Time']//60,booking_dict[id]['Pickup Time']%60))
            print('Drop Time:{}.{} '.format(booking_dict[id]['Drop Time']//60,booking_dict[id]['Drop Time']%60))
            print('Amount Charged: ',booking_dict[id]['Amount Charged'])
    print("Total amount received: ",taxi_dict[taxi]['amount'])


## Booking and history

book_taxi('B','C',2*60)
book_taxi('E','C',3*60)
book_taxi('A','E',3*60)
book_taxi('A','B',4*60)
book_taxi('E','B',4*60)
book_taxi('D','E',4*60)
book_taxi('A','C',4*60)
book_taxi('A','D',4*60)

booking_history('taxi1')

loop='y'
while loop == 'y':
    print("Taxi locations available: ",locations.keys())
    start=input("Enter starting location: ")
    end=input("Enter ending location: ")
    pickup= int(input("Enter pickup time: "))
    book_taxi(start,end,pickup)

    loop=input("continue booking... (y/n): ")
loop='y'
while loop == 'y':
    print("Taxis available...",taxi_dict.keys())
    history=input("Enter taxi for history: ")
    booking_history(history)

    loop=input("continue booking... (y/n): ")
