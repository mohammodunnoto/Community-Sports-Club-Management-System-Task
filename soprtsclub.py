class Person:
    def __init__(self, name, age, gender, contact_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact_number

    def set_details(self):
        self.name = input("Please enter the person's name:\n")
        self.age = input("Please enter the person's age:\n")
        self.gender = input("Please enter the person's gender:\n")
        self.contact = input("Please enter the person's contact:\n")
    
    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Contact Number: {self.contact}.")
    
class Member(Person):
    def __init__(self, name, age, gender, contact_number, membership_id, sport):
        super().__init__(name, age, gender, contact_number)
        self.memb_id = membership_id
        self.sport = sport
        self.performance_scores = []
        self.mentors = []
    
    def set_member_details(self):
        self.memb_id = input("Please enter the member's id.")
        self.sport = input("Please enter the member's sport.")

    def add_performance_scores(self):
        while True:
            gradenum = input("How many performance scores of the member will you enter?\n")
            if gradenum.isdigit():
                for i in gradenum:
                    n = 1
                    while n <= int(gradenum):
                        grade = input(f"Please enter the member's score #{n}.\n")
                        if grade.isdigit():
                            self.performance_scores.append(int(grade))
                            n += 1
                break
            else:
                print("Please enter a number.")
    
    def calculate_average_score(self):
        gradenum = len(self.performance_scores)
        totalgrades = sum(self.performance_scores)
        if gradenum == 0:
            average = "Score Not Available"
        else:
            average = totalgrades / gradenum
        print(f"The average score is: {average}.")
        return average
    
    def get_member_summary(self):
        av = Member.calculate_average_score(self)
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Contact Number: {self.contact}, Member ID: {self.memb_id}, Sport: {self.sport}, Average Score: {av}.")

class Coach(Person):
    def __init__(self, name, age, gender, contact_number, coach_id, specialisation, salary):
        super().__init__(name, age, gender, contact_number)
        self.coachid = coach_id
        self.special = specialisation
        self.salary = salary
        self.mentored_members = []

    
    def set_coach_details(self):
        self.staffid = input("Enter the Staff ID:\n")
        self.department = input("Enter the department:\n")
        self.salary = input("Enter the salary:\n")

    def mentor_member(self, Member):
        print(f"Coach {self.name} is now mentoring {Member.name} on {Member.sport}.")
        self.mentored_members.append(Member.name)
        Member.mentors.append(self.name)
    
    def get_mentored_members(self):
        for member in self.mentored_members:
            print(f"Coach {self.name} is mentoring {member}.")

    def increase_salary(self, percentage):
        self.salary = self.salary * (1 + (percentage / 100))
        print(f"The coach's new salary is {self.salary}.")
        return self.salary
    
    def get_coach_summary(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Contact: {self.contact} Coach ID: {self.coachid}, Specialty: {self.special}, Salary: £{self.salary}")
    
class Staff(Person):
    def __init__(self, name, age, gender, contact_number, staff_id, position, years_of_service):
        super().__init__(name, age, gender, contact_number)
        self.staffid = staff_id
        self.position = position
        self.yearsofservice = years_of_service
    
    def set_staff_details(self):
        self.staffid = input("Enter the Staff ID:\n")
        self.position = input("Enter the position:\n")
        self.yearsofservice = input("Enter the Years of Service:\n")
    
    def increment_service_years(self):
        self.yearsofservice += 1
        print(f"The new years of service is: {self.yearsofservice}.")

    def assist(self, Member):
        print(f"Staff {self.name} has assisted {Member.name}.")
    
    def get_staff_summary(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Contact: {self.contact} Staff ID: {self.staffid}, Position: {self.position}, Years of Service: {self.yearsofservice}")

member1 = Member("Bob", 20, "Male", 123456, "M1234", "Basketball")
member2 = Member("James", 20, "Male", 123456, "M2345", "Football")
coach1 = Coach("Mr Hank", 38, "Male", 123456, "C1234", "Basketball", 55000)
coach2 = Coach("Mr Kate", 34, "Female", 123456, "C2345", "Football", 60000)
staff1 = Staff("Mr Tom", 43, "Male", 123456, "S1234", "Head of Ball Sports", 5)
coach1.mentor_member(member1)
member1.add_performance_scores()
member1.calculate_average_score()
staff1.assist(member2)
coach2.increase_salary(15)
staff1.increment_service_years()
member1.get_member_summary()
member2.get_member_summary()
coach1.get_coach_summary()
coach2.get_coach_summary()
staff1.get_staff_summary()