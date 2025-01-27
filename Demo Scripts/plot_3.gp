#https://thetimetube.herokuapp.com/gnuplotviewer/

#set terminal svg enhanced font "Arial,13"

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
set style line 1 linecolor rgb "#E41A1C" lw 2 pt 7 ps 1 # Red (Circle)
set style line 2 linecolor rgb "#377EB8" lw 2 pt 5 ps 1 # Blue (Square)
set style line 3 linecolor rgb "#4DAF4A" lw 2 pt 9 ps 1 # Green (Triangle)
set style line 4 linecolor rgb "#FF7F00" lw 2 pt 11 ps 1 # Orange (Star)
set style line 5 linecolor rgb "#984EA3" lw 2 pt 13 ps 1 # Purple (Diamond)
set style line 6 linecolor rgb "#A65628" lw 2 pt 6 ps 1 # Brown (Cross)
#-----------------------------------------------------------------

# Mandatory
set title 'Name/ID : Full Name / 2023B5PS000P'
 

set key top left  Left width -2
set grid

set xlabel 'X-label First Plot'
set ylabel 'Y-label First Plot'

set autoscale 
#set xrange[0:10] 
#set yrange[-1:1]

f(x,a,b) = a * x + b 

fit f(x,a,b) 'file_two_set.dat' u 1:3 i 1:1 via a,b

print "a = ", a;
print "b = ", b; 
 
plot 'file_two_set.dat' using 1:3 i 1:1 title 'Exp Data' w p ls 1,\
f(x,a,b) t 'Fitted Data' w l ls 2
 
