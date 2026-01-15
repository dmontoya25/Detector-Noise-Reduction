import numpy as np
def moving_average(signal, window_size=15):
    """
    Apply a simple moving average filter.
    
    Parameters:
        signal : np.array
            Input signal
        window_size : int
            Number of samples to average
    Returns:
        np.array : filtered signal
    """
    window = np.ones(window_size) / window_size
    return np.convolve(signal, window, mode='same')
