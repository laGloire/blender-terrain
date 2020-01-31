import math

# see conversion formulas at
# http://en.wikipedia.org/wiki/Transverse_Mercator_projection
# and
# http://mathworld.wolfram.com/MercatorProjection.html
class Mercator:
    radius = 6378137

    def __init__(self, **kwargs):
        # setting default values
        self.lat = 0 # in degrees
        self.lon = 0 # in degrees
        self.k = 1 # scale factor
        
        for attr in kwargs:
            setattr(self, attr, kwargs[attr])
        self.latInRadians = math.radians(self.lat)

    def fromGeographic(self, lat, lon):
        lat = math.radians(lat - self.lat)
        lon = math.radians(lon - self.lon)
        x = self.k * self.radius * lon
        y = self.k * self.radius * math.log( math.tan(lat) + (1 / math.cos(lat)))
        return (x,y)

    def toGeographic(self, x, y):
        x = x/(self.k * self.radius)
        y = y/(self.k * self.radius)

        lat = math.degrees(lat)
        lon = self.lon + math.degrees(lon)
        return (lat, lon)
