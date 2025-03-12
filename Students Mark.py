class Student:
    def __init__(self, name, regno, mark1, mark2, mark3):
        self.name = name
        self.regno = regno
        self.marks = [mark1, mark2, mark3]
        self.total_marks = sum(self.marks)
    
    def __repr__(self):
        return f"{self.name} (Reg No: {self.regno}, Total Marks: {self.total_marks})"


def main():
    students = []
    num_students = int(input("Enter the number of students to be created: "))
    
    for _ in range(num_students):
        name = input("Enter student name: ")
        regno = input("Enter student registration number: ")
        mark1 = float(input("Enter mark 1: "))
        mark2 = float(input("Enter mark 2: "))
        mark3 = float(input("Enter mark 3: "))
        
        student = Student(name, regno, mark1, mark2, mark3)
        students.append(student)
    
    students.sort(key=lambda student: student.total_marks, reverse=True)
    
    print("\nStudents ranked by total marks:")
    for rank, student in enumerate(students, start=1):
        print(f"Rank {rank}: {student}")


if __name__ == "__main__":
    main()
