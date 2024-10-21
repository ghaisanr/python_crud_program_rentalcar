# ===================================
# [Rental car]
# ===================================
# Developed by. Ghaisan Rabbani
# JCDS - [JCDS-0412]


# /import function/
from utils.output_data import show_cars, show_cars_detail, show_one_cars, show_all_customer
from utils.edit_data import change_data, confirmation
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

customer_rent={
    "license plate": ["L 8031 BP", "W 2348 TY","W 1111 WW","L 2021 PI","W 1222 KK"],
    "customer name":  ["ghaisan","rabbani","yoga","mawar","budi"],
    "number telphone": ["081234345656","081342425454", "081234567890",  "081234567891", "081234567892"],
    "rent date": ["16-02-24","17-02-24","15-02-24", "16-02-24", "18-02-24"],
    "return date": ["20-02-24","21-02-24","22-02-24", "20-02-24", "21-02-24"]
}

confirmation_customer_rent={
    "license plate":[],
    "customer name":[],
    "number telphone": [],
    "rent date": [],
    "return date": [],
}





# /===== Feature Program =====/
# Create your feature program here
def report_car(data:dict,objects:str):
    """Read data and show data for all or for one car by license plate

    Args:
        data (dict): data for display
    """
    while True:
        print("\nreport menu for rental car")
        print("1.Report all rental car")
        print("2.Report by license plate")
        print("3.back to main menu")
        isubmenu=input("\nchoose sub menu for read data [1-3]: ")
        if isubmenu=="1": #menampilkan semua data mobil
            print("\nList Rental car")
            show_cars(data)
        elif isubmenu=="2": #menampilkan data mobil berdasarkan plat nomor
            print("\nList Rental car by license plate")
            license_plate = input("Enter license plate: ").upper()
            if license_plate not in data["license plate"]:
                print("License plate not found") #jika plat nomor tidak ada
            else:
                show_cars_detail(data, license_plate) #plat nomor ada
        elif isubmenu=="3":
            if objects=="admin": #output buat admin
                admin_menu(data_rent,objects)
            elif objects=="customer": #output buat customer
                customer_menu(data_rent,objects)
        else:
            print("Invalid choice. Please choose again.")
            report_car(data_rent,objects)


def add_car(data:dict):
    """add car to data model

    Args:
        data (dict): data model car

    """
    while True:
        print("\nadd your car to rent menu")
        print("1.add your car")
        print("2.back to main menu")
        isubmenu=input("\nchoose sub menu for add data [1-2]: ")
        if isubmenu=="1": #menambah mobil dari plat nomor
            license_plate=input("Input license plate : ").upper()
            if license_plate in data["license plate"]: # jika plat nomor sudah ada di data
                print("License plate already exist")
            else: #jika belum ada maka
                car_brand= input("input car brand: ")
                car_type = input("input car type (automatic, manual): ")
                year=  int(input("input year: "))
                price = int(input("input price/day: "))
                available = bool(int(input("input available (1 for True or 0 for False): ")))
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
        elif isubmenu=="2":
            admin_menu(data_rent,"admin")
        else:
            print("Invalid choice. Please choose again.")
            add_car(data_rent)

def edit_car(data:dict):
    """edit your car in data rental car by primary key

    Args:
        data (dict): data rental car
    """
    while True:
        print("\nedit car in rent menu")
        print("1.edit field car")
        print("2.back to main menu")
        isubmenu=input("\nchoose sub menu for edit data [1-2]: ")
        if isubmenu=="1": #edit mobil berdasarkan plat nomor
            license_plate=input("Input plat nomor : ").upper()
            show_cars_detail(data_rent, license_plate)
            change_continue=confirmation(data_rent, "update",license_plate)
            if change_continue==True: #edit data
                colum_change=input("\nplease enter column  you want to change (license plate, car brand, car type, year, price, available): ")
                change_data(data_rent,license_plate, colum_change, "license plate")
                change_data(data_rent,license_plate, colum_change, "car brand")
                change_data(data_rent,license_plate, colum_change, "car type")
                change_data(data_rent,license_plate, colum_change, "year")
                change_data(data_rent,license_plate, colum_change, "price")
                change_data(data_rent,license_plate, colum_change, "available")
            else: #else konfirmasi
                print("\nyour car has not been changed")
        elif isubmenu=="2":
            admin_menu(data_rent,"admin")
        else:
            print("Invalid choice. Please choose again.")
            edit_car(data_rent)


def delete_car(data:dict):
    """delete your car in data rental car by primary key

    Args:
        data (dict): data rental car
    """
    while True:
        print("\ndelete your car in rent menu")
        print("1. delete data car")
        print("2. back to main menu")
        isubmenu=input("\nchoose sub menu for edit data [1-2]: ")
        if isubmenu=="1": #hapus mobil
            license_plate=input("Input license plate : ").upper()
            show_cars_detail(data_rent,license_plate) #menampilkan mobil yang mau dihapus
            delete_data=confirmation (data_rent,"Delete",license_plate) #konfirmasi
            if delete_data==True: #penghapusan data
                data["car brand"].remove(data["car brand"][data["license plate"].index(license_plate)])
                data["car type"].remove(data["car type"][data["license plate"].index(license_plate)])
                data["year"].remove(data["year"][data["license plate"].index(license_plate)])
                data["price"].remove(data["price"][data["license plate"].index(license_plate)])
                data["available"].remove(data["available"][data["license plate"].index(license_plate)])
                data["license plate"].remove(license_plate)
                print("\nyour car has been deleted")
            else: #else konfirmasi
                print("\nyour car has not been deleted")

        elif isubmenu=="2":
            admin_menu(data_rent,"admin")
        else:
            print("Invalid choice. Please choose again.")
            delete_car(data_rent)

