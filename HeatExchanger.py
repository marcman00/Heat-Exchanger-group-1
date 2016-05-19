# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:28:12 2016
Due on 
@author: Group 1
Project link here: http://apmonitor.com/che263/uploads/Main/heat_exchanger_project.pdf
"""
class HeatExchanger():
    # Variables that are given in getInput() and then used in another function are declared here
    units=""    # aes or si
    U=0         # Heat Transfer Coefficient
    Tci=0       # T cold fluid, in
    Thi=0       # T hot fluid, in
    mc=0        # flow rate cold fluid
    mh=0        # flow rate hot fluid
    cold=""     # options given below in input
    hot=""      # options given below in input
    given=""    # Tco or Tho
    Cp=0        # Heat capacity
    
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
        # All variables are set here.
        # Note that cp is the average of inlet and outlet temperatures
    """user can specify:
            aes or si units
            U, Tci, Thi, mc, mh, Tco or Tho
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
        
    def solveT():
        # calculates Tco or Tho (whichever one was NOT given in getInput() )
        # (Hint: You will need to determine the unspecified temperature from the first two listed equations.)
        if given=="Tco":
            cp=(Tco+Tci)/2
            # something
        else:
            cp=(Tho+thi)/2
            # something else
        
    def solveCost():
        # cost = $1000 * area (m^2)
        
# Marcus        
    def output(area, T, cost):
        # Displays solutions all in SI units
        print("Surface Area=",area,"$m^2$")
        if given=="Tco":
            print("$T_ho$=",T,"K")
        else:
            print("$T_co$=",T,"K")
        print("Cost= $"+str(cost))
