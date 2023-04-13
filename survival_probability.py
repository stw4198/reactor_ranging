import numpy as np
import matplotlib.pyplot as plt

colours = ['#66CCEE','#CCBB44','k','#EE6677']
Tol_bright = ['#4477AA','#66CCEE','#228833',
            '#CCBB44','#EE6677','#AA3377','#BBBBBB','k']
linestyles = ['dashdot','dashed','dotted','solid']

#//----------------------------------------------------------------------------------------------------------------------//
#//Defining the functions used to generate the Probability Distribution Functions from theory

#//Flux: thi(E)

def U_l(energy):
    ul = 0.7248*np.exp(3.217-3.111*energy+1.395*energy**2-0.369*energy**3+0.04445*energy**4-0.002053*energy**5)
    return ul

def U_h(energy):
    uh = 0.042*np.exp(0.4833+0.1927*energy-0.1283*energy**2-0.06762*energy**3+0.002233*energy**4-0.0001536*energy**5)
    return uh

def Pu_l(energy):
    pul = 0.2127*np.exp(6.413-7.432*energy+3.535*energy**2-0.8820*energy**3+0.1025*energy**4-0.00455*energy**5)
    return pul

def Pu_h(energy):
    puh = 0.0205*np.exp(3.251-3.204*energy+1.428*energy**2-0.3675*energy**3+0.04254*energy**4-0.001896*energy**5)
    return puh

def Phi(ul,uh,pul,puh):
    return (ul + uh + pul + puh)

#//Cross-Section: sigma(E)
me = 0.51099895#;//MeV
delta = 939.56542052 - 938.27208816#;//MeV

q_ibd = (939.56542052 + 0.51099895) - 938.27208816#;//MeV

def Ee(energy,q_ibd):
    ee = energy - q_ibd
    return ee
    
def Pe(ee,me):
    pe = np.sqrt(ee**2 - me**2)
    return pe

def Sigma(ee, pe):
    sigma = ee*pe
    return sigma

#//oscillations: P(E)
theta_13 = 0.15#;//rad
theta_12 = 0.59#;//rad

#//Normal mass ordering
m_21 = 7.39e-5#;//eV^2
m_31 = 2.52e-3#;//eV^2
m_32 = 2.45e-3#;//eV^2

def P21(l,e):
    p21 = (np.cos(theta_13))**4 * (np.sin(2*theta_12))**2 * (np.sin(1.27*m_21*l/(e/1000)))**2
    return p21

def P31(l,e):
    p31 = (np.cos(theta_12))**2 * (np.sin(2*theta_13))**2 * (np.sin(1.27*m_31*l/(e/1000)))**2
    return p31

def P32(l,e):
    p32 = (np.sin(theta_12))**2 * (np.sin(2*theta_13))**2 * (np.sin(1.27*m_32*l/(e/1000)))**2
    return p32
    
def P(p21,p31,p32):
    p = 1-p21-p31-p32
    return p

#//Combined function F(L/E):

def reactor_func(sig,flux,osc):
    func = sig*flux*osc
    return func

energy = np.linspace(q_ibd,10,220)
l = 26

reactor_data = []
phi_data = []
sigma_data = []
p_data = []
p21_data = []
p31_data = []

for i in range(len(energy)):
    ul=U_l(energy[i])
    uh=U_h(energy[i])
    pul=Pu_l(energy[i])
    puh=Pu_h(energy[i])
    phi=Phi(ul,uh,pul,puh)
    phi_data.append(phi)

    ee=Ee(energy[i],q_ibd)
    pe=Pe(energy[i],me)
    sigma=Sigma(ee,pe)
    sigma_data.append(sigma)

    p21=P21(l,energy[i])
    p31=P31(l,energy[i])
    p32=P32(l,energy[i])
    p=P(p21,p31,p32)
    p21_data.append(p21)
    p31_data.append(p31)
    p_data.append(p)

    func=reactor_func(sigma,phi,p)
    reactor_data.append(func)

l = np.linspace(0,200,10001)
energy = 4

reactor_data = []
phi_data = []
sigma_data = []
p_data = []
p21_data = []
p31_data = []

for i,v in enumerate(l):

    ul=U_l(energy)
    uh=U_h(energy)
    pul=Pu_l(energy)
    puh=Pu_h(energy)
    phi=Phi(ul,uh,pul,puh)
    phi_data.append(phi)

    ee=Ee(energy,q_ibd)
    pe=Pe(energy,me)
    sigma=Sigma(ee,pe)
    sigma_data.append(sigma)

    p21=P21(v,energy)
    p31=P31(v,energy)
    p32=P32(v,energy)
    p=P(p21,p31,p32)
    p21_data.append(p21)
    p31_data.append(p31)
    p_data.append(p)

    func=reactor_func(sigma,phi,p)
    reactor_data.append(func)

plt.plot(l,(1-np.array(p31_data))/(max(1-np.array(p31_data))),color='b',linestyle='--',label=r'$\theta_{13}$')
plt.plot(l,(1-np.array(p21_data))/(max(1-np.array(p21_data))),color='k',linestyle=':',label=r'$\theta_{12}$')
plt.plot(l,p_data/np.max(p_data),color='r',label=r'Total')
plt.legend(fontsize=12)
plt.xticks(fontsize=12, rotation=0)
plt.yticks(fontsize=12, rotation=0)
plt.xlabel('Distance [km]',fontsize=14, fontweight='bold')
plt.ylabel(r'P$_{\bf{\bar{{\nu}}_e\rightarrow\bar{{\nu}}_e}}$',fontsize=14, fontweight='bold')
plt.xscale('log')
plt.savefig('survival_prob.png',dpi=1200)
plt.show()

