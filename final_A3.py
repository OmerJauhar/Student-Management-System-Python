
def Add_Student(a,b):
    for keys,values in b.items():
        a[keys]=values
    return a 

def Search_Student(a,name):
    for keys,values in a.items():
        if values[0]==name:
            y = True
            break 
        else:
            y = False
    return y 
def Update_Student(a,list):
    for keys,values in a.items():
        if keys == list[0]:
            if list[1] == "First_name":
                values[0]=list[2]
                break
            elif list[1]=="Last_name":
                values[1]=list[2]
                break
            elif list[1]=="is_Registered":
                values[2]=list[2]
                break
            elif list[1]=="CGPA":
                values[3]=list[2]
                break
            elif list[1]=="Semester":
                values[4]=list[2]
                break
            else:
                a[list[0]]=list[1]+list[2]
    return a 
def Delete_student(a,name):
    key_to_be_deleted = name
    result_dict = {}
    for keys,values in a.items():
        if values[0] != name:
            result_dict[keys] =values
    a = result_dict
    return a 
def Get_Students(a):
    CGPA = []
    same_CGPA = []
    semester = []
    same_semester = []
    same_CGPA_semester = []
    a1 = a
    for keys,values in a.items():
        CGPA.append(values[3])
        semester.append(values[4])
    a=CGPA
    b=[a[i] for i in range(len(a)) if a[i] in a[:i]][1:]
    print(b)
    d = semester
    c = [d[i] for i in range(len(d)) if d[i] in d[:i]][1:]
    print(c)
    for keys, values in a1.items():
        for i in b:
            if values[3] == i:
                same_CGPA.append(values[0]+values[1])
        for i in c:
            if values[4] == i:
                same_semester.append(values[0]+values[1])
    print(same_CGPA,same_semester)
    for i in same_CGPA:
        for j in same_semester:
            if i==j:
                same_CGPA_semester.append(j)
    nested_list = [same_CGPA,same_semester,same_CGPA_semester]
    return nested_list
def boolean(n):
    if n==1:
        return "True"
    else:
        return "False"
