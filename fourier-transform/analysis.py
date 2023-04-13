import numpy as np
import matplotlib.pyplot as plt

#Read in data
folder = "/home/stw4198/Documents/WATCHMAN/ranging/reactor_ranging_code/paper/ranging_data/heysham_2"
heyx_e, heyy_e = np.loadtxt(folder+"/heysham_2_e.txt",delimiter=',',unpack=True)
heyx_r, heyy_r = np.loadtxt(folder+"/heysham_2_r.txt",delimiter=',',unpack=True)
torx_e, tory_e = np.loadtxt(folder+"/torness_e.txt",delimiter=',',unpack=True)
torx_r, tory_r = np.loadtxt(folder+"/torness_r.txt",delimiter=',',unpack=True)
sizex_e, sizey_e = np.loadtxt(folder+"/sizewell_b_e.txt",delimiter=',',unpack=True)
sizex_r, sizey_r = np.loadtxt(folder+"/sizewell_b_r.txt",delimiter=',',unpack=True)
hinkx_e, hinky_e = np.loadtxt(folder+"/hinkley_c_e.txt",delimiter=',',unpack=True)
hinkx_r, hinky_r = np.loadtxt(folder+"/hinkley_c_r.txt",delimiter=',',unpack=True)
gravx_e, gravy_e = np.loadtxt(folder+"/gravelines_e.txt",delimiter=',',unpack=True)
gravx_r, gravy_r = np.loadtxt(folder+"/gravelines_r.txt",delimiter=',',unpack=True)
worx_e, wory_e = np.loadtxt(folder+"/world_e.txt",delimiter=',',unpack=True)
worx_r, wory_r = np.loadtxt(folder+"/world_r.txt",delimiter=',',unpack=True)
geox_e, geoy_e = np.loadtxt(folder+"/geo_e.txt",delimiter=',',unpack=True)
geox_r, geoy_r = np.loadtxt(folder+"/geo_r.txt",delimiter=',',unpack=True)
li9x_e, li9y_e = np.loadtxt(folder+"/li9_e.txt",delimiter=',',unpack=True)
li9x_r, li9y_r = np.loadtxt(folder+"/li9_r.txt",delimiter=',',unpack=True)
n17x_e, n17y_e = np.loadtxt(folder+"/n17_e.txt",delimiter=',',unpack=True)
n17x_r, n17y_r = np.loadtxt(folder+"/n17_r.txt",delimiter=',',unpack=True)
fnx_e, fny_e = np.loadtxt(folder+"/fn_e.txt",delimiter=',',unpack=True)
fnx_r, fny_r = np.loadtxt(folder+"/fn_r.txt",delimiter=',',unpack=True)
unoscx_e, unoscy_e = np.loadtxt(folder+"/non-osc_e.txt",delimiter=',',unpack=True)
unoscx_r, unoscy_r = np.loadtxt(folder+"/non-osc_r.txt",delimiter=',',unpack=True)

def offset(name_x,name_y):
    offset_axis = np.linspace(0,13.8,276+1) # new axis from 0 to 13.8 MeV with 0.05 increments
    offset_axis_y = np.zeros(len(offset_axis))
    name_x += 1.80
    offset_axis = np.round(offset_axis,2)
    name_x = np.round(name_x,2)
    for i in range(len(offset_axis)):
        for j in range(len(name_x)):  
            if offset_axis[i] == name_x[j]:
                offset_axis_y[i] = np.copy(name_y[j])
    x = np.copy(offset_axis)
    y = np.copy(offset_axis_y)
    return x,y

def no_offset(name_x,name_y):
    offset_axis = np.linspace(0,13.8,276+1) # new axis from 0 to 13.8 MeV with 0.05 increments
    offset_axis_y = np.zeros(len(offset_axis))
    name_x += 0
    offset_axis = np.round(offset_axis,2)
    name_x = np.round(name_x,2)
    for i in range(len(offset_axis)):
        for j in range(len(name_x)):  
            if offset_axis[i] == name_x[j]:
                offset_axis_y[i] = np.copy(name_y[j])
    x = np.copy(offset_axis)
    y = np.copy(offset_axis_y)
    return x,y
        
heye = offset(heyx_e,heyy_e)
heyx_e = heye[0]
heyy_e = heye[1]
heyr = offset(heyx_r,heyy_r)
heyx_r = heyr[0]
heyy_r = heyr[1]

tore = offset(torx_e,tory_e)
torx_e = tore[0]
tory_e = tore[1]
torr = offset(torx_r,tory_r)
torx_r = torr[0]
tory_r = torr[1]

