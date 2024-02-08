class Students():
    '''
    ID = Mã sinh viên
    NAME = Tên sinh viên
    SEX = Giới tính
    BIRTHDAY = Ngày sinh
    ADDRESS = Địa chỉ
    SPECIALIZE = Chuyên ngành
    CLASSS = Lớp
    '''
    def __init__(self, id, name, sex , birthday, address, specialize, classs):
        self.id = id
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.address = address
        self.specialize = specialize
        self.classs = classs
        self.students_list = {
        self.id: {'NAME': self.name, 'SEX': self.sex, 'BIRTHDAY': self.birthday, 'ADDRESS': self.address, 'SPECIALIZE': self.specialize, 'CLASSS': self.classs}
        }



class Students_Manager():
    def __init__(self):
        pass

    students_list = {
    1: {'NAME': 'NAME1', 'SEX': 'nu', 'BIRTHDAY': '1', 'ADDRESS': 'address', 'SPECIALIZE': 'specialize', 'CLASSS': 'classs'},
    2: {'NAME': 'NAME4', 'SEX': 'nam', 'BIRTHDAY': '2', 'ADDRESS': 'address', 'SPECIALIZE': 'specialize', 'CLASSS': 'classs'},
    3: {'NAME': 'NAME3', 'SEX': 'nu', 'BIRTHDAY': '3', 'ADDRESS': 'address', 'SPECIALIZE': 'specialize', 'CLASSS': 'classs'},
    4: {'NAME': 'NAME2', 'SEX': 'sex', 'BIRTHDAY': '4', 'ADDRESS': 'address', 'SPECIALIZE': 'specialize', 'CLASSS': 'classs'}
    }

    # Đếm số lượng students in code
    def count_students(self):
        return self.students_list.__len__()

    # Get ID in code
    def get_ID(self):
        MAX_ID = 1   
        if self.count_students() > 0:
            # MAX_ID = self.students_list.keys()
            for student in self.students_list.keys():
                if student > MAX_ID:
                    MAX_ID = student
            MAX_ID = MAX_ID + 1
        return MAX_ID

    # Display list
    def show_all_students(self):
        # all_students_list = {}
        for student in self.students_list:
            print(student, ':', self.students_list[student])

    # Find student ID
    def find_student_ID(self, keyword):
        searchResult = None
        if self.count_students() > 0:
            for id in self.students_list:
                if id == keyword:
                    searchResult = {id: self.students_list[id]}
        return searchResult
    
    # Find student NAME
    def find_student_NAME(self, keyword):
        list_name_students = {}
        if self.count_students() > 0:
            for id in self.students_list:
                if self.students_list[id]['NAME'].upper() == keyword.upper():
                    list_name_students.update({id: self.students_list[id]})
        return list_name_students
    
    # Add student
    def add_student(self):
        id = self.get_ID()
        name = input('Enter new student\'s NAME: ')
        sex = input('Enter new student\'s SEX: ')
        birthday = input('Enter new student\'s BIRTHDAY: ')
        address = input('Enter new student\'s ADDRESS: ')
        specialize = input('Enter new student\'s SPECIALIZE: ')
        classs = input('Enter new student\'s CLASS: ')
        new_student = Students(id, name, sex, birthday, address, specialize, classs)
        self.students_list.update({id: {'NAME': name.upper(), 'SEX': sex.upper(), 'BIRTHDAY': birthday, 'ADDRESS': address, 'SPECIALIZE': specialize.upper(), 'CLASSS': classs.upper()}})
        print('Student\n{} : {}\nhas been added to the list'.format(id ,self.students_list[id]))
        print('Your new students list:')
        self.show_all_students()

    # Update student
    def update_student(self, keyword):
        if type(keyword) == str:
            self.find_student_NAME(keyword)
            if self.find_student_NAME(keyword) != {}:
                for id in self.find_student_NAME(keyword):
                    print(id, ':', self.find_student_NAME(keyword)[id])
                keyword_id = int(input('Select the ID you want to Update: '))
                if keyword_id in self.find_student_NAME(keyword):
                    name = input('Enter student\'s NAME: ')
                    if name == '':
                        name = self.students_list[keyword_id]['NAME']
                    sex = input('Enter student\'s SEX: ')
                    if sex == '':
                        sex = self.students_list[keyword_id]['SEX']
                    birthday = input('Enter student\'s BIRTHDAY: ')
                    if birthday == '':
                        birthday = self.students_list[keyword_id]['BIRTHDAY']
                    address = input('Enter student\'s ADDRESS: ')
                    if address == '':
                        address = self.students_list[keyword_id]['ADDRESS']
                    specialize = input('Enter student\'s SPECIALIZE: ')
                    if specialize == '':
                        specialize = self.students_list[keyword_id]['SPECIALIZE']
                    classs = input('Enter student\'s CLASS: ')
                    if classs == '':
                        classs = self.students_list[keyword_id]['CLASS']
                    self.students_list.update({keyword_id: {'NAME': name.upper(), 'SEX': sex.upper(), 'BIRTHDAY': birthday, 'ADDRESS': address, 'SPECIALIZE': specialize.upper(), 'CLASSS': classs.upper()}})
                    print('{0} : {1} \nhas been updated to the list'.format(keyword_id, self.students_list[keyword_id]))
                else:
                    print('{} doesn\'t exists'.format(keyword_id))
            else:
                print('{} doesn\'t exists'.format(keyword))
        elif type(keyword) == int:
            self.find_student_ID(keyword)
            if self.find_student_ID(keyword) != None:
                name = input('Enter student\'s NAME: ')
                if name == '':
                    name = self.students_list[keyword]['NAME']
                sex = input('Enter student\'s SEX: ')
                if sex == '':
                    sex = self.students_list[keyword]['SEX']
                birthday = input('Enter student\'s BIRTHDAY: ')
                if birthday == '':
                    birthday = self.students_list[keyword]['BIRTHDAY']
                address = input('Enter student\'s ADDRESS: ')
                if address == '':
                    address = self.students_list[keyword]['ADDRESS']
                specialize = input('Enter student\'s SPECIALIZE: ')
                if specialize == '':
                    specialize = self.students_list[keyword]['SPECIALIZE']
                classs = input('Enter student\'s CLASS: ')
                if classs == '':
                    classs = self.students_list[keyword]['CLASS']
                self.students_list.update({keyword: {'NAME': name.upper(), 'SEX': sex.upper(), 'BIRTHDAY': birthday, 'ADDRESS': address, 'SPECIALIZE': specialize.upper(), 'CLASSS': classs.upper()}})
                print('{0} : {1} \nhas been updated to the list'.format(keyword, self.students_list[keyword]))
            else:
                print('{} doesn\'t exists'.format(keyword))

    # Sort students ID
    def sort_students_ID(self):
        temporary = sorted(self.students_list.items())
        new_students_list = dict(temporary)
        print('List after sorting')
        for id in new_students_list:
            print(id, ':', new_students_list[id])

    # Sort students NAME
    def sort_students_NAME(self):
        temporary = sorted(self.students_list.items())
        for i in range(0, len(temporary) - 1):
            for j in range(i + 1, len(temporary)):
                if temporary[i][1]['NAME'] > temporary[j][1]['NAME']:
                    tmp =  temporary[i]
                    temporary[i] = temporary[j]
                    temporary[j] = tmp
        new_students_list = dict(temporary)
        print('List after sorting')
        for id in new_students_list:
            print(id, ':', new_students_list[id])




    



