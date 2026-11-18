city_flight = input("Choose between CapeTown or Durban: ") # The city they will be flying to 

num_nights = input("Enter the number of nights you will be saying at the hotel: ") # The number of nights they will be staying at the hotel

rental_days = input("Enter the number of days for which you will be hiring a car: ") # The number of days for which they will be hiring a car

def hotel_cost(num_nights):
    '''
    hotel_cost() : num_nights will be used to get the total cost for the entire hotel stay
    '''
    total = int(num_nights) * 900
    return(total)

def plane_cost(city_flight):
    '''
    plane_cost() : city_flight will be used to get the return cost for the flight
    '''
    if city_flight == "CapeTown":
        return(1200)

    else:
        return(700)

def car_rental(rental_days):
    '''
    car_rental() : rental_days will be used get the total cost of the car rental
    '''
    total_cost_rental = int(rental_days) * 400
    return(total_cost_rental)

def holiday_cost(num_nights, city_flight, rental_days):
    '''
    holiday_cost() : will use num_nights, city_flight and rental_days to get the total cost of the holiday
    '''
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)

    total_holiday_cost = hotel + plane + car
    return(total_holiday_cost)

print("The details for your holiday are as follows: ")
print(f"City choosen: {city_flight}")
print(f"Car rental cost: {rental_days}")
print(f"Number of nights in the hotel: {num_nights}")
print(f"Total cost of trip:{holiday_cost(num_nights, city_flight, rental_days)}")