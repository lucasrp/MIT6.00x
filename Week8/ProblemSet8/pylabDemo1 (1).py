"""Ploting several plots on the same graph """

import pylab as pl   # importing module for plotting

def f1(t):            # defining the first function to plot
	y= t**2*pl.exp(-t**2)
	return y
	
def f2(t):           # defining the second function to plot
	y = t**2*f1(t)
	return y
	
if __name__=='__main__':
	t = pl.linspace(0, 3, 51)         # create a set of  51 evenly spaced points in [0,3]
	y1 = f1(t)      
	y2 = f2(t)
	pl.plot(t, y1, 'r-')              # plot the first function with red (r) dashed lines (-)
	pl.hold('on')
	pl.plot(t, y2, 'bo')              # plot the second function with blue (b) circles (o)
	pl.xlabel('t')
	pl.ylabel('y')
	pl.legend(['t^2*exp(-t^2)', 't^4*exp(-t^2)'])
	pl.title('Plotting two curves in the same plot')
	pl.savefig("doubleplot.png")
	pl.show()

