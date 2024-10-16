
def show_cars(data:dict):
    """to display all data in database

    Args:
        data (dict): data rental cara
    """
    print("| License Plate | Car Brand           | Car type      |  Year  | Price     | Available |")
    for j in range (len(data["license plate"])):
        print(f'|  {data["license plate"][j]:<13}| {data["car brand"][j]:<20}| {data["car type"][j]:<13} | {data["year"][j]:<6} | {data["price"][j]:<9} | {data["available"][j]:<10}|')

def show_cars_detail(data:dict,license_plate:str):
    """to display one car by license platedata in database


    Args:
        data (dict): data rental car
        license_plate (str): license plat for display a car
    """
    print("| License Plate | Car Brand           | Car type      |  Year  | Price     | Available |")
    for j in range (len(data["license plate"])):
        if data["license plate"][j] == license_plate.upper():
            print(f'|  {data["license plate"][j]:<13}| {data["car brand"][j]:<20}| {data["car type"][j]:<13} | {data["year"][j]:<6} | {data["price"][j]:<9} | {data["available"][j]:<10}|')

def show_one_cars(license_plate,car_brand,car_type,year,price,available):
    """To  display one car by license plate, car brand, car type, year, price, available in database

    Args:
        license_plate (_type_): license plate  for display a car

        car_brand (_type_): car brand for display a car
        car_type (_type_): car type for a display
        year (_type_): year car for display
        price (_type_): price rent/day for display

        available (_type_): available or not
    """
    print("| License Plate | Car Brand           | Car type      |  Year  | Price     | Available |")
    print(f'|  {license_plate:<13}| {car_brand:<20}| {car_type:<13} | {year:<6} | {price:<9} | {available:<10}|')