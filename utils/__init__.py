import random

import numpy as np

from config.config import DataPoint, distributions_x, Activity


def encode(datapoints: list[DataPoint], prediction) -> float:
    """
    Predicts the activity based on the datapoints.

    :param datapoints: list of datapoints
    :return: predicted activity
    """

    average_x = np.mean([dp.x for dp in datapoints])

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
    elif activity == Activity.RUNNING:
        return random.uniform(3.0, 3.7)
    elif activity == Activity.CYCLING:
        return random.uniform(6.0, 7.0)
    else:
        return random.uniform(0, 0.5)
