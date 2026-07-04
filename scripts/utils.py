import numpy as np

def random_rows(df, percent):

    count = max(1, int(len(df) * percent))

    return np.random.choice(
        df.index,
        count,
        replace=False
    )