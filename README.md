# chicken-project
Local database solution to paper-based storage of chicken information for local chicken breeder.

## Project Purpose
This project was started as a digital solution to the issue a local chicken breeder was facing, trying to keep a record of the information of his chickens. The local breeder was recording the information on paper and found it was impossible to keep track of the constant changes that happen naturally. 

This app uses a simple CLI-based menu system that utilises a CRUD system to manipulate the data of the chickens stored in a local database. The app takes user input to select a menu option, enter information and then saves it to a new or existing record in the database.

## Infrastructure
This project starts with a CSV of raw chicken data, provided by the chicken breeder, and uses that the form the basis of the lcoal database. The db_setup and db_utils files creates a database connection and then sets up the table used to store the information. It grabs the data from the CSV and populates the table with records.

The main_menu file contains the functions that prints the menu to the CLI for the user to view. It then takes user input to choose an option (view, add, update, delete). This will trigger another function which will manipulate the data in the database. The functions are linked to the db_utils functions, which will update the actual database with the given user information and then save it. 