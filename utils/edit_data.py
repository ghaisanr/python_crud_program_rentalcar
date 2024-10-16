def change_data(data:dict,license_plate, colum_change, key_change):
    if colum_change.lower()==key_change:
        new_key=input(f"input new {key_change}: ")
        saved_change= input(f" do you seriously change your car {key_change} (yes or no) ? ")
        if saved_change.lower()=="yes" and key_change=="license plate":
            data[key_change][data["license plate"].index(license_plate.upper())]=new_key.upper()
            print("your car status has been changed")
        elif saved_change.lower()=="yes" and (key_change=="year" or key_change=="price") :   
            data[key_change][data["license plate"].index(license_plate.upper())]=int(new_key)
            print("your car status has been changed")
        elif saved_change.lower()=="yes" and key_change=="available":
            data[key_change][data["license plate"].index(license_plate.upper())]=bool(new_key.capitalize())
            print("your car status has been changed")
        elif saved_change.lower()=="yes":
            data[key_change][data["license plate"].index(license_plate.upper())]=new_key
            print("your car status has been changed")
        else:
            print("your car status has not been changed")