print("**************Student Survey Program****************\n\n ")
print("Select from the following options: ")
dict = {}
achoice = 1
while (achoice != -1):
    try :
        choice = int(input(" 1: Enter new details \n 2: Add student \n 3: Search student\n 4: Update student \n 5: Delete student \n 6: Get students \n 7: final record \n 8: To save record  "))
    except:
        print("INVALID INPUT TRY AGAIN ")
        choice = int(input(" 1: Enter new details \n 2: Add student \n 3: Search student\n 4: Update student \n 5: Delete student \n 6: Get students \n 7: final record \n 8: To save record  "))
    if choice == 1:
        try :
            record_name1 = input("what do you want to name this record :")
            record_name = record_name1
        except:
            print("INVALID INPUT TRY AGAIN ")
            record_name1 = input("what do you want to name this record :")
            record_name = record_name1
        num = 1 
        while(num != 0):
            try:
                roll_no =input("Enter Roll Number in following format 21P-1234 :")
            except:
                print("INVALID INPUT TRY AGAIN ")
                roll_no =input("Enter Roll Number in following format 21P-1234 :")
            stri = []
            try:
                name1 = input("Enter your first name :")
                stri.append(name1)
            except:
                print("INVALID INPUT TRY AGAIN ")
                name1 = input("Enter your first name :")
                stri.append(name1)
            try:
                name2 = input("Enter your last name :")
                stri.append(name2)
            except:
                print("INVALID INPUT TRY AGAIN ")  
                name2 = input("Enter your last name :")
                stri.append(name2)
            try:
                n = boolean(int(input("Select 1 if admission in the uni is active else 0 ")))
                stri.append(n) 
            except:
                print("INVALID INPUT TRY AGAIN ")
                n = boolean(int(input("Select 1 if admission in the uni is active else 0 ")))
                stri.append(n)
            try:
                gpa = float(input("Enter your CGPA :"))
                stri.append(gpa) 
            except:
                print("INVALID INPUT TRY AGAIN ")
                gpa = float(input("Enter your CGPA :"))
                stri.append(gpa)
            try:
                semester = int(input("Enter your semester eg : 1,2,4 :"))
                stri.append(semester) 
            except:
                print("INVALID INPUT TRY AGAIN ")
                semester = int(input("Enter your semester eg : 1,2,4 :"))
            stri.append(semester) 
            dict[roll_no]=stri
            num = int(input("Press 1 for adding a new entry, press 0 for exit new details "))
    elif choice == 2:
        print("A")
    elif choice == 3:
        try:
            name = input("Enter the name you want to search in the records :")
            print("Result ",Search_Student(dict,name))
        except:
            print("INVALID INPUT TRY AGAIN ")
            name = input("Enter the name you want to search in the records :")
            print("Result ",Search_Student(dict,name))
    elif choice == 4:
        try:
            list4 =[]
            input41 = input("Enter your Roll number in the given format 21P-1234 :")
            list4.append(input41)
            input42 =int(input("Select from the following variables which you wish to update :\n 1:First name \n 2:Last name \n 3:is_regestered \n 4:CGPA \n 5:Semester  "))
            n = input42
            if n==1:
                result42 = "First_name"
            elif n==2:
                result42 = "Last_name"
            elif n==3:
                result42 = "is_Registered"
            elif n==4:
                result42 = "CGPA"
            elif n==5:
                result42 = "Semester"
            list4.append(result42)
            input43 = input("Enter the value you wish to update the variable with :")
            list4.append(input43)
            Update_Student(dict,list4)
        except:
            print("INVALID INPUT TRY AGAIN ")
            list4 =[]
            input41 = input("Enter your Roll number in the given format 21P-1234 :")
            list4.append(input41)
            input42 =int(input("Select from the following variables which you wish to update :\n 1:First name \n 2:Last name \n 3:is_regestered \n 4:CGPA \n 5:Semester  "))
            n = input42
            if n==1:
                result42 = "First_name"
            elif n==2:
                result42 = "Last_name"
            elif n==3:
                result42 = "is_Registered"
            elif n==4:
                result42 = "CGPA"
            elif n==5:
                result42 = "Semester"
            list4.append(result42)
            input43 = input("Enter the value you wish to update the variable with :")
            list4.append(input43)
            Update_Student(dict,list4)
    elif choice ==5:
        try:
            name1 = input("Enter the first name of the student whose record you want to delete: ")
            Delete_student(dict,name1)
        except:
            print("INVALID INPUT TRY AGAIN ")
            name1 = input("Enter the first name of the student whose record you want to delete: ")
            Delete_student(dict,name1)
    elif choice == 6:
        try:
            print("A nested list of students who have same CGPA in 1st list , same semester in 2nd list and same CGPA and same semester in 3rd list ")
            Get_Students(dict)
        except:
            print("INVALID INPUT TRY AGAIN ")
            print("A nested list of students who have same CGPA in 1st list , same semester in 2nd list and same CGPA and same semester in 3rd list ")
            Get_Students(dict)

    elif choice ==7:
        try:
            print("you have Entered the exit menu :\n The final student record is as following ",dict)
        except:
            print("INVALID INPUT TRY AGAIN ")
            print("you have Entered the exit menu :\n The final student record is as following ",dict)
            

    achoice =int(input("Press any key to continue or Enter -1 to exit the program "))
    if achoice==-1:
        record_name = dict
        file1 = open("Student_Database","a")
        output = ("*****************  RECORD NAME :",record_name1,'****************\n')
        file1.writelines(output)
        for keys,values in dict.items():
            print(keys)
            print(values)
        string1 = ":"
        m = "\n"
        for keys,values in dict.items():
            a = ("Roll Number :",keys)
            file1.writelines(a)
            j = values
            j = [str(i) for i in j]
            a =  "First Name: ",j[0]," Last Name: ",j[1]," Admission Status: ",j[2]," CGPA: ",j[3]," Semester: ",j[4]
            a = str(a)
            string1 +=a
            string1 += "  ,  "
            file1.writelines(m)
            file1.writelines(string1)
            file1.writelines(m)
            string1 = ":"
        a = "\n \n \n "
        file1.writelines(a)
        file1.close

        
        print("The record has been successfully saved in Student_Database file with the record  name ",record_name1," .")







    
