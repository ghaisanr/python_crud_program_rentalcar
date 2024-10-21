
def change_data(data:dict,license_plate:str, colum_change:str, key_change:str):
    """function for edit data in rental car

    Args:
        data (dict): data rental car
        license_plate (str): primary key for change only one car
        colum_change (str): variable equals function
        key_change (str): field changes
    """
    if colum_change.lower()==key_change:
        new_key=input(f"input new {key_change}: ")
        saved_change= input(f" do you seriously change your car {key_change} (yes or no) ? ")
        if saved_change.lower()=="yes" and key_change=="license plate":
            data[key_change][data["license plate"].index(license_plate)]=new_key.upper()
            print("your car status has been changed")
        elif saved_change.lower()=="yes" and (key_change=="year" or key_change=="price") :   
            data[key_change][data["license plate"].index(license_plate)]=int(new_key)
            print("your car status has been changed")
        elif saved_change.lower()=="yes" and key_change=="available":
            data[key_change][data["license plate"].index(license_plate)]=bool(int(new_key))
            print("your car status has been changed")
        elif saved_change.lower()=="yes":
            data[key_change][data["license plate"].index(license_plate)]=new_key
            print("your car status has been changed")
        else:
            print("your car status has not been changed")

def confirmation (data:dict,submenu:str,license_plate:str):
    """for confirmation function with license plate

    Args:
        data (dict): data rental car
        submenu (str): what a submenu?
        license_plate (str): primary key

    Returns:
        _type_: _description_
    """
    
    if  license_plate in data["license plate"]:
        confirmation_data=input(f"\nthis is a car, do you want continue to {submenu} (yes or no) ? ")
        if confirmation_data.lower()=="yes":
            return True
        elif confirmation_data.lower()=="no":
            return False
    



        


    
