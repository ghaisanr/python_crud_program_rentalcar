# ===================================
# [Rental car]
# ===================================
# Developed by. Ghaisan Rabbani
# JCDS - [JCDS-0412]


# /import function/
from utils.output_data import show_cars, show_cars_detail, show_one_cars
from utils.edit_data import change_data
from utils.admin import admin_security

# /===== Data Model =====/
# Data rental car 
data_rent = {
    "license plate": ["W 1687 SG","L 2984 AI","L 8031 BP", "W 2348 TY","W 1111 WW","L 3021 RI", "L 2021 PI", "W 9090 GG", "W 1222 KK", "L 7777 FC"], 
    "car brand": ["nissan","hyundai","jazz", "toyota", "jeep", "BMW", "alya", "Xenia", "fred", "mars"],
    "car type":["manual","automatic","automatic","manual","manual","automatic", "manual", "automatic", "manual", "automatic"],
    "year":  [2015, 2019, 2018, 2017, 2016, 2017, 2020, 2021, 2017, 2018],
    "price" :  [500_000, 700_000, 600_000, 800_000, 650_000, 900_000,  750_000, 550_000, 700_000, 850_000],
    "available" : [True,True,False,False,False, True, False, True, False, True]
}
#data admin for security key
data_admin={
    "username": ["admin1","admin2","admin3"],
    "password": ["admin123","admin123","admin123"]
}



# /===== Feature Program =====/
# Create your feature program here
def report_car(data:dict,objects:str):
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
        if i==1: #menampilkan semua data mobil
            print("\nList Rental car")
            show_cars(data)
        elif i==2: #menampilkan data mobil berdasarkan plat nomor
            print("\nList Rental car by license plate")
            license_plate = input("Enter license plate: ")
            if license_plate.upper() not in data["license plate"]:
                print("License plate not found") #jika plat nomor tidak ada
            else:
                show_cars_detail(data, license_plate) #plat nomor ada
        elif i==3:
            if objects=="admin": #output buat admin
                admin_menu(data_rent,objects)
            elif objects=="customer": #output buat customer
                customer_menu(data_rent,objects)
        else:
            print("Invalid choice. Please choose again.")


def add_car(data:dict):
    """add car to data model

    Args:
        data (dict): data model car

    """
    while True:
        print("\nadd your car to rent menu")
        print("1.add your car")
        print("2.back to main menu")
        i=int(input("\nchoose sub menu for add data [1-2]: "))
        if i==1: #menambah mobil dari plat nomor
            license_plate=input("Input license plate : ")
            license_plate=license_plate.upper()
            if license_plate in data["license plate"]: # jika plat nomor sudah ada di data
                print("License plate already exist")
            else: #jika belum ada maka
                car_brand= input("input car brand: ")
                car_type = input("input car type (automatic, manual): ")
                year=  int(input("input year: "))
                price = int(input("input price/day: "))
                available = bool(input("input available (True or False): ").capitalize())
                show_one_cars(license_plate,car_brand,car_type,year,price,available) #output mobil yang mau ditambahkan
                saved=input("do you seriously add your car to rent? (yes or no) ") # konfirmasi
                if saved.lower() == "yes": #simpan data
                    data["license plate"].append(license_plate)
                    data["car brand"].append(car_brand)
                    data["car type"].append(car_type)
                    data["year"].append(year)
                    data["price"].append(price)
                    data["available"].append(available)
                    print("your car has been added to rent")
                    print("\nList Rental car")
                    show_cars(data) #outup semua data mobil
                else: #else buat konfirmasi
                    print("your car not added to rent, maybe next time")
        elif i==2:
            admin_menu(data_rent,"admin")
        else:
            print("Invalid choice. Please choose again.")

def edit_car(data:dict):
    """edit your car in data rental car by primary key

    Args:
        data (dict): data rental car
    """
    while True:
        print("\nedit your car in rent menu")
        print("1.edit your car")
        print("2.back to main menu")
        i=int(input("\nchoose sub menu for edit data [1-2]: "))
        if i==1: #edit mobil berdasarkan plat nomor
            license_plate=input("Input plat nomor : ")
            if license_plate.upper() in data["license plate"]:
                show_cars_detail(data_rent,license_plate) #output mobil yang mau diedit
                change_continue=input("this is your car, do you want continue to update (yes or no) ? ") #konfirmasi
                if change_continue.lower()=="yes": #edit data
                    colum_change=input("please enter column  you want to change (license plate, car brand, car type, year, price, available): ")
                    change_data(data_rent,license_plate, colum_change, "license plate")
                    change_data(data_rent,license_plate, colum_change, "car brand")
                    change_data(data_rent,license_plate, colum_change, "car type")
                    change_data(data_rent,license_plate, colum_change, "year")
                    change_data(data_rent,license_plate, colum_change, "price")
                    change_data(data_rent,license_plate, colum_change, "available")
                else: #else konfirmasi
                    print("your car has not been changed")
                show_cars_detail(data_rent,license_plate)
            else: #else platnomor 
                print("plat number not found")
        elif i==2:
            admin_menu(data_rent,"admin")
        else:
            print("Invalid choice. Please choose again.")


