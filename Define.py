


PASS = 1
FAIL = 0

TRUE = 1
FALSE = 0

DEVICEOK = 1
PROGRAM = 2
PASS = 3
FAIL = 4

BinFile = ""
Status = 0
DeviceDetected = 0
TestModeGUI = 0
UpdateModeGUI = 0
PartSN = ""
Partnumber = ""
Rev = ""
Issue = 0
Day = 0
Month = 0
Year = 0

def initialize(): 
    global BinFile
    global AppRunning
    global Status
    global DeviceDetected
    global TestModeGUI
    global UpdateModeGUI
    global PartSN
    global Partnumber
    global Rev
    global Issue
    global Day
    global Month
    global Year
    BinFile = ""
    AppRunning = 1
    DeviceDetected = 0
    TestModeGUI = 0
    UpdateModeGUI = 0
    PartSN = ""
    Partnumber = ""
    Rev = ""
    Issue = 0
    Day = 0
    Month = 0
    Year = 0

def SetAppRun(val):
    global AppRunning
    AppRunning = val

def GetAppRun():
    global AppRunning
    return(AppRunning)

def SetStatus(x):
    global Status
    Status = x

def GetStatus():
    global Status
    return(Status)

def SetBinFile(val):
    global BinFile
    BinFile = val

def GetBinFile():
    global BinFile
    return(BinFile)

def SetDeviceDetected(x):
    global DeviceDetected
    DeviceDetected = x

def GetDeviceDetected():
    global DeviceDetected
    return(DeviceDetected)

def SetTestModeGUI(x):
    global TestModeGUI
    TestModeGUI = x

def GetTestModeGUI():
    global TestModeGUI
    return(TestModeGUI)

def SetUpdateModeGUI(x):
    global UpdateModeGUI
    UpdateModeGUI = x

def GetUpdateModeGUI():
    global UpdateModeGUI
    return(UpdateModeGUI)

def SetDayMonthYear(D,M,Y):
    global Day
    global Month
    global Year
    Day = D
    Month = M
    Year = Y

def GetDayMonthYear():
    global Day
    global Month
    global Year
    return ([Day,Month,Year])

def SetSN(SN):
    global PartSN
    PartSN = SN

def GetSN():
    global PartSN
    return (PartSN)

def SetPart(PN,R):
    global Partnumber
    global Rev
    Partnumber = PN
    Rev = R

def GetPart():
    global Partnumber
    global Rev
    return ([Partnumber,Rev])

def GetIssue():
    global Issue
    return (Issue)

def SetIssue(x):
    global Issue
    Issue = x
