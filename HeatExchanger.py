# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:22:25 2016

@author: Marcus Reynolds, Dan Addington, Gabriel Poulson
"""
import sys
from Fluid import Fluid
import sympy as sp

class HeatExchanger:
    
    def __init__(self):        
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
        self.t_xo=0      # output temperature of the known stream
        
# Marcus
    # Runs all the other functions
    def runAll(self):
        fluids=Fluid()
        self.C=fluids.getInfo()
        self.getInput()        
        print("Calculating...\n")        
        T=self.solveT()
        area=self.solveArea(T)
        cost=self.solveCost(area)
        self.output(area,T,cost)
   
# Gabriel
   # gets all the input variables
    def getInput(self):
        self.getUnits()
        one = self.getSubstance("1")
        print()
        two = self.getSubstance("2")
        if one[2]>two[2]:
            self.hot=self.liquidToNumber(one[0])
            self.cold=self.liquidToNumber(two[0])
            self.m_h=one[1]
            self.T_hi=one[2]
            self.m_c=two[1]
            self.T_ci=two[2]
        else:
            self.cold=self.liquidToNumber(two[0])
            self.hot=self.liquidToNumber(one[0])
            self.m_h=two[1]
            self.T_hi=two[2]
            self.m_c=one[1]
            self.T_ci=one[2]
            
        try:
            if self.units=="AES":
                self.U=self.convertU(float(input("U (Btu/ft^2*hr*F)= ")))
            else:
                self.U=float(input("U (J/s*m^2*K)= "))
        except:
            self.throwError()
        self.isValid(self.U)
        self.getTempOut()
        if self.t_xo>self.T_hi or self.t_xo<self.T_ci:
            self.throwError()    
    # Lets user choose between AES and SI units
    def getUnits(self):
        while self.units != "AES" and self.units != "SI":
            self.units = input("What measurement system would you like to use? ('AES' or 'SI'): ").upper()
            if self.units != "SI" and self.units != "AES":
                print("Error, input 'AES' or 'SI'")
            #print error and restart function if not AES or SI
       
    
    # Gets a liquid type, mass flow rate, and temperature
    def getSubstance(self,number):
        print("-- Liquid",number+" --")
        print("The available fluids are Water, R134a, Ethanol, 2,2,4-trimethylpentane")
        print("Use 'W', 'R134a', 'Ethanol', or 'TMP'")
        liquidType=""
        while liquidType !="W" and liquidType !="R134A" and liquidType !="ETHANOL" and liquidType !="TMP":
          liquidType = input("What substance?: ").upper()
          if liquidType !="W" and liquidType !="R134A" and liquidType !="ETHANOL" and liquidType !="TMP":
              print("Error. Try again. Use 'W', 'R134a', 'Ethanol', or 'TMP'")
              #print error and restart function if not one of possible liquid types
              
        massFlow=self.getMassFlow()
        self.isValid(massFlow)
        tempIn=self.getTempIn()         # returns temperature in K
        self.isValidTemp(self.liquidToNumber(liquidType),tempIn)
         # return variables for this liquid as an array
        return [liquidType,massFlow,tempIn]
        
    # converts the type of liquid to a number for later use in a fluid array
    def liquidToNumber(self,liquid):
        if liquid=="W":
            return 0
        elif liquid=="R134A":
            return 1
        elif liquid=="ETHANOL":
            return 2
        elif liquid=="TMP":
            return 3
        else:
            self.throwError()
            
   # throws an error and exits the program             
    def throwError(self):
         print("Error, invalid input. Exiting program.\n")
         sys.exit()
    # checks if the temperature of given fluid is below freezing or above boiling point
         
    def isValidTemp(self,liquid,temp):
        if temp>=self.C[liquid].BP or temp<=self.C[liquid].MP:
                self.throwError()
                
    # gets the mass flow rate for a fluid        
    def getMassFlow(self):
        try:
            if self.units=="AES":
                m = float(input("Please define a flow rate (lbs/s): "))
                m = m * 0.453592 #kg/s
            else:
                m = float(input("Please define a flow rate (kg/s): "))
        except:
            self.throwError()
        return m
        
    # gets the temperature for a fluid    
    def getTempIn(self):
        try:
            if self.units=="AES":
                temp = float(input("Please enter a temperature (degrees F): " ))
            else:
                temp = float(input("Please enter a temperature (degrees K): "))
            return self.convertTemp(temp)
        except:
            self.throwError()
            
    # gets the type and temperature of the known out fluid        
    def getTempOut(self):
        out=""
        while out!="cold" and out!="hot":
            out=input("Which fluid temperature are you solving for? ('hot' or 'cold'): ").lower()            
            
        if self.units=="AES":
            unit="F"
        else:
            unit="K"
        try:    
            if out=="hot":
                t_xo=float(input("Choose an outlet temperature for your cold fluid (degrees "+unit+"): "))      
                self.given="cold"
            else:
                t_xo=float(input("Choose an outlet temperature for your hot fluid (degrees "+unit+"): "))
                self.given="hot"
            self.t_xo=self.convertTemp(t_xo)
        except:
            self.throwError()
            
     # converts F to K if needed       
    def convertTemp(self,temp):
        if self.units=="AES":
            return ((temp + 459.67) * (5/9))
        else:
            return temp
    
    # converts lbs/s to kg/s if needed        
    def convertMassFlow(self,m):
        if self.units=="AES":
            return m*0.453592
        else:
            return m
            
    # converts AES U to SI U        
    def convertU(self,u):
        if self.units=="AES":
            return u*5.6784
        else:
            return u
    
    # Checks to see if a value is 0 or negative
    def isValid(self,value):
            if value<=0:
                self.throwError()

       
    def solveCp(self):
        Thi=self.T_hi
        Tci=self.T_ci
        C=self.C
        k=self.cold
        j=self.hot
        
        T_out=self.t_xo
        if self.given == "hot":
            
            #Calculates Heat Capacity determined by Temperature-out of the hot fluid
            Th_avg = (Thi+T_out)/2
            
            def Cph(j,Th_avg):  #j = compound number of hot fluid, and T is change in temperature in Kelvin
                heat_capacity_h = C[j].A + C[j].B*Th_avg + C[j].C*Th_avg**2 + C[j].D*Th_avg**3 + C[j].E*Th_avg**4
                return heat_capacity_h/1000       #converts from J/kmol to J/mol
            return Cph(j, Th_avg)
        
        else:
            #Calculates Heat Capacity determined by Temperature-out of the cold fluid
            Tc_avg = (Tci + T_out)/2
            
            def Cpc(k,Tc_avg): #k = compound number of cold fluid, and T is change in temperature in Kelvin
                heat_capacity_c = C[k].A + C[k].B*Tc_avg + C[k].C*Tc_avg**2 + C[k].D*Tc_avg**3 + C[k].E*Tc_avg**4
                return heat_capacity_c/1000
            return Cpc(k, Tc_avg)


    def solveT(self):
        
        #call variables
        Tci=self.T_ci
        Thi=self.T_hi
        mc=self.m_c
        mh=self.m_h
        C=self.C
        k=self.cold
        j=self.hot
        T_out=self.t_xo
        
        
        if self.given == "hot":
            
            #Call Variables
            Tho = T_out

            #Solves for Heat Transfer Rate 'q'
            q_h = 1000*mh*(1/C[j].Mol_Wt)*self.solveCp()*(Thi-Tho)   # note that q_h = q_c (q_c = mc*Cpc(k,Tc_avg)*(Tco-Tci))    
            #Multiplied by a thousand to convert kilograms to grams. Make sure that Gabriel hasn't already solved this!!!!!!!!
    
            #solve polynomial equation with one variable (variable = Tc_avg) by setting equation equal to zero
            #0 = 2*mc*(C[k].A + C[k].B*Tc_avg + C[k].C*Tc_avg**2 + C[k].D*Tc_avg**3 + C[k].E*Tc_avg**4)*(Tc_avg - Tci) - q_h
            Tc_avg = sp.Symbol('Tc_avg')
            y = sp.solve(2*mc*(C[k].A + C[k].B*Tc_avg + C[k].C*Tc_avg**2 + C[k].D*Tc_avg**3 + C[k].E*Tc_avg**4)*(Tc_avg-Tci) - q_h, Tc_avg)
            Tc_avg = y[0]
            
            
            #Calculates Heat Capacity determined by average Temperature of the cold fluid
            def Cpc(k,Tc_avg): #k = compound number of cold fluid, and T is change in temperature in Kelvin
                heat_capacity_c = C[k].A + C[k].B*Tc_avg + C[k].C*Tc_avg**2 + C[k].D*Tc_avg**3 + C[k].E*Tc_avg**4
                return heat_capacity_c/1000
            
            #Calculates the Temparture-out of the cold fluid
            Tco = mh*self.solveCp()*(Thi-Tho)/(mc*Cpc(k, Tc_avg)) + Tci
            return Tco
            
            
        else:
            #Call varibles
            Tco = T_out
            
            #Solve for Heat Transfer Rate 'q'
            q_c = 1000*mc*(1/C[k].Mol_Wt)*self.solveCp()*(Tco-Tci) # note that q_h = q_c (q_h = mh*Cph(j,Th_avg)*(Thi-Tho))    
            #Multiplied by a thousand to convert kilograms to grams
            
            #solve polynomial equation with one variable (variable = Th_avg) by setting equation equal to zero
            #0 = 2*mc*(C[j].A + C[j].B*Th_avg + C[j].C*Th_avg**2 + C[j].D*Th_avg**3 + C[j].E*Th_avg**4)*(Th_avg - Tci) - q_h
            Th_avg = sp.Symbol('Th_avg')
            z = sp.solve(2*mh*(C[j].A + C[j].B*Th_avg + C[j].C*Th_avg**2 + C[j].D*Th_avg**3 + C[j].E*Th_avg**4)*(Thi-Th_avg) - q_c, Th_avg)
            Th_avg = z[0]
            
            #Calculates Heat Capacity determined by average Temperature of the hot fluid
            def Cph(j,Th_avg): #j = compound number of hot fluid, and T is change in temperature in Kelvin
                heat_capacity_h = C[j].A + C[j].B*Th_avg + C[j].C*Th_avg**2 + C[j].D*Th_avg**3 + C[j].E*Th_avg**4
                return heat_capacity_h/1000
            
            #caluclates the Temperature-out of the hot fluid
            Tho = -mc*self.solveCp()*(Tco-Tci)/(mh*Cph(j,Th_avg)) + Thi
            return Tho
            

        
#Solve for the Surface Area
    def solveArea(self,T): # T is the unspecified temperature in the beginning
        #Call variables
        U=self.U
        Tci=self.T_ci
        Thi=self.T_hi
        mc=self.m_c
        mh=self.m_h
        C=self.C
        k=self.cold
        j=self.hot
        T_out=self.t_xo
        
        if self.given == "hot":
            Tho = T_out
            Tco = T
            
        else:
            Tho = T
            Tco = T_out
        
        
        q_h = 1000*mh*(1/C[j].Mol_Wt)*self.solveCp()*(Thi-Tho)
        
        #Correction Factor 'F' as a function of 'R' and 'P'
        R = (Thi-Tho)/(Tco-Tci)
        P = (Tco-Tci)/(Thi-Tci)
        
        F_part1 = (((R**2 +1.)**(0.5))/(R-1))
        F_part2 = sp.log((1.-P)/(1.-P*R))
        F_part3 =  sp.log((2.-P*(R+1.-((R**2 +1.)**(0.5))))/(2.-P*(R+1+((R**2 +1.)**(0.5)))))
        F = F_part1 * (F_part2/F_part3)
    
        #Log Mean Temperature Difference
        dT1 = Thi - Tco
        dT2 = Tho - Tci
        T_logmean = (dT2 - dT1)/sp.log(dT2/dT1)
    
        
        #Caluclate and Return Area
        
        area = q_h/(F*U*T_logmean) #m^2
        return (area)
                
    #Solve for the Cost
    def solveCost(self,area):
        # cost = $1000 * area (m^2)
        cost = 1000*area  # $ in USD
        try:
            cost = float("{0:.2f}".format(cost))
            return (cost)
        except:
            self.throwError()

# Marcus
    # Displays all solved information   
    def output(self, area, T, cost):
        # Displays solutions
        T=float("{0:.3f}".format(T))
        area=float("{0:.3f}".format(area))
        if self.units=="AES":
            areaUnits="ft^2"
            tempUnits="F"
            T=(T*9/5) - 459.67
            area=area*10.76
        else:
            areaUnits="m^2"
            tempUnits="K"
        print("Surface Area=",area,areaUnits)
        if self.given=="T_co":
            print("T_ho=",T,tempUnits)
        else:
            print("T_co=",T,tempUnits)
        print("Cost= $"+str(cost))
###############################################################################      
heat=HeatExchanger()
heat.runAll()
