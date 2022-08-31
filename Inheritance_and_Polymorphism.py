import logging

logging.basicConfig(filename="InheritandeExamples.log", level=logging.DEBUG)


class NotstringException(Exception):
    def __init__(self,msg):
        self.message = msg
        print(msg)

    def __str__(self):
        return self.message


class NotIntergerException(Exception):
    def __init__(self,msg):
        self.message = msg
        print(msg)

    def __str__(self):
        return self.message


class NotRangeClassException(Exception):
    def __init__(self,msg):
        self.message = msg
        print(msg)

    def __str__(self):
        return self.message


# Example-1 on Hierarchical Inheritance and Method overriding Ineuron Students
class IneuronStudent:
    name = ""
    _servicetype = ""
    __qualification = ""
    __empststus = ""

    def __init__(self,name,servicetype,qualifiction,empstatus):
        """
        :param name: Name of the student
        :param servicetype: The kind of service the student has opted in ineuron
        :param qualifiction: The qualification the student holds before joining into ineuron
        :param empstatus: The status of employement the student holds before joining into ineuron
        """
        try:
            logging.info("The given name is %s",name)
            if type(name) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.name = name
            logging.info("The given service type is %s",servicetype)
            if type(servicetype) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self._servicetype = servicetype
            logging.info("The given qualifiction is %s",qualifiction)
            if type(qualifiction) != str:
                raise (NotstringException("The given is not of string type"))
            else:
                self.__qualification = qualifiction
            logging.info("The given emp status is %s",empstatus)
            if type(empstatus) != str:
                raise (NotstringException("The given value is not a string type"))
            else:
                self.__empststus = empstatus
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.name = ""
            self._servicetype = ""
            self.__qualification = ""
            self.__empststus = ""

    def printDetails(self):
        """
        It prints the detailsof the students
        """
        print(self.name,self._servicetype,self.__qualification,self.__empststus)

    def WelcomeNote(self):
        print("Hi {}, welcome to Ineuron!".format(self.name))


class TechNeuron(IneuronStudent):
    courseName = ""

    def __init__(self,name,sericetype,qualification,empStatus, courseName):
        super().__init__(name,sericetype,qualification,empStatus)
        try:
            logging.info("The given name is %s",courseName)
            if type(courseName) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.courseName =courseName
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.courseName = ""

    def printTechNeuronDetails(self):
        """
        :return: It prints the details of the students present in TechNeuron with the courseName that they are doing
        """
        print(self.courseName,self.name,self._servicetype)

    def WelcomeNote(self):
        print("Hi {}, Welcome to FSDS!".format(self.name))


class FSDS(IneuronStudent):

    def __init__(self,name,servicetype,qualification,empStatus):
        super().__init__(name,servicetype,qualification,empStatus)

    def printFSDSDetails(self):
        """
        :return: It prints the details of the students present in TechNeuron with the courseName that they are doing
        """
        print(self.name,self._servicetype)

        def WelcomeNote(self):
            print("Hi {}, Welcome to FSDS!".format(self.name))


# Example-2 Ineuron Internship on Single Inheritance
# Using the super class Ineuronstudent class of Example-1
class IneuronIntership(IneuronStudent):
    intershipProjectName = ""
    intershipDescription = ""

    def __init__(self,name,servicetype,qualification,empStatus,interdshipProjectName,intershipDescription):
        super().__init__(name,servicetype,qualification,empStatus)
        try:
            logging.info("The given name is %s",interdshipProjectName)
            if type(interdshipProjectName) != str:
                raise (NotstringException("The given value is not string type"))
            else:
                self.intershipProjectName = interdshipProjectName
            logging.info("The given name is %s",intershipDescription)
            if type(intershipDescription) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.intershipDescription = intershipDescription
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.intershipProjectName = ""
            self.intershipDescription = ""

    def printIntershipDetails(self):
        """
        :return: It prints the details of the students present in Ineuron Internship with the projectname and description
        """
        print(self.name,self._servicetype,self.intershipProjectName,self.intershipDescription)


    def WelcomeNote(self):
        print("Hi {}, Welcome to Ineuron Internshio!".format(self.name))


# Example-3 on Polymorphism on contact Info using 2 classes and 1 function which is specified outside all the classes
class StudentContactInformation:
    studentMailId = ""
    studentphoneNumber = ""

    def setStudentEmailId(self,email):
        """
        :param email: The email id of the student
        :return: no Return
        """
        try:
            logging.info("The given email id is %s",email)
            if type(email) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.studentMailId = email
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.studentMailId = ""

    def setStudentPhoneNumber(self,phone):
        """
        :param phone:The phone number of the student
        :return: no Return
        """
        try:
            logging.info("The given phone number is %s",phone)
            if type(phone) != int:
                raise (NotIntergerException("The given value is not a integer type"))
            else:
                self.studentphoneNumber = phone
        except Exception as e:
            logging.exception("The exception we have got:" + "\n" + str(e))
            self.studentphoneNumber = ""

    def getEmilId(self):
        """
        :return: Prints student Email ID
        """
        print("The Student's Email ID is: ", self.studentMailId)

    def getPhoneNumber(self):
        """
        :return: Prints student Phone number
        """
        print("The student's Phone Number is:", self.studentphoneNumber)


class InstructorContactinformation:
    InstructorMailId = ""
    InstructorPhoneNumber = ""

    def setInstructorEmailId(self,email):
        """
        :param email:The email id of the instructor
        :return: No Return
        """
        try:
            logging.info("The given email id is %s", email)
            if type(email) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.InstructorMailId = email
        except Exception as e:
            logging.info("The exceptiom that we have got:" + "\n" + str(e))
            self.InstructorMailId = ""

    def setInstructorphonenumber(self,phone):
        """
        :param phone: The phone number of the instrutor
        :return: No Return
        """
        try:
            logging.info("The given phone no is %s", phone)
            if type(phone) != int:
                raise (NotIntergerException("The given value is not of integer type"))
            else:
                self.InstructorPhoneNumber = phone
        except Exception as e:
            logging.info("The exception that we have got:" + "\n" + str(e))
            self.InstructorPhoneNumber = ""

    def getPhoneNumber(self):
        """
        :return: Prints Instructor Phone Number
        """
        print("The Instructor's Phone Number is:", self.InstructorPhoneNumber)

    def getEmailId(self):
        """
        :return: Prints Instructor phone number
        """
        print("The Instructor's phone Number is:",self.InstructorMailId)


def check(a):
    a.getEmailId()
    a.getPhoneNumber()







