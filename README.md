# Python CRUD Application for Rental Car

A comprehensive Python application for managing rental car data with Create, Read, Update, Delete, order, and check customer (CRUD) operations with 2 POV, customer and admin.

## Business Understanding

This project caters to the Business Domain industry, specifically addressing the need to manage rental car data efficiently. rental car plays a crucial role in enabling them to operate efficiently, enhance customer experiences, optimize fleet management, and drive profitability.

**Benefits:**

* Improved data accuracy and consistency
* Streamlined data management processes
* Enhanced decision-making through readily available data
* Operate efficiently to optimization in logistic

**Target Users:**

This application is designed for admin and customer who want rent a car to facilitate their related to rental car.

## Features

### ADMIN
* **Create:**
    * Add new rental car data entries with essential details like license plate, car brand, car type, year, price, available.
    * Implement validation rules to ensure license plate not same in rental car data.
* **Read:**
    * Search and retrieve specific rental car records by applying filters based on license plate.
    * Display comprehensive information for each rental car in a user-friendly format.
* **Update:**
    * Modify existing rental car data to reflect changes in license plate, car brand, car type, year, price, available.
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete:**
    * Allow for the removal of unwanted rental car records with appropriate authorization checks.
* **Customer:**
    * check all customer who rent a car
    * can submit customer who want rent a car.
* **Security:**
    * Implement user authentication and authorization mechanisms (if sensitive data is involved) to control access to different CRUD operations.
    * The security used is to enter a username and password for the admin, and for customers do not need to enter username and password.
      
### CUSTOMER
* **Read:**
    * Search and retrieve specific rental car records by applying filters based on license plate.
    * Display comprehensive information for each rental car in a user-friendly format.
  * **order:**
    * booking a car and waiting acc by admin
  

## Installation

1. **Prerequisites:**
    * Python version 3.12.5.

2. **Installation:**
    ```bash
    git clone https://github.com/<your-username>/<your-repo-name>.git
    cd <your-repo-name>
    pip install -r requirements.txt  # If using a requirements.txt file
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new rental car record, for example, a new car in a rental car management system, providing details like license plate, car brand, car type, year, price, and available.
    * **Read:** Search and retrieve car information by license plate.
    * **Update:** Modify car details, such as updating their license plate until available car .
    * **Delete:** Remove a car record from the system with license plate.
    * **Order:** booking a car with license plate and waiting acc by admin.

## Data Model
This project utilizes a dictionary in python code to represent rental car data. The following fields are typically stored:
   * license plate: str - primary key in data rental car and to describe license plate from car
   * car brand : str - Description brand for car.
   * car type :str- description type for car, automatic or manual.
   * year :int- description year for car.
   * price : int- price rent a car for one day.
   * available : bool- car is available or no for rental car.

and customer data, the following dields are typically stored:
   * license plate: str - primary key in data rental car and to describe license plate from car
   * customer name : str - name customer who rent a car.
   * number telphone :str - number telphone for communication with customer.
   * rent date :str - start date of rental.
   * return date : str- end date of rental.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to ghaisanrabbani5@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.

