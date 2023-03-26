import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:

        array = np.array(list).reshape(3, 3)
        calculations = {
            name: [fun(array, axis=x).tolist()
                   for x in [0, 1, None]]
            for (name, fun)
            in zip(['mean', 'variance', 'standard deviation', 'max', 'min', 'sum'],
                   [np.mean, np.var, np.std, np.max, np.min, np.sum])
        }
        return calculations
