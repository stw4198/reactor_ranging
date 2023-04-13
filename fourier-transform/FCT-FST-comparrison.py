import numpy as np
import matplotlib.pyplot as plt

N = 100
t = np.linspace(0,12,N)
y = np.cos(3 * t)
yerror = 1



# plt.errorbar(t,y, yerror, errorevery = 1, color = "blue",  fmt='o', markersize = 3 ,label = "cos(3t)")
# plt.xlabel("Time (t)", fontsize = 14)
# plt.ylabel("Amplitude", fontsize = 14)
# plt.ylim(-3,4)
# plt.xlim(0,10)
# plt.legend()
# #plt.savefig("Prop1.pdf", bbox_inches='tight')
# #plt.figure()

from matplotlib.ticker import MaxNLocator

fig, ax = plt.subplots()
xs = range(26)
ys = range(26)
labels = [0,0,'L/2','L','3L/2','2L']#list('012L345')

def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''

# A FuncFormatter is created automatically.
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

FTaxis = np.linspace(1,5,N)
FCT = np.zeros(N)
for w in range(N):
    summation = 0
    for s in range(len(y)):
        summation += y[s] * np.cos(  FTaxis[w] * t[s] )
    FCT[w] = summation
    
plt.errorbar(FTaxis,FCT / 50, 0.25, label = "FCT ", linestyle='dashed', color = "blue" )
plt.errorbar(FTaxis[46:54],FCT[46:54] / 50, 0.25, color = "red" )


FST = np.zeros(N)
for w in range(N):
    summation = 0
    for s in range(len(y)):
        summation += y[s] * np.sin(  FTaxis[w] * t[s] )
    FST[w] = summation

plt.errorbar(FTaxis,FST / 50, 0.25 ,label = "FST ", color = "gray" )
plt.errorbar(FTaxis[49:51],FST[49:51] / 50, 0.25, color = "red" )

#plt.plot(3+ np.zeros(100),np.linspace(-400,1050,100) / max(FTs), "--", linewidth = 0.7, color = "blue")
#plt.plot(7+ np.zeros(100),np.linspace(-400,350,100) / max(FTs), "--", linewidth = 0.8, color = "orange")
plt.xlabel("Distance", fontsize = 15)
plt.ylabel("Amplitude", fontsize = 15)
plt.xlim(1,5)
#plt.xticks(list(plt.xticks()[0]/3))
#ax.set_xticks([0,3,6])
#plt.ylim(-0.5, 1.4)
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)
plt.legend(fontsize=15)
plt.savefig("FCTFST-new.pdf", bbox_inches='tight')
plt.show()
