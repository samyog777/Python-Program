import statistics

def improved_average(num1, num2, num3, num4, num5):
    # Calculate mean value
    mean = (num1 + num2 + num3 + num4 + num5) / 5
    
    # Calculate median value
    median = statistics.median([num1, num2, num3, num4, num5])
    
    # Calculate mode value
    mode = statistics.mode([num1, num2, num3, num4, num5])
    
    return (mode, median, mean)
improved_average(9,8,7,6,5)

                     
            
