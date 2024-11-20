# Simple portable quantum key distribution for science outreach

This repository contains scripts and data files for analyzing photon delay data and visualizing waveform data, used for the paper: Simple portable quantum key distribution for science outreach. 

---

## Repository Structure

Simple portable quantum key distribution for science outreach/ 
├── Data_pulses_delay.zip    # Zipped input file for photon delay analysis 
├── Delay_analysis.py        # Photon delay analysis script 
├── plot_waveform.py         # Waveform visualization script 
├── waveform_data.txt        # Input file for waveform visualization 
├── README.md                # Project documentation 
└── requirements.txt         # Python dependencies



---

## Overview

The project consists of two main scripts:

1. **Delay_analysis**:
   - Processes photon arrival delays triggered by specific events and generates a histogram of time delays.
   - Input data: Data_pulses_delay.zip (contains the required data file)
   - Output: `Delay_Distribution.pdf`.

2. **Waveform Visualization**:
   - Plots the time-voltage graph for two voltage channels and generates a waveform graph.
   - Input data: `waveform_data.txt`.
   - Output: `Waveform.pdf`.

---

## Installation and Requirements

### Prerequisites
- Python 3.7 or later.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/QuLab-IT/Simple-portable-quantum-key-distribution-for-science-outreac.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Scripts and Usage

### Photon Delay Analysis

**Script**: `Delay_analysis.py`  
**Purpose**: Analyzes photon delays triggered by event type `4` and calculates the time delays to event types `1` and `2`.

#### Input
Extract Data_pulses_delay.zip to retrieve Data_pulses_delay.txt, and place the file in the repository root.

#### Steps to Run
1. Execute the script:
    ```bash
    python Delay_analysis.py
    ```
2. The output histogram will be saved as `Delay_Distribution.pdf`.

---

### Waveform Visualization

**Script**: `plot_waveform.py`  
**Purpose**: Visualizes two voltage waveforms over time.

#### Input
Place `waveform_data.txt` in the repository root.


#### Steps to Run
1. Execute the script:
    ```bash
    python plot_waveform.py
    ```
2. The output graph will be saved as `Waveform.pdf`.

---




