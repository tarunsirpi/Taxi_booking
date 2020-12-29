## TAXI BOOKING USING CLASSES

locations={'A':1,'B':2,'C':3,'D':4,'E':5}

def calculate_distance(loc1,loc2):
    return abs(locations[loc1]-locations[loc2]) * 15

def calculate_amount(distance):
    return distance *10

taxi_dict = {}
booking_dict = {}

class taxi:
    def add_taxi(self, name, location, amount, drop_time):
        taxi_dict[name] = {'name': name,
                           'location': location,
                           'amount': amount,
                           'drop_time': drop_time}

    def booking_history(self,taxi):
        print('Booking History of ', taxi)
        count = 0
        for id in booking_dict:
            if booking_dict[id]['Taxi Name'] == taxi:
                count += 1
                print(count)
                print('Customer ID: ', booking_dict[id]['Customer ID'])
                print('From: ', booking_dict[id]['From'])
                print('To: ', booking_dict[id]['To'])
                print('Pickup Time:{}.{} '.format(booking_dict[id]['Pickup Time'] // 60,booking_dict[id]['Pickup Time'] % 60))
                print('Drop Time:{}.{} '.format(booking_dict[id]['Drop Time'] // 60, booking_dict[id]['Drop Time'] % 60))
                print('Amount Charged: ', booking_dict[id]['Amount Charged'])
        print("Total amount received: ", taxi_dict[taxi]['amount'])


class booking:
    def book_taxi(self, from_loc, to_loc, pickup_time):
        min_distance = -1
        available_taxis = []

        for i in taxi_dict:
            taxi = taxi_dict[i]

            if taxi['drop_time'] <= pickup_time:
                distance = calculate_distance(from_loc, taxi['location'])

                if min_distance == -1:
                    available_taxis.append(i)
                    min_distance = distance

                elif distance < min_distance:
                    available_taxis.clear()
                    available_taxis.append(i)
                    min_distance = distance

                elif distance == min_distance:
                    available_taxis.append(i)

        selected_taxi = available_taxis[0]
        min_amount = taxi_dict[selected_taxi]['amount']
        for i in available_taxis:
            if taxi_dict[i]['amount'] < min_amount:
                min_amount = taxi_dict[i]['amount']
                selected_taxi = i

        taxi_booked=selected_taxi
        booking_id = str(len(booking_dict) + 1)
        customer_id = str(len(booking_dict) + 1)

        distance = calculate_distance(from_loc, to_loc)
        fare = calculate_amount(distance)
        drop_time = pickup_time + distance

        taxi_dict[taxi_booked]['location'] = to_loc
        taxi_dict[taxi_booked]['drop_time'] = drop_time
        taxi_dict[taxi_booked]['amount'] += fare

        booking_dict[booking_id] = {'Customer ID': customer_id,
                                    'From': from_loc,
                                    'To': to_loc,
                                    'Pickup Time': pickup_time,
                                    'Drop Time': drop_time,
                                    'Amount Charged': fare,
                                    'Taxi Name': taxi_booked}
        print("Taxi booked...")
        print("Booking ID : ", booking_id)
        print("Allotted Taxi : ", taxi_booked)


t1=taxi()
t1.add_taxi('taxi1','A',0,-1)
t1.add_taxi('taxi2','A',0,-1)
t1.add_taxi('taxi3','A',0,-1)
t1.add_taxi('taxi4','A',0,-1)
t1.add_taxi('taxi5','A',0,-1)

b1= booking()
b1.book_taxi('B','C',2*60)
b1.book_taxi('E','C',3*60)
b1.book_taxi('A','E',3*60)
b1.book_taxi('A','B',4*60)
b1.book_taxi('E','B',4*60)
b1.book_taxi('D','E',4*60)
b1.book_taxi('A','C',4*60)
b1.book_taxi('A','D',4*60)

t1.booking_history('taxi2')
print(taxi_dict)