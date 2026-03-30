class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


def fcfs(processes):
    processes.sort(key=lambda x: x.at)
    time = 0

    print("\nFCFS:")
    print("PID AT BT CT TAT WT")

    for p in processes:
        if time < p.at:
            time = p.at

        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        print(p.pid, p.at, p.bt, p.ct, p.tat, p.wt)


def sjf(processes):
    pro = processes[:]
    time = 0
    completed = []

    print("\nSJF:")
    print("PID AT BT CT TAT WT")

    while pro:
        ready = [p for p in pro if p.at <= time]

        if not ready:
            time += 1
            continue

        ready.sort(key=lambda x: x.bt)
        p = ready[0]

        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        print(p.pid, p.at, p.bt, p.ct, p.tat, p.wt)

        completed.append(p)
        pro.remove(p)

    return completed


# Input
processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 8),
    Process(4, 3, 6)
]

fcfs_list = processes[:]
fcfs(fcfs_list)

sjf_list = processes[:]
sjf_result = sjf(sjf_list)