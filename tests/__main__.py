import unittest
from reportlab.lib.units import inch
from ejournal.device.devices import KoboSage

class TestPageSize(unittest.TestCase):
    def test_kobosage(self):
        sage = KoboSage()
        pagesize = sage.get_pagesize()
        self.assertAlmostEqual(pagesize[0], 4.8*inch)
        self.assertAlmostEqual(pagesize[1], 6.4*inch)

if __name__ == '__main__':
    unittest.main()
