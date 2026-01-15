import numpy as np

def add_gaussian_noise(signal, noise_std=0.1):
    """
    Add Gaussian white noise to a signal.

    Parameters
    ----------
    signal : np.ndarray
        Clean input signal
    noise_std : float
        Standard deviation of Gaussian noise

    Returns
    -------
    np.ndarray
        Noisy signal
    """
    noise = np.random.normal(
        loc=0.0,
        scale=noise_std,
        size=signal.shape
    )
    return signal + noise
