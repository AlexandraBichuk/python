#import time
#end_time = time.time() + 20
#while time.time() < end_time:
    #print ("Ok lets wait 5 sec")
    #time.sleep(5)
#else:
    #print("Alarm")

def generator(rang):
    for num in range(rang):
        yield num

generator(10)



