import numpy as np
from sklearn.decomposition import PCA


def pca_denoise(signals, n_components=5):
    """
    Apply PCA-based denoising to a set of signals.

    Parameters
    ----------
    signals : np.ndarray
        Shape (n_samples, n_timepoints)
    n_components : int
        Number of principal components to keep

    Returns
    -------
    np.ndarray
        Denoised signals (same shape as input)
    """
    pca = PCA(n_components=n_components)
    
    # Fit PCA on noisy signals
    transformed = pca.fit_transform(signals)
    
    # Reconstruct signals using selected components
    reconstructed = pca.inverse_transform(transformed)
    
    return reconstructed
