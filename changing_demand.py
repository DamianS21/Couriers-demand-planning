import sys
global stats
global demand
stats = []
sys.setrecursionlimit(400000)
avg_time_of_delivery = 30
day = 24 * 60  # 24h, 3600 min
typical_time_of_work = 8*60
couriers_id=set()
couriers = dict()
couriers_time_of_start_work = dict()
couriers[1] = 660 # [time of "avaiability"]
couriers_time_of_start_work[1] = 660  # start work at 11:00
import ast
file = open('demand.txt', mode='r')
contents = file.read()
demand = ast.literal_eval(contents)


for time in range(660,2100):
    stats.append(len(couriers))
    list_to_del = []
    for idx, time_of_start_of_work in couriers_time_of_start_work.items():
        if time - time_of_start_of_work > typical_time_of_work:
            list_to_del.append(idx)
    # courier assigning:
    for _ in range(demand[time]):  # demand
        min_avb_index = min(couriers, key=couriers.get)
        maximum_index = max(couriers)
        if couriers[min_avb_index] <= time:
            couriers[min_avb_index] = time + avg_time_of_delivery
        else:
            if time > 1140:  # if courier starts to work at 19:00:
                couriers[maximum_index + 1] = time + avg_time_of_delivery
                couriers_time_of_start_work[maximum_index + 1] = 1140
            else:
                couriers[maximum_index + 1] = time + avg_time_of_delivery
                couriers_time_of_start_work[maximum_index + 1] = time
    for i in list_to_del:
        couriers.pop(i)
        couriers_time_of_start_work.pop(i)
    couriers_id.add(maximum_index)

print(sorted(couriers_id))
import matplotlib.pyplot as plt
plt.plot(stats)
ax = plt.gca() # grab the current axis
ax.set_xticks([0,540,720,960,1440]) # choose which x locations to have ticks
ax.set_xticklabels(["11:00","20:00","23:00","03:00","10:59"]) # set the labels to display at those ticks
plt.title('Demand for couriers')
plt.xlabel('Time [hrs]')
plt.ylabel('Couriers demand [-]')
plt.savefig('couriers_demand_changing_demand.png')