# -*- coding: utf-8 -*-
"""
Due on Tue May 31 9:00am
@author: Group 1-- Marcus Reynolds, Gabriel Poulson, Dan Addington
Project link here: http://apmonitor.com/che263/uploads/Main/heat_exchanger_project.pdf
"""
class HeatExchanger():
   # Marcus     
    def __init__(self):
        # Import packages
        import numpy as np
        import sys
        
        # Instance variables that are given in getInput() and then used in another function are declared here
        self.units=""    # aes or si
        self.U=0         # Heat Transfer Coefficient
        self.T_ci=0       # T cold fluid, in
        self.T_hi=0       # T hot fluid, in
        self.m_c=0        # flow rate cold fluid
        self.m_h=0        # flow rate hot fluid
        self.cold=""     # options given below in input
        self.hot=""      # options given below in input
        self.given=""    # T_co or T_ho
        # Run the program
        runAll()

    def runAll(self):
    # Runs all the other functions
        getInput()
        T=solveT()
        area=solveArea()
        cost=solveCost(area)
        output(area,T,cost)
   
Gabriel
   # def getInput(self)
   
    def Units(self):
            AES = "American Engineering System"
            SI = "System International"
            Units = input("What measurement system would you like to use? AES or SI")
            #print error and restart function if not AES or SI
        #Temp_Units = input("Specify inlet temperature units")
        #Units_Mass = input("Please specify the units you would like to use") #K,C,F,R
       # Stream_1_in_cold = input("A number") #FLOAT FUNCTION?
        #Stream_2_in_hot = input(float(x)) #Store values in an array so that it all flows together
        
       # u_aes_mass1 = "lbs"
       # u_aes_mass2 = "tons"
       # u_si_mass = "kg"  
        
    def getSubstance(self):
        print("The available fluids are Water,R134a,Ethanol,2,2,4-trimethylpentane")
        print("Use W,R134a,Ethanol, or TMP")
        #Liquid = np.empty()
        #Water = Liquid[0]
        #R134a = Liquid[1]
        #Ethanol = Liquid[2]
        #tryimethylpethane = Liquid[3]
        #add float function in here
        self.cold = input("What substance will you choose as your cooling stream?")
        self.hot = input("What substance will you choose as your heating stream?")
        return self.T_ci, self.T_hi
        
    def getLiquid(self):
        # Liquids = np.empty(2)
        #define units as valid as we are running them through the program.
        while Units == AES:
            self.m_c = float(input("Define cooling flow rate in lbs./s"))
            self.T_ci =  float(input("Define cooling inlet temperature in degrees Farenheit(F)"))
            self.m_h = float(input("Define heating flow rate in lbs./s"))
            self.T_hi =  float(input("Define heating inlet temperature in degrees Farenheit(F)"))
            self.U = float(input("Define heat transfer coefficient in Btu/ft2 hr oF"))
        else:
            self.m_c = float(input("Define cooling flow rate in kg/s"))
            self.T_ci = float(input("Define cooling inlet temperature in degrees Celsius"))
            self.m_h = float(input("Define heating flow rate in kg/s"))
            self.T_hi = float(input("Define heating inlet temperature in degrees Celsius"))
            self.U = float(input("Define heat transfer coefficient in W/m2 K:"))
   
    def convertUnits(self):
        # convert AES to SI units
        if Units == AES:
            self.m_c = self.m_c * 0.453592
            self.T_ci =  (self.T_ci + 459.67) * 5/9
            self.m_h = self.m_h * 0.453592
            self.T_hi = (self.T_hi + 459.67) * 5/9
            self.U = self.U * 5.6784   
        else:
           # self.m_c = self.m_c
            self.T_ci = self.T_ci + 273.15
            #self.m_h = self.m_h
            self.T_hi = self.T_hi + 273.15
            #self.U = self.U
        #return all converted inputs
        
  
        
    #Might need some if elif statements in here.
    """user can specify: #define each of these inputs as separate functions, getTemp, getMass, getflowrate, getunits,getmaterial, etc. 
            aes or si units
            U, T_ci, T_hi, m_c, m_h, T_co or T_ho
            Cold: water or 1,1,1,2-Tetrafluoroethane or ethanol or 2,2,4-trimethylpentane
            Hot: same options as cold
            # Need to import thermophysical data to see if substance is a fluid at said temperature and pressure"""

    
    def isValid(self,value): #see if the liquids are valid at the given temperatures
        while self.T_ci<=0 and self.T_hi<=0:
            print("Invalid Temperatures. Program restarting")
            break
        
         #Heating must be greater than cooling
            
        
  
        
    #Might need some if elif statements in here.
    """user can specify: #define each of these inputs as separate functions, getTemp, getMass, getflowrate, getunits,getmaterial, etc. 
            aes or si units
            U, T_ci, T_hi, m_c, m_h, T_co or T_ho
            Cold: water or 1,1,1,2-Tetrafluoroethane or ethanol or 2,2,4-trimethylpentane
            Hot: same options as cold
            # Need to import thermophysical data to see if substance is a fluid at said temperature and pressure"""
# Dan        
    def solveArea(self):
    # Calculates area from input
    
     #Correction Factor 'F' as a function of 'R' and 'P'
            R = (self.T_hi-self.T_ho)/(self.T_co-self.T_ci)
            P = (self.T_co-self.T_ci)/(self.T_hi-self.T_ci)
        
            F = (np.sqrt(R**2 +1)/(R-1)) * \
                np.log((1-P)/(1-P*R))/ \
                np.log((2-P*(R+1-np.sqrt(R**2 +1)))/(2-P*(R+1+np.sqrt(R**2 +1))))
        
            #Log Mean Temperature Difference
            T_logmean = (dT1 - dT2)/np.log(dT2/dT1)
        
            #Caluclate and Return Area
            area = q/(F*self.U*T_logmean) #m^2
            return (area)
    
        return area
        
    def getCp(self):
       # Cp is the average of inlet and outlet temperatures
        if self.given=="T_co":
            Cp=(self.T_co+self.T_ci)/2
            # something
        elif self.given=="T_ho":
            Cp=(self.T_ho+self.T_hi)/2
            # something else
        else:
            print("Cp calculation went wrong")
            
    def solveT(self):
       """ Problem here, there can only be 1 return in a function"""
    # calculates Tco or Tho (whichever one was NOT given in getInput() )
        #To do!! define m_c, m_h, Cp_h, Cp_c
        
        #Solve for Tco or Tho
        if getInput() == "T_ho":
            T_co = m_h*Cp_h*(T_hi-T_ho)/(m_c*Cp_c) + T_ci
            return T_co
        else:
            T_ho = -m_c*Cp_c*(T_co-T_ci)/(m_h*Cp_h) + T_hi
            return T_ho
        
        #Solve for Change in Temp 1 and 2
        dT1 = T_hi - T_co
        dT2 = T_ho - T_ci
        
        
        #Solve for Heat Transfer Rate 'q'
        q = m_h*Cp_h*(T_co-T_ci)
            
        return T
        
    def solveCost(self,area):
        # cost = $1000 * area (m^2)
        cost=1000*area # in USD
        
        return cost
        
# Marcus        
    def output(self, area, T, cost):
        # Displays solutions all in SI units
        print("Surface Area=",area,"m^2")
        if self.given=="T_co":
            print("T_ho=",T,"K")
        else:
            print("T_co=",T,"K")
        print("Cost= $"+str(cost))
