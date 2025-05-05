from typing import List, Tuple, Optional
import math


class ElevationMap:
    def __init__(self, elevation_data: List[Tuple[float, float, float]]):
        self.data = sorted(elevation_data, key=lambda x: x[0])

    def get_elevation(self, latitude: float) -> Optional[Tuple[float, float, float]]:
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_lat = self.data[mid][0]
            if abs(mid_lat - latitude) < 1e-6:
                return self.data[mid]
            elif mid_lat < latitude:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def get_nearest_elevation(self, latitude: float) -> Tuple[float, float, float]:
        if not self.data:
            raise ValueError("Elevation data is empty")
        left, right = 0, len(self.data) - 1
        closest = self.data[0]
        while left <= right:
            mid = (left + right) // 2
            mid_entry = self.data[mid]
            if abs(mid_entry[0] - latitude) < abs(closest[0] - latitude):
                closest = mid_entry
            if mid_entry[0] < latitude:
                left = mid + 1
            else:
                right = mid - 1
        return closest

    def get_range(self, lat_min: float, lat_max: float) -> List[Tuple[float, float, float]]:
        return [entry for entry in self.data if lat_min <= entry[0] <= lat_max]

    def average_elevation(self, lat_min: float, lat_max: float) -> float:
        points = self.get_range(lat_min, lat_max)
        if not points:
            return 0.0
        return sum(p[2] for p in points) / len(points)

    def find_maximum(self) -> Tuple[float, float, float]:
        return max(self.data, key=lambda x: x[2])

    def find_minimum(self) -> Tuple[float, float, float]:
        return min(self.data, key=lambda x: x[2])

    def elevation_gradient(self, lat1: float, lat2: float) -> Optional[float]:
        point1 = self.get_nearest_elevation(lat1)
        point2 = self.get_nearest_elevation(lat2)
        if point1 and point2:
            dlat = abs(point2[0] - point1[0]) * 111.0
            return (point2[2] - point1[2]) / dlat if dlat != 0 else 0.0
        return None

    def filter_by_elevation(self, min_elev: float, max_elev: float) -> List[Tuple[float, float, float]]:
        return [p for p in self.data if min_elev <= p[2] <= max_elev]

    def segment_analysis(self, segment_size: float) -> List[Tuple[float, float]]:
        segments = []
        lat = self.data[0][0]
        max_lat = self.data[-1][0]
        while lat < max_lat:
            next_lat = lat + segment_size
            avg = self.average_elevation(lat, next_lat)
            segments.append((lat, avg))
            lat = next_lat
        return segments
