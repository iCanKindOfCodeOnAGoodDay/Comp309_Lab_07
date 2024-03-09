"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Lab #07
    Created on  Friday March 8 1600 2024   

    Description: 
        The program plots the time it takes to calculate the sin 
        using (1) built-in math and (2) numpy calculation on various problem sizes.
    
    Inputs: 
        
        PlotData(xData, yData, xAxisLab, yAxisLab, title)
        
            xData :
                List of Integers
                - problem sizes
                
            yDataMath : 
                List of Floats 
                - total time taken to perform calculation
                
            yDataNumpy : 
                List of Floats 
                - total time taken to perform calculation

    Returns: 
        none

    Dependencies: time, mathhplotlib.pyplot as plt, math, numpy  as np

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.3.1
"""

#----Import all modules

import time, math
import matplotlib.pyplot as plt
import numpy as np



 

#----Define All Functions

def PrintNameDateTime():
    
    """
    
    Description
    ----------  
    Prints dev name and current time/ date

    Parameters
    ----------
    None.
            
    Returns
    -------
    None.

    """
    
    print( "Scott Quashen", time.asctime() )
    
# end PrintNameDateTime


def createPlot( xData, yDataMath, yDataNumpy ):
    
    """
    
    Description
    ----------  
    createPlot() uses mathPlot to create a chart representing the time 
    taken to calculate sin using numpy vs. math on various problem sizes.

    Parameters
    ----------
        
        xData : 
            List of integers
            Our problem sizes
            
        yData : 
            List of floats
            Our y-axis values for plotting

    Returns
    -------
    None.

    """
    
    X = [ str( t ) for t in xData ] # string values for x ticks
    
    X_axis = np.arange( len( xData ) ) 
    
    plt.bar( X_axis - 0.2, yDataMath, 0.4, label='Math', color='red' )
    plt.bar( X_axis + 0.2, yDataNumpy, 0.4, label='Numpy', color='lightgreen' )
    
    plt.xticks( X_axis, X )    
    plt.title( "Numpy Vs. Built in Math Calculations" )
    plt.xlabel( 'Problem Size' )
    plt.ylabel( 'Time (seconds)' )
    plt.legend( [ "Math", "Numpy" ], loc=2 )    
    plt.savefig( "Scott Quashen_Lab_7.png", dpi=600 )   
    plt.show()

# end createPlot() func


def LoopAndTime(initialSize, problemSizesList, initialDx):
        
    """
    
    Description
    ----------  
    The LoopAndTime() func Calculates sin using numpy vs. math on various problem sizes, save results and pass them into our plot function.

    Parameters
    ----------
        
        initial size : 
            Integer
            Our N value
            
        problemSizeList : 
            List< Int >
            List of values that equate to our growing problem sizes
        initialDx :
            Float
            dx is the item that we add to our list via a calculation performed on each index within a problem size.
            
    Returns
    -------
    None.

    """
    
    timeMath = []
    timeNP = []
    
    #N = initialSize # doesn't need to be passed in

    problemSizes = problemSizesList
    dx = initialDx
    
    for nSize in problemSizes:
        
        a = np.zeros( nSize ) #create your np arrays

        #calculate your data values
        for i in range( nSize ):
            a[ i ] = dx = dx + ( 2 * np.pi ) / ( nSize - 1 )
                     
        startTime = time.time()                                      # start timing ---------------math 
                
        for b in range( nSize ):                                     # loop over data calling math.sin on each value
        
            math.sin( a[ b ] )
                
        stopTime = time.time()                                       # stop timing
        
        timeMath.append( stopTime - startTime )                      # append values
        
        startTime = time.time()                                      # start timing ---------------numpy 
        
        np.sin( a )                                                  # calculate the np.sin (in parallel)
        
        stopTime = time.time()                                       # stop timing
        
        timeNP.append( stopTime - startTime )                        # append values
                                           
    createPlot( problemSizes, timeMath, timeNP )                     # call plot passing results data into func

# end loopAndTime func


def main():
    
    """
    
    Description
    ----------  
    Our main() is the entry point to our program, holds our constants, and calls LoopAndTime() func

    Parameters
    ----------
    None.
            
    Returns
    -------
    None.

    """
        
    # Best to define your variables here.   
    N = 8192
    problemSizes = [ N, N * 4, N * 16, N * 64 ]
    dx = 0.0
    
    PrintNameDateTime()
    LoopAndTime( N, problemSizes, dx )    
    return None

# end of main function

 


#----Entry point

if __name__ == "__main__":
    main()
















