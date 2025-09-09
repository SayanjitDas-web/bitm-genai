# student management system
# - student add
# - student information get
# - student information update
#  -student delete
# - student data filtering
        

class StudentManagementSystem:
    def __init__(self):
        self.storage = []

    def add_student(self):
        name = input("enter student name: ")
        age = input("enter student's age: ")
        roll = input("enter student's roll no. : ")
        stream = input("enter student's stream: ")
        year = int(input("enter student's year: "))
        session = input("enter strudent's session: ")
        gender = input("enter student's gender: ")
        data = {
            "name":name,
            "age": age,
            "roll":roll,
            "stream": stream,
            "year":year,
            "session": session,
            "gender":gender
        }
        self.storage.append(data)

    def update_student_info(self):
        roll = input("enter student's roll no. : ")
        if len(self.storage) != 0:
            for student in self.storage:
                if roll == student["roll"]:
                    choice = input("enter the field name to update: ")
                    match choice:
                        case "name":
                            name = input("enter student name: ")
                            student["name"] = name
                        case "stream":
                            stream = input("enter student's stream: ")
                            student["stream"] = stream

    def get_student_info(self):
        roll = input("enter student's roll no. : ")
        if len(self.storage) != 0:
            for student in self.storage:
                if roll == student["roll"]:
                    for [key, val] in student.items():
                        print(f"{key}-> {val}")

    def filter_student_info(self):
        field = input("enter field name you want to filter: ")
        match field:
            case "stream":
                stream = input("enter the stream name you want to filter out: ")
                if len(self.storage) != 0:
                    for student in self.storage:
                        if student["stream"] == stream:
                            for [key,val] in student.items():
                                print(f"{key}-> {val}")
                        print()
                    print("_____________________")
            case "gender":
                gender = input("enter the gender you want to filter out: ")
                if len(self.storage) != 0:
                    for student in self.storage:
                        if student["gender"] == gender:
                            for [key,val] in student.items():
                                print(f"{key}-> {val}")
                        print()
                    print("_____________________")
sms = StudentManagementSystem()

while(True):
    print('''choose an option:
          to add student -> type add
          to update student -> type update
          to get info of student -> type get
          to filter info of student -> type filter
          to exit the app -> type q
          ''')
    choice = input("enter an option: ")
    match choice:
        case "add":
            sms.add_student()
        case "update":
            sms.update_student_info()
        case "get":
            sms.get_student_info()
        case "filter":
            sms.filter_student_info()
        case "q":
            break