import time


print("Robot System Start")


for angle in range(0,91,10):
    print("Joint Angle:", angle)
    time.sleep(0.2)


print("Robot Move Finished")