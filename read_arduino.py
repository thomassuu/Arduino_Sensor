import serial
import serial.tools.list_ports
from datetime import datetime as dt
import csv
import os.path
PORT = "COM7"
BAUDRATE = 9600
HEADERS = ['Date', 'Time', 'Detected']

# ports = serial.tools.list_ports.comports()
# port_list = []
# for port in ports:
#     port_list.append(str(port))
# print(port_list)

def main():
    
    ser = serial.Serial()
    ser.baudrate = BAUDRATE
    ser.port = PORT
    try:
        ser.open()
    except Exception as e:
        print(e)
        return
    
    curr_date = start_date = dt.now().strftime("%d/%m/%Y")
    filename = "Output_Detection_" + start_date.replace("/","_") + ".csv"
    if not os.path.exists(filename):
        print("file not existed -> creating...")
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
            
    while curr_date == start_date:
        if ser.in_waiting:
            now = dt.now()
            curr_time = now.strftime("%H:%M:%S")
            curr_date = now.strftime("%d/%m/%Y")
            data = ser.readline()
            try:
                with open(filename, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([curr_time, curr_date, int(data)])
            except ValueError:
                break
if __name__ == '__main__':
    main()