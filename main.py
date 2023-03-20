# ----------------------------- RR -----------------------------
def RR(data):
    global process_time
    value = 0
    count = 0
    while sum(jobs[data]) != 0:
        for i in range(len(jobs[data])):
            if jobs[data][i] == 0:
                continue
            
            if count == time:
                value = 1
                break

            jobs[data][i] -= 1
            count += 1
            process_time += 1
            
            if jobs[data][i] == 0:
                turnaround_time[data][i] = process_time

        if value:
            break

    print("---------RR---------", " ".join([str(i) for i in jobs[data]]))



# -------------------------- SJF 01 --------------------------
def SJF1(data):
    global process_time
    value = 0
    count = time
    while sum(jobs[data]) != 0:
        if count == 0:
            break
        
        non_zero_list = [x for x in jobs[data] if x != 0]
        index = jobs[data].index(min(non_zero_list))

        if min(non_zero_list) >= count:
            process_time += count
            jobs[data][index] -= count
            count = 0

            if jobs[data][index] == 0:
                turnaround_time[data][index] = process_time
                
            break


        process_time += jobs[data][index]
        jobs[data][index] = 0
        count -= min(non_zero_list)
        
        if jobs[data][index] == 0:
            turnaround_time[data][index] = process_time
            
                    

    print("--------SJF1--------", " ".join([str(i) for i in jobs[data]]))



# -------------------------- SJF 02 --------------------------
def SJF2(data):
    global process_time
    value = 0
    count = time
    while sum(jobs[data]) != 0:
        if count == 0:
            break
        
        non_zero_list = [x for x in jobs[data] if x != 0]
        index = jobs[data].index(min(non_zero_list))

        if min(non_zero_list) >= count:
            process_time += count
            jobs[data][index] -= count
            count = 0

            if jobs[data][index] == 0:
                turnaround_time[data][index] = process_time
                
            break


        process_time += jobs[data][index]
        jobs[data][index] = 0
        count -= min(non_zero_list)
        
        if jobs[data][index] == 0:
            turnaround_time[data][index] = process_time
            
                    

    print("--------SJF2--------", " ".join([str(i) for i in jobs[data]]))
   


# ---------------------------- FCFS ----------------------------
def FCFS(data):
    global process_time
    value = 0
    count = time
    for i in range(len(jobs[data])):        
        if count == 0 or sum(jobs[data]) == 0:
            break

        if jobs[data][i] == 0:
            continue

        if jobs[data][i] >= count:
            jobs[data][i] -= count
            process_time += count
            count = 0
            
            if jobs[data][i] == 0:
                turnaround_time[data][i] = process_time
                
            break

        process_time += jobs[data][i]
        count -= jobs[data][i]
        jobs[data][i] = 0

        if jobs[data][i] == 0:
            turnaround_time[data][i] = process_time
            


    print("--------FCFS--------", " ".join([str(i) for i in jobs[data]]))


def Scheduler():
    for i in priority:
        if sum(jobs[i]) != 0:
            globals()[i](i)
    

if __name__ == "__main__":
    time = 20

    process_time = 0
    

    priority = {'RR': 0, 'SJF1': 1, 'SJF2': 2, 'FCFS': 3}
    jobs = {'RR': [], 'SJF1': [], 'SJF2': [], 'FCFS': []}
    
    for i in priority:
        jobs[i] = [int(i) for i in input("Enter values for " + i + "(priority level " + str(priority[i]) + "): ").split()]

    turnaround_time = {'RR': [0] * len(jobs['RR']), 'SJF1': [0] * len(jobs['SJF1']), 'SJF2': [0] * len(jobs['SJF2']), 'FCFS': [0] * len(jobs['FCFS'])}
    waiting_time = {'RR': [0] * len(jobs['RR']), 'SJF1': [0] * len(jobs['SJF1']), 'SJF2': [0] * len(jobs['SJF2']), 'FCFS': [0] * len(jobs['FCFS'])}
    burst_time = {'RR': jobs['RR'].copy(), 'SJF1': jobs['SJF1'].copy(), 'SJF2': jobs['SJF2'].copy(), 'FCFS': jobs['FCFS'].copy()}


    print()
    
    while True:
        if sum(jobs["RR"]) == 0 and sum(jobs["SJF1"]) == 0 and sum(jobs["SJF2"]) == 0 and sum(jobs["FCFS"]) == 0:
            break

        Scheduler()
        

    for i in jobs:
        for j in range(len(turnaround_time[i])):
            waiting_time[i][j] = turnaround_time[i][j] - burst_time[i][j]

    print("\n")
    print("Burst Times:")
    for i in priority:
        print("Priority level", priority[i], ":", ", ".join(str(i) for i in burst_time[i]))

    print()

    print("Consume Times:")
    for i in priority:
        print("Priority level", priority[i], ":", ", ".join(str(i) for i in turnaround_time[i]))

    print()

    print("Waiting Times:")
    for i in priority:
        print("Priority level", priority[i], ":", ", ".join(str(i) for i in waiting_time[i]))
