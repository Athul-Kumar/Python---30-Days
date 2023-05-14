'''
                            STATISTICS MODULE

---> provides functions for mathematical statistic of numeric data

---> popular functions defined in this module are

        1.mean
        2.median
        3.mode
        4.srdev etc

'''


from statistics import mean, median,mode,stdev

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))