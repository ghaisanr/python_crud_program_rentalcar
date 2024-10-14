def change_data(data,license_plate, colum_change, key_change):
    if colum_change.lower()==key_change:
        new_key=input(f"input new {key_change}: ")
        saved_change= input(f" do you seriously change your car {key_change}? (yes or no) ")
        if saved_change.lower()=="yes":
            data[key_change][data["license plate"].index(license_plate)]=new_key