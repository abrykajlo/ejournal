from ._device import Device
from .display import Display

class KoboSage(Device):
    def __init__(self):
        Device.__init__(self)
        self.display = Display((1440, 1920), 300)
    
    def get_pagesize(self) -> (float, float):
        return self.display.get_pagesize()