sizee = offset(sizex_e,sizey_e)
sizex_e = sizee[0]
sizey_e = sizee[1]
sizer = offset(sizex_r,sizey_r)
sizex_r = sizer[0]
sizey_r = sizer[1]

hinke = offset(hinkx_e,hinky_e)
hinkx_e = hinke[0]
hinky_e = hinke[1]
hinkr = offset(hinkx_r,hinky_r)
hinkx_r = hinkr[0]
hinky_r = hinkr[1]

grave = offset(gravx_e,gravy_e)
gravx_e = grave[0]
gravy_e = grave[1]
gravr = offset(gravx_r,gravy_r)
gravx_r = gravr[0]
gravy_r = gravr[1]

wore = offset(worx_e,wory_e)
worx_e = wore[0]
wory_e = wore[1]
worr = offset(worx_r,wory_r)
worx_r = worr[0]
wory_r = worr[1]

geoe = offset(geox_e,geoy_e)
geox_e = geoe[0]
geoy_e = geoe[1]
geor = offset(geox_r,geoy_r)
geox_r = geor[0]
geoy_r = geor[1]

unosce = offset(unoscx_e,unoscy_e)
unoscx_e = unosce[0]
unoscy_e = unosce[1]
unoscr = offset(unoscx_r,unoscy_r)
unoscx_r = unoscr[0]
unoscy_r = unoscr[1]

li9e = offset(li9x_e,li9y_e)
li9x_e = li9e[0]
li9y_e = li9e[1]
li9r = offset(li9x_r,li9y_r)
li9x_r = li9r[0]
li9y_r = li9r[1]

n17e = offset(n17x_e,n17y_e)
n17x_e = n17e[0]
n17y_e = n17e[1]
n17r = offset(n17x_r,n17y_r)
n17x_r = n17r[0]
n17y_r = n17r[1]

fne = offset(fnx_e,fny_e)
fnx_e = fne[0]
fny_e = fne[1]
fnr = offset(fnx_r,fny_r)
fnx_r = fnr[0]
fny_r = fnr[1]

#unoscy_r = EspecNonOsc

# plt.plot(n17x_e,n17y_e)
# plt.plot(torx_e,tory_e)
# plt.plot(unoscx_e,unoscy_e)
# plt.figure()

# Define uncertainties
mu=0
hey_uncert = 0.023
tor_uncert = 0.026
size_uncert = 0.0275
hink_uncert = 0.03
grav_uncert = 0.034
react_uncert = 0.06
radio_uncert = 0.002
geo_uncert = 0.25
fn_uncert = 0.27

def error_func():
    # Loop through Heysham 2 data (reconstructed data)
    heyy_r_uncert = []
    for i,v in enumerate(heyy_r):
        # Draw uncertainties at random from Gaussian
        s_wor = np.random.normal(mu,react_uncert)
        s_tor = np.random.normal(mu,tor_uncert)
        s_size = np.random.normal(mu,size_uncert)
        s_hink = np.random.normal(mu,hink_uncert)
        s_grav = np.random.normal(mu,grav_uncert)
        s_geo = np.random.normal(mu,geo_uncert)
        s_li9 = np.random.normal(mu,radio_uncert)
        s_n17 = np.random.normal(mu,radio_uncert)
#        s_fn = np.random.normal(mu,fn_uncert)
        # Add uncertainties into Heysham 2 data
        data = v
        data+=(s_wor*wory_r[i])
        data+=(s_tor*tory_r[i])
        data+=(s_size*sizey_r[i])
        data+=(s_hink*hinky_r[i])
        data+=(s_grav*gravy_r[i])
        data+=(s_geo*geoy_r[i])
        data+=(s_li9*li9y_r[i])
        data+=(s_n17*n17y_r[i])
        heyy_r_uncert.append(data)
    
    # Loop through Heysham 2 data (MC data)
    heyy_e_uncert = []
    for i,v in enumerate(heyy_e):
        # Draw uncertainties at random from Gaussian
        s_wor = np.random.normal(mu,react_uncert)
        s_tor = np.random.normal(mu,react_uncert)
        s_size = np.random.normal(mu,react_uncert)
        s_hink = np.random.normal(mu,react_uncert)
        s_grav = np.random.normal(mu,react_uncert)
        s_geo = np.random.normal(mu,geo_uncert)
        s_li9 = np.random.normal(mu,radio_uncert)
        s_n17 = np.random.normal(mu,radio_uncert)
