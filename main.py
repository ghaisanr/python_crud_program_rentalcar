# ===================================
# [Rental car]
# ===================================
# Developed by. Ghaisan Rabbani
# JCDS - [JCDS-0412]


# /import function/
from utils.output_data import show_cars, show_cars_detail, show_one_cars
from utils.edit_data import change_data

# /===== Data Model =====/
# Data rental car 
data_rent = {
    "license plate": ["W 1687 SG","L 2984 AI","L 8031 BP", "W 2348 TY","W 1111 WW","L 3021 RI", "L 2021 PI", "W 9090 GG", "W 1222 KK", "L 7777 FC"], 
    "car brand": ["nissan","hyundai","jazz", "toyota", "jeep", "BMW", "alya", "Xenia", "fred", "mars"],
    "car type":["manual","automatic","automatic","manual","manual","automatic", "manual", "automatic", "manual", "automatic"],
    "year":  [2015, 2019, 2018, 2017, 2016, 2017, 2020, 2021, 2017, 2018],
    "price" :  [500_000, 700_000, 600_000, 800_000, 650_000, 900_000,  750_000, 550_000, 700_000, 850_000],
    "available" : [True,True,False,False,False, True, False, True, False, True],
}



# /===== Feature Program =====/
# Create your feature program here
def read(data:dict):
    """Read data from data model

    Args:
        data (dict): data for display
    """
    while True:
        print("\nreport menu for rental car")
        print("1.Report all rental car")
        print("2.Report by license plate")
        print("3.back to main menu")
        i=int(input("\nchoose sub menu for read data [1-3]: "))
        if i==1:
            print("\nList Rental car")
            show_cars(data)
        elif i==2:
            print("\nList Rental car by license plate")
            license_plate = input("Enter license plate: ")
            if license_plate.upper() not in data["license plate"]:
                print("License plate not found")
            else:
                show_cars_detail(data, license_plate)
        elif i==3:
            break
        else:
            print("Invalid choice. Please choose again.")


def create(data:dict):
    """add car to data model

    Args:
        data (dict): data model car

    """
    while True:
        print("\nadd your car to rent menu")
        print("1.add your car")
        print("2. back to main menu")
        i=int(input("\nchoose sub menu for add data [1-2]: "))
        if i==1:
            license_plate=input("Input license plate : ")
            if license_plate in data["license plate"]:
                print("License plate already exist")
            else:
                car_brand= input("input car brand: ")
                car_type = input("input car type (automatic, manual): ")
                year=  int(input("input year: "))
                price = int(input("input price/day: "))
                available = bool(input("input available (True or False): ").capitalize())
                show_one_cars(license_plate,car_brand,car_type,year,price,available)
                saved=input("do you seriously add your car to rent? (yes or no) ")
                if saved.lower() == "yes":
                    data["license plate"].append(license_plate)
                    data["car brand"].append(car_brand)
                    data["car type"].append(car_type)
                    data["year"].append(year)
                    data["price"].append(price)
                    data["available"].append(available)
                    print("your car has been added to rent")
                    print("\nList Rental car")
                    show_cars(data)
                else:
                    print("your car not added to rent, maybe next time")
        elif i==2:
            break
        else:
            print("Invalid choice. Please choose again.")

def update(data:dict):
    """edit your car in data rental car by primary key

    Args:
        data (dict): data rental car
    """
    while True:
        print("\nedit your car in rent menu")
        print("1.edit your car")
        print("2. back to main menu")
        i=int(input("\nchoose sub menu for edit data [1-2]: "))
        if i==1:
            license_plate=input("Input plat nomor : ")
            if license_plate in data["license plate"]:
                show_cars_detail(data_rent,license_plate)
                change_continue=input("this is your car, do you want continue to update? (yes or no)")
                if change_continue.lower()=="yes":
                    colum_change=input("pleas enter colum  you want to change (license plate, car brand, car type, year, price, available): ")
                    change_data(data_rent,license_plate, colum_change, "license plate")
                    change_data(data_rent,license_plate, colum_change, "car brand")
                    change_data(data_rent,license_plate, colum_change, "car type")
                    change_data(data_rent,license_plate, colum_change, "year")
                    change_data(data_rent,license_plate, colum_change, "price")
                    change_data(data_rent,license_plate, colum_change, "available")
                    show_cars_detail(data_rent, license_plate)
                    print("your car status has been changed")
                else:
                    print("your car has not been changed")
            else:
                print("plat number not found")
        elif i==2:
            break
        else:
            print("Invalid choice. Please choose again.")


def delete(data:dict):
    """delete your car in data rental car by primary key

    Args:
        data (dict): data rental car


    """
    while True:
        print("\ndelete your car in rent menu")
        print("1. delete your car")
        print("2. back to main menu")
        i=int(input("\nchoose sub menu for edit data [1-2]: "))
        if i==1:
            license_plate=input("input your car license plate: ")
            if license_plate.upper() in data["license plate"]:
                show_cars_detail(data_rent, license_plate)
                delete_data=input("do you want to delete this data? (yes or no)")
                if delete_data.lower()=="yes":
                    data["car brand"].remove(data["car brand"][data["license plate"].index(license_plate)])
                    data["car type"].remove(data["car type"][data["license plate"].index(license_plate)])
                    data["year"].remove(data["year"][data["license plate"].index(license_plate)])
                    data["price"].remove(data["price"][data["license plate"].index(license_plate)])
                    data["available"].remove(data["available"][data["license plate"].index(license_plate)])
                    data["license plate"].remove(license_plate)
                    print("your car has been deleted")
                else:
                    print("your car has not been deleted")
            else:
                print("your car is not found")
        elif i==2:
            break
        else:
            print("Invalid choice. Please choose again.")


# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    print("\nMenu for rental car")
    print("1.view data in rental car")
    print("2.add your car for rental your car")
    print("3.edit your car in rental car")
    print("4.delete your car in rental car")
    input_user = input("Insert your option: ")
    if input_user == "1":
        read(data_rent)
    elif input_user == "2":
        create(data_rent)
    elif input_user == "3":
        update(data_rent)
    elif input_user == "4":
        delete(data_rent)
    else:
        print("Input is not valid !")


if __name__ == "__main__":
    main()
