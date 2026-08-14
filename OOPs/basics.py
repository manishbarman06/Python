class Student:
    """ Constructor """
    def __init__(self, name, email, course):
        self.name = name # instance attribute
        self.email = email
        self.course = course

    """ Function to show info """
    def showInfo(self):
        print(f"Name: {self.name:<10}   Email: {self.email:<10}    Course: {self.course:<10}") # (:<15) to give equal space of 15

if __name__=="__main__":
    s1 = Student("Manish", "manish@gmail.com", "BCA")
    s1.showInfo()
    s2 = Student("Krishna", "krishna@gmail.com", "MCA")
    s2.showInfo()
    s3 = Student("Anirudh", "anirudh@gmail.com", "BCA")
    s3.showInfo()