def order_car(data:dict):
    """function order car for customer

    Args:
        data (dict): data_rent car
    """
    while True:
        print("\norder car sub menu")
        print("1. order car")
        print("2. back to main menu")
        isubmenu=input("\nchoose sub menu for edit data [1-2]: ")
        if isubmenu=="1": #order mobil
            show_cars(data_rent) #menampilkan semua mobil
            license_plate=input("Input license plate : ").upper()
            validasi= confirmation(data_rent, "order",license_plate) #konfirmasi mobil
            if validasi==True and data_rent["available"][data_rent["license plate"].index(license_plate)]==True:
                data_rent["available"][data_rent["license plate"].index(license_plate)]=False
                name_customer=input("your name: ")
                phone_customer=input("your phone number: ")
                date_start=input("time start rental (dd-mm-yy): ")
                date_end=input("time end rental (dd-mm-yy): ")
                confirmation_customer_rent["license plate"].append(license_plate)
                confirmation_customer_rent["customer name"].append(name_customer)
                confirmation_customer_rent["number telphone"].append(phone_customer)
                confirmation_customer_rent["rent date"].append(date_start)
                confirmation_customer_rent["return date"].append(date_end)
                print("your car has been rented, please confirmation to admin for payment")
            else: #else konfirmasi
                print("your car has not been rented")
        elif isubmenu=="2":
            customer_menu(data_rent,"customer")
        else:
            print("Invalid choice. Please choose again.")
            order_car(data_rent)

def view_customer():
    """for admin view  customer data and confirmation about a  car rental"""

    while True:
        print("\nview customer sub menu")
        print("1.view all customer")
        print("2.rent confirmation for customer")
        print("3.back to main menu")
        isubmenu=input("\nchoose sub menu for edit data [1-3]: ")
        if isubmenu=="1": #liat semua customer yang minjam mobil
            show_all_customer(customer_rent)
        elif isubmenu=="2": #konfirmasi customer berdasrkan  license plate
            show_all_customer(confirmation_customer_rent)
            license_plate=input("\nInput license plate : ").upper()
            confirm=confirmation (confirmation_customer_rent,"accept the rent",license_plate) #konfimasi
            if confirm==True: #penghapusan data
                data=confirmation_customer_rent
                customer_rent["license plate"].append(data["license plate"][data["license plate"].index(license_plate)])
                customer_rent["customer name"].append(data["customer name"][data["license plate"].index(license_plate)])
                customer_rent["number telphone"].append(data["number telphone"][data["license plate"].index(license_plate)])
                customer_rent["rent date"].append(data["rent date"][data["license plate"].index(license_plate)])
                customer_rent["return date"].append(data["return date"][data["license plate"].index(license_plate)])
                data["customer name"].remove(data["customer name"][data["license plate"].index(license_plate)])
                data["number telphone"].remove(data["number telphone"][data["license plate"].index(license_plate)])
                data["rent date"].remove(data["rent date"][data["license plate"].index(license_plate)])
                data["return date"].remove(data["return date"][data["license plate"].index(license_plate)])
                data["license plate"].remove(license_plate)
                print("rent confirmation has been accepted")
            else:
                print("rent confirmation has been cancelled")
        elif isubmenu=="3":
            customer_menu(data_rent,"customer")
        else:
            print("Invalid choice. Please choose again.")
            view_customer(data_rent)
        


#=================================================================================================#
####################################### menu #####################################################
#=================================================================================================#

def admin_menu(data_rent:dict,objects:str):
    """Function for menu admin to acces 

    Args:
        data_rent (dict): data rental car
        objects (str): admin or customers for submenu
    """
    print("\nMenu for rental car")
    print("1.view data in rental car")
    print("2.add a new car for rental car")
    print("3.edit field car in rental car")
    print("4.delete car broken in rental car")
    print("5.customer")
    print("6.back to login")
    print("7.exit")
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
        view_customer()
    elif input_user=="6":
        main_menu()
    elif input_user=="7":
        print("thanks for using our service")
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
    print("3.login again")
    print("4.exit")
    input_user = input("choose menu (input number)? ")
    if input_user == "1":
        report_car(data_rent,objects)
    elif input_user == "2":
        order_car(data_rent)
    elif input_user == "3":
        main_menu()
    elif input_user == "4":
        print("thank you for using this program")
        exit()
    else:
        print("Input is not valid !")
        customer_menu(data_rent,objects)                  

# /===== Main Program =====/
# Create your main program here
def main_menu():
    print("\n===== WELCOME TO RENTAL CAR =====")
    objects=input("Please select admin or customer? ")
    if objects.lower()=="admin":
        wrong=2
        while wrong>=0:
            print("\n=========please login your account=========")
            username=input("username: ")
            password=input("password: ")
            if admin_security(data_admin,username,password) == True:
                print("you succesfully login your account")
                admin_menu(data_rent,objects)
            else:
                print(f"username or password is not valid !, Only {wrong} more attempts left")
                wrong-=1
    elif objects.lower()=="customer":
        customer_menu(data_rent,objects)
    else:
        print("Input is not valid !")
        main_menu()

main_menu()
