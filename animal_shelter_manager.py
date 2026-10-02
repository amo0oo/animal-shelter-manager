def display_menu():
    print("========== ANIMAL SHELTER MANAGER ==========")
    print("1. Intake Animal")
    print("2. Feeding Calculator")
    print("3. Medication Schedule")
    print("4. Adoption Fee Calculator")
    print("5. Daily Shelter Summary")
    print("6. Exit\n")

def intake_animal():
    name = input("Animal name: ").lower()
    while name == '':
        print("Name cannot be blank.")
        name = input("Animal name: ").lower()

    typeof = input("Animal type (dog/cat): ").lower()
    while typeof != "dog" and typeof != "cat":
        print("Invalid animal type.")
        typeof = input("Animal type (dog/cat): ").lower()

    age = int(input("Age: "))
    while age < 0 or age > 30:
        input("Age must be between 0 and 30")
        age = int(input("Age: "))

    weight = float(input("Weight: "))
    while weight <= 0:
        input("Invalid weight.")
        weight = float(input("Weight: "))

    print("===== INTAKE SUMMARY =====")
    print(f"Name: {name}")
    print(f"Type: {typeof}")
    print(f"Age: {age}")
    print(f"Weight: {weight:.2f} lbs\n")
    print("1. Confirm")
    print("2. Start Over")
    print("3. Cancel\n")

    intake_choice = int(input("Enter choice: "))
    while intake_choice < 1 or intake_choice > 3:
        print("Invalid selection")
        intake_choice = int(input("Enter choice: "))

    if intake_choice == 1:
        with open("animal.txt", "a") as file:
            file.write(f"{name}, {typeof}, {age}, {weight}\n")
            return
    elif intake_choice == 2:
        intake_animal()
        return
    elif intake_choice == 3:
        return
    
def feeding_calculator():
    name = input("Enter animal's name: ").lower()

    with open("animal.txt", "r") as file:
        animals = file.readlines()

    found = False

    for animal in animals:
        parts = animal.split(",")

        if name == parts[0].strip():
            found = True

            weight = float(parts[3].strip())
            if weight <= 10:
                food = 1
            elif weight <= 25:
                food = 1.5
            elif weight <= 50:
                food = 2
            elif weight <= 100:
                food = 3
            else:
                food = 4

            feeding = int(input("Feedings per day (1-4): "))
            while feeding < 1 or feeding > 4:
                print("Invalid")
                feeding = int(input("Feedings per day (1-4): "))

            food_per_feeding = food / feeding

            print("===== FEEDING =====")
            print(f"Animal: {animal}")
            print(f"Weight: {weight:.2f} lbs")
            print(f"Food per day: {food} cups")
            print(f"Feedings per day: {feeding}")
            print(f"Food per feeding: {food_per_feeding:.2f} cup\n")

    if found == False:
        print("Animal not found.\n")

def medication_schedule():
    name = input("Enter animal's name (0 to cancel): ").lower()
    if name == '0':
        return

    with open("animal.txt", "r") as file:
            animals = file.readlines()
        
    found = False
        
    for animal in animals:
        parts = animal.split(",")

        if name == parts[0].strip():
           found = True

        med = input("Medication name: ").lower()
        times = int(input("Times per day (1-4): "))
        while times < 1 or times > 4:
            print("Invalid")
            times = int(input("Times per day (1-4): "))

        days = int(input("Number of days(1-30): "))   
        while days < 1 or days > 30:
            print("Invalid")
            days = int(input("Number of days(1-30): ")) 

        total_doses = times * days

        if times == 1:
            schedule = "Morning"
        elif times == 2:
            schedule = "Morning / Evening"
        elif times == 3:
            schedule = "Morning / Afternoon / Evening"
        elif times == 4:
            schedule = "Morning / Afternoon / Evening/ Bedtime"

        print("===== MEDICATION SCHEDULE =====")
        print(f"Animal: {name}")
        print(f"Medication: {med}")
        print(f"Days: {days}")
        print(f"Times per day: {times}")
        print(f"Total doses: {total_doses}")
        print(f"Schedule: {schedule}\n")

        return
                
    if found == False:
        print("Animal not found.\n")       

def calculate_adoption_fee():
    name = input("Enter animal's name: ").lower()

    with open("animal.txt", "r") as file:
        animals = file.readlines()

    found = False

    for animal in animals:
        parts = animal.split(",")

        if name == parts[0].strip():
            found = True
            typeof = parts[1].strip()
            age = int(parts[2].strip())

            if typeof == 'dog':
                fee = 150
            elif typeof == 'cat':
                fee = 100

            if age < 1:
                fee += 50
            elif age >= 7:
                fee -= 50

            print("===== ADOPTION FEE =====")
            print(f"Animal: {name}")
            print(f"Type: {typeof}")
            print(f"Age: {age}")
            print(f"Adoption fee: {fee}\n")

            return

    if found == False:
        print("Animal not found.\n")

def display_summary():
    with open("animal.txt", "r") as file:
        animals = file.readlines()

    total_animals = 0
    dogs = 0 
    cats = 0

    for animal in animals:
        parts = animal.split(",")

        total_animals += 1

        typeof = parts[1].strip()
        if typeof == "dog":
            dogs += 1
        elif typeof == "cat":
            cats += 1

        print("===== DAILY SHELTER SUMMARY =====")
        print(f"Total animals: {total_animals}")
        print(f"Dogs: {dogs}")
        print(f"Cats: {cats}\n")

def main():
    while True:
        display_menu()

        menu_choice = int(input("Enter choice (1-6): "))

        if menu_choice == 1:
            intake_animal()
        elif menu_choice == 2:
            feeding_calculator()
        elif menu_choice == 3:
            medication_schedule()
        elif menu_choice == 4:
            calculate_adoption_fee()
        elif menu_choice == 5:
            display_summary()
        elif menu_choice == 6:
            break
        else:
            print("Invalid selection")

main()