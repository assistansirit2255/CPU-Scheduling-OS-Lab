def fcfs(requests, head):
    seek_time = 0
    for r in requests:
        seek_time += abs(head - r)
        head = r
    print("FCFS Seek Time:", seek_time)


def sstf(requests, head):
    seek_time = 0
    req = requests.copy()

    while req:
        nearest = min(req, key=lambda x: abs(x - head))
        seek_time += abs(head - nearest)
        head = nearest
        req.remove(nearest)

    print("SSTF Seek Time:", seek_time)


def scan(requests, head, disk_size):
    seek_time = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    for r in right:
        seek_time += abs(head - r)
        head = r

    seek_time += abs(head - (disk_size - 1))
    head = disk_size - 1

    for r in left:
        seek_time += abs(head - r)
        head = r

    print("SCAN Seek Time:", seek_time)


def cscan(requests, head, disk_size):
    seek_time = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    for r in right:
        seek_time += abs(head - r)
        head = r

    seek_time += abs(head - (disk_size - 1))
    head = 0
    seek_time += disk_size - 1

    for r in left:
        seek_time += abs(head - r)
        head = r

    print("C-SCAN Seek Time:", seek_time)


# INPUT
requests = list(map(int, input("Enter requests: ").split()))
head = int(input("Enter head position: "))
disk_size = int(input("Enter disk size: "))

fcfs(requests, head)
sstf(requests, head)
scan(requests, head, disk_size)
cscan(requests, head, disk_size)