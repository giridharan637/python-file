patients = []

def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    problem = input("Enter patient's problem: ")
    patient = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Problem": problem
    }
    patients.append(patient)
    print("atient added successfully.\n")

def view_patients():
    if not patients:
        print("No patients yet.\n")
        return
    print("\n--- Patient List ---")
    for i, p in enumerate(patients, 1):
        print(f"{i}. {p['Name']} | Age: {p['Age']} | Gender: {p['Gender']} | Problem: {p['Problem']}")
    print()

def search_patient():
    search_name = input("Enter name to search: ")
    found = False
    for p in patients:
        if p['Name'].lower() == search_name.lower():
            print("\natient Found:")
            print(f"Name: {p['Name']}")
            print(f"Age: {p['Age']}")
            print(f"Gender: {p['Gender']}")
            print(f"Problem: {p['Problem']}\n")
            found = True
            break
    if not found:
        print("atient not found.\n")

while True:
    print("--- Hospital Management System ---")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_patient()
    elif choice == '2':
        view_patients()
    elif choice == '3':
        search_patient()
    elif choice == '4':
        print("Thank you! Exiting...")
        break
    else:
        print("⚠️ Invalid choice. Try again.\n")
