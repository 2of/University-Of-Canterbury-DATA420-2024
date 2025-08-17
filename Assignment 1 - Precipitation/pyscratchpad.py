import math


def distance(Lat1, Lon1, Lat2, Lon2):
  EarthRadius = 6371  # Earth radius in kilometers
  # to rads for all
  Lat1 = math.radians(Lat1)
  Lat2 = math.radians(Lat2)
  Lon1 = math.radians(Lon1)
  Lon2 = math.radians(Lon2)

  # Calculate the angle between the two points
  dLon = Lon2 - Lon1
  dLat = Lat2 - Lat1

  a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(Lat1)) * math.cos(math.radians(Lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)

  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

  # Calculate the distance
  distance = EarthRadius * c

  return distance

fss = []
fns = []

with open('filesizes.txt', 'r') as f:
    # Read lines from the file
    lines = f.readlines()

    # Iterate through each line
    
    
    
    for line in lines:
        # Split the line into two columns
        columns = line.split()

        # Extract the filesize and filename
        filesize = columns[0]
        filename = columns[1][-11:][:4]
        
        fss.append(filesize)
        fns.append(filename)




def get_ticks(years):
    # Sort the years array
    years_sorted = sorted(years)
    
    # Calculate the number of elements in the years array
    num_years = len(years_sorted)
    
    # Calculate the step size for equally spaced values
    step_size = (num_years - 1) // 7
    
    # Initialize the ticks list with the first and last years
    ticks = [years_sorted[0], years_sorted[-1]]
    
    # Add four equally spaced values in between
    for i in range(1, 7):
        index = i * step_size
        ticks.append(years_sorted[index])
    
    return ticks



for (a,b) in zip (fns,fss):
    print(b)

import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
ticksx = get_ticks(fns)
ticksy = get_ticks(fss)
# Plotting
plt.scatter(fns, fss)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('File Size')
plt.title('File Size Over the Years')

# Displaying the plot
plt.grid(False)
plt.xticks(ticksx)
plt.yticks(ticksy)
plt.show()


