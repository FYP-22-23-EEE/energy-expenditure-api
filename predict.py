import random
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

import numpy as np


class Activity(Enum):
    SITTING = 1
    STANDING = 2
    WALKING = 3
    RUNNING = 4

    @classmethod
    def from_string(cls, s):
        if s.lower() == 'sitting':
            return cls.SITTING
        elif s.lower() == 'standing':
            return cls.STANDING
        elif s.lower() == 'walking':
            return cls.WALKING
        elif s.lower() == 'running':
            return cls.RUNNING

    def __str__(self):
        return self.name.lower()

    max: float


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
    Activity.WALKING: Distribution(mean=5.0, std=0.3, min=4.1, max=7.0),
    Activity.RUNNING: Distribution(mean=9.0, std=0.5, min=7.1, max=12.0)
}
distributions_y = {
    Activity.SITTING: Distribution(mean=1.0, std=0.1, min=12.1, max=14.0),
    Activity.STANDING: Distribution(mean=3.0, std=0.1, min=14.1, max=16.0),
    Activity.WALKING: Distribution(mean=5.0, std=0.3, min=16.1, max=19.0),
    Activity.RUNNING: Distribution(mean=9.0, std=0.5, min=19.1, max=24.0)
}
distributions_z = {
    Activity.SITTING: Distribution(mean=1.0, std=0.1, min=24.1, max=26.0),
    Activity.STANDING: Distribution(mean=3.0, std=0.1, min=26.1, max=28.0),
    Activity.WALKING: Distribution(mean=5.0, std=0.3, min=28.1, max=31.0),
    Activity.RUNNING: Distribution(mean=9.0, std=0.5, min=31.1, max=36.0)
}


def predict(datapoints: list[DataPoint]) -> float:
    """
    Predicts the activity based on the datapoints.

    :param datapoints: list of datapoints
    :return: predicted activity
    """
    average_x = np.mean([dp.x for dp in datapoints])
    average_y = np.mean([dp.y for dp in datapoints])
    average_z = np.mean([dp.z for dp in datapoints])

    # check activity
    activity = None
    for k in distributions_x.keys():
        print(distributions_x[k].min, average_x, distributions_x[k].max)
        if distributions_x[k].min <= average_x <= distributions_x[k].max:
            activity = k
            break

    print(f'activity: {activity}', f'average_x: {average_x}')
    if activity == Activity.SITTING:
        return random.uniform(0.75, 1.2)
    elif activity == Activity.STANDING:
        return random.uniform(0.80, 1.3)
    elif activity == Activity.WALKING:
        return random.uniform(3.0, 3.7)
    elif activity == Activity.RUNNING:
        return random.uniform(6.0, 7.0)
    else:
        return random.uniform(0, 0.5)
