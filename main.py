import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments)

while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_lists_access.asp
        user_choice = int(input("Enter the apartament's sequence number"))
        print(apartments[user_choice])
        pass
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def sorting(apartment):
            return int(apartment[-1])
        apartments.sort(key = sorting, reverse = True)
        print (apartments[0:10])
        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def sorting2(apartment1):
            return int(apartment1[-1])
        apartments.sort(key = sorting2)
        print (apartments[0:10])
        pass
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        amount = 0
        apartments2 = int(input("What is your maximum price you would like to pay"))
        def sorting3(apartments3):
            return int(apartment3[-1])
        apartments.sort(key = sorting3, reverse = True)
        for element in apartments:
            if int(element[-1])<=apartments2:
                if amount<=20:
                    print(element)
                    amount = amount+1
        pass
    elif choice == '5':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        amount2 = 0
        apartments4 = int(input("What is your maximum price you would like to pay"))
        def sorting4(apartments5):
            return int(apartment5[-1])
        apartments.sort(key = sorting4)
        for element in apartments:
            if int(element[-1])<=apartments4:
                if amount2>=20:
                    print(element)
                    amount2 = amount2+1
        pass

    elif choice == '6':
        # 
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")




