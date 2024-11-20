import numpy as np
import matplotlib.pyplot as plt

def load_waveform_data(file_path, skip_rows=15):
    """
    Loads waveform data from a text file and extracts time and voltage channels.

    Args:
        file_path (str): Path to the input text file containing waveform data.
        skip_rows (int): Number of initial lines to skip in the file (metadata or headers).

    Returns:
        tuple: A tuple containing:
            - time (ndarray): Array of time values in microseconds (µs).
            - channel1 (ndarray): Voltage data for Channel 1.
            - channel2 (ndarray): Voltage data for Channel 2.
    """
    # Load data from the text file, skipping metadata rows
    data = np.loadtxt(file_path, skiprows=skip_rows)

    # Extract columns and scale time to microseconds
    time = data[:, 0] * 1e6  # Convert time to microseconds
    channel1 = data[:, 1]  # Voltage data for Channel 1
    channel2 = data[:, 2]  # Voltage data for Channel 2

    return time, channel1, channel2

def plot_waveform(time, channel1, channel2, output_file='Waveform.pdf'):
    """
    Plots waveform data for two channels and saves the plot to a PDF file.

    Args:
        time (ndarray): Array of time values in microseconds (µs).
        channel1 (ndarray): Voltage data for Channel 1.
        channel2 (ndarray): Voltage data for Channel 2.
        output_file (str): Path to save the generated plot as a PDF.

    Returns:
        None
    """
    # Set up the figure size
    plt.figure(figsize=(8, 6))

    # Configure font size for better readability
    plt.rcParams.update({'font.size': 16})

    # Plot data for each channel
    plt.plot(time, channel1, color='purple', label='Channel 1')
    plt.plot(time, channel2, color='blue', linestyle='dashed', label='Channel 2')

    # Add labels and layout adjustments
    plt.xlabel('Time (µs)')
    plt.ylabel('Voltage (V)')
    plt.tight_layout()

    # Add grid lines to the plot
    plt.grid(True)

    # Set axis ranges
    plt.ylim(-17, 17)  # Voltage range from -17 to 17 V
    plt.xlim(-180, 180)  # Time range from -180 to 180 µs

    # Add a legend to the plot
    plt.legend(loc='upper right')

    # Save the plot as a PDF
    plt.savefig(output_file)

    # Display the plot on screen
    plt.show()

def main():
    """
    Main function to load waveform data, process it, and plot the waveform.

    Args:
        None

    Returns:
        None
    """
    # Input and output file paths
    input_file = 'waveform_data.txt'  # Input data file in the same directory
    output_file = 'Waveform.pdf'  # Output PDF file for the plot

    # Load waveform data
    time, channel1, channel2 = load_waveform_data(input_file)

    # Plot and save the waveform
    plot_waveform(time, channel1, channel2, output_file)

if __name__ == '__main__':
    main()
