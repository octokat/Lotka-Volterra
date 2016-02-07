import numpy
import pylab


pylab.figure(1)
clf()

dt = 0.1
x_0 = 10 #This is the initial number of prey species
y_0 = 5  #This is the initial number of predators

#The constants are included in the terms of the two Ordinary Differential
# equations that describe the population dynamics of this predator/prey system 
# as follows, where dx_dt is the rate of change of prey, dy_dt is the rate
# of change of predators, x is the amount of prey, and y is the amount of predators
    
    # dx_dt = x(A - By)
    # dy_dt = -y(C - Dx)

# Since unlimited food is assumed, Ax is the terms assoc. with the exponential 
# growth of the prey (thus A is the rate of growth).  -Byx is terms associated 
# with the rate of predidation. Thus B is the parameter would change is the 
# predators got better at hunting.

# Dxy is the growth rate of the predator population (thus D is that rate of growth).
# If the prey got bigger, yielding more calories to the predators, D is the parameter
# that would change.
# Lastly, the -yC term represents the loss rate of predators due to natural death or
# emigration, for example (thus C is that rate of death).

A = 0.5 
B = 0.2
C = 0.3
D = 0.02

# Note: x[0] is the amount of prey species at a given moment in time and 
# x[1] is likewise the corresponding amount of predators at that time. 

def Lotka_Volterra(x, t):
    dx_dt = x[0]*(A - B*x[1])
    dy_dt = -x[1]*(C - D*x[0])
    res = [dx_dt, dy_dt]   # Creating a list to hold the associated values (x[0],x[1]) 
    res = numpy.array(res)  # Converting that list to an array
    return res
    
def density_dep_growth(x, t):
    return x*(1-x)

def euler_richardson(f, t_n, x_n, dt):
    t_n = t_n + (dt/2)
    x_m = x_n + f(x_n,t_n)*(dt/2)
    x = x_n + f(x_m,t_n)*(dt)
    return x
    
# This last bit of code creates two arrays that make plotting the data easy: 
# x holds the tuples of data that are the amount of prey x[0] and the amount 
# of predators x[1] for a given time step, and t holds the time steps. The main
# trick was that the data needed to be the same size in order to run the program,
# so I used the calls .reshape and x.shape[1] (the dimension of element 1 in array x) 
# to reformatt the raw form of data coming from calling euler on Lotka_Volterra.
    
t_end = 100
t = [0]
x = [[x_0,y_0]]
x = numpy.array(x)
while t[-1] <= t_end:
    x = numpy.append(x, euler(Lotka_Volterra, t[-1], x[-1], dt).reshape(1,x.shape[1]), axis=0)
    t.append(t[-1] + dt)

pylab.plot(t, x[:,0])
pylab.plot(t, x[:,1])

pylab.xlabel('Time (note: dt = 0.1)')
pylab.ylabel('Amount of Individuals in the Population')
pylab.title('Population Fluctuations Over Time - Lotka-Volterra')
pylab.grid(True)
pylab.legend(['Prey Population','Predator Population'])