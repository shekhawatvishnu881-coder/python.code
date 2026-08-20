class teacher:
    def __init__(self,id,name,subject,salary):
        self.id=id
        self.name=name
        self.subject=subject
        self.salary=salary

    def print_details(self):
        print(f" id :{self.id}")
        print(f" name :{self.name}")
        print(f" subject :{self.subject}")
        print(f" salary :{self.salary}")
#teacher 1 details
id1=int(input(" enter teacher 1 id "))
name1=input("enter name of teacher 1")
subject1=input("enter subject of teacher 1 ")
salary1=int(input(" enter salary of t1"))

#teacher 2 details


id2=int(input(" enter teacher 2 id "))
name2=input("enter name of teacher 2")
subject2=input("enter subject of teacher 2 ")
salary2=int(input(" enter salary of t2"))

#teacher 3 details

id3=int(input(" enter teacher 3 id "))
name3=input("enter name of teacher 3")
subject3=input("enter subject of teacher 3 ")
salary3=int(input(" enter salary of t3"))

t1=teacher(id1,name1,subject1,salary1)
t1.print_details()
t2=teacher(id2,name2,subject2,salary2)
t2.print_details()
t3=teacher(id3,name3,subject3,salary3)
t3.print_details()

if t1.salary>t2.salary and t1.salary>t3.salary:
    print(" max is ",t1)
    t1.print_details()
elif t2.salary>t1.salary and t2.salary>t3.salary:
    print("max is ", t2)
    t2.print_details()
else:
    print("max is ",t3)
    t3.print_details()

average_salary=t1.salary+t2.salary+t3.salary/3
print(f" average salary is {average_salary}")
