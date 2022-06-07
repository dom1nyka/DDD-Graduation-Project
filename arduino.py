import serial
import time
import json

# set up the serial line
ser = serial.Serial('/dev/cu.usbmodem1101', 9600)


# get participant and song ids
participant = input('Enter participant name:')
song_id = input('Enter song id:')

# Read and record the data
data = []
for i in range(1800):      # number of readings
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    integer = int(string)        # convert string to float
    print(integer)
    data.append(integer)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds


json_string = json.dumps(data)
#print(json_string)

with open(participant + "/" + song_id + '.json', 'w') as outfile:
    json.dump(json_string, outfile)

ser.close()

# show the data

# for line in data:
#     print(line)
#
# import matplotlib.pyplot as plt
#
# plt.plot(data)
# plt.xlabel('Time (miliseconds)')
# plt.ylabel('Potentiometer Reading')
# plt.title('Potentiometer Reading vs. Time')
# plt.show()
#
