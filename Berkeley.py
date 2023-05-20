def berkeley_algorithm(time_offsets):

    # calculate average time_offset
    avg_timeoffset = sum(time_offsets)/len(time_offsets)
    print("Average time offset is =", avg_timeoffset)

    # adjust the clocks
    adjusted_clocks = [time-avg_timeoffset for time in time_offsets]

    return adjusted_clocks

time_offsets = [1.2, 0.5, -0.3, 2.1, -1.0]
adjusted_clocks = berkeley_algorithm(time_offsets)
print(adjusted_clocks)