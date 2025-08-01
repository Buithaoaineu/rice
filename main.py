class Student :
    def __init__ (self, student_ID, name, birth_date, class_name) :
        self.student_ID = student_ID
        self.name = name
        self.birth_date = birth_date
        self.class_name = class_name
    
    def __str__(self) :
        return f"""
    Student ID : {self.student_ID}
    Student name : {self.name}
    Birth date : {self.birth_date}
    Class_name : {self.class_name}"""

student_1 = Student("11247353", "Bùi Phương Thảo", "08/01/2006", "AI66B")
print(student_1)

