import os
import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    """
    Reads the input data file, skipping the first two header lines.
    
    Args:
        filename (str): Path to the input data file.
    
    Returns:
        list: A list of strings, where each string represents a line of data after the header.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()[2:]  # Skip the header lines
    return lines

def process_data(lines):
    """
    Processes the lines of the input file to extract time differences for event types. To do this it starts a timer after each event in channel 4 and saves the time from each event in either channel 1 or 2.
    
    Args:
        lines (list): A list of strings where each string is a line from the data file.
    
    Returns:
        tuple: Two lists of time differences in microseconds:
            - time_diff_4_1_microsec: Time differences between event type '1' and trigger '4'.
            - time_diff_4_2_microsec: Time differences between event type '2' and trigger '4'.
    """
    # Initialize storage for time differences
    time_diff_4_2 = []
    time_diff_4_1 = []
    event_time_trigger = 0  # Tracks the time of the last trigger event (type '4')

    # Process each line of data
    for line in lines:
        line_values = line.strip().split('|')  # Split the line into columns
        event_type = line_values[1].strip()  # Extract the event type
        event_time = int(line_values[2].strip())  # Extract the event time as an integer

        # Update trigger time or calculate time differences
        if event_type == '4':
            event_time_trigger = event_time  # Update the trigger time
        elif event_type == '1':
            time_diff_4_1.append(event_time - event_time_trigger)
        elif event_type == '2':
            time_diff_4_2.append(event_time - event_time_trigger)

    # Convert time differences to microseconds
    time_diff_4_1_microsec = [x / 1_000_000 for x in time_diff_4_1]
    time_diff_4_2_microsec = [x / 1_000_000 for x in time_diff_4_2]

    return time_diff_4_1_microsec, time_diff_4_2_microsec

def plot_histogram(time_diff_4_1_microsec, time_diff_4_2_microsec, output_file):
    """
    Plots and saves a histogram of time differences for the two event types.
    
    Args:
        time_diff_4_1_microsec (list): Time differences for event type '1' in microseconds.
        time_diff_4_2_microsec (list): Time differences for event type '2' in microseconds.
        output_file (str): Path to save the generated histogram plot as a PDF.
    
    Returns:
        None
    """
    # Define histogram parameters
    bins = 200  # Number of bins for the histogram
    range_min = 0  # Minimum value for the histogram range
    range_max = 20  # Maximum value for the histogram range
    bin_edges = np.linspace(range_min, range_max, bins + 1)  # Define bin edges

    # Create a figure for the plot
    plt.figure(figsize=(8, 6))
    plt.rcParams.update({'font.size': 16})  # Increase font size for readability

    # Plot histograms for each event type
    plt.hist(time_diff_4_1_microsec, bins=bin_edges, color='black', alpha=0.7, 
             label='Z Basis', linestyle='dashed')
    plt.hist(time_diff_4_2_microsec, bins=bin_edges, color='gray', alpha=0.7, 
             label='X Basis', linestyle='dashdot')

    # Add labels, legend, and layout adjustments
    plt.xlabel('Time of arrival after trigger pulse ($\mu s$)')
    plt.ylabel('Number of photons')
    plt.legend()
    plt.tight_layout()

    # Save the plot to a file and display it
    plt.savefig(output_file)
    plt.show()

def main():
    """
    Main function to coordinate reading data, processing it, and generating the plot.
    
    Args:
        None
    
    Returns:
        None
    """
    # Set default file paths
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
    input_file = os.path.join(script_dir, 'Data_pulses_delay.txt')  # Input data file
    output_file = os.path.join(script_dir, 'Delay_Distribution.pdf')  # Output plot file

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} does not exist.")
        return

    # Read and process data
    lines = read_data(input_file)
    time_diff_4_1_microsec, time_diff_4_2_microsec = process_data(lines)

    # Generate and save the plot
    plot_histogram(time_diff_4_1_microsec, time_diff_4_2_microsec, output_file)

if __name__ == '__main__':
    main()
