import os

DIRECTORY = "C:\\Users\\kellygr\\Desktop\\Scouting Data"

class Match:

    def __init__(self, number):

        #Auto fields
        self.number = number
        self.baseline = 0
        self.autoLowComplete = 0
        self.autoLowFailed = 0
        self.autoHighComplete = 0
        self.autoHighFailed = 0
        self.autoGear = 0
        self.autoHopperComplete = 0
        self.autoHopperFailed = 0
        #Teleop fields
        self.teleLowComplete = 0
        self.teleLowFailed = 0
        self.teleHighComplete = 0
        self.teleHighFailed = 0
        self.teleGearsComeplete = 0
        self.teleGearsFailed = 0
        #Endgame fields
        self.climb = 0
        self.comments = ""        

    def __str__(self):
        #Auto fields
        return(
        "Match Number:\t" + str(self.number) + "\n\n" +
        "Baseline:\t" + str(self.baseline) + "\n\n" +
        "Auto Low:\t" + str(self.autoLowComplete) + "\t" + str(self.autoLowFailed) + "\n\n" +
        "Auto High:\t" + str(self.autoHighComplete) + "\t" + str(self.autoHighFailed) + "\n\n" +
        "Auto Gear:\t" + str(self.autoGear) + "\n\n" +
        "Auto Hopper:\t" + str(self.autoHopperComplete) + "\t" + str(self.autoHopperFailed) + "\n\n" +
        #Teleop fields
        "Tele Low:\t" + str(self.teleLowComplete) + "\t" + str(self.teleLowFailed) + "\n\n" +
        "Tele High:\t" + str(self.teleHighComplete) + "\t" + str(self.teleHighFailed) + "\n\n" +
        "Tele Gear:\t" + str(self.teleGearsComeplete) + "\t" + str(self.teleGearsFailed) + "\n\n" +
        #Endgame fields
        "Climb:\t\t" + str(self.climb) + "\n\n" +
        "Comments:\t" + str(self.comments))
        

