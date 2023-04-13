import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize = (6.6,5.0))

# Variables
L = 200e3         # Length from detector - m
EMin = 1.81         # Minimum energy - MeV
EMax = 12        # Maximum energy - MeV
N = 1000        # Number of data points

E = np.linspace(EMin,EMax,N)     # Energy range 
inverseE = np.linspace(1/EMax, 1/EMin, N)   # 1/E linear scale


thermalPower = 3e9   # Thermal power of reactors - 3 Gigawatts
P_th = thermalPower / 1.6e-19 / 1e6     # thermal power in MeV


Mn = 939.56542        # Mass of neutron - MeV
Mp = 938.27209        # Mass of proton - MeV
Me = 0.511            # Mass of electron - MeV

n = 6.69e31     # Number of protons in 1 KTon of water
tau = 2.63e6    # Exposure time (1 month)
coefficients = n * tau / (4 * np.pi * L**2)

neutrinos = []
neutrinosSum = []




m21 = 7.6e-5    # Solar mass splitting  NOTE THESE VALUES ARE SQUARED ALREADY
m31 = 2.5e-3    # Atmospheric mass splitting
m32 = 2.5e-3


# IBD cross section term

Ee = 1/inverseE - (Mn - Mp)    # Energy conservation
p = np.sqrt( Ee**2 - Me**2 )  # Relativistic mass conservation
crossSection = 0.0952e-42 * p * Ee




# Reactor neutrino emission rate dR/dE

#    U-235      U-238      Pu-239      Pu-241
P = [0.56,      0.08,      0.30,       0.06]     # Fraction of reactor power
Q = [202.4,     206.0,     211.1,      214.3]    # Average energy per fission - MeV

a0= [0.87,      0.976,     0.896,      0.793]    # Constants a0 a1 a2
a1= [-0.160,   -0.162,    -0.239,     -0.080]
a2= [-0.091,   -0.079,    -0.0981,    -0.1085]

def lambdas(I):
    return np.exp(a0[i] + a1[i] * I + a2[i] * (I ** 2))

for I in range(N):
#    I = (I / N * (EMax - EMin)) + EMin       # Energy range from EMin to EMax
    I = (I / N * (1/EMin - 1/EMax)) + 1/EMax    # Inverse E range
    
    for i in range(0,4):    # Iterates through isoptopes 0 1 2 3
        neutrinosSum.append(P[i] / Q[i] * lambdas(1/I) )  # Performs sum
        
    neutrinos.append(np.sum(neutrinosSum))  # Adds each energy iteration to output array
    neutrinosSum = []
    
neutrinos = np.array(neutrinos) * P_th




# Neutrino oscillation P(L,E)

delta21 = 1.27 * abs(m21) * L * inverseE
delta31 = 1.27 * abs(m31) * L * inverseE
delta32 = 1.27 * abs(m32) * L * inverseE

theta12 = 34 * np.pi / 180   # Solar mixing angle converted to radians
theta13 = 8.7 * np.pi / 180     # Reactor mixing angle converted to radians

term1 = (np.cos(theta13))**4 * (np.sin(2 * theta12))**2 * (np.sin(delta21))**2
term2 = (np.cos(theta12))**2 * (np.sin(2 * theta13))**2 * (np.sin(delta31))**2
term3 = (np.sin(theta12))**2 * (np.sin(2 * theta13))**2 * (np.sin(delta32))**2
prob =  (term1 + term2 + term3)




## Prewhitening the noise 

# Putting it all together
spectrum = np.zeros(N)
for j in range(N):
    spectrum[j] = coefficients * (1 - prob[j]) * crossSection[j] * neutrinos[j]
spectrum = spectrum / np.sum(spectrum) / ((EMax - EMin) / N)


# Prewhitening the noise 
spectrum = spectrum - spectrum.mean() 



# Fourier transform 21

LMin = 0        # Input length range (km)
LMax = 350 
Len = np.linspace(LMin*1e3 * 2,LMax * 1e3 * 2,N)
FT1 = np.zeros(N)


##
for w in range(N):
    summation = 0
    for s in range(N):
        summation += spectrum[s] * np.cos( (1.27 * m21 * Len[w]) * (inverseE[s]) )
    FT1[w] = summation
 
cosine = FT1

maxx = max(cosine[int(0.1 * N):])
maxy = np.where(cosine == maxx)

print(Len[maxy] / 2 / 1000)
# label = "$P_{21}$, L = 150.3 km")
#plt.plot(Len / 1000 / 2 , cosine, "green", label = "N(L,E), L = 150.3 km")









