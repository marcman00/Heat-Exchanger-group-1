# -*- coding: utf-8 -*-
"""
Due on Tue May 31 9:00am
@author: Group 1-- Marcus Reynolds, Gabriel Poulson, Dan Addington
Project link here: http://apmonitor.com/che263/uploads/Main/heat_exchanger_project.pdf
"""
class HeatExchanger():
    
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
# Marcus    
    def runAll(self):
    # Runs all the other functions
        getInput()
        T=solveT()
        area=solveArea()
        cost=solveCost(area)
        output(area,T,cost)
   
# Gabriel
    def getInput(self):
        # Variables are set here.
    """user can specify:
            aes or si units
            U, T_ci, T_hi, m_c, m_h, T_co or T_ho
            Cold: water or 1,1,1,2-Tetrafluoroethane or ethanol or 2,2,4-trimethylpentane
            Hot: same options as cold
    """
    
    def isValid(self,value):
        # checks if a number is negative. If so, returns error message and exits program.    
        
    def convertUnits(self,value):
        # convert AES to SI units
        return newValue
# Dan        
    def solveArea(self):
    # Calculates area from input
    
        return area
        
    def solveT(self):
    # calculates Tco or Tho (whichever one was NOT given in getInput() )
    # (Hint: You will need to determine the unspecified temperature from the first two listed equations.)
        
        # Cp is the average of inlet and outlet temperatures
        if self.given=="T_co":
            Cp=(self.T_co+self.T_ci)/2
            # something
        elif self.given=="T_ho":
            Cp=(self.T_ho+self.T_hi)/2
            # something else
        else:
            print("Something, somewhere, went horribly wrong.")
        return T
        
    def solveCost(self):
        # cost = $1000 * area (m^2)
        
        return cost
        
# Marcus        
    def output(self, area, T, cost):
        # Displays solutions all in SI units
        print("Surface Area=",area,"$m^2$")
        if self.given=="T_co":
            print("T_ho=",T,"K")
        else:
            print("T_co=",T,"K")
        print("Cost= $"+str(cost))
