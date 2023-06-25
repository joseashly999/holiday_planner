# the site of ABC holiday planner
print(f"Below are this week's deal on travel around Europe on ABC planner. Answer the following questions and we will show you the total estimate of your trip."+"\n"+" Choose from the below destinations"+"\n"+"Venice"+"  "+ "Greece"+" "+"Spain"+" "+"France")

city_flight=input("Please select your destination:")          # user inputs the destination from above choices
city_flight=city_flight.lower()                               # converts the input into lower case
num_nights= int(input("Please enter the number of nights spent at the ABC planner partner hotel:"))
rental_days=int(input("Please enter the number of days you will require a car provided by ABC planner:"))
pernight_hotel=55                                             # set default hotel price 
perday_car=75                                                 # set default car rental price




def hotel_cost(num_nights=0):                                 # function 1, to estimate the money spent on stay. default value=0 incase the user doesnt choose to stay at ABC partner hotel
    cost=num_nights*pernight_hotel
    return cost

def plane_cost(city_flight):                                  # function2, flight cost. destination_dict has the ticket prices to the cities
    destination_dict={'venice':300,'greece':360,'spain':400,'france':400}
    cost=destination_dict[city_flight]
    return cost

def car_rental(rental_days=0):                                # function 3, rental price. default value 0 , if the user doesnt want to rent a car
    cost=rental_days*perday_car
    return cost

stay_cost=hotel_cost(num_nights)                              # creating three variables to store the "cost" returned from each functions
flight_cost=plane_cost(city_flight)
rental_cost=car_rental(rental_days)

def holiday_cost(stay_cost,flight_cost,rental_cost):          # function 4
    total_cost= stay_cost + flight_cost + rental_cost           
    return total_cost



total_cost=holiday_cost(stay_cost,flight_cost,rental_cost)     # total estimated cost
print(f"Round trip ticket price:{flight_cost}")
print(f"Cost of stay at ABC partner hotel:{stay_cost} ")
print(f"Car rental cost for {rental_days}: {rental_cost}")
print(f" Your total cost for trip to {city_flight} will be {total_cost} GBP. Please contact us for further details and booking. Thank you")
    
    