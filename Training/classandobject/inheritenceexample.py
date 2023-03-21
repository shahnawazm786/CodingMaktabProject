class Camera():
    def __init__(self):
        print('Modern camera clicks photos and recrod videos')
    def click(self):
        print('Clicking photos')
    def record(self):
        print('Recording videos')

c= Camera()
c.click()
c.record()

class SonyCemera(Camera):
    def __init__(self):
        print("Sony camera")

s=SonyCemera()

