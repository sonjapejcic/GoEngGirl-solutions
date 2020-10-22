#Import Libraries (external ready-built code from other sources that we don't have to re-write)
import numpy as np
import astropy as ap
import math
from matplotlib import pyplot as plt

#This is next section of code is called a function by the keyword 'def' or define
#The name of the function is 'get_ellipse'
#It takes two inputs 'major', and 'e' (e is an optional parameter, if its not given then it's default value is 0)
def get_ellipse(major, e=0):
    '''This function returns the coordinate x and y positions of an ellipse (with the focus at the origin (0,0)) 
    given the length of its semi-major axis and eccentricity. We assume that the semi-major axis is along the x-axis'''
    
    #we are going to "parameterize" the equation such that x and y are now functions of theta 
    #(don't worry if you dont know what that means)
    theta = np.linspace(0, 2*np.pi, 100)  
    #calculating the "focus" of the ellipse
    focal = major*e
    #calculation the semi-minor axis
    minor = math.sqrt((major**2) - (focal**2))
    #now finally we can 
    x = major*np.cos(theta)
    y = minor*np.sin(theta)
    #Here is our outputs! (by keyword "return")
    return x+focal, y 
#(note that we returned x+focal not just x -> this is because we want to shift the ellipse so that the focus is at (0,0)


def plot_orbit(major, e, color, ax, max_major=0, label=''):
    '''This function plots an ellipse given its semi-major axis, eccentricity, plot color and figure axis.
    Optionally, you can set the maximum x and y limits using max_major and label your ellipses'''
    
    #checking for invalid enteries of e
    if e>1 or e<0:
        print('INVALID VALUE - Remember that e has to be between 0 and 1!')
        return # exit out of function if invalid input (note that there is no output in this case)
    #Here we call our previous function! This is a good way to break up code into smaller bit-size chunks 
    x, y = get_ellipse(major, e) 
    
    #Now we are ready for plotting! 
    #Given that the plot figure is already defined, we can pass the function acess to the plot through the 'ax' axis parameter
    #from library of 'matplotlib'
    ax.grid(True, linewidth=0.2)                    # Setting the plot to have a grid
    ax.scatter(0, 0, color='yellow', s=2**9)        # Adding a yellow circle marker for the sun
    ax.plot(x, y, color=color, label=label)         # Plotting the ellipse with the given color and label (for legend)
    ax.set_xlabel('Distance from Sun (AU)')         # Setting the x-axis label
    if np.max(x) > max_major:                       # Setting the axis limits such that the largest ellipses fits
        max_major = np.max(x)                       # We determint the maximum value of the ellipse on the x-axis
        ax.set_xlim(-1.2*max_major, 1.2*max_major)  # We set limits slightly bigger and smaller than the max value (i.e max*1.2)
        ax.set_ylim(-1.2*max_major, 1.2*max_major)  
#And we're done! Notice we dont have to 'return' this time since we did not calculate anything. We only updated our plot 