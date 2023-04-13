import numpy as np
import matplotlib.pyplot as plt

results = np.genfromtxt("range_results.txt",dtype=str,delimiter="\n")#open('range_results.txt', 'r').read()

months = []
events = []
ranges = []
errors = []

rate = 3.26456/2

for i in range(len(results)):
    split = results[i].split(" ")
    split_events = split[1].split("(")
    months.append(float(split_events[1])/(rate*365.25/12))
    events.append(float(split_events[1]))
    ranges.append(float(split[4]))
    error = (float(split[6]))**2/(float(split[4]))**2
    error += 1/float(split_events[1])
    error = np.sqrt(error) * (float(split[4]))
    # errors.append(float(split[6]))
    errors.append(error)

results_2 = np.genfromtxt("range_results_v2.txt",dtype=str,delimiter="\n")#open('range_results.txt', 'r').read()

months_2 = []
events_2 = []
ranges_2 = []
errors_2 = []

for i in range(len(results_2)):
    split = results_2[i].split(" ")
    split_events = split[1].split("(")
    months_2.append(float(split_events[1])/(rate*365.25/12))
    events_2.append(float(split_events[1]))
    ranges_2.append(float(split[4]))
    error = (float(split[6]))**2/(float(split[4]))**2
    error += 1/float(split_events[1])
    error = np.sqrt(error) * (float(split[4]))
    # errors.append(float(split[6]))
    errors_2.append(error)

for i,v in enumerate(events):
    print("Events: %f, Range = %f +/- %f"%(v,ranges[i],errors[i]))

# print(ranges.index(min(ranges)))
print("Optimal range (%f events, %f months) = %f +/- %f km"%(events[ranges.index(min(ranges))],months[ranges.index(min(ranges))],min(ranges),errors[ranges.index(min(ranges))]))

plt.plot(events,errors)
plt.plot(events_2,errors_2)
plt.clf()

plt.errorbar(months, ranges, yerr=errors,color='k',label="Observed range")
plt.hlines(min(ranges),min(months),max(months),colors='b',linestyles='dashed',label="Best observed range")
plt.hlines(26, min(months),max(months),colors='r',linestyles='dotted',label="True range")
plt.xlabel("Observation time [Months]",fontsize=15)
plt.ylabel("Range [km]",fontsize=15)
plt.ylim(0,1.01*(ranges[0]+errors[0]))
plt.yticks(list(plt.yticks()[0]) + [26])
plt.rc('xtick',labelsize=15)
plt.rc('ytick',labelsize=15)
plt.legend(fontsize=15)

#get handles and labels
handles, labels = plt.gca().get_legend_handles_labels()

#specify order of items in legend
order = [2,0,1]

#add legend to plot
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order]) 

plt.savefig("hartlepool_res_events_v2.pdf")
plt.show()

