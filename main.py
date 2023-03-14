# ----------------------------- RR -----------------------------
def RR():
    global process_time
    value = 0
    count = 0
    while sum(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i] == 0:
                continue

            if count == time:
                value = 1
                break

            jobs[i] -= 1
            count += 1
            process_time += 1

            if jobs[i] == 0:
                turnaround_time[i] = process_time

        if value:
            break

    print("---------RR---------", " ".join([str(i) for i in jobs]))


# -------------------------- SJF 01 --------------------------
def SJF1():
    global process_time
    value = 0
    count = time
    while sum(jobs) != 0:
        if count == 0:
            break

        non_zero_list = [x for x in jobs if x != 0]
        index = jobs.index(min(non_zero_list))

        if min(non_zero_list) >= count:
            process_time += count
            jobs[index] -= count
            count = 0

            if jobs[index] == 0:
                turnaround_time[index] = process_time

            break

        process_time += jobs[index]
        jobs[index] = 0
        count -= min(non_zero_list)

        if jobs[index] == 0:
            turnaround_time[index] = process_time

    print("--------SJF1--------", " ".join([str(i) for i in jobs]))


# -------------------------- SJF 02 --------------------------
def SJF2():
    global process_time
    value = 0
    count = time
    while sum(jobs) != 0:
        if count == 0:
            break

        non_zero_list = [x for x in jobs if x != 0]
        index = jobs.index(min(non_zero_list))

        if min(non_zero_list) >= count:
            process_time += count
            jobs[index] -= count
            count = 0

            if jobs[index] == 0:
                turnaround_time[index] = process_time

            break

        process_time += jobs[index]
        jobs[index] = 0
        count -= min(non_zero_list)

        if jobs[index] == 0:
            turnaround_time[index] = process_time

    print("--------SJF2--------", " ".join([str(i) for i in jobs]))


# ---------------------------- FCFS ----------------------------
def FCFS():
    global process_time
    value = 0
    count = time
    for i in range(len(jobs)):
        if count == 0 or sum(jobs) == 0:
            break

        if jobs[i] == 0:
            continue

        if jobs[i] >= count:
            jobs[i] -= count
            process_time += count
            count = 0

            if jobs[i] == 0:
                turnaround_time[i] = process_time

            break

        process_time += jobs[i]
        count -= jobs[i]
        jobs[i] = 0

        if jobs[i] == 0:
            turnaround_time[i] = process_time

    print("--------FCFS--------", " ".join([str(i) for i in jobs]))


if __name__ == "__main__":
    jobs = [int(i) for i in input("Enter Burst Times: ").split()]
    burst_time = jobs.copy()
    time = 20
    turnaround_time = [0] * len(jobs)
    waiting_time = [0] * len(jobs)

    process_time = 0

    priority = {'RR': -1, 'SJF1': -1, 'SJF2': -1, 'FCFS': -1}
    for i in priority:
        print("Enter Priority for", i, end=" : ")
        priority[i] = int(input())

    priority = dict(sorted(priority.items(), key=lambda item: item[1]))
    print()

    print("-----Burst Time-----", " ".join([str(i) for i in burst_time]))

    while True:
        if sum(jobs) == 0:
            break

        for i in priority:
            if sum(jobs) != 0:
                globals()[i]()

    for i in range(len(turnaround_time)):
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    print("\n")
    print("Burst Time   :", " ".join([str(i) for i in burst_time]))
    print("Consume Time :", " ".join([str(i) for i in turnaround_time]))
    print("Waiting Time :", " ".join([str(i) for i in waiting_time]))
