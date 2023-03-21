class camera:
    def __init__(self):
        print('click to photo and video')
    def click(self):
        print('Take photo')


#c=camera()
#c.click()
class Sony_camera(camera):
    def __init__(self):
        print('Sony camera')
    def sony_range(self):
        print('Up to 500 meter')

s=Sony_camera()
s.click()
s.sony_range()

class Cannon(camera):
    def __init__(self):
        print('Cannon Camera')
    def bluetooth(self):
        print('Cannon has blue tooth')

c=Cannon()
c.click()
c.bluetooth()


