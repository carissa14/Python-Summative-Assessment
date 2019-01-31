import random as rand # to generate the random numbers between range(0-1) for the 16 required readings per cluster
import pickle # Use pickle to dump the data to the text file

#creating a dataset for 32 Sensor Clusters
clusters = list(range(1,33))
for i, cluster in enumerate(clusters): #Enumerate to iterate through the list
    print("cluster{}".format(cluster))

#Creating a 2D array
numClusters = 32
readings = 16
SensorReading = [[0 for x in range(readings)] for y in range(numClusters)] #iterating through the matrix
for i in range(32):
    print(" Cluster {}".format(i+1))# iterating through the 32 clusters

    for j in range(16):
        SensorReadingNumbers = rand.random() # creating 16 random numbers
        SensorReading[i][j] = SensorReadingNumbers
        print(" {}".format(SensorReading[i][j]))

#Using a call function to write ("ab" to ammend not overwrite) output data to a file : Created file Assessment.txt

def PushToFile():

    f = open("Assessment.txt", "ab")
    pickle.dump(SensorReading, f)
    f.close()
    return()
PushToFile()

#Copy of Corrupt dataset: Deleted 1 value and replaced it with "err" to make a corrupt dataset
corrupt_set = SensorReading[:]
del corrupt_set[0]
corrupt_set.append("err")
print(corrupt_set) # confirms 1 value has been removed and replaced with "err"

#Testing Data for string entries (to find the "err" added above)


def check_for_error(corrupt_set):
    for each in corrupt_set:
        if isinstance(each, str) == True:
            print("Dataset containts the folling string:", each)


check_for_error(corrupt_set)
