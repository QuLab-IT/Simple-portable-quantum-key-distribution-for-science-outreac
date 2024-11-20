# Simple portable quantum key distribution for science outreach

This repository contains scripts and data files for analyzing photon delay data and visualizing waveform data, used for the paper: Simple portable quantum key distribution for science outreach. 

---

## Repository Structure

Simple portable quantum key distribution for science outreach
- **Data_pulses_delay_link.txt**: A txt file where the link to the data is provided
- **Delay_analysis.py**: Python script designed to analyze the delay of photons based on the data provided.
- **plot_waveform.py**: Script to visualize and plot the waveform data for better understanding.
- **waveform_data.txt**: Contains the input data for the waveform visualization script.
- **README.md**: Detailed documentation about the project, including how to use the scripts.
- **requirements.txt**: List of required Python libraries and dependencies to run the scripts.




---

## Overview

The project consists of two main scripts:

1. **Delay_analysis**:
   - Processes photon arrival delays triggered by specific events and generates a histogram of time delays.
   - Input data: Data_pulses_delay.txt (Accessed through link)
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
Download data from the link provided in `Data_pulses_delay_link.txt` and added to the folder.

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




