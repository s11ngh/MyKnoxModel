class Major:
    def __init__(self, major, requiredclasses):
        self.major = major
        self.reqiredclasses = requiredclasses

        if type(major) != str:
            raise TypeError("major name must be of String type")
        if type(requiredclasses) is not list[KnoxClass]:
            raise TypeError(
                "requiredclasses must be an instance of the KnoxClass class")

    def __str__(self):
        return 'major='+self.major+' required classes='+(self.requiredclasses)


"""
    def addrequirements(self, KnoxClass):
        if KnoxClass in self.reqiredclasses:
            raise FileExistsError(
                "This class is already a requirement for the major")
            # Sets automatically handle duplication but this error will help prevent multiple attempts
        else:
            self.requiredclasses.add(KnoxClass)

    def requirements(self):
        return self.reqiredclasses

    def classinmajorcheck(self, KnoxClass) -> bool:
        return (KnoxClass in self.reqiredclasses)
"""


class KnoxClass:
    def __init__(self, classname, majordept, period, faculty):
        self.classname = classname
        self.majordept = majordept
        self.period = period
        self.faculty = faculty

        if type(classname) is not str:
            raise TypeError("classname must be of type string")
        if type(majordept) is not Major:
            raise TypeError("majordept must be an instance of class Major")
        if type(period) is int:
            # i think knox has 8 periods (not sure)
            if period > -1 or period < 9:
                raise ValueError("Enter a period in range 0-8 (inclusive)")
        else:
            raise TypeError("period must be of type int")
        if type(faculty) is not list[Professor]:
            raise TypeError("period must be of type list")

    def __str__(self):
        return 'class='+self.classname+' period='+str(self.period) + '\n faculty='+self.faculty + 'majorddept = ' + self.faculty


"""
    def periodchange(self, newperiod):
        if type(newperiod) is int and newperiod < 9 and newperiod > -1:
            self.period = newperiod
        else:
            raise ValueError("Enter a period within 0-8")

    def add_faculty(self, facultyname):
        if type(facultyname) is str:
            self.faculty.append(facultyname)

    def remove_faculty(self, facultyname):
        if type(facultyname) is str:
            self.faculty.remove(facultyname)
"""


class Professor:
    def __init__(self, name, majordept, email, knoxid, classesteaching, advisees):
        self.name = name
        self.majordept = majordept
        self.email = email
        self.knoxid = knoxid
        self.classesteaching = classesteaching
        self.advisees = advisees

        if type(name) is not str:
            raise TypeError("Professor name must be a string")
        if type(majordept) is not Major:
            raise TypeError(
                "Professor's dept/major must be an instance of Major class")
        if type(email) is not str:
            raise TypeError("Professor email must be a string")
        if type(knoxid) is not int:
            raise TypeError("Professor KnoxID must be a int")
        if type(classesteaching) is not list[KnoxClass]:
            raise TypeError(
                "Professor's classes must be a list of KnoxClass instances")
        if type(advisees) is not list[Student]:
            raise TypeError(
                "Professor's advisees list must be a list of Student class instances")

    def __str__(self):
        return 'name='+self.name+' department='+self.majordept + 'knoxid =' + self.knoxid + '\n email = ' + self.email + 'advisees=' + self.advisees


"""
    def addclass(self, classname):

        if type(classname) is not KnoxClass:
            raise TypeError("Class must be an instance of KnoxClass")

        for i in self.classesteaching:
            if i == classname:
                raise FileExistsError(
                    "The professior has already been assigned this class")
        self.classesteaching.append(classname)

    def removeclass(self, classname):

        if type(classname) is not KnoxClass:
            raise TypeError("Class must be an instance of KnoxClass")

        self.classesteaching.remove(classname)

    def addadvisee(self, studentname):  # implement student lookup within this
        if type(studentname) is not str:
            raise TypeError("Class must be of type string")
        for i in self.advisees:
            if i == studentname:
                raise FileExistsError("This advisee has already been assigned")
        self.advisees.append(studentname)

    def removeadvisee(self, studentname):  # implement student lookup within this
        if type(studentname) is not str:
            raise TypeError("Class must be of type string")

        self.advisees.remove(studentname)
"""


class Student:
    def __init__(self, name, majordept, knoxID, email, academicrecord, advisor):
        self.name = name
        self.majordept = 'Undecided'
        self.knoxID = knoxID
        self.email = email
        self.academicrecord = academicrecord
        self.advisor = advisor

        if type(name) is not str:
            raise TypeError("Student name must be a string")
        if type(majordept) is not Major:
            raise TypeError(
                "Professor's dept/major must be an instance of Major class")
        if type(email) is not str:
            raise TypeError("Professor email must be a string")
        if type(knoxID) is not int:
            raise TypeError("Professor KnoxID must be a int")
        if type(academicrecord) is not list[KnoxClass]:
            raise TypeError(
                "Student's classes must be a list of KnoxClass instances")
        if type(advisor) is not Professor:
            raise TypeError(
                "Student's advisees  must be an instance of Professor")

    def __str__(self):
        return 'name='+self.name+' major='+self.majordept + 'knoxID= ' + self.knoxID + '\n classes taken = ' + self.academicrecord
