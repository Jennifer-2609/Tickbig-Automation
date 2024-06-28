import configparser

config=configparser.ConfigParser()
config.read('C:\\Users\\jenni\\PycharmProjects\\PythonFramework\\Configurations\\config.ini')
# username = config.get('settings',"BaseUrl")
# print(username)

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        url=config.get('settings','BaseURL')
        return url

    @staticmethod
    def getUseremail():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        username = config.get('settings', 'username')
        return username

    @staticmethod
    def getPassword():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        password = config.get('settings', 'password')
        return password

    @staticmethod
    def getType():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        Type = config.get('settings', 'type')
        return Type

    @staticmethod
    def getNewemail():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        email = config.get('settings', 'email')
        return email

    @staticmethod
    def getNewemailone():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        emailone = config.get('settings', 'emailone')
        return emailone
    @staticmethod
    def getNewpwd():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        newpassword= config.get('settings', 'newpassword')
        return newpassword

    @staticmethod
    def getConfirmpwd():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        confirmpwd = config.get('settings', 'confirmpwd')
        return confirmpwd

    @staticmethod
    def getlengthemail():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        lengthemail = config.get('settings', 'lengthemail')
        return lengthemail

    @staticmethod
    def getlengthpassword():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        lengthpassword = config.get('settings', 'lengthpassword')
        return lengthpassword

    @staticmethod
    def getcompname():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        compname = config.get('settings', 'compname')
        return compname

    @staticmethod
    def getbrandname():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        brandname = config.get('settings', 'brandname')
        return brandname

    @staticmethod
    def getmobnum():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        mobnum = config.get('settings', 'mobnum')
        return mobnum

    @staticmethod
    def getquote():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        quote = config.get('settings', 'quote')
        return quote

    @staticmethod
    def getshortquote():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        shortquote = config.get('settings', 'shortquote')
        return shortquote

    @staticmethod
    def getlongquote():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        longquote = config.get('settings', 'longquote')
        return longquote



    @staticmethod
    def getlevel():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        level = config.get('settings', 'level')
        return level

    @staticmethod
    def getskill():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        skill = config.get('settings', 'skill')
        return skill

    @staticmethod
    def getdesdignation():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        designation = config.get('settings', 'designation')
        return designation

    @staticmethod
    def gettagline():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        tagline = config.get('settings', 'tagline')
        return tagline

    @staticmethod
    def getsummary():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        summary = config.get('settings', 'summary')
        return summary

    @staticmethod
    def getaddress1():
        # config = configparser.ConfigParser()
        # config.read('.\\Configurations\\config.ini')
        address1 = config.get('settings', 'address1')
        return address1

    @staticmethod
    def getaddress2():
        address2 = config.get('settings', 'address2')
        return address2

    @staticmethod
    def getcity():
        city = config.get('settings', 'city')
        return city

    @staticmethod
    def getstate():
        state = config.get('settings', 'state')
        return state

    @staticmethod
    def getcountry():
        country = config.get('settings', 'country')
        return country

    @staticmethod
    def getpincode():
        pincode = config.get('settings', 'pincode')
        return pincode

    @staticmethod
    def getExpDesgination():
        ExpDesgination = config.get('settings', 'ExpDesgination')
        return ExpDesgination

    @staticmethod
    def getExpCompname():
        ExpCompname = config.get('settings', 'ExpCompname')
        return ExpCompname

    @staticmethod
    def getJobLocation():
        JobLocation = config.get('settings', 'JobLocation')
        return JobLocation

    @staticmethod
    def getStartYearExp():
        StartYearExp = config.get('settings', 'StartYearExp')
        return StartYearExp

    @staticmethod
    def getEndYearExp():
        EndYearExp = config.get('settings', 'EndYearExp')
        return EndYearExp

    @staticmethod
    def getqualification():
        qualification = config.get('settings', 'qualification')
        return qualification

    @staticmethod
    def getinstname():
        instname = config.get('settings', 'instname')
        return instname

    @staticmethod
    def getInstLocation():
        InstLocation = config.get('settings', 'InstLocation')
        return InstLocation

    @staticmethod
    def getStartYearEdu():
        StartYearEdu = config.get('settings', 'StartYearEdu')
        return StartYearEdu

    @staticmethod
    def getEndYearEdu():
        EndYearEdu = config.get('settings', 'EndYearEdu')
        return EndYearEdu

    @staticmethod
    def getAchieveTitle():
        AchieveTitle = config.get('settings', 'AchieveTitle')
        return AchieveTitle

    @staticmethod
    def getAchieveDescription():
        AchieveDescription = config.get('settings', 'AchieveDescription')
        return AchieveDescription

    @staticmethod
    def getAchieveDescriptionnew():
        AchieveDescriptionnew = config.get('settings', 'AchieveDescriptionnew')
        return AchieveDescriptionnew

    @staticmethod
    def getAchieveDescriptionmax():
        AchieveDescriptionmax = config.get('settings', 'AchieveDescriptionmax')
        return AchieveDescriptionmax


    @staticmethod
    def getMilestoneYear():
        MilestoneYear = config.get('settings', 'MilestoneYear')
        return MilestoneYear

    @staticmethod
    def getMilestoneDescription():
        MilestoneDescription = config.get('settings', 'MilestoneDescription')
        return MilestoneDescription

    @staticmethod
    def getMSDescriptionAtLeast():
        MSDescriptionAtLeast = config.get('settings', 'MSDescriptionAtLeast')
        return MSDescriptionAtLeast

    @staticmethod
    def getMSDescriptionMaxChar():
        MSDescriptionMaxChar = config.get('settings', 'MSDescriptionMaxChar')
        return MSDescriptionMaxChar

    @staticmethod
    def getInvalidYear():
        InvalidYear = config.get('settings', 'InvalidYear')
        return InvalidYear

    @staticmethod
    def getprojectname():
        projectname = config.get('settings', 'projectname')
        return projectname

    @staticmethod
    def getprojectcompanyname():
        projectcompanyname = config.get('settings', 'projectcompanyname')
        return projectcompanyname

    @staticmethod
    def getprojectlinks():
        projectlinks = config.get('settings', 'projectlinks')
        return projectlinks

    @staticmethod
    def getprojectresponsibility():
        projectresponsibility = config.get('settings', 'projectresponsibility')
        return projectresponsibility

    @staticmethod
    def getprojectdescription():
        projectdescription = config.get('settings', 'projectdescription')
        return projectdescription

    @staticmethod
    def getprojectdescriptionmin():
        projectdescriptionmin = config.get('settings', 'projectdescriptionmin')
        return projectdescriptionmin

    @staticmethod
    def getprojectdescriptionmax():
        projectdescriptionmax = config.get('settings', 'projectdescriptionmax')
        return projectdescriptionmax


    # security details

    @staticmethod
    def getcurrentpwd():
        currentpwd = config.get('settings', 'currentpwd')
        return currentpwd

    @staticmethod
    def getnewpwd():
        newpwd = config.get('settings', 'newpwd')
        return newpwd

    @staticmethod
    def getrenewpwd():
        renewpwd = config.get('settings', 'newpwd')
        return renewpwd

    @staticmethod
    def getforgptpwdmail():
        forgptpwdmail = config.get('settings', 'forgptpwdmail')
        return forgptpwdmail