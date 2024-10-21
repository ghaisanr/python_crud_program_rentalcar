
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
    print("\n| License Plate | Car Brand           | Car type      |  Year  | Price     | Available |")
    for j in range (len(data["license plate"])):
        if data["license plate"][j] == license_plate.upper():
            print(f'|  {data["license plate"][j]:<13}| {data["car brand"][j]:<20}| {data["car type"][j]:<13} | {data["year"][j]:<6} | {data["price"][j]:<9} | {data["available"][j]:<10}|')

def show_one_cars(license_plate:str,car_brand:str,car_type:str,year:int,price:int,available:bool):
    """To  display one car by license plate, car brand, car type, year, price, available in database

    Args:
        license_plate (str): license plate  for display a car

        car_brand (str): car brand for display a car
        car_type (str): car type for a display
        year (int): year car for display
        price (int): price rent/day for display

        available (bool): available or not
    """
    print("\n| License Plate | Car Brand           | Car type      |  Year  | Price     | Available |")
    print(f'|  {license_plate:<13}| {car_brand:<20}| {car_type:<13} | {year:<6} | {price:<9} | {available:<10}|')

def show_all_customer(data):
    print("| License Plate | name customer       | number telphone  |  rent date  | return date |")
    for j in range (len(data["license plate"])):
        print(f'|  {data["license plate"][j]:<13}| {data["customer name"][j]:<20}| {data["number telphone"][j]:<16} | {data["rent date"][j]:<11} | {data["return date"][j]:<12}|')