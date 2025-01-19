from math import nan
import pandas as pd
import os

def main_menu():
    print("MAIN MENU")
    print("1. Dataset Operation")
    print("2. File Operation")
    print("3. EXIT")


def file_operations():
    print("\nFILE OPERATIONS")
    print("1. Read a file")
    print("2. Write data to a file")
    print("3. Delete a file")
    print("4. Go Back to Main Menu")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        filename = input("Enter the path of the file to read: ")
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                print("\nFile Content:\n")
                print(file.read())
        else:
            print("File does not exist.")
    
    elif choice == '2':
        filename = input("Enter the path to save the file: ")
        data_to_write = input("Enter the data you want to write to the file: ")
        with open(filename, 'w') as file:
            file.write(data_to_write)
        print(f"Data written to {filename} successfully.")
    
    elif choice == '3':
        filename = input("Enter the path of the file to delete: ")
        if os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} has been deleted.")
        else:
            print("File does not exist.")
    
    elif choice == '4':
        print("Going back to main menu...")
        return
    else:
        print("Invalid choice! Returning to main menu...")


def main():
    while (True):
        main_menu()
        choice = input('\nEnter choice(1, 2 or 3): ')
        if choice == '1':
            print("\nThank you for choosing Dataset operation")
            while True:
                rchoice = input('Choice(1-> print Dataset, 2->Print 5 Rows, 3->Exit, 4->Data Types, 5->Last5, 6->DataSet info, 7->DataSet columns, 8->DataSet mean, 9->DataSet missing value, 10->DataSet duplicate): ')
                dataSet = pd.read_csv(r"C:\Users\MAINUL ISLAM\Downloads\Titanic-Dataset.csv", header=0, sep=",")
                print()
                if rchoice == '1':
                    print(dataSet)
                if rchoice == '2':
                    print(dataSet.head())
                if rchoice == '4':
                    print(dataSet.dtypes)
                if rchoice == '5':
                    print(dataSet.tail())
                if rchoice == '6':
                    print(dataSet.info())
                if rchoice == '7':
                    print(dataSet.columns)
                if rchoice == '8':
                    print(dataSet.mean())
                if rchoice == '9':
                    print(dataSet.isnull().sum())
                if rchoice == '10':
                    print(dataSet.duplicated().sum())
                elif rchoice == '3':
                    print('\nExiting Dataset Operations.')
                    break

        elif choice == '2':
            print('\nThank you for choosing File operation.')
            while True:
                file_operations()
                back = input("\nDo you want to return to File Operations? (yes/no): ").lower()
                if back == 'no':
                    break

        elif choice == '3':
            print('\nThanks for using the program!')
            break
        else:
            print('\nInvalid input!!!')


if __name__ == "__main__":
    main()


