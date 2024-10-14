
def show_cars(data):
    print("| License Plate | Car Brand           | Car type      |  Year  | Price     | Available |")
    for j in range (len(data["license plate"])):
        print(f'|  {data["license plate"][j]:<13}| {data["car brand"][j]:<20}| {data["car type"][j]:<13} | {data["year"][j]:<6} | {data["price"][j]:<9} | {data["available"][j]:<10}|')

def show_cars_detail(data,license_plate):
    print("| License Plate | Car Brand           | Car type      |  Year  | Price     | Available |")
    for j in range (len(data["license plate"])):
        if data["license plate"][j] == license_plate.upper():
            print(f'|  {data["license plate"][j]:<13}| {data["car brand"][j]:<20}| {data["car type"][j]:<13} | {data["year"][j]:<6} | {data["price"][j]:<9} | {data["available"][j]:<10}|')

def show_one_cars(license_plate,car_brand,car_type,year,price,available):
    print("| License Plate | Car Brand           | Car type      |  Year  | Price     | Available |")
    print(f'|  {license_plate:<13}| {car_brand:<20}| {car_type:<13} | {year:<6} | {price:<9} | {available:<10}|')