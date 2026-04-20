def fifo(pages, frames):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1
        print(memory)

    print("FIFO Page Faults:", faults)


def lru(pages, frames):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda x: pages[:pages.index(page)].count(x))
                memory.remove(lru_page)
                memory.append(page)
            faults += 1
        print(memory)

    print("LRU Page Faults:", faults)


def optimal(pages, frames):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                future = pages[i+1:]
                replace = max(memory, key=lambda x: future.index(x) if x in future else float('inf'))
                memory.remove(replace)
                memory.append(pages[i])
            faults += 1
        print(memory)

    print("Optimal Page Faults:", faults)


def mru(pages, frames):
    memory = []
    faults = 0
    recent = []

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                mru_page = recent[-1]
                memory.remove(mru_page)
                memory.append(page)
            faults += 1
        recent.append(page)
        print(memory)

    print("MRU Page Faults:", faults)


def second_chance(pages, frames):
    memory = [None] * frames
    ref_bit = [0] * frames
    pointer = 0
    faults = 0

    for page in pages:
        if page not in memory:
            while ref_bit[pointer] == 1:
                ref_bit[pointer] = 0
                pointer = (pointer + 1) % frames

            memory[pointer] = page
            ref_bit[pointer] = 1
            pointer = (pointer + 1) % frames
            faults += 1
        else:
            ref_bit[memory.index(page)] = 1

        print(memory)

    print("Second Chance Faults:", faults)


# INPUT
pages = list(map(int, input("Enter pages: ").split()))
frames = int(input("Enter frames: "))

fifo(pages, frames)
lru(pages, frames)
optimal(pages, frames)
mru(pages, frames)
second_chance(pages, frames)