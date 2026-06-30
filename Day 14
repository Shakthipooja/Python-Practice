# Hospital Patient Management System

class Patient:

    def __init__(self, patient_id, name, age, disease, blood_group):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.blood_group = blood_group

    def display(self):
        print("\nPatient Details")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Blood Group:", self.blood_group)


# Patient database
patients = []


# Add patient
def add_patient():

    try:
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")
        blood_group = input("Enter Blood Group: ")

        patient = Patient(
            patient_id,
            name,
            age,
            disease,
            blood_group
        )

        patients.append(patient)

        print("Patient Added Successfully!")

    except ValueError:
        print("Invalid age entered.")


# Display patients
def display_patients():

    if len(patients) == 0:
        print("No patients available.")
        return

    print("\n----- ALL PATIENTS -----")

    for patient in patients:
        patient.display()


# Search patient
def search_patient():

    search_id = input(
        "Enter Patient ID to search: "
    )

    found = False

    for patient in patients:

        if patient.patient_id == search_id:

            print("\nPatient Found")
            patient.display()

            found = True
            break

    if not found:
        print("Patient Not Found")


# Delete patient
def delete_patient():

    delete_id = input(
        "Enter Patient ID to delete: "
    )

    found = False

    for patient in patients:

        if patient.patient_id == delete_id:

            patients.remove(patient)

            print(
                "Patient Deleted Successfully"
            )

            found = True
            break

    if not found:
        print("Patient Not Found")


# Save to file
def save_to_file():

    try:

        with open(
            "patients.txt",
            "w"
        ) as file:

            for patient in patients:

                file.write(
                    f"{patient.patient_id},"
                    f"{patient.name},"
                    f"{patient.age},"
                    f"{patient.disease},"
                    f"{patient.blood_group}\n"
                )

        print(
            "Patient data saved successfully."
        )

    except Exception as e:
        print("Error:", e)


# Main Menu
while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")

    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Save to File")
    print("6. Exit")

    try:

        choice = int(
            input("Enter your choice: ")
        )

        if choice == 1:
            add_patient()

        elif choice == 2:
            display_patients()

        elif choice == 3:
            search_patient()

        elif choice == 4:
            delete_patient()

        elif choice == 5:
            save_to_file()

        elif choice == 6:
            print(
                "Program Closed"
            )
            break

        else:
            print(
                "Invalid Choice"
            )

    except ValueError:
        print(
            "Please enter a valid number."
        )
