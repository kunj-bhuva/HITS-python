import unittest
from c import ElevationMap
class TestElevationMap(unittest.TestCase):

    def test_get_elevation(self):
        elevation_map = ElevationMap([(1.0, 2.0, 3.0), (2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])
        self.assertEqual(elevation_map.get_elevation(2.0), (2.0, 3.0, 4.0))
        self.assertIsNone(elevation_map.get_elevation(4.0))

    def test_get_nearest_elevation(self):
        elevation_map = ElevationMap([(1.0, 2.0, 3.0), (2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])
        self.assertEqual(elevation_map.get_nearest_elevation(2.5), (3.0, 4.0, 5.0))
        self.assertEqual(elevation_map.get_nearest_elevation(1.5), (1.0, 2.0, 3.0))

    def test_get_range(self):
        elevation_map = ElevationMap([(1.0, 2.0, 3.0), (2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])
        self.assertEqual(elevation_map.get_range(1.5, 3.5), [(2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])

    def test_average_elevation(self):
        elevation_map = ElevationMap([(1.0, 2.0, 3.0), (2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])
        self.assertEqual(elevation_map.average_elevation(1.5, 3.5), 4.5)

    def test_find_maximum(self):
        elevation_map = ElevationMap([(1.0, 2.0, 3.0), (2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])
        self.assertEqual(elevation_map.find_maximum(), (3.0, 4.0, 5.0))

    def test_find_minimum(self):
        elevation_map = ElevationMap([(1.0, 2.0, 3.0), (2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])
        self.assertEqual(elevation_map.find_minimum(), (1.0, 2.0, 3.0))

    def test_elevation_gradient(self):
        elevation_map = ElevationMap([(1.0, 2.0, 3.0), (2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])
        self.assertAlmostEqual(elevation_map.elevation_gradient(1.0, 3.0), 1.0)

    def test_filter_by_elevation(self):
        elevation_map = ElevationMap([(1.0, 2.0, 3.0), (2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])
        self.assertEqual(elevation_map.filter_by_elevation(3.0, 4.0), [(2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])

    def test_segment_analysis(self):
        elevation_map = ElevationMap([(1.0, 2.0, 3.0), (2.0, 3.0, 4.0), (3.0, 4.0, 5.0)])
        self.assertEqual(elevation_map.segment_analysis(1.0), [(1.0, 3.0), (2.0, 4.0), (3.0, 5.0)])

if __name__ == '__main__':
    unittest.main()