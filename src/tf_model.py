from control import TransferFunction, tf


def tf_1st_order_lag_model() -> TransferFunction:
    return tf([1], [1, 1])


def tf_2nd_order_lag_model() -> TransferFunction:
    return tf([1], [0.1, 0.2, 0.3])
