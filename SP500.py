with open('SP500.txt','r') as infile:
    sum_SP = 0
    max_interest = 0
    lines = infile.readlines()[6:18]
    for line in lines:
        values = line.strip().split(',')
        sum_SP = sum_SP + float(values[1])
        interest_rate = float(values[5])
        if interest_rate > max_interest:
            max_interest = interest_rate
    mean_SP = sum_SP/len(lines)
print(mean_SP)
print(max_interest)
