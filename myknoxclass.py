
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


a = Major("Computer Sci", {1})
