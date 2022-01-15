mph_data = list()
kph_data = list()

def average(x):  
    '''calculates the average'''
    avg = sum(x)/len(x) 
    return avg
    
def task_2():
    '''turns miles into kilometer and vice-versa'''
    print("Swallow Speed Analysis: Version 1.0", end="\n\n")
    read = input("Enter the Next Reading: ")

    if read == "":
        print("No readings entered. Nothing to do.", end="\n")

    else:
        while read != "":
            if(read.startswith("U") or read.startswith("u")): 
                mph = float(read[1:])
                kph = float(read[1:]) * 1.60934
                mph_data.append(mph)
                kph_data.append(kph)

            else:
                kph = float(read[1:])
                mph = float(read[1:]) * 0.62137
                mph_data.append(mph)
                kph_data.append(kph)
            print("Reading saved.")
            read = input("Enter the Next Reading: ")
        
        print("\n\nResults Summary", end="\n\n")
        print("{} Readings Analysed.".format(len(mph_data)), end="\n\n")
        print("Max Speed: {:.1f} MPH, {:.1f} KPH.".format(max(mph_data),max(kph_data)))
        print("Min Speed: {:.1f} MPH, {:.1f} KPH.".format(min(mph_data),min(kph_data)))
        print("Avg Speed: {:.1f} MPH, {:.1f} KPH.".format(average(mph_data),average(kph_data)))


task_2()