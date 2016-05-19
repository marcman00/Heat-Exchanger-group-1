# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:28:12 2016

@author: Group 1
Project link here: http://apmonitor.com/che263/uploads/Main/heat_exchanger_project.pdf
"""
class HeatExchanger():
    
    def runAll():
    # Source functions, runs all the other functions
    
    ### Pseduocode shell
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
        
    def solveArea():
        # Calculates area from input
        
    def solveT():
        # calculates Tco or Tho (whichever one was NOT given in getInput() )
        
    def solveCost():
        # cost = $1000 * area (m^2)
        
    def output(area, T, cost):
        # Displays solutions all in SI units
        
