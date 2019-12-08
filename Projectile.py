import random, math, os, shutil

class Projectile:
    def __init__(self):
        self.vi =round(random.randint(1320,2810)/100 , 4) 
        self.theta = round(random.randint(1000,7000)/100 , 4)
        self.vx = self.vi*math.cos((2*math.pi)*self.theta/360)
        self.vy = self.vi*math.sin((2*math.pi)*self.theta/360)
        #while True:
        #    self.randomMode = random.randint(0, 2)
        #    if self.randomMode == 1 or self.randomMode == 0:
        #        break
        self.randomMode = 1
        
        maxValue = int(998*(self.vy**2/(2*9.8))) + 1
        minValue = random.randint(1, maxValue)
        self.buildingHeight = round(random.randint(minValue, maxValue)/1000, 4)        
    '''
        if self.randomMode == 0:
            self.buildingHeight = round(random.randint(750, 2001)/100, 4)
        elif self.randomMode == 1:
            maxValue = 100*(int(self.vy**2/(2*9.8))) -1
            minValue = random.randint(0, maxValue)
            self.buildingHeight = round(random.randint(minValue, maxValue)/100, 4)
    '''
    def question1(self):
        text = ("A ball is rolled horizonally at velocity of %4.2f m/s off a %4.2f m building. Determine:" 
            "\\\\ a) How long is the ball in the air for"    
            "\\\\ b) How far the ball lands from the side of the building it was rolled off of" 
            )% (self.vi, self.buildingHeight )
        return text
    
    def answer1(self):
        return str(round(self.getDropTime(), 2)) + "\\\\" + str(round(self.vi*self.getDropTime(), 2))

    def question2(self):
        text = ("A ball is thrown at %4.2f m/s at an angle of %4.2f degrees above the horizontal.  Determine:" 
            "\\\\ a) The maximum height it reaches"
            "\\\\ b) How long is the ball in the air for"  
            "\\\\ a) How far the ball lands from its initally thrown"   
            )% (self.vi, self.theta )
        return text
    
    def answer2(self):
        return str(round(self.getMaxHeight(), 2)) + "\\\\" + str(round(self.getFlightTime(), 2)) + "\\\\" + str(round(self.getRange(), 2))
    
    def question3(self):
        text = ["",""]
        text[0] = ("A ball is thrown at %4.2f m/s at an angle of %4.2f degrees above the horizontal off a %4.2f m tall building.  Determine:" 
            "\\\\ a) The maximum height it reaches"
            "\\\\ b) How long is the ball in the air for"   
            "\\\\ c) How far the ball lands from its initally thrown"  
            )% (self.vi, self.theta, self.buildingHeight )
        text[1] = ("A ball is thrown at %4.2f m/s at an angle of %4.2f degrees above the horizontal.  If a magical animal is able to jump and catch the ball at exactly %4.2f m above the ground.  Determine:" 
            "\\\\ a) At what time(s), the animal is able to catch the ball" 
            "\\\\ b) What is the longest distance the animal must run to catch the ball"   
            "\\\\ c) How \\textbf{fast} is the ball travelling when the animal catches it"
            )% (self.vi, self.theta, self.buildingHeight )
        return text[self.randomMode]
    
    def answer3(self):
        text = ["",""]
        text[0] = str(round(self.getBuildingMaxHeight(), 2)) + "\\\\" + str(round(self.getBuildingFlightTime(), 2)) + "\\\\" + str(round(self.getBuildingRange(), 2))
        text[1] = str(round(self.getJumpTime()[0], 2)) + " , " +str(round(self.getJumpTime()[1], 2)) + "\\\\" + str(round(self.vx * self.getJumpTime()[1], 2)) + "\\\\" + str(round(self.getCatchVelocity(), 2))
        return text[self.randomMode]

# This is the section handles the traditional/ideal projectile
    def getDropTime(self):
        return math.sqrt(2*self.buildingHeight/9.8)

    def getMaxHeight(self):
        return ((self.vy)**2)/(2*9.8)
    
    def getRange(self):
        return (self.vi**2 *math.sin(2*(2*math.pi)*self.theta/360)/(2*9.8))

    def getFlightTime(self):
        return ((self.vy)*2)/(9.8)

# This section works with projectiles that have been elevated on top of a building    
    def getBuildingFlightTime(self):
        x = (-self.vy + math.sqrt(self.vy**2 + 2*9.8*(self.buildingHeight)))/(-9.8)
        y = (-self.vy - math.sqrt(self.vy**2 + 2*9.8*(self.buildingHeight)))/(-9.8)
        # Selecting the appropriate positive solution
        if x > y:
            return x
        else:
            return y
        
    def getJumpTime(self):
        x = (-self.vy + math.sqrt(self.vy**2 - 2*9.8*(self.buildingHeight)))/(-9.8)
        y = (-self.vy - math.sqrt(self.vy**2 - 2*9.8*(self.buildingHeight)))/(-9.8)
        return [x, y]
    
    def getCatchVelocity(self):
        vyf = math.sqrt(self.vy**2 - 2*9.8*self.buildingHeight)
        return math.sqrt(vyf**2 + self.vx**2)
        
    def getBuildingMaxHeight(self):
        return (self.vy**2)/(2*9.8) + self.buildingHeight

    def getBuildingRange(self):
        t = self.getBuildingFlightTime()
        return self.vx * t
    
    def LaTeXWriter(self, row):
        # Initialize read file
        latexFile = open('SPH3U Projectile Quest Template.tex', 'r')
        latexFileData = latexFile.readlines()
        n = 0

        for line in latexFileData:
            # Insert student name and student number
            if line == "\\hfill }\n":
                latexFileData[n] = row[0] + " \\hfill " + row[1] + " " + row[2] +"}\n"
            
            # Insert Questions into .tex file
            if line == "%INSERT QUESTION 1\n":
                latexFileData[n] = self.question1()
            if line == "%INSERT QUESTION 2\n":
                latexFileData[n] = self.question2()
            if line == "%INSERT QUESTION 3\n":
                latexFileData[n] = self.question3()

            # Insert Answers into .tex file
            if line == "% INSERT Q1 ANSWERS HERE\n":
                latexFileData[n] = self.answer1()
            if line == "% INSERT Q2 ANSWERS HERE\n":
                latexFileData[n] =  self.answer2()
            if line == "% INSERT Q3 ANSWERS HERE\n":
                latexFileData[n] = self.answer3()
            n = n + 1

    # Building the LaTeX PDFs
        file = str(row[0]) +".tex"
        outputFile = open(file, "w")
        outputFile.writelines(latexFileData)
        outputFile.close()
        latexOutput = "pdflatex -interaction=nonstopmode -halt-on-error " + file    
        os.system(latexOutput)

    # Moving files to the appropriate locations
        if os.path.isdir("Projectile Quest PDFs"):
            shutil.move(file[:-3]+"pdf", "Projectile Quest PDFs" )
        else:
            os.mkdir("Projectile Quest PDFs")
            shutil.move(file[:-3]+"pdf", "Projectile Quest PDFs" )
        
    # Cleaning up the directory of unnessessarry files
        os.remove(file[:-3] + "tex")
        os.remove(file[:-3] + "aux")
        os.remove(file[:-3] + "log")
'''
#In case someone wants the .tex files
        if not os.path.isdir("Projectile Quest tex Files"):
            os.mkdir("Projectile Quest tex Files")
            shutil.move(file,"Projectile Quest tex Files" )
        else:
            shutil.move(file,"Projectile Quest tex Files" )
'''
        
