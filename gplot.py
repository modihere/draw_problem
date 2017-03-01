import numpy as np
import scipy as sp 
import math
import time
import random
import Gnuplot

data1=[[0,0],[1,1],[2,2],[3,3],[5,5]]
gp1=Gnuplot.Gnuplot(persist =1)
gp1('set terminal x11 size 350,350')
gp1('set pointsize 3')
gp1('set font "Times-Roman, 30"')
gp1('set xlabel "x-axis"')
gp1('set ylabel "y-axis"')
gp1('set xrange [0:6]')
gp1('set yrange [0:20]')
plot1 = Gnuplot.PlotItems.Data(data1, with_="lines" ,title='d1')
gp1.plot(plot1)
epsFilename ='t.eps'
gp1.hardcopy(epsFilename, terminal = 'postscript',color=1)
gp1.reset()