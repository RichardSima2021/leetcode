def daily_temps(temps):
    temp_stack = []
    res_list = [0] * len(temps)
    head_ptr = 0
    tail_ptr = 0
    for temp in temps:
        curr_temp = temp

        if len(temp_stack) == 0:
            temp_stack.append(temp)
        else:
            if curr_temp > temp_stack[-1]:



        index_ptr += 1
