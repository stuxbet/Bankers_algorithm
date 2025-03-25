
def bankers_algo(allocation, max_need, available):
    num_processes = len(allocation)
    num_resources = len(available)

    need_array = [] # this will rep the need for every process
    for i in range(num_processes):
        need_row = []
        for j in range(num_resources):
            need = max_need[i][j] - allocation[i][j]
            need_row.append(need)
        need_array.append(need_row)
    
    tasks_finish = [False] * num_processes
    safe_sequence = []

    for passes in range(num_processes):  #so it iterates n^2 and allows n trys to find a allocation that works
        allocated_this_round = False

        for i in range(num_processes):
            if not tasks_finish[i]:
                #we are iterating over processes not done

                can_allocate = True
                for r in range(num_resources):
                    if need_array[i][r] > available[r]:  
                        can_allocate = False
                        break  # abort because we cant do this
                
                if can_allocate:
                    for r in range(num_resources):
                        available[r] += allocation[i][r]
                    safe_sequence.append(f"P{i}")
                    tasks_finish[i] = True
                    allocated_this_round = True
                    # break
        if not allocated_this_round:
            break


    if all(tasks_finish):
        print(f"Safe Sequence Found: {safe_sequence}")
    else:
        print("No Safe Sequence (Deadlock possible).")






if __name__ == "__main__":
    x = 1
    allocation = [
        [0, 1, 0],  # example for P0
        [2, 0, 0],  # example for P1
        [3, 0, 2],  # example for P2
        [2, 1, 1],  # example for P3
        [0, 0, 2]   # example for P4
    ]

    needed = [
        [7, 5, 3],  # example for P0
        [3, 2, 2],  # example for P1
        [9, 0, 2],  # example for P2
        [2, 2, 2],  # example for P3
        [4, 3, 3]   # example for P4
    ]

    starting_resources = [3, 3, 2]

    bankers_algo(allocation, needed, starting_resources)
