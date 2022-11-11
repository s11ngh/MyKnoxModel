class Major:
    def __init__(self, major, requiredclasses):
        self.major = major
        self.reqiredclasses = requiredclasses

        if type(major) != str:
            raise TypeError("major name must be of String type")
        if type(requiredclasses) is not set:
            raise TypeError(
                "requiredclasses must be an instance of the set class")

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


class KnoxClass:
    def __init__(self, classname, majordept, period, faculty) -> None:
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
        if type(faculty) is not list:
            raise TypeError("period must be of type list")

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
