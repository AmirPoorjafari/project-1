#aliakbar poorahmadi     amir poorjafari

import random


class Car:
    def __init__(self, car_id, name, color, max_speed, acceleration, fuel_capacity, fuel_efficiency, initial_fuel):
        self.car_id = car_id
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.fuel_capacity = fuel_capacity
        self.fuel_efficiency = fuel_efficiency  
        self.initial_fuel = initial_fuel
        self.current_fuel = initial_fuel
        self.distance_covered = 0
        self.current_speed = max_speed  
        self.fuel_consumed_per_second = self.max_speed / self.fuel_efficiency 
        self.weight = 1000  
    
    
    def refuel(self, fuel_amount):
        self.current_fuel = min(self.current_fuel + fuel_amount, self.fuel_capacity)

    
    def drive(self, distance):
        fuel_needed = distance / self.fuel_efficiency
        if self.current_fuel >= fuel_needed:
            self.current_fuel -= fuel_needed
            self.distance_covered += distance
            return True
        return False

    
    
    def modify_weight_due_to_fuel(self):
        self.weight = 1000 + (self.fuel_capacity - self.current_fuel) * 2

    
    
    def update_speed(self):
        self.current_speed = max(self.max_speed - self.weight / 100, 10)

    
    
    def get_fuel_efficiency_at_current_speed(self):
        return self.fuel_consumed_per_second * (self.max_speed / self.current_speed)

    
    
    def __str__(self):
        return (f"ID: {self.car_id}, Name: {self.name}, Color: {self.color}, Speed: {self.current_speed} km/h, "
                f"Fuel: {self.current_fuel}L, Distance Covered: {self.distance_covered} km")



class FuelStation:
    
    
    def __init__(self, name, location):
        self.name = name
        self.location = location

    
    def refuel_car(self, car):
        fuel_amount = random.randint(10, 30)
        car.refuel(fuel_amount)
        print(f"{car.name} refueled {fuel_amount}L at {self.name} station.")


def create_random_car(car_id):
    name = f"Car {car_id}"
    color = random.choice(["Red", "Blue", "Green", "Yellow", "Black", "White"])
    max_speed = random.randint(120, 220)
    acceleration = random.uniform(2.0, 5.0)
    fuel_capacity = random.randint(40, 70)
    fuel_efficiency = random.uniform(8, 15)
    initial_fuel = random.randint(20, fuel_capacity)
    return Car(car_id, name, color, max_speed, acceleration, fuel_capacity, fuel_efficiency, initial_fuel)

def race(cars, distance):
    fuel_stations = [FuelStation("Station 1", 15), FuelStation("Station 2", 30), FuelStation("Station 3", 45)]
    for station in fuel_stations:
        print(f"Fuel Station at {station.location} km ")
    
    results = []

    for car in cars:
        print(f"Starting car {car.name}")
        total_time = 0
        distance_covered = 0
        
        while distance_covered < distance:
            car.modify_weight_due_to_fuel()
            car.update_speed()
            speed = car.current_speed
            time_to_cover = ((distance - distance_covered) / speed)*100
            total_time += time_to_cover
            distance_covered = distance
            
            print(f"{car.name} covered {distance_covered} km at speed {speed} km/h. ")
            
            if random.random() < 0.3:
                station = random.choice(fuel_stations)
                station.refuel_car(car)

        
        
        results.append((car.name, total_time,car.color))
        print(f"{car.name} finished the race in {total_time:.0f} min  and  color is {car.color}")



    
    winner = min(results, key=lambda x: x[1])
    print(f"\nThe winner is {winner[0]}  time  {winner[1]:.0f} min  color is {winner[2]}")




car_names = ["Car A", "Car B", "Car C", "Car D"]
cars = [create_random_car(i+1) for i in range(len(car_names))]



race(cars, 60)
