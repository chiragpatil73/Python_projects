import rotatescreen
import time
s = rotatescreen.get_primary_display()
for i in range(1,5):
    time.sleep(1)
    s.rotate_to(i*90%360)