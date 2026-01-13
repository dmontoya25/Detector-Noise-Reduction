# Noise Reduction and Signal Reconstruction for Simulated Particle Detector Waveforms

## Overview

Particle detectors produce noisy signals due to electronic noise and environmental effects; this project explores classical and ML-based approaches to recover underlying physical signals.

## Project Goals

This project implements and compares different noise reduction techniques for simulated particle detector waveforms:

1. **Generate clean detector-like signals** - Simulate realistic detector waveforms
2. **Add realistic noise** - Model electronic noise and environmental effects
3. **Apply classical filtering** - Implement traditional signal processing methods
4. **Apply ML-based denoising** - Explore machine learning approaches for signal reconstruction
5. **Compare results** - Evaluate and compare the performance of different methods


```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/dmontoya25/Detector-Noise-Reduction.git
cd Detector-Noise-Reduction
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Signal Generation

Start with the signal generation notebook to create clean detector waveforms:

```bash
jupyter notebook notebooks/01_signal_generation.ipynb
```

### Adding Noise

Use the noise module to add realistic noise to clean signals:

```python
from src.noise import add_noise
noisy_signal = add_noise(clean_signal)
```

### Classical Filtering

Apply traditional signal processing filters:

```python
from src.filters import apply_filter
filtered_signal = apply_filter(noisy_signal)
```

### ML-Based Denoising

Use machine learning models for signal reconstruction:

```python
from src.models import denoise_signal
reconstructed_signal = denoise_signal(noisy_signal)
```

## Methodology

This project takes a systematic approach to noise reduction:

1. **Signal Simulation**: Generate realistic detector waveforms with known ground truth
2. **Noise Modeling**: Add controlled noise to simulate real-world detector conditions
3. **Baseline Methods**: Implement classical filtering techniques (e.g., low-pass, band-pass, Kalman filters)
4. **ML Approaches**: Train and evaluate machine learning models (e.g., autoencoders, CNNs, transformers)
5. **Evaluation**: Compare methods using metrics such as SNR, MSE, and signal fidelity

