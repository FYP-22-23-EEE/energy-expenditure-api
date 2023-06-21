from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Activity(Enum):
    SITTING = 1
    STANDING = 2
    RUNNING = 3
    CYCLING = 4

    @classmethod
    def from_string(cls, s):
        if s.lower() == 'sitting':
            return cls.SITTING
        elif s.lower() == 'standing':
            return cls.STANDING
        elif s.lower() == 'running':
            return cls.RUNNING
        elif s.lower() == 'cycling':
            return cls.CYCLING

    def __str__(self):
        return self.name.lower()


class DeviceType(Enum):
    E4 = 1
    MUSE = 2
    ZEPHYR = 3
    EARBUDS = 4

    @classmethod
    def from_string(cls, s):
        if s.lower() == 'e4':
            return cls.E4
        elif s.lower() == 'muse':
            return cls.MUSE
        elif s.lower() == 'zephyr':
            return cls.ZEPHYR
        elif s.lower() == 'earbuds':
            return cls.EARBUDS

    def __str__(self):
        return self.name.lower()


@dataclass
class Distribution:
    mean: float
    std: float
    min: float
    max: float


@dataclass
class DataPoint:
    timestamp: datetime
    device: DeviceType
    x: float
    y: float
    z: float

    def to_dict(self):
        return {
            'timestamp': self.timestamp.isoformat(),
            'device': self.device.name,
            'x': self.x,
            'y': self.y,
            'z': self.z
        }

    def __str__(self):
        return str(self.to_dict())


distributions_x = {
    Activity.SITTING: Distribution(mean=1.0, std=0.1, min=0.0, max=2.0),
    Activity.STANDING: Distribution(mean=3.0, std=0.1, min=2.1, max=4.0),
    Activity.RUNNING: Distribution(mean=5.0, std=0.3, min=4.1, max=7.0),
    Activity.CYCLING: Distribution(mean=9.0, std=0.5, min=7.1, max=12.0)
}
distributions_y = {
    Activity.SITTING: Distribution(mean=1.0, std=0.1, min=12.1, max=14.0),
    Activity.STANDING: Distribution(mean=3.0, std=0.1, min=14.1, max=16.0),
    Activity.RUNNING: Distribution(mean=5.0, std=0.3, min=16.1, max=19.0),
    Activity.CYCLING: Distribution(mean=9.0, std=0.5, min=19.1, max=24.0)
}
distributions_z = {
    Activity.SITTING: Distribution(mean=1.0, std=0.1, min=24.1, max=26.0),
    Activity.STANDING: Distribution(mean=3.0, std=0.1, min=26.1, max=28.0),
    Activity.RUNNING: Distribution(mean=5.0, std=0.3, min=28.1, max=31.0),
    Activity.CYCLING: Distribution(mean=9.0, std=0.5, min=31.1, max=36.0)
}