#        s_fn = np.random.normal(mu,fn_uncert)
        # Add uncertainties into Heysham 2 data
        data = v
        data+=(s_wor*wory_e[i])
        data+=(s_tor*tory_e[i])
        data+=(s_size*sizey_e[i])
        data+=(s_hink*hinky_e[i])
        data+=(s_grav*gravy_e[i])
        data+=(s_geo*geoy_e[i])
        data+=(s_li9*li9y_e[i])
        data+=(s_n17*n17y_e[i])
        heyy_e_uncert.append(data)
    
    
#    # Plot data with MC energy
#    plt.plot(heyx_e,heyy_e,label='Heysham 2 MC')
#    plt.plot(torx_e,tory_e,label='Torness MC')
#    plt.plot(sizex_e,sizey_e,label='Sizewell B MC')
#    plt.plot(hinkx_e,hinky_e,label='Hinkley Point C MC')
#    plt.plot(gravx_e,gravy_e,label='Gravelines MC')
#    plt.plot(worx_e,wory_e,label='World MC')
#    plt.plot(li9x_e,li9y_e,label='9Li MC')
#    plt.plot(n17x_e,n17y_e,label='17N MC')
#    plt.plot(geox_e,geoy_e, label = "Geo MC")
#    plt.plot(fnx_e,fny_e,label='Fn MC')
#    plt.xlabel("Kinetic Energy [MeV]")
#    plt.ylabel("Events per day")
#    plt.legend()
#    plt.show()
#    
#    # Plot data with reconstructed energy
#    plt.plot(heyx_r,heyy_r,label='Heysham 2 Reco')
#    plt.plot(torx_r,tory_r,label='Torness Reco')
#    plt.plot(sizex_r,sizey_r,label='Sizewell B Reco')
#    plt.plot(hinkx_r,hinky_r,label='Hinkley Point C Reco')
#    plt.plot(gravx_r,gravy_r,label='Gravelines Reco')
#    plt.plot(worx_r,wory_r,label='World Reco')
#    plt.plot(li9x_r,li9y_r,label='9Li Reco')
#    plt.plot(n17x_r,n17y_r,label='17N Reco')
#    plt.plot(geox_r,geoy_r, label = "Geo Reco")
#    plt.plot(fnx_r,fny_r,label='Fn Reco')
#    plt.xlabel("Kinetic Energy [MeV]")
#    plt.ylabel("Events per day")
#    plt.legend()
#    plt.show()
#    
    # #Plot data including background uncertainties
    # plt.plot(heyx_r,heyy_r_uncert,label="Heysham 2 Reco (Uncertainties)")
    # plt.xlabel("Kinetic Energy [MeV]")
    # plt.ylabel("Events per day")
    # plt.legend()
    # plt.show()
#    
#    plt.plot(heyx_e,heyy_e_uncert,label="Heysham 2 MC (Uncertainties)")
#    plt.xlabel("Kinetic Energy [MeV]")
#    plt.ylabel("Events per day")
#    plt.legend()
#    plt.show()
    return heyy_r_uncert



m21 = 7.42e-5    # Solar mass splitting SQUARED ALREADY

### Fourier cosine transform scaled to m21 frequency ###
LMin = 0                                       # length range (km)
LMax = 500 
Nft = 1000                                       # Number of data points for FT domain
Len = np.linspace(LMin * 1e3 ,LMax * 1e3 , Nft)  # FT length axis


# Reactor FT dict.
FTyTotal = dict()
for i in range(Nft):
    FTyTotal[i] = []

FTyTotal_sin = dict()
for i in range(Nft):
    FTyTotal_sin[i] = []
    
    
heyy_e_uncert = 0 # real value defined in error_func(), this line removes undefined name error below

