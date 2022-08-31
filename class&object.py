import logging

logging.basicConfig(filename="constructorExample.log",level=logging.DEBUG)


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


# Example-1 on Ineuron Students


class IneuronStudent:
    name = ""
    _servicetype = ""
    __qualification = ""
    __empstatus = ""

    def __init__(self,name,servicetype,qualification,empstatus):
        """
        :param name: Name of the student
        :param servicetype: The kind of the service the student has opted in ineuron
        :param qualification: The qualification the student holds before joining into ineuron
        :param empstatus:The status of employment the student holds before joining into ineuron
        """
        try:
            logging.info("The given is %s",name)
            if type(name) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.name=name
            logging.info("The given service type is %s",servicetype)
            if type(servicetype) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self._servicetype=servicetype
            logging.info("The given qualification is %s",qualification)
            if type(qualification) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.__qualification=qualification
            logging.info("The given emp status is %s",empstatus)
            if type(empstatus) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.__empstatus=empstatus
        except Exception as e:
            logging.exception("The exception that we have got:"+"\n"+str(e))
            self.name=""
            self._servicetype=""
            self.__qualification=""
            self.__empstatus=""

    def printDetails(self):
        """
        It prints the details of the students
        """
        print(self.name,self._servicetype,self.__qualification,self.__empstatus)


# Example-2 on TechNeuron

class TechNeuron:
    mainTopic = ""
    subtopics = []

    def setMainTopic(self,mt):
        """
        :param mt: It is a string variable with value for main topic
        :return: No return
        """
        try:
            logging.info("The given topic is %s",mt)
            if type(mt) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.mainTopic=mt
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.mainTopic = ""

    def setSubTopics(self,*st):
        """
        :param st:It is a tuple of string variables ref to main topic
        :return: No return
        """
        logging.info("The given main topic is %s",str(st))
        self.subtopics = list(st)

    def getcoursedetails(self):
        """
        Print course Details
        """
        print("The main Topic is:",self.mainTopic)
        print("The sub Topics is:",self.subtopics)


# Example-3 on Ineuron Classes

class IneuronClasses:
    classTopic= ""
    classInstructorName = ""
    noOfHours = 0

    def __init__(self,classTopic,classInstructorName,noOfHours):
        """
        :param classTopic:The name of the topic that will taken in class
        :param classInstructorName: The name of the instructor who will take the class
        :param noOfHours: The number of hour the class will be conducted
        """
        try:
            logging.info("The given class topic is %s", str(classTopic))
            if type(classTopic) != str:
                raise (NotstringException("The given value is not of string type"))
            else:
                self.classTopic=classTopic
            logging.info("The given class instructor name is %s",str(classInstructorName))
            if type(classInstructorName) != str:
                raise (NotstringException("The given value is not string type"))
            else:
                self.classInstructorName =classInstructorName
            logging.info("The given number if hour is %s", str(noOfHours))
            if type(noOfHours) != int:
                raise (NotstringException("The given value is not of interger type"))
            else:
                self.noOfHours=noOfHours
        except Exception as e:
            logging.exception("The exception that we have got:"+"\n"+str(e))
            self.classTopic =""
            self.classInstructorName =""
            self.noOfHours = 0


# Example -9 on jobs
class Jobs:
    companyName = ""
    companyJobDescription = ""
    _salaryRange = range(0,1)

    def setCompanyName(self,cname):
        """
        :param cname: It is the company's name
        :return: No Return
        """



