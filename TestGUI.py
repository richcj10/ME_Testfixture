import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.constants, tkinter.filedialog
import Define as DF
import datetime
import Main
import re
import random
import datetime as dt

font1="Arial 16 bold"

TestConfigArrayGUI = []
ChannelCountGUI = 0
GlobalRoot = 0
TestModeGUI = 0
EpromType = ["USB hub","PD","MFB","Drawer"]

def DataSetter(TestArrayIN, TestChannelCount):
    global TestConfigArrayGUI
    global ChannelCountGUI
    TestConfigArrayGUI = TestArrayIN
    ChannelCountGUI = int(TestChannelCount)
    print(TestConfigArrayGUI)
    print(ChannelCountGUI)

class PythonGUI():
    def __init__(self):
        root = tk.Tk()
        global GlobalRoot
        GlobalRoot = root
        ##root.attributes('-fullscreen', True)
        ##root.configure(background='SteelBlue4')
        #scrW = root.winfo_screenwidth()
        #scrH = root.winfo_screenheight()
        #workwindow = str(1024) + "x" + str(768) + "+" + str(int((scrW - 1024) / 2)) + "+" + str(int((scrH - 768) / 2))
        #top1 = tk.Toplevel(root, bg="light blue")
        #top1.geometry(workwindow)
        root.protocol("WM_DELETE_WINDOW", self.Closing)
        root.geometry('850x450')
        root.title("  Enovate eeprom programer")
        root.attributes("-topmost", 1)  # make sure top1 is on top to start
        root.update()  # but don't leave it locked in place
        root.attributes("-topmost", 0)  # in case you use lower or lift
        # exit button - note: uses grid
        ##b3 = tk.Button(root, text="Exit", command= self.GUIShutdown)
        ##b3.grid(row=0, column=0, ipadx=10, ipady=10, pady=5, padx=5, sticky=tk.W + tk.N)

        self.MainLayer = ttk.Notebook(root)
        ##self.MainLayer.pack()
        ##self.StartLayer = ttk.Frame(self.MainLayer)
        ##self.TestSettings = ttk.Frame(self.MainLayer)
        ##self.ChannelConfig = ttk.Frame(self.MainLayer)

        ##self.MainLayer.add(self.StartLayer, text =' EEPROM Program    ')
        ##self.MainLayer.add(self.TestSettings, text =' EEPROM read ')
        ##self.MainLayer.add(self.ChannelConfig, text =' Channel Configure ')
        self.MainLayer.pack(expand = 1, fill ="both")

        self.VarSetup()
        self.MainWindowStart()
        ##self.ChannelConfigStart()
        ##self.TestSettingsStart()

    def Closing(self):
        global GlobalRoot
        if(self.GUIAskMsgBox("Do you wish to close?")):
            DF.SetAppRun(0)

    def VarSetup(self):
        t = datetime.datetime.now()
        self.ProgramTime = tk.StringVar()
        self.TestUIStat = tk.StringVar()
        self.USBHubFile=tk.StringVar()
        self.USBHubFilePath=tk.StringVar()
        self.USBHubFile.set("*.bin")
        self.TestUIStat.set("Wait")

        self.MFB_PartNumber=tk.StringVar()
        self.MFB_Rev=tk.StringVar()
        self.MFB_SN=tk.StringVar()
        self.MFB_Day=tk.StringVar()
        self.MFB_Month=tk.StringVar()
        self.MFB_Year=tk.StringVar()
        self.MFB_Issue=tk.IntVar()
        self.MFB_PartNumber.set("P0002850")
        self.MFB_Rev.set("1")
        #self.MFB_SN.set("Hi")
        self.MFB_Day.set(t.strftime("%d"))
        self.MFB_Month.set(t.strftime("%m"))
        self.MFB_Year.set(t.strftime("%y"))

        self.PD_PartNumber=tk.StringVar()
        self.PD_Rev=tk.StringVar()
        self.PD_SN=tk.StringVar()
        self.PD_Day=tk.StringVar()
        self.PD_Month=tk.StringVar()
        self.PD_Year=tk.StringVar()
        self.PD_Issue=tk.IntVar()
        self.PD_PartNumber.set("P0002893")
        self.PD_Rev.set("1")
        self.PD_Day.set(t.strftime("%d"))
        self.PD_Month.set(t.strftime("%m"))
        self.PD_Year.set(t.strftime("%y"))

        self.MB_PartNumber=tk.StringVar()
        self.MB_Rev=tk.StringVar()
        self.MB_SN=tk.StringVar()
        self.MB_Day=tk.StringVar()
        self.MB_Month=tk.StringVar()
        self.MB_Year=tk.StringVar()
        self.MB_Issue=tk.IntVar()
        self.MB_PartNumber.set("P0002893")
        self.MB_Rev.set("1")
        self.MB_Day.set(t.strftime("%d"))
        self.MB_Month.set(t.strftime("%m"))
        self.MB_Year.set(t.strftime("%y"))

    def GetUSBBin(self):
        global GlobalRoot
        GlobalRoot.filename =  tk.filedialog.askopenfilename(initialdir = "C:/Users/",title = "Select file",filetypes = [("bin files","*.bin")])
        self.USBHubFilePath = GlobalRoot.filename
        print(self.USBHubFilePath)
        split_string = re.split(r'[/.]', self.USBHubFilePath)
        ##print(split_string)
        ##print(len(split_string))
        NewFileName = str(split_string[len(split_string)-2] + "." + split_string[len(split_string)-1])
        self.USBHubFile.set(NewFileName)
        print(NewFileName)
        DF.SetBinFile(self.USBHubFilePath)

    def USBProgram(self):
        print("Program Hub")
        result = self.GUIAskMsgBox("Do you wish to proceed? \r\n This will erase the contese of the USB HUB EEPROM memory")
        if(result):
            DF.SetStatus(1) ## Tell main to start Program process

    def MFBProgram(self):
        if(self.MFB_SN.get() == ''):
            self.GUIErrorMsgBox("Please add a MFB serial number")
            return 0
        result = self.GUIAskMsgBox("Do you wish to proceed? \r\n This will erase the contese of the MFB EEPROM memory")
        if(result):
            DF.SetPart(self.MFB_PartNumber.get(),self.MFB_Rev.get())
            #print(self.MFB_SN.get())
            DF.SetSN(str(self.MFB_SN.get()))
            DF.SetDayMonthYear(self.MFB_Day.get(),self.MFB_Month.get(),self.MFB_Year.get())
            DF.SetIssue(self.MFB_Issue.get())
            DF.SetStatus(2)
            ##print("Program Hub")

    def PDProgram(self):
        if(self.PD_SN.get() == ''):
            self.GUIErrorMsgBox("Please add a PD serial number")
            return 0
        result = self.GUIAskMsgBox("Do you wish to proceed? \r\n This will erase the contese of the PD EEPROM memory")
        if(result):
            DF.SetPart(self.PD_PartNumber.get(),self.PD_Rev.get())
            #print(self.MFB_SN.get())
            DF.SetSN(str(self.PD_SN.get()))
            DF.SetDayMonthYear(self.PD_Day.get(),self.PD_Month.get(),self.PD_Year.get())
            DF.SetIssue(self.PD_Issue.get())
            DF.SetStatus(3)
            #print("Program PD")

    def MBProgram(self):
        if(self.PD_SN.get() == ''):
            self.GUIErrorMsgBox("Please add a MedBin serial number")
            return 0
        result = self.GUIAskMsgBox("Do you wish to proceed? \r\n This will erase the contese of the MedBin EEPROM memory")
        if(result):
            DF.SetPart(self.PD_PartNumber.get(),self.PD_Rev.get())
            #print(self.MFB_SN.get())
            DF.SetSN(str(self.PD_SN.get()))
            DF.SetDayMonthYear(self.PD_Day.get(),self.PD_Month.get(),self.PD_Year.get())
            DF.SetIssue(self.PD_Issue.get())
            DF.SetStatus(4)
            print("Med Bin Program")

    def MFBRead(self):
        DF.SetStatus(5)
        print("MFB Read")

    def PDRead(self):
        DF.SetStatus(6)
        print("PD Read")

    def MBRead(self):
        DF.SetStatus(7)
        print("MB Read")

    def MainWindowStart(self):

        self.StartPannelHome = tk.PanedWindow(self.MainLayer, height=400, width=200)
        self.StartPannelHome.pack(fill=tk.BOTH, expand=1)  # use a simple pack geometry to install this widget, use it all

        # fill the left side with a big LabelFrame
        self.TestControl = tk.LabelFrame(self.StartPannelHome, text="  EEPROM Config  ", relief=tk.GROOVE, width=100, height=500)  # do NOT pack it yet!
        self.Programlbl = tk.Label(self.TestControl, text="Program Option ")
        self.SelectProgram = ttk.Combobox(self.TestControl, values = EpromType, width=10)
        self.SelectProgram.current(0)
        self.SelectProgram.bind("<<ComboboxSelected>>", self.TestMode)
        self.Status_entry = tk.Entry(self.TestControl,textvariable = self.TestUIStat, width=15, justify="center")
        self.Programlbl.grid(padx=5, pady=5, row=0,column=0,sticky='n')
        self.SelectProgram.grid(padx=5, pady=5, row=1,column=0,sticky='n')
        self.Status_entry.grid(padx=5, pady=5, row=2,column=0,sticky='n')
        self.TestControl.pack()
        self.TestControl.pack_propagate(False)
        self.StartPannelHome.add(self.TestControl)
        self.StartPannelHome.pack(fill=tk.BOTH, expand=1)
        ##Test Output GUI
        self.TestOutput = tk.LabelFrame(self.StartPannelHome, text="  Program / Read  ", relief=tk.GROOVE)  # do NOT pack it yet!
        self.TestOutput.pack()
        self.TestOutput.pack_propagate(False)
        self.StartPannelHome.add(self.TestOutput)  # pw has its own "geometry" for arranging things internally
        self.StartPannelHome.pack(fill=tk.BOTH, expand=1)

        ##CH output List
        ####USB Hub
        self.USBLF = tk.LabelFrame(self.TestOutput, text="  Program USB Hub ", relief=tk.GROOVE)
        self.USBLF.grid(padx=2, pady=5, row=1,column=0,columnspan = 2)
        self.USBFilelbl = tk.Label(self.USBLF,anchor=tk.W, text="Program File: ")
        self.USBFile_entry = tk.Entry(self.USBLF,textvariable = self.USBHubFile,width=25,state=tk.DISABLED, disabledbackground="white", disabledforeground="black")
        self.GetButton = tk.Button(self.USBLF,anchor=tk.W,command=self.GetUSBBin,padx=5,pady=5,text="Open")
        self.ProgramButton = tk.Button(self.USBLF,anchor=tk.W,command=self.USBProgram,padx=5,pady=5,text="Program")

        self.USBFilelbl.grid(padx=1, pady=5, row=0,column=0,sticky = tk.N+tk.W+tk.E)
        self.USBFile_entry.grid(padx=1, pady=5, row=1,column=0)
        self.GetButton.grid(padx=5, pady=5, row=1,column=1)
        self.ProgramButton.grid(padx=5, pady=5, row=2,column=1)
        ####MFB
        self.MFBLF = tk.LabelFrame(self.TestOutput, text="  Program MFB EEPROM ", relief=tk.GROOVE)
        self.MFBLF.grid(padx=5, pady=5, row=2,column=0,columnspan = 2)
        self.MFBPNlbl = tk.Label(self.MFBLF, text="Part Number ")
        self.MFBRevlbl = tk.Label(self.MFBLF, text="Revison ")
        self.MFBSNlbl = tk.Label(self.MFBLF, text="Serial Number")
        self.MFBDaylbl = tk.Label(self.MFBLF, text="Day")
        self.MFBMonthlbl = tk.Label(self.MFBLF, text="Month")
        self.MFBYearlbl = tk.Label(self.MFBLF, text="Year")
        
        self.MFB_PN_entry = tk.Entry(self.MFBLF,textvariable = self.MFB_PartNumber, width = 8)
        self.MFB_BR_entry = tk.Entry(self.MFBLF,textvariable = self.MFB_Rev, width = 2)
        self.MFB_SN_entry = tk.Entry(self.MFBLF,textvariable = self.MFB_SN, width = 12)
        self.MFB_Day_entry = tk.Entry(self.MFBLF,textvariable = self.MFB_Day, width = 3)
        self.MFB_Month_entry = tk.Entry(self.MFBLF,textvariable = self.MFB_Month, width = 3)
        self.MFB_Year_entry = tk.Entry(self.MFBLF,textvariable = self.MFB_Year, width = 3)
        self.MFBProgramButton = tk.Button(self.MFBLF,anchor=tk.W,command=self.MFBProgram,padx=5,pady=5,text="MFB Program")
        self.MFBReadButton = tk.Button(self.MFBLF,anchor=tk.W,command=self.MFBRead,padx=5,pady=5,text="MFB Read")

        self.MFBPNlbl.grid(padx=5, pady=5, row=0,column=0)
        self.MFBRevlbl.grid(padx=5, pady=5, row=1,column=0)
        self.MFBSNlbl.grid(padx=5, pady=5, row=2,column=0)
        self.MFB_PN_entry.grid(padx=5, pady=5, row=0,column=1)
        self.MFB_BR_entry.grid(padx=5, pady=5, row=1,column=1)
        self.MFB_SN_entry.grid(padx=5, pady=5, row=2,column=1)
        self.MFBDaylbl.grid(padx=5, pady=5, row=0,column=2)
        self.MFBMonthlbl.grid(padx=5, pady=5, row=1,column=2)
        self.MFBYearlbl.grid(padx=5, pady=5, row=2,column=2)
        self.MFB_Day_entry.grid(padx=5, pady=5, row=0,column=3)
        self.MFB_Month_entry.grid(padx=5, pady=5, row=1,column=3)
        self.MFB_Year_entry.grid(padx=5, pady=5, row=2,column=3)
        #self.MFB_Year_entry.grid(padx=5, pady=5, row=2,column=1)
        self.MFBReadButton.grid(padx=5, pady=5, row=3,column=0)
        self.MFBProgramButton.grid(padx=5, pady=5, row=3,column=3)
        ####PD
        self.PDLF = tk.LabelFrame(self.TestOutput, text="  Program PD EEPROM ", relief=tk.GROOVE)
        self.PDLF.grid(padx=5, pady=5, row=1,column=2,columnspan = 2)
        self.PDPNlbl = tk.Label(self.PDLF, text="Part Number ")
        self.PDRevlbl = tk.Label(self.PDLF, text="Revison ")
        self.PDSNlbl = tk.Label(self.PDLF, text="Serial Number")
        self.PDDaylbl = tk.Label(self.PDLF, text="Day")
        self.PDMonthlbl = tk.Label(self.PDLF, text="Month")
        self.PDYearlbl = tk.Label(self.PDLF, text="Year")
        
        self.PD_PN_entry = tk.Entry(self.PDLF,textvariable = self.PD_PartNumber, width = 8)
        self.PD_BR_entry = tk.Entry(self.PDLF,textvariable = self.PD_Rev, width = 2)
        self.PD_SN_entry = tk.Entry(self.PDLF,textvariable = self.PD_SN, width = 12)
        self.PD_Day_entry = tk.Entry(self.PDLF,textvariable = self.PD_Day, width = 3)
        self.PD_Month_entry = tk.Entry(self.PDLF,textvariable = self.PD_Month, width = 3)
        self.PD_Year_entry = tk.Entry(self.PDLF,textvariable = self.PD_Year, width = 3)
        self.PDProgramButton = tk.Button(self.PDLF,anchor=tk.W,command=self.PDProgram,padx=5,pady=5,text=" PD Program")
        self.PDRedButton = tk.Button(self.PDLF,anchor=tk.W,command=self.PDRead,padx=5,pady=5,text=" PD Read")

        self.PDPNlbl.grid(padx=5, pady=5, row=0,column=0)
        self.PDRevlbl.grid(padx=5, pady=5, row=1,column=0)
        self.PDSNlbl.grid(padx=5, pady=5, row=2,column=0)
        self.PD_PN_entry.grid(padx=5, pady=5, row=0,column=1)
        self.PD_BR_entry.grid(padx=5, pady=5, row=1,column=1)
        self.PD_SN_entry.grid(padx=5, pady=5, row=2,column=1)
        self.PDDaylbl.grid(padx=5, pady=5, row=0,column=2)
        self.PDMonthlbl.grid(padx=5, pady=5, row=1,column=2)
        self.PDYearlbl.grid(padx=5, pady=5, row=2,column=2)
        self.PD_Day_entry.grid(padx=5, pady=5, row=0,column=3)
        self.PD_Month_entry.grid(padx=5, pady=5, row=1,column=3)
        self.PD_Year_entry.grid(padx=5, pady=5, row=2,column=3)
        self.PDRedButton.grid(padx=5, pady=5, row=3,column=0)
        self.PDProgramButton.grid(padx=5, pady=5, row=3,column=3)
        ####MedBin
        self.MBLF = tk.LabelFrame(self.TestOutput, text="  Program MedBin EEPROM ", relief=tk.GROOVE)
        self.MBLF.grid(padx=5, pady=5, row=2,column=2,columnspan = 2)
        self.MBPNlbl = tk.Label(self.MBLF, text="Part Number ")
        self.MBRevlbl = tk.Label(self.MBLF, text="Revison ")
        self.MBSNlbl = tk.Label(self.MBLF, text="Serial Number")
        self.MBDaylbl = tk.Label(self.MBLF, text="Day")
        self.MBMonthlbl = tk.Label(self.MBLF, text="Month")
        self.MBYearlbl = tk.Label(self.MBLF, text="Year")
        
        self.MB_PN_entry = tk.Entry(self.MBLF,textvariable = self.MB_PartNumber, width = 8)
        self.MB_BR_entry = tk.Entry(self.MBLF,textvariable = self.MB_Rev, width = 2)
        self.MB_SN_entry = tk.Entry(self.MBLF,textvariable = self.MB_SN, width = 12)
        self.MB_Day_entry = tk.Entry(self.MBLF,textvariable = self.MB_Day, width = 3)
        self.MB_Month_entry = tk.Entry(self.MBLF,textvariable = self.MB_Month, width = 3)
        self.MB_Year_entry = tk.Entry(self.MBLF,textvariable = self.MB_Year, width = 3)
        self.MBProgramButton = tk.Button(self.MBLF,anchor=tk.W,command=self.MBProgram,padx=5,pady=5,text=" MedBin Program")
        self.MBRedButton = tk.Button(self.MBLF,anchor=tk.W,command=self.MBRead,padx=5,pady=5,text=" MedBin Read")

        self.MBPNlbl.grid(padx=5, pady=5, row=0,column=0)
        self.MBRevlbl.grid(padx=5, pady=5, row=1,column=0)
        self.MBSNlbl.grid(padx=5, pady=5, row=2,column=0)
        self.MB_PN_entry.grid(padx=5, pady=5, row=0,column=1)
        self.MB_BR_entry.grid(padx=5, pady=5, row=1,column=1)
        self.MB_SN_entry.grid(padx=5, pady=5, row=2,column=1)
        self.MBDaylbl.grid(padx=5, pady=5, row=0,column=2)
        self.MBMonthlbl.grid(padx=5, pady=5, row=1,column=2)
        self.MBYearlbl.grid(padx=5, pady=5, row=2,column=2)
        self.MB_Day_entry.grid(padx=5, pady=5, row=0,column=3)
        self.MB_Month_entry.grid(padx=5, pady=5, row=1,column=3)
        self.MB_Year_entry.grid(padx=5, pady=5, row=2,column=3)
        self.MBRedButton.grid(padx=5, pady=5, row=3,column=0)
        self.MBProgramButton.grid(padx=5, pady=5, row=3,column=3)

    def GUIShutdown(self):
        DF.SetAppRun(0)

    def GUIStatus(self, Stat):
        if(Stat == DF.DEVICEOK):
            self.Status_entry.config(bg = "#0747ea") 
            self.TestUIStat.set("Ready")
        if(Stat == DF.PROGRAM):
            self.Status_entry.config(bg = "#f0fc0a") 
            self.TestUIStat.set("Run")
        if(Stat == DF.PASS):
            self.Status_entry.config(bg = "#31ff11")
            self.TestUIStat.set("PASS")
        if(Stat == DF.FAIL):
            self.Status_entry.config(bg = "#ef0e33")
            self.TestUIStat.set("FAIL")

    def GUIErrorMsgBox(self, msg):
        tk.messagebox.showerror("Warning:", msg,parent=self.MainLayer)

    def GUIAskMsgBox(self, msg):
        resut = tk.messagebox.askyesno("Proceed:", msg,parent=self.MainLayer)
        return resut

    def TestMode(self, event):
        TestModeGUI = EpromType.index(self.SelectProgram.get())
        DF.SetTestModeGUI(TestModeGUI)
        DF.SetUpdateModeGUI(1)
        ##print("Mode = ",TestModeGUI)
