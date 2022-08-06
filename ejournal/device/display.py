from reportlab.lib.units import inch

class Display:
    def __init__(self, resolution: (int, int), ppi: int):
        self.resolution = resolution
        self.ppi = ppi

    def get_pagesize(self) -> (float, float):
        return tuple([x * inch / self.ppi for x in self.resolution])
