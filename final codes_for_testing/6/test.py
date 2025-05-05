import unittest
from c import ElevationMap

class TestElevationMap(unittest.TestCase):

    def test_init_empty_data(self):
        elevation_data = []
        em = ElevationMap(elevation_data)
        self.assertEqual(em.data, [])

    def test_init_single_data(self):
        elevation_data = [(0.0, 100.0, 200.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.data, [(0.0, 100.0, 200.0)])

    def test_init_multiple_data(self):
        elevation_data = [(1.0, 50.0, 150.0), (0.5, 75.0, 125.0), (2.0, 25.0, 175.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.data, [(0.5, 75.0, 125.0), (1.0, 50.0, 150.0), (2.0, 25.0, 175.0)])

    def test_init_negative_data(self):
        elevation_data = [(-1.0, 50.0, 150.0), (-0.5, 75.0, 125.0), (-2.0, 25.0, 175.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.data, [(-2.0, 25.0, 175.0), (-1.0, 50.0, 150.0), (-0.5, 75.0, 125.0)])

    def test_init_duplicate_data(self):
        elevation_data = [(1.0, 50.0, 150.0), (1.0, 75.0, 125.0), (1.0, 25.0, 175.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.data, [(1.0, 50.0, 150.0), (1.0, 75.0, 125.0), (1.0, 25.0, 175.0)])

    def test_get_elevation(self):
        elevation_data = [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0), (37.5, 80.0, 180.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.get_elevation(37.7749), (37.7749, 100.0, 200.0))

    def test_get_nearest_elevation(self):
        elevation_data = [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0), (37.5, 80.0, 180.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.get_nearest_elevation(37.8), (38.0, 150.0, 250.0))

    def test_get_range(self):
        elevation_data = [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0), (37.5, 80.0, 180.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.get_range(37.5, 38.0), [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0)])

    def test_average_elevation(self):
        elevation_data = [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0), (37.5, 80.0, 180.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.average_elevation(37.5, 38.0), 175.0)

    def test_find_maximum(self):
        elevation_data = [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0), (37.5, 80.0, 180.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.find_maximum(), (38.0, 150.0, 250.0))

    def test_find_minimum(self):
        elevation_data = [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0), (37.5, 80.0, 180.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.find_minimum(), (37.5, 80.0, 180.0))

    def test_elevation_gradient(self):
        elevation_data = [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0), (37.5, 80.0, 180.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.elevation_gradient(37.5, 38.0), 70.0)

    def test_filter_by_elevation(self):
        elevation_data = [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0), (37.5, 80.0, 180.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.filter_by_elevation(100.0, 200.0), [(37.7749, 100.0, 200.0)])

    def test_segment_analysis(self):
        elevation_data = [(37.7749, 100.0, 200.0), (38.0, 150.0, 250.0), (37.5, 80.0, 180.0)]
        em = ElevationMap(elevation_data)
        self.assertEqual(em.segment_analysis(0.5), [(37.7749, 100.0), (38.2749, 150.0)])

if __name__ == '__main__':
    unittest.main()
