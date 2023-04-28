#program to calculate user's holiday cost



def plane_cost(city_flight):
    if city_flight.lower() == 'london':
        
        return 1000
       
          
    elif city_flight.lower() == 'paris':
         
         return 5000
         
    elif city_flight.lower() == 'milan':
        
        return 100
    else:
       
        print(0)
     

def hotel_costs(num_nights):
    
    return num_nights * 100
   

def car_rental(rental_days):
    total_car = rental_days * 10
    return total_car
    

def holiday_cost():
    total_holiday = hotel_costs(num_nights)+ plane_cost(city_flight)+ car_rental(rental_days)
    
    return total_holiday

city_flight= (input('Please enter the name of the city you are flying to, please choose from Paris, London, or  Milan: '))

num_nights = int((input('Please enter the number of nights you will be staying at the hotel:')))

rental_days = int(input('Enter the number of days you will be hiring a car:'))


print('The cost for car hire is:')
print(car_rental(rental_days))


print('The cost for hotel stay is:')
print(hotel_costs(num_nights))

print('The cost for plane flight is:')

print(plane_cost(city_flight))

print('The total cost for the holiday is:')

print(holiday_cost())
