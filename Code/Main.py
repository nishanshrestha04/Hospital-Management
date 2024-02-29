# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def patient_read_patient(filename):
    try:
        patients_data = []
        with open(filename, 'r') as file:
            for line in file:
                patient_info = line.strip().split(',')
                if len(patient_info) == 5:
                    patients_data.append(patient_info)
        return patients_data
    except FileNotFoundError:
        print('File not found.')
    except:
        print('Invalid Syntax')

def main():
    """
    the main function to be ran when the program runs
    """
    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    filename = "Patient.txt"
    patient = patient_read_patient(filename)

    patients = []
    for i in patient:
        patient = Patient(i[0], i[1], i[2], i[3], i[4])
        patients.append(patient)
    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')


    while running:
        # print the menu
        print('\nChoose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- View Grouped patients')
        print(' 7- View total number of doctor')
        print(' 8- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
            admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            admin.view(patients)

            while True:
                op = input('\nDo you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge(patients, discharged_patients)

                elif op == 'no' or op == 'n':
                    print('Thank you.')
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
        elif op == '6':
            admin.patinets_surname(patients)
        elif op == '7':
            print(admin.total_number_of_doc(doctors))

        elif op == '8':
            # 8 - Quit
            #ToDo5
            print('\nThank You for using our system')
            break
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
