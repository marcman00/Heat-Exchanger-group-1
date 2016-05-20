# -*- coding: utf-8 -*-
"""
Due on Tue May 31 9:00am
@author: Group 1-- Marcus Reynolds, Gabriel Poulson, Dan Addington
Project link here: http://apmonitor.com/che263/uploads/Main/heat_exchanger_project.pdf
"""
class HeatExchanger():
    # Variables that are given in getInput() and then used in another function are declared here
    units=""    # aes or si
    U=0         # Heat Transfer Coefficient
    T_ci=0       # T cold fluid, in
    T_hi=0       # T hot fluid, in
    m_c=0        # flow rate cold fluid
    m_h=0        # flow rate hot fluid
    cold=""     # options given below in input
    hot=""      # options given below in input
    given=""    # T_co or T_ho
    
    def __init__(self):
        # Constructor, starts everything
        import numpy as np
        import sys
        runAll()
# Marcus    
    def runAll():
    # Source functions, runs all the other functions
        getInput()
        T=solveT()
        area=solveArea()
        cost=solveCost(area)
        output(area,T,cost)
   
# Gabriel
    def getInput():
        # Variables are set here.
    """user can specify:
            aes or si units
            U, T_ci, T_hi, m_c, m_h, T_co or T_ho
            Cold: water or 1,1,1,2-Tetrafluoroethane or ethanol or 2,2,4-trimethylpentane
            Hot: same options as cold
    """
    
    def isValid(value):
        # checks if a number is negative. If so, returns error message and exits program.    
        
    def convertUnits(value):
        # convert AES to SI units
# Dan        
    def solveArea():
    # Calculates area from input
    
        return area
        
    def solveT():
    # calculates Tco or Tho (whichever one was NOT given in getInput() )
        # (Hint: You will need to determine the unspecified temperature from the first two listed equations.)
        # Cp is the average of inlet and outlet temperatures
        if given=="T_co":
            Cp=(T_co+T_ci)/2
            # something
        else:
            Cp=(T_ho+T_hi)/2
            # something else
        return T
        
    def solveCost():
        # cost = $1000 * area (m^2)
        
        return cost
        
# Marcus        
    def output(area, T, cost):
        # Displays solutions all in SI units
        print("Surface Area=",area,"$m^2$")
        if given=="T_co":
            print("T_ho=",T,"K")
        else:
            print("T_co=",T,"K")
        print("Cost= $"+str(cost))
