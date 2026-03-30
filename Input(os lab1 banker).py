class Bankers:
    def __init__(self, processes, resources, allocation, maximum, available):
        self.p = processes
        self.r = resources
        self.alloc = allocation
        self.max = maximum
        self.avail = available
        self.need = [[self.max[i][j] - self.alloc[i][j] for j in range(self.r)] for i in range(self.p)]

    def is_safe(self):
        work = self.avail[:]
        finish = [False] * self.p
        safe_seq = []

        while len(safe_seq) < self.p:
            found = False
            for i in range(self.p):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(self.r)):
                    for j in range(self.r):
                        work[j] += self.alloc[i][j]
                    safe_seq.append(i)
                    finish[i] = True
                    found = True

            if not found:
                return False, []

        return True, safe_seq


# Example Input
processes = 3
resources = 3

allocation = [
    [1, 0, 1],
    [2, 1, 0],
    [1, 1, 1]
]

maximum = [
    [3, 2, 1],
    [2, 2, 2],
    [3, 3, 3]
]

available = [1, 1, 2]

bank = Bankers(processes, resources, allocation, maximum, available)

print("\nNeed Matrix:")
for i in range(processes):
    print(f"P{i}: {bank.need[i]}")

safe, seq = bank.is_safe()

if safe:
    print("\nSystem is in SAFE state")
    print("Safe Sequence:", " -> ".join(f"P{i}" for i in seq))
else:
    print("\nSystem is NOT SAFE")