#prob = term1
### Prewhitening the noise 
#
## Putting it all together
#spectrum = np.zeros(N)
#for j in range(N):
#    spectrum[j] = coefficients * (1 - prob[j]) 
#spectrum = spectrum / np.sum(spectrum) / ((EMax - EMin) / N)
#
## Prewhitening the noise 
#spectrum = spectrum - spectrum.mean() 
#
## Fourier transform 31
#
#FT1 = np.zeros(N)
#
#for w in range(N):
#    summation = 0
#    for s in range(N):
#        summation += spectrum[s] * np.cos( (1.27 * m21 * Len[w]) * (inverseE[s]) )
#    FT1[w] = summation
# 
#cosine2 = FT1
#
#
#maxx = max(cosine[int(0.2 * N):])
#maxy = np.where(cosine == maxx)
#
#print("bbb", Len[maxy] / 2 / 1000)
#
#
##plt.plot(Len / 1000 / 2, cosine2, color='blue', label = "$P_{21}$, L = 149.0 km")





#
#
#prob = term2
### Prewhitening the noise 
#
## Putting it all together
#spectrum = np.zeros(N)
#for j in range(N):
#    spectrum[j] = coefficients * (1 - prob[j]) 
#spectrum = spectrum / np.sum(spectrum) / ((EMax - EMin) / N)
#
## Prewhitening the noise 
#spectrum = spectrum - spectrum.mean() 

## Fourier transform 31
#
#FT1 = np.zeros(N)
#
#for w in range(N):
#    summation = 0
#    for s in range(N):
#        summation += spectrum[s] * np.cos( (1.27 * m31 * Len[w]) * (inverseE[s]) )
#    FT1[w] = summation
# 
#cosine2 = FT1
#
#
#maxx = max(cosine[int(0.2 * N):])
#maxy = np.where(cosine == maxx)
#
#print(Len[maxy] / 2 / 1000)

#
##plt.plot(Len / 1000 / 2, cosine2, color='orange', label = "$P_{31}$, L = 149.0 km")
#
#
#prob = term3
### Prewhitening the noise 
#
## Putting it all together
#spectrum = np.zeros(N)
#for j in range(N):
#    spectrum[j] = coefficients * (1 - prob[j]) 
#spectrum = spectrum / np.sum(spectrum) / ((EMax - EMin) / N)
#
## Prewhitening the noise 
#spectrum = spectrum - spectrum.mean() 
#
##
#
## Fourier transform 32
#FT1 = np.zeros(N)
#
#for w in range(N):
#    summation = 0
#    for s in range(N):
#        summation += spectrum[s] * np.cos( (1.27 * m32 * Len[w]) * (inverseE[s]) )
#    FT1[w] = summation
# 
#cosine3 = FT1
#
#maxx = max(cosine[int(0.2 * N):])
#maxy = np.where(cosine == maxx)
#
#print(Len[maxy] / 2 / 1000)
#
##plt.plot(Len / 1000 / 2, cosine3, "r", label = "$P_{32}$, L = 149.0 km")
#

# Putting it all together
spectrum = np.zeros(N)
for j in range(N):
    spectrum[j] = coefficients * 1 * crossSection[j] * neutrinos[j]
spectrum = spectrum / np.sum(spectrum) / ((EMax - EMin) / N)
# Prewhitening the noise 
spectrum = spectrum - spectrum.mean() 

# Fourier transform non osc.
FT1 = np.zeros(N)

for w in range(N):
    summation = 0
    for s in range(N):
        summation += spectrum[s] * np.cos( ( 1.27 * m21 * Len[w]) * (inverseE[s]) )
    FT1[w] = summation
 
cosine1 = FT1

spe =  cosine - cosine1

maxx = max(spe)
maxy = np.where(spe == maxx)

print(Len[maxy] / 2 / 1000)

plt.plot(Len / 2e3 , cosine / max(cosine), color="k", linestyle="solid", label = r"L = 200 km")

plt.plot(Len / 1000 / 2, cosine1 / max(cosine), color="r", linestyle='dashed', label = "No Oscillations")

#plt.plot(Len / 1000 / 2, cosine/max(cosine) - cosine1/max(cosine), "darkblue", label = r"$f(E_{\bar{v}}|L=150)$ - unoscillated", alpha = 0.9)


plt.xlim([0,350])
plt.ylim(-1.2,1.4)
#plt.xlim(0,350 * 1.27 * m21 * 20)

plt.ylabel("Amplitude", fontsize = 15)
plt.plot(102 + np.zeros(40),np.linspace(-1.2,0.85,40), linestyle="dotted", linewidth = 1, color = "r")
plt.plot(202 + np.zeros(40),np.linspace(-1.2,0.87,40), linestyle="dotted", linewidth = 1, color = "k")
#plt.plot(149 + np.zeros(40),np.linspace(-0.8,0.68,40), "--", linewidth = 1, color = "blue", alpha = 0.9)

#plt.xlabel("Calculated range to detector (km)", fontsize = 14)
plt.xlabel("Distance (km)", fontsize = 15)
#plt.xlabel("$1.27 \Delta m_{mn}^2 L$", fontsize = 14)
#plt.xlim(0,520)
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)
plt.legend(fontsize=15)
plt.savefig("FCT-osc-sub_v2.pdf", bbox_inches='tight')
plt.show()