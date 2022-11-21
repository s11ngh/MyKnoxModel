import myknoxclass
"""
    1. Store list of majors available at Knox (alphabetical)
    2. Store names of professors (alphabetical prefrable)
    3. Store classes offered at Knox College + Link w/ majors they come under
    4. Store student list in directory database
    5. Move functions from myknoxclass to here
"""


majors = dict()  # <Name of Major(Str), MajorReqList[KnoxClass]>
studentdir = dict()
profdir = dict()
class_list = []


class KnoxDatabase:

    # Student Methods
    def newmajor(newmajor):
        if type(newmajor) is not myknoxclass.Major:
            raise TypeError("Arguement must be an instance of class Major")
        majors[newmajor.major] = newmajor.requiredclasses

    def requirements(self, majorname):
        return majors[majorname]

    def classinmajorcheck(self, classname, majorname) -> bool:
        if majorname not in majors:
            raise FileNotFoundError(
                "Major does not exist. Check your spelling or use newmajor()")
        if type(classname) is not myknoxclass.KnoxClass:
            raise TypeError("class name must be an instance of KnoxClass")

        for i in majors[majorname].requiredclasses:
            if i == classname:
                return True
        return False

    # KnoxClass methods
    def periodchange(self, majorname, classname, newperiod):
        if majorname not in majors:
            raise FileNotFoundError(
                "Major does not exist. Check your spelling or use newmajor()")
        if type(newperiod) is not int:
            raise TypeError("period  must be an int")
        for i in majors[majorname].requiredclass:
            if i == classname:
                i.period = newperiod

    def add_faculty(self, majorname, classname, facultyname):
        if majorname not in majors:
            raise FileNotFoundError(
                "Major does not exist. Check your spelling or use newmajor()")
        if type(facultyname) is not myknoxclass.Professor:
            raise TypeError("period  must be an int")
        for i in majors[majorname].requiredclass:
            if i == classname:
                i.faculty.append(facultyname)
                # add a statement to do the same to prof's class list

    def remove_faculty(self, majorname, classname, facultyname):
        if majorname not in majors:
            raise FileNotFoundError(
                "Major does not exist. Check your spelling or use newmajor()")
        if type(facultyname) is not myknoxclass.Professor:
            raise TypeError("period  must be an int")
        for i in majors[majorname].requiredclass:
            if i == classname:
                i.faculty.remove(facultyname)
                # add a statement to do the same to prof's class list

    # Professor methods
    def add_class(self, profname, classname):
        if type(classname) is not myknoxclass.KnoxClass:
            raise TypeError("Class must be an instance of KnoxClass")

        for i in profname.classesteaching:
            if i == classname:
                raise FileExistsError(
                    "The professior has already been assigned this class")
        self.classesteaching.append(classname)

    def removeclass(self, prof, classname):
        if type(prof) is not myknoxclass.Professor:
            raise TypeError("prof must be an instance of professor class")
        if type(classname) is not myknoxclass.KnoxClass:
            raise TypeError("Class must be an instance of KnoxClass")

        prof.classesteaching.remove(classname)

    def add_advisee(self, prof, advisee):
        if type(prof) is not myknoxclass.Professor:
            raise TypeError("Prof must be an instance of professor class")
        if type(advisee) is not myknoxclass.Student:
            raise TypeError("Advisee must be an instance of student class")
        prof.advisees.append(advisee)

    def remove_advisee(self, prof, advisee):
        if type(prof) is not myknoxclass.Professor:
            raise TypeError("Prof must be an instance of professor class")
        if type(advisee) is not myknoxclass.Student:
            raise TypeError("Advisee must be an instance of student class")
        prof.advisees.remove(advisee)

    # Major methods
    def add_major(self, newmaj):
        if type(newmaj) is not myknoxclass.Major:
            raise TypeError("newmaj must be an instance of class Major")
        majors[newmaj.major, newmaj.reqiredclasses]

    def removemajor(self, rmmaj):
        if type(rmmaj) is not myknoxclass.Major:
            raise TypeError("rmmaj must be an instance of class Major")
        del majors[rmmaj.major]
