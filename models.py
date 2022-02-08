class Segment(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake(object):
    def __init__(self, segments):
        self.segments = segments
