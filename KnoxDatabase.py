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


class KnoxDatabase:

    # Student Methods
    def newmajor(newmajor):
        if newmajor is not myknoxclass.Major:
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
    def periodchange(self, majorname, )
