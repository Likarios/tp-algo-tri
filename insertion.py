import random
import time
from plot import plot_graph

# Sort a table by insertion
# Complexity seems to be o(n^2)
def insertion_sort(table: list[int]):
    for i in range(1, len(table)):
        current_index = table[i]
        j = i-1
        while j >=0 and current_index < table[j] :
            table[j+1] = table[j]
            j -= 1
        table[j+1] = current_index
    return table

entries = []
time_per_entry = []

for i in range(1, 11):
    number_of_entries = 1000 * i
    table = [random.randint(0, 10000) for i in range(number_of_entries)]
    start: float = time.time()
    insertion_sort(table)
    end: float = time.time()
    time_elpased = end - start
    entries.append(number_of_entries)
    time_per_entry.append(time_elpased)
    print(str(number_of_entries) + " entries sorted.")

plot_graph(entries, time_per_entry, "insertion.png")