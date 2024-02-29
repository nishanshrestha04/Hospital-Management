from Person import Person

class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        #ToDo1
        super().__init__(first_name, surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = ['Fever', 'Common Cold']
        self.__doctor = 'None'
       

    
    # def full_name(self) :
    #     """full name is first_name and surname"""
    #     #ToDo2
    #     return f'{self.__first_name} {self.__surname}'
    def get_doctor(self) :
        #ToDo3
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def get_age(self):
        return self.__age

    def get_mobile(self):
        return self.__mobile

    def get_postcode(self):
        return self.__postcode

    def get_symptom(self):
        return self.__symptoms

    def get_symptoms(self):
        return self.__symptoms

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        if len(self.__symptoms) != 0:
            for i, j in enumerate(self.__symptoms):
                print('The patient symptoms are:')
                print(f'{i + 1} {j}')

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'

