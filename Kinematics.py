import random, math, os, shutil

class Kinematics:
    def __init__(self):
        # Defining random attibutes for problem
        v1_lower, v1_upper = self.generate_random(10, 98)
        v2_lower, v2_upper = self.generate_random(55, 490)
        a_lower, a_upper = self.generate_random(60, 100)
        t_lower, t_upper = self.generate_random(3, 32)


        self.v1 = round(random.randint(v1_lower, v1_upper)/10, 2)
        self.v2 = round(random.randint(v2_lower, v2_upper)/10, 2)
        self.a = round(random.randint(a_lower, a_upper)/10, 2)
        self.t = round(random.randint(t_lower, t_upper)/10, 2)


        param = ["1D Displacement", "2D Displacement", "Average Velocity", 
                "Instantanious Velocity", "Average Acceleration", "Instantanious Acceleration", 
                "motion graphs (not working)", "Big 5 Equations", "Projectile Motion"]

        displacement_q = ['''Determie the total displacement for the following motion using algebraic methods.  
                        Provide a scaled and labelled diagram with your solution: \\\\ 
                        $ \\Delta d_1 $ = {d1} m\\\\
                        $ \\Delta d_2 $ = {d2} m\\\\'''
        ]

        velocity_q = ["What is the displacement of a horse that runs at a velocity of {v1} m/s for {t} s"]

        acceleration_q = [ #'''a) While approacing a traffic light, a student driver begins to apply the breaks.  
                        # If the car's breaks can cause an average acceleration of {a1} $m/s^2$ [S] and it takes 
                        # {t} s for the car to come to rest, what was the car's initial velocity? \\\\
                        # b) What is the significance of the direction of the initial velocity and that of 
                        # the acceleration?''',
                            '''A squash ball with an initial velocity of {v1} m/s [W] is hit by a squash racket,
                            changing its velocity to {v2} m/s [E] in {t} s.  What is the squash ball's 
                            average acceleration'''  
        ]

        motion_graphs = []

        '''
        Right now, the focus is randomly generating 
        '''

        big_five_eq_q = [ # Eq 1
                        '''A dart is thrown at a target that is supported by a wooden backstop.  It strikes the 
                        backstop with an initial velocity of {v1} m/s[E].  The dart comes to rest in {t} s. \\\\
                            a) What is the acceleration of the dart? \\\\
                            b) How far does the dart penetrate into the backstop when it finally stops ''',
                        #Eq 3
                        '''A sports car approaches a highway on-ramp at a velocity of {v1} m/s [E].  If the car 
                        accelerates at a rage of {a} $m/s^2$ [E] for {t} s, what is the displacement of the car?''',
                        # Eq 4
                        '''A sailboat accelerates uniformly from {v1} m/s [N] to {v2} m/s [N] at a rate of {a} $m/s^2$ .
                        What distance does the boat travel?'''
        ]

        # Generate random question values
        rand_question_num1, rand_question_num2 = self.generate_random(0, len(big_five_eq_q)-1)

        if rand_question_num1 == 0:
            # For Eq 1
            self.big_five_eq_q_1 = big_five_eq_q[rand_question_num1].format(v1 = self.v1, t = self.t)
            self.solution_1 = self.eq1()
        elif rand_question_num1 == 1:
            self.big_five_eq_q_1 = big_five_eq_q[rand_question_num1].format(v1 = self.v1, a = self.a, t = self.t)
            self.solution_1 = self.eq3()
        elif rand_question_num1 == 2:
            self.big_five_eq_q_1 = big_five_eq_q[rand_question_num1].format(v1 = self.v1, v2 = self.v2, a = self.a)
            self.solution_1 = self.eq4()


        ###########################################
        #       Temporary Reroll of Values        #
        ###########################################
        v1_lower, v1_upper = self.generate_random(10, 98)
        v2_lower, v2_upper = self.generate_random(55, 490)
        a_lower, a_upper = self.generate_random(60, 100)
        t_lower, t_upper = self.generate_random(3, 32)


        self.v1 = round(random.randint(v1_lower, v1_upper)/10, 2)
        self.v2 = round(random.randint(v2_lower, v2_upper)/10, 2)
        self.a = round(random.randint(a_lower, a_upper)/10, 2)
        self.t = round(random.randint(t_lower, t_upper)/10, 2)

        if rand_question_num2 == 0:
                # For Eq 1
            self.big_five_eq_q_2 = big_five_eq_q[rand_question_num2].format(v1 = self.v1, t = self.t)
            self.solution_2 = self.eq1()
        elif rand_question_num2 == 1:
            self.big_five_eq_q_2 = big_five_eq_q[rand_question_num2].format(v1 = self.v1, a = self.a, t = self.t)
            self.solution_2 = self.eq3()
        elif rand_question_num2 == 2:
            self.big_five_eq_q_2 = big_five_eq_q[rand_question_num2].format(v1 = self.v1, v2 = self.v2, a = self.a)
            self.solution_2 = self.eq4()


    def eq1(self):
        return ((self.v2 - self.v1)/self.t, self.t*(self.v2 + self.v1)/2)
    def eq3(self):
        return self.v1 * self.t + 0.5*self.a*self.t**2
    def eq4(self):
        return (self.v2**2 - self.v1**2)/(2*self.a)

    def generate_random(self, lower, upper):
        ''' Generates a random, ordered tuple'''
        min_value = random.randint(lower, upper)
        max_value = random.randint(lower, upper)
        while min_value == max_value:
            max_value = random.randint(lower, upper)
        if min_value > max_value:
            return (max_value, min_value)
        else:
            return (min_value, max_value)

    def generate_q_a(self, q_num):
        pass

    def get_q1(self):
        return self.big_five_eq_q_1

    def get_q2(self):
        return self.big_five_eq_q_2

    def LaTeXWriter(self, row):
        # Initialize read file
        latexFile = open('SPH3U Kinematics Quiz Template.tex', 'r')
        latexFileData = latexFile.readlines()
        n = 0

        for line in latexFileData:
            # Insert student name and student number
            if line == "\\hfill }\n":
                latexFileData[n] = row[0] + " \\hfill " + row[1] + " " + row[2] +"}\n"
            
            # Insert Questions into .tex file
            if line == "%INSERT QUESTION 1\n":
                latexFileData[n] = self.big_five_eq_q_1
            if line == "%INSERT QUESTION 2\n":
                latexFileData[n] = self.big_five_eq_q_2
            n = n + 1

    # Building the LaTeX PDFs
        file = str(row[0]) +".tex"
        outputFile = open(file, "w")
        outputFile.writelines(latexFileData)
        outputFile.close()
        latexOutput = "pdflatex -interaction=nonstopmode -halt-on-error " + file    
        os.system(latexOutput)

    # Moving files to the appropriate locations
        if os.path.isdir("Kinematics Quiz PDFs"):
            shutil.move(file[:-3]+"pdf", "Kinematics Quiz PDFs" )
        else:
            os.mkdir("Kinematics Quiz PDFs")
            shutil.move(file[:-3]+"pdf", "Kinematics Quiz PDFs" )
        
    # Cleaning up the directory of unnessessarry files
        os.remove(file[:-3] + "tex")
        os.remove(file[:-3] + "aux")
        os.remove(file[:-3] + "log")