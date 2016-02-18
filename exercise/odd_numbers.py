def odd_numbers(low, high):
    odd_nos = []
    for item in range(low, high):
        if item % 2 != 0:
        	odd_nos.append(item)
    print odd_nos