def delete_car(data:dict):
    """delete your car in data rental car by primary key

    Args:
        data (dict): data rental car
    """
    while True:
        print("\ndelete your car in rent menu")
        print("1. delete your car")
        print("2. back to main menu")
        i=int(input("\nchoose sub menu for edit data [1-2]: "))
        if i==1: #hapus mobil
            license_plate=input("input your car license plate: ")
            if license_plate.upper() in data["license plate"]: #cek plat nomor
                show_cars_detail(data_rent, license_plate) #output mobil yang mau dihapus
                delete_data=input("do you want to delete this data (yes or no) ? ") #konfirmasi
                if delete_data.lower()=="yes": #penghapusan data
                    license_plate=license_plate.upper() #untuk license plate bisa dihapus
                    data["car brand"].remove(data["car brand"][data["license plate"].index(license_plate)])
                    data["car type"].remove(data["car type"][data["license plate"].index(license_plate)])
                    data["year"].remove(data["year"][data["license plate"].index(license_plate)])
                    data["price"].remove(data["price"][data["license plate"].index(license_plate)])
                    data["available"].remove(data["available"][data["license plate"].index(license_plate)])
                    data["license plate"].remove(license_plate)
                    print("your car has been deleted")
                else: #else konfirmasi
                    print("your car has not been deleted")
            else: #else plat nomor
                print("your car is not found")
        elif i==2:
            admin_menu(data_rent,"admin")
        else:
            print("Invalid choice. Please choose again.")

def order_car(data:dict):
    """function order car for customer

    Args:
        data (dict): data_rent car
    """
    while True:
        print("\norder car sub menu")
        print("1. order car")
        print("2. back to main menu")
        i=int(input("\nchoose sub menu for edit data [1-2]: "))
        if i==1: #order mobil
            show_cars(data_rent)
            license_plate=input("input license plat for rent: ") #input plat nomor yang mau di order
            if license_plate.upper() in data_rent["license plate"] and  data_rent["available"][data_rent["license plate"].index(license_plate.upper())]==True:
                show_cars_detail(data,license_plate) #print mobil yang mau diorder
                validasi= input("this is car you want to rent (yes/no)? ") #validasi
                if validasi.lower()=="yes": #merubah status
                    data_rent["available"][data_rent["license plate"].index(license_plate.upper())]=False
                    print("your car has been rented, please confirmation to admin for payment")
                else: #else konfirmasi
                    print("your car has not been rented")
            else: #else plat nomor
                print("car is not available!!!")
        elif i==2:
            customer_menu(data_rent,"customer")
        else:
            print("Invalid choice. Please choose again.")

################## menu #####################
def admin_menu(data_rent,objects):
    """Function for admin to main program
    """
    print("\nMenu for rental car")
    print("1.view data in rental car")
    print("2.add your car for rental your car")
    print("3.edit your car in rental car")
    print("4.delete your car in rental car")
    print("5.exit")
    input_user = input("choose menu (input number)? ")
    if input_user == "1":
        report_car(data_rent,objects)
    elif input_user == "2":
        add_car(data_rent)
    elif input_user == "3":
        edit_car(data_rent)
    elif input_user == "4":
        delete_car(data_rent)
    elif input_user == "5":
        print("thank you for using this program")
        exit()
    else:
        print("Input is not valid !")
        admin_menu(data_rent,objects)

def customer_menu(data_rent,objects):
    """Function for customer to main program for order rental car
    """
    print("\nMenu for rental car")
    print("1.view data in rental car")
    print("2.order car for rental")
    print("3.exit")
    input_user = input("choose menu (input number)? ")
    if input_user == "1":
        report_car(data_rent,objects)
    elif input_user == "2":
        order_car(data_rent)
    elif input_user == "3":
        print("thank you for using this program")
        exit()
    else:
        print("Input is not valid !")
        customer_menu(data_rent,objects)                  

# /===== Main Program =====/
# Create your main program here
def main_menu():
    print("===== WELCOME TO RENTAL CAR =====")
    objects=input("admin or customer? ")
    if objects.lower()=="admin":
        print("=========please login your account=========")
        username=input("username: ")
        password=input("password: ")
        if admin_security(data_admin,username,password) == True:
            print("you succesfully login your account")
            admin_menu(data_rent,objects)
        else:
            print("username or password is not valid !, please try again!!!")
    elif objects.lower()=="customer":
        customer_menu(data_rent,objects)
    else:
        print("Input is not valid !")

main_menu()