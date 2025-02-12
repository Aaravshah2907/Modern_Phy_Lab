#https://thetimetube.herokuapp.com/gnuplotviewer/

set terminal svg enhanced font "Arial,16"
set datafile separator ","
set output 'Experimental_graph.svg'

# Physical Constant 
c = 299792458.0 # Speed of light 
me = 9.10938291e-31 # Electron's mass
mp = 1.67262164e-27 # Proton mass
e = 1.60217657e-19 # Electron charge
h = 6.62607e-34 # Planck's constant
hbar = h/(2*pi) 
kb = 1.38064852e-23 # Boltzmann constant
eps0 = 8.85418781762039e-12 # Permitivity of free space
mu0 = 4*pi*1e-7 # Permiability of free space
a0 = 4*pi*eps0*hbar**2/(me*e**2) # Bohr Radius
alpha = e**2/(4*pi*eps0*hbar*c) # Fine strcuture constant
hartee = me*c**2 * alpha**2/e

#-----------------------------------------------------------------
#Line Styles

set style line 1 linecolor rgb "#E41A1C" lw 2 pt 7 ps 0.2 # Red (Circle)
set style line 2 linecolor rgb "#377EB8" lw 2 pt 7 ps 0.2 # Blue (Square)
set style line 3 linecolor rgb "#4DAF4A" lw 2 pt 7 ps 0.2 # Green (Triangle)
set style line 4 linecolor rgb "#FF7F00" lw 2 pt 7 ps 0.2 # Orange (Star)
set style line 5 linecolor rgb "#984EA3" lw 2 pt 13 ps 1.5 # Purple (Diamond)
set style line 6 linecolor rgb "#A65628" lw 2 pt 6 ps 1.5 # Brown (Cross)
#-----------------------------------------------------------------

# Mandatory
set title 'Name/ID : AARAV ANKIT SHAH / 2023B5AD1325P'

set key top right  Left width -4
set grid

set ylabel "Potential U(V))"
set xlabel "Current Squared I(A^2)"

# Either set autoscale or custom range (default- autoscale)
#set autoscale 
set xrange[0:17] 
set yrange[150:180]

#Calculate(x) = me * x / mp # User define function

#set label "B = 400 Gauss" at 3,20

plot 'experimental_readings.csv' using 6:1 title 'd = 2 cm' w lp ls 1,\
'experimental_readings.csv' using 7:1 title 'd = 3 cm' w lp ls 2,\
'experimental_readings.csv' using 8:1 title 'd = 4 cm' w lp ls 3,\
'experimental_readings.csv' using 9:1 title 'd = 5 cm' w lp ls 3,\