how_many = 100
for i in range(how_many):
#    error_func()
    E = heyx_e
    Y = np.array(error_func()) # defined in error_func()
    Y = Y / sum(Y)
    Yosc = np.copy(unoscy_r)
    Yosc = Yosc / sum(Yosc) 
    # Remove DC offsets to remove FT peak at 0 Hz. This is a standard technique often used.
    #Yosc = unosc[1] ### defined above
    Y = Y - Y.mean()
    Yosc = Yosc - Yosc.mean()
    
    
    ### Final FT used to subtract the unoscillated contributions ###
    FTyVaried = np.zeros(Nft)
    FToscVaried = np.zeros(Nft)
    FTyVaried_sin = np.zeros(Nft)
    FToscVaried_sin = np.zeros(Nft)
    for w in range(Nft): # Iterates over FT x axis
        summation = 0
        summation1 = 0
        summation += Y[1:] * np.cos( 2 *(1.27 * m21 * Len[w]) * 1/E[1:] ) # SUM[ f(E)Cos(1.27 m21 L / E) ]
        summation1 += Yosc[1:] * np.cos( 2 *(1.27 * m21 * Len[w]) * 1/E[1:] )
        FTyVaried[w] = sum(summation)
        FToscVaried[w] = sum(summation1)
        FTyTotal[w].append(FTyVaried[w])

        summation_sin = 0
        summation1_sin = 0
        summation_sin += Y[1:] * np.sin( 2 *(1.27 * m21 * Len[w]) * 1/E[1:] ) # SUM[ f(E)Cos(1.27 m21 L / E) ]
        summation1_sin += Yosc[1:] * np.sin( 2 *(1.27 * m21 * Len[w]) * 1/E[1:] )
        FTyVaried_sin[w] = sum(summation_sin)
        FToscVaried_sin[w] = sum(summation1_sin)
        FTyTotal_sin[w].append(FTyVaried_sin[w])
    
#     plt.plot(Len/1e3,FTyVaried)
#     #plt.plot(Len/1e3,FToscVaried)
#     #plt.plot(Len/1e3,FTyVaried - FToscVaried)
#     plt.xlabel("Calculated distance (km)", fontsize = 14)
#     plt.ylabel("FT Amplitude \n (arbitrary units)", fontsize = 14)
#     plt.xlim(0,500)
#     #plt.ylim(-0.7,1.2)
# #    plt.legend()
# #    plt.savefig("Torness final data.pdf", bbox_inches='tight')
#     #    plt.figure()

### Creates FT spectrum and errors from the dictionaries    
Average = np.zeros(Nft)
Average = [sum(FTyTotal[a]) / how_many for a in FTyTotal]
Average = np.array(Average)
maximum = [max(FTyTotal[a]) for a in FTyTotal]
minimum = [min(FTyTotal[a]) for a in FTyTotal]
maximum = np.array(maximum)
minimum = np.array(minimum)
ErrorBar = (maximum - minimum) / 2

Average_sin = np.zeros(Nft)
Average_sin = [sum(FTyTotal_sin[a]) / how_many for a in FTyTotal_sin]
Average_sin = np.array(Average_sin)
maximum_sin = [max(FTyTotal_sin[a]) for a in FTyTotal_sin]
minimum_sin = [min(FTyTotal_sin[a]) for a in FTyTotal_sin]
maximum_sin = np.array(maximum_sin)
minimum_sin = np.array(minimum_sin)
ErrorBar_sin = (maximum_sin - minimum_sin) / 2

plt.figure()
#plt.errorbar(Len/1e3, Average - FToscVaried , ErrorBar, errorevery = 10, label = "FCT Heysham Reco")
#plt.errorbar(Len/1e3, Average_sin - FToscVaried_sin, yerr=ErrorBar_sin, errorevery = 10, label = "FST Heysham Reco")
plt.errorbar(Len/1e3, Average , yerr=ErrorBar, errorevery = 10 ,linestyle='dotted', color='r', label = "FCT")
plt.errorbar(Len/1e3, Average_sin, yerr=ErrorBar_sin, errorevery = 10, color='k', label = "FST")
plt.xlabel("Distance (km)", fontsize = 15)
plt.ylabel("Amplitude", fontsize = 15)
plt.xlim(0,500)
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)
plt.legend(fontsize=15)
plt.savefig("hey-FT.pdf", bbox_inches='tight')
plt.show()
### Calculate reactor range SINE ###
High = Average + ErrorBar
Low = Average - ErrorBar

# for i in range(len(High)):   
#     if Low[i] <= 0 <= High[i]:
#         print(Len[i]/1e3)


Final = Average
FinalErrors = ErrorBar
### Calculate reactor range COSINE ###
added = np.zeros(Nft)
for i in range(Nft):
   added[i] = Final[i] + abs(FinalErrors[i])
maxY = max(added)
maxX = np.where(added == maxY)
print(Len[maxX]/1e3)

ara = (Final[maxX] - abs(FinalErrors[maxX]))
rangesX = np.where((Final + abs(FinalErrors)) > ara[0])
rangesX = rangesX[0]
rangesOfData = Len[rangesX] / 1e3
print("range of distances", rangesOfData)
minMax = rangesOfData[-1] - rangesOfData[0]
midpoint = rangesOfData[0] + minMax / 2

print(minMax,midpoint)








