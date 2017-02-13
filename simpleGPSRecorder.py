from dronekit import connect
import time

address = 'localhost'
port = 9000

vehicle = connect('udpout:'+address+':'+str(port),wait_ready=False)

while True:
	lat = vehicle.location.global_frame.lat
	lon = vehicle.location.global_frame.lon
	
	time.sleep(1)

