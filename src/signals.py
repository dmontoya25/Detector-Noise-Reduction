import numpy as np

def gaussian_pulse(t, amplitude=1.0, t0=5.0, sigma=0.5):
    """
    Generate a Gaussian pulse representing a detector response.

    Parameters
    ----------
    t : np.ndarray
        Time axis
    amplitude : float
        Peak amplitude of the pulse
    t0 : float
        Time of pulse center
    sigma : float
        Pulse width (standard deviation)

    Returns
    -------
    np.ndarray
        Gaussian pulse signal
    """
    return amplitude * np.exp(-(t - t0)**2 / (2 * sigma**2))