class Robot:

    def __init__(self, number):
        self.matches = []
        self.number = number
        
        self.autoLowAverage = 0
        self.autoLowAccuracy = 0
        
        self.autoHighAverage = 0
        self.autoHighAccuracy = 0
        
        self.autoGearCount = 0
        
        self.teleLowAverage = 0
        self.teleLowAccuracy = 0
        
        self.teleHighAverage = 0
        self.teleHighAccuracy = 0
        
        self.teleGearAverage = 0
        self.teleGearCount = 0
    
    
    def calculate(self):
        autoLowAccuracy = 0
        autoLowCount = 0
        
        autoHighAccuracy = 0
        autoHighCount = 0
        
        autoGearCount = 0
        
        teleLowAccuracy = 0
        teleLowCount = 0
        
        teleHighAccuracy = 0
        teleHighCount = 0
        
        teleGearAccuracy = 0
        teleGearCount = 0
        
        matchCount = 0
        for match in self.matches:
            matchCount += 1
            
            autoLowCount += match.autoLowComplete
            autoLowAccuracy += match.autoLowComplete/(match.autoLowComplete+match.autoLowFailed)
            
            autoHighCount += match.autoHighComplete
            autoHighAccuracy += match.autoHighComplete/(match.autoHighComplete+match.autoHighFailed)
                        
            autoGearCount += match.autoGear
            
            teleLowCount += match.teleLowComplete
            teleLowAccuracy += match.teleLowComplete/(match.teleLowComplete+match.teleLowFailed)
            
            teleHighCount += match.teleHighComplete
            teleHighAccuracy += match.teleHighComplete/(match.teleHighComplete+match.teleHighFailed)
                        
            teleGearCount += match.teleGearsComplete
            teleGearAccuracy += match.teleGearsComplete/(match.teleGearsComplete+match.teleGearsFailed)
            
            
        self.autoLowAccuracy = autoLowAccuracy/matchCount
        self.autoLowAverage = autoLowCount/matchCount
        
                    
        self.autoHighAccuracy = autoHighAccuracy/matchCount
        self.autoHighAverage = autoHighCount/matchCount
        
        self.autoGearAverage = autoGearCount/matchCount
        
        self.teleLowAccuracy = teleLowAccuracy/matchCount
        self.teleLowAverage = teleLowCount/matchCount
        
                    
        self.teleHighAccuracy = teleHighAccuracy/matchCount
        self.teleHighAverage = teleHighCount/matchCount
        
        self.teleGearAccuracy = teleGearAccuracy/matchCount
        self.teleGearAverage = teleGearCount/matchCount
            

    def addMatch(self, match):
        self.matches.append(match)
        
    def average(self):
        baseline = 0
        autoLowComplete = 0
        autoLowFailed = 0
        autoHighComplete = 0
        autoHighFailed = 0
        autoGear = 0
        autoHopperComplete = 0
        autoHopperFailed = 0
        teleLowComplete = 0
        teleLowFailed = 0
        teleHighComplete = 0
        teleHighFailed = 0
        teleGearsComeplete = 0
        teleGearsFailed = 0
        count = 0
        
        for match in self.matches:
            baseline += match.baseline
            autoLowComplete += match.autoLowComplete
            autoLowFailed += match.autoLowFailed
            autoHighComplete += match.autoHighcomplete
            autoHighFailed += match.autoHighFailed
            autoGear += match.autoGear
            autoHopperComplete += match.autoHopperComplete
            autoHopperFailed += match.autoHopperFailed
            teleLowComplete += match.teleLowComplete
            teleLowFailed += match.teleLowFailed
            teleHighComplete += match.teleHighComplete
            teleHighFailed += match.teleHighFailed
            teleGearsComeplete += match.teleGearsComeplete
            teleGearsFailed += match.teleGearsFailed
            count += 1
            
        baseline /= count
        autoLowComplete /= count
        autoLowFailed /= count
        autoHighComplete /= count
        autoHighFailed /= count
        autoGear /= count
        autoHopperComplete /= count
        autoHopperFailed /= count
        teleLowComplete /= count
        teleLowFailed /= count
        teleHighComplete /= count
        teleHighFailed /= count
        teleGearsComeplete /= count
        teleGearsFailed /= count
        
        print("Baseline:\t"+str(baseline) + "\n\n" +
        "Auto Low:\t"+str(autoLowComplete) + "\t" + str(autoLowFailed) + "\n\n" +
        "Auto High:\t"+str(autoHighComplete) + "\t" + str(autoHighFailed) + "\n\n" +
        "Auto Gear:\t"+str(autoGear) + "\n\n" +
        "Auto Hopper:\t"+str(autoHopperComplete) + "\t" + str(autoHopperFailed) + "\n\n" +
        #Teleop fields
        "Tele Low:\t"+str(teleLowComplete) + "\t" + str(teleLowFailed) + "\n\n" +
        "Tele High:\t"+str(teleHighComplete) + "\t" + str(teleHighFailed) + "\n\n" +
        "Tele Gears:\t"+str(teleGearsComeplete) + "\t" + str(teleGearsFailed))
        


robots = []

def readData():
    global robots
    for fileName in os.listdir(DIRECTORY):
        print(fileName.replace(".txt",""), end=" -> ")
        file = open(DIRECTORY+"\\"+fileName, "r")
        robot = Robot(fileName.replace(".txt",""))
    
        match = Match(0)
    
        for line in file:
            line.replace("\n","")
            if(line.startswith("start")):
                data = line.split(" ")
                print(data[1], end = ",")
                match = Match(int(data[1]))
            else:
                data = line.split(",")
                if(line.startswith("auto")):
                    match.baseline = int(data[1])
                    match.autoLowComplete = int(data[2])
                    match.autoLowFailed = int(data[3])
                    match.autoHighComplete = int(data[4])
                    match.autoHighFailed = int(data[5])
                    match.autoGear = int(data[6])
                    match.autoHopperComplete = int(data[7])
                    match.autoHopperFailed = int(data[8])
                if(line.startswith("teleop")):
                    match.teleLowComplete = int(data[1])
                    match.teleLowFailed = int(data[2])
                    match.teleHighComplete = int(data[3])
                    match.teleHighFailed = int(data[4])
                    match.teleGearsComplete = int(data[5])
                    match.teleFailedFailed = int(data[6])
                if(line.startswith("endgame")):
                    match.climb = int(data[1])
                    match.comments = data[2]
                elif(line.startswith("end")):
                    robot.matches.append(match)
                    
                   
        robot.calculate()
        robots.append(robot)
    
        print()
    print("\n")



readData()