all_students_list = {
1: {'NAME': 'self.name1', 'SEX': 'self.sex', 'BIRTHDAY': 'self.birthday', 'ADDRESS': 'self.address', 'SPECIALIZE': 'self.specialize', 'CLASSS': 'self.classs'},
2: {'NAME': 'self.name2', 'SEX': 'self.sex', 'BIRTHDAY': 'self.birthday', 'ADDRESS': 'self.address', 'SPECIALIZE': 'self.specialize', 'CLASSS': 'self.classs'},
3: {'NAME': 'self.name3', 'SEX': 'self.sex', 'BIRTHDAY': 'self.birthday', 'ADDRESS': 'self.address', 'SPECIALIZE': 'self.specialize', 'CLASSS': 'self.classs'},
4: {'NAME': 'self.name4', 'SEX': 'self.sex', 'BIRTHDAY': 'self.birthday', 'ADDRESS': 'self.address', 'SPECIALIZE': 'self.specialize', 'CLASSS': 'self.classs'}
                    }


# # Test code -- Chạy ok
# a = Students_Manager()

# a.show_all_students()
# a.find_student_ID(2)
# a.find_student_NAME('name3')
# a.add_student()
# a.update_student('name1')
# a.sort_students_ID()
# a.sort_students_NAME()

while True:
    manager = Students_Manager()
    ask = input('Choose the option you want.\n\
                    Show all students = 1\n\
                    Find student = 2\n\
                    Add student = 3\n\
                    Update student = 4\n\
                    Sort students = 5\n\
                    Exit = 0\n\
                    ')
    if ask == '1' or ask == 'Show list' or ask == 'show list' or ask == 'Show' or ask == 'show' or ask == 'S'  or ask == 's':
        manager.show_all_students()
        
    elif ask == '2' or ask == 'Find student' or ask == 'find student' or ask == 'Find' or ask == 'find' or ask == 'F'  or ask == 'f':
        ask = input('Do you want to find Student ID or Student NAME?\n\
                    Student ID = 1\n\
                    Student NAME = 2\n\
                    ')
        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
            id = int(input('Enter Student ID: '))
            print(manager.find_student_ID(id))
        elif ask == '2' or ask == 'No' or ask == 'no' or ask == 'N'  or ask == 'n':
            name = input('Enter Student NAME: ')
            print(manager.find_student_NAME(name))
        else:
            print("Invalid input")
    elif ask == '3' or ask == 'Add student' or ask == 'add student' or ask == 'Add' or ask == 'add' or ask == 'A'  or ask == 'a':
        manager.add_student()
    elif ask == '4' or ask == 'Update student' or ask == 'update student' or ask == 'Update' or ask == 'update' or ask == 'U'  or ask == 'u':
        ask = input('Do you want to update Student ID or Student NAME?\n\
                    Student ID = 1\n\
                    Student NAME = 2\n\
                    ')
        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
            id = int(input('Enter Student ID: '))
            manager.update_student(id)
        elif ask == '2' or ask == 'No' or ask == 'no' or ask == 'N'  or ask == 'n':
            name = input('Enter Student NAME: ')
            manager.update_student(name)
        else:
            print("Invalid input")
    elif ask == '5' or ask == 'Sort student' or ask == 'sort student' or ask == 'Sort' or ask == 'sort' or ask == 'S'  or ask == 's':
        ask = input('Do you want to sort Student ID or Student NAME?\n\
                    Student ID = 1\n\
                    Student NAME = 2\n\
                    ')
        if ask == '1' or ask == 'Yes' or ask == 'yes' or ask == 'Y'  or ask == 'y' or ask == '':
            manager.sort_students_ID()
        elif ask == '2' or ask == 'No' or ask == 'no' or ask == 'N'  or ask == 'n':
            manager.sort_students_NAME()
        else:
            print("Invalid input")
    else:
        print('Thank you!\nSee you again!')
        break