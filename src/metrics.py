import numpy as np

def mse(reference, estimate):
    """
    Mean Squared Error between reference and estimate
    """
    return np.mean((reference - estimate) ** 2)

def snr(signal, noise):
    """
    Signal-to-Noise Ration in dB

    Parameters
    ----------
    signal: np.ndarray
        Clean signal
    noise: np.ndarray
        Noise component (estimate - clean)
    
    Returns
    --------
    float
        SNR in decibels
    """
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    return 10 * np.log10(signal_power / noise_power)
