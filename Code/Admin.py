from Doctor import Doctor

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        if self.__username == username and self.__password == password:
            return True

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input('\nEnter the first name of the doctor: ')
        surname = input('\nEnter the surname of the doctor: ')
        speciality = input('\nEnter the speciality of the doctor: ')
        return first_name, surname, speciality
    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('\nChoose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input('\nInput: ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('\nEnter the doctor\'s details:')
            #ToDo4
            first_name, surname, speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('\nName already exists.')
                    name_exists = True
                    #ToDo5
                    break
            

            #ToDo6
            if not name_exists:
                new_doctor = Doctor(first_name, surname, speciality)
                doctors.append(new_doctor)
                # add the doctor ...
                                                         # ... to the list of doctors
            print('\nDoctor registered.')
            self.view(doctors)

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("\nDoctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')
                except Exception:
                    print('\nInvalid Syntax')

            # menu
            print('\nChoose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')

            #ToDo8
            try:
                op = int(input('\nInput: ')) # make the user input lowercase
                if op == 1:
                    new_first_name = input('Enter the new first name: ')
                    doctors[index].set_first_name(new_first_name)
                    print('\nFirst name upadated')
                elif op == 2:
                    new_surname = input('Enter the new surname: ')
                    doctors[index].set_surname(new_surname)
                    print('\nSurname upadated')
                
                elif op == 3:
                    new_speciality = input('Enter the new speciality: ')
                    doctors[index].set_speciality(new_speciality)
                    print('\nSpeciality upadated')
                else: 
                    print('\nPlease chose from option (1, 2, 3)')
                self.view(doctors)
                
            except ValueError:
                print('\nInvalid Option! Please select a numeric value')
            except Exception:
                print('\nInvalid Syntax')
        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            #ToDo9
            try:
                remove_id = int(doctor_index) - 1
                doctors.pop(remove_id)
                print('\nDoctor Deleted')
                self.view(doctors)
            except IndentationError:
                print('\nThe id entered was not found')
            except Exception as e:
                # e = 'The id entered is incorrect'
                print('\nInvalid Syantax')

        # if the id is not in the list of patients
        else:
            print('\nInvalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('\nPlease enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) - 1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('\nThe id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('\nThe id entered is incorrect')
            return # stop the procedures
        except Exception:
            print('\nInvalid Syantax')

        print("-----Doctors Select-----")
        print('\nSelect the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        try:
            doctor_index = int(input('\nPlease enter the doctor ID: ')) 
            # doctor_index is the patient ID mines one (-1)
            doctor_index = doctor_index -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                doctors[doctor_index].add_patient(patients[patient_index])
                patients[patient_index].link(doctors[doctor_index].full_name())                
                print('\nThe patient is now assign to the doctor.')
                print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
                self.view(patients)

            # if the id is not in the list of doctors
            else:
                print('\nThe id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')
        except Exception:
            print('\nInvalid Syntax')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")


        #ToDo12
        try:
            patient_index = int(input('Please enter the patient ID: '))
            patient_index = patient_index - 1

            if patient_index in range(len(patients)):
                discharged_patient = patients.pop(patient_index)
                discharge_patients.append(discharged_patient)
                print('\nPatient discharged.')

            else:
                print('\nThe id entered was not found.')

        except ValueError:
            print('\nThe id entered is incorrect')
        except Exception:
            print('\nInvalid Syntax')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        self.view(discharged_patients)
    
    # def management_report(self, patients, doctors):
    #     print(f'Total number of doctor: {len(doctors)}')


    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')

        try:
            op = int(input('Input: '))

            if op == 1:
                new_username = input('Enter the new username: ')
                self.__username = new_username
                print('Username Updated')

            elif op == 2:
                password = input('Enter the new password: ')
                # validate the password
                if password == input('Enter the new password again: '):
                    self.__password = password
                    print('Password Updated')

            elif op == 3:
                new_address = input('Enter the new address: ')
                self.__address = new_address
                print('Address Updated')
            else:
                print('Please choose the correct option!')


        except ValueError:
            print('Enter a numeric value only.')
        except Exception:
            print('Invalid Syntax')

    def patinets_surname(self, patients):
        surnames = {}

        for i in patients:
            last_name = i.get_surname()
            if last_name in surnames:
                surnames[last_name].append(i.full_name())
            else:
                surnames[last_name] = [i.full_name()] 

        for i, j in surnames.items():
            print(f"{i}: {', '.join(j)}")
        
    def total_number_of_doc(self, doctors):
        return f'\nThe total number of doctor is {len(doctors)}'
    




        