def help():
    print("""
    FUNCTIONS:\n
        -help -> View this information
        -reload -> Reload data
        -average [robot] -> Prints averages for robot
        -match [robot] [match] -> Prints data for specific match
        -list -> Lists all teams
        -top [auto:tele] [gear:low:high] [count:accuracy]-> Lists Teams sorted by category, based on average count or accuracy, prints scores w/ team, gear NOT PROPERLY functional
        -all match [match] -> Prints data from that match for all robots in that match""")


help()
while True:
    inp = input("\n\n-> ").lower()
    inp += "\n"
    #Robot and Match not found status
    rnf = True
    mnf = True
    if("average" in inp):
        mnf = False
        for robot in robots:
            if(" "+robot.number+"\n" in inp):
                robot.average()
                rnf = False
    elif("all match" in inp):
        rnf = False
        for robot in robots:
            for match in robot.matches:
                if(" "+str(match.number)+"\n" in inp):
                    print("Robot:", robot.number,"\n",match)
                    mnf = False
                    
                
    elif("match" in inp):
        for robot in robots:
            if(" "+robot.number + " "  in inp):
                for match in robot.matches:
                    if(" "+str(match.number)+"\n" in inp):
                        print(match)
                        mnf = False
                rnf = False
    elif("list" in inp):
        rnf = False
        mnf = False
        robots.sort(key=lambda robot: int(robot.number), reverse=False)
        for robot in robots:
            print(robot.number)
    elif("top" in inp):
        rnf = False
        mnf = False
        
        if("auto" in inp):
            if("low" in inp):
                if("accuracy" in inp):
                    robots.sort(key=lambda robot: int(robot.autoLowAccuracy), reverse=False)
                if("count" in inp):
                    robots.sort(key=lambda robot: int(robot.autoLowAverage), reverse=False)
                for robot in robots:
                    print(robot.number,"\t",robot.autoLowAverage,"\t",robot.autoLowAccuracy*100,"%")
                    
            
            if("high" in inp):
                if("accuracy" in inp):
                    robots.sort(key=lambda robot: int(robot.autoHighAccuracy), reverse=False)
                if("count" in inp):
                    robots.sort(key=lambda robot: int(robot.autoHighAverage), reverse=False)
                for robot in robots:
                    print(robot.number,"\t",robot.autoHighAverage,"\t",robot.autoHighAccuracy*100,"%")
                    
            if("gear" in inp):
                if("accuracy" in inp):
                    robots.sort(key=lambda robot: int(robot.autoGearAccuracy), reverse=False)
                if("count" in inp):
                    robots.sort(key=lambda robot: int(robot.autoGearAverage), reverse=False)
                for robot in robots:
                    print(robot.number,"\t",robot.autoGearAverage*100,"%")
                    
        if("tele" in inp):
            if("low" in inp):
                if("accuracy" in inp):
                    robots.sort(key=lambda robot: int(robot.teleLowAccuracy), reverse=False)
                if("count" in inp):
                    robots.sort(key=lambda robot: int(robot.teleLowAverage), reverse=False)
                for robot in robots:
                    print(robot.number,"\t",robot.teleLowAverage,"\t",robot.teleLowAccuracy*100,"%")
                    
            
            if("high" in inp):
                if("accuracy" in inp):
                    robots.sort(key=lambda robot: int(robot.teleHighAccuracy), reverse=False)
                if("count" in inp):
                    robots.sort(key=lambda robot: int(robot.teleHighAverage), reverse=False)
                for robot in robots:
                    print(robot.number,"\t",robot.teleHighAverage,"\t",robot.teleHighAccuracy*100,"%")
                    
            if("gear" in inp):
                if("accuracy" in inp):
                    robots.sort(key=lambda robot: int(robot.teleGearAverage), reverse=False)
                if("count" in inp):
                    robots.sort(key=lambda robot: int(robot.teleGearAverage), reverse=False)
                for robot in robots:
                    print(robot.number,"\t",robot.teleGearAverage,"\t",robot.teleGearAccuracy*100,"%")
    
    elif("help" in inp):
        help()
        rnf = False
        mnf = False
        
    elif("reload" in inp):
        readData()
        rnf = False
        mnf = False
                    
            
    else:
        print("Unkown Function")
        rnf = False
        mnf = False
    
    if(rnf):
        print("Robot Not Found")
    elif(mnf):
        print("Match Not Found")


