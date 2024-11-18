import pandas as pd
import matplotlib.pyplot as plt

"""
CSV file with the following columns:
- rows: Number of rows of the tested matrix
- cols: Number of columns of the tested matrix
- attempt: Number of the attempt of the sum of the matrix with r rows and c columns
- time: Time in seconds that the attempt took
- operation: Type of algorithm used to sum the matrix (0 for the first algorithm, 1 for the second algorithm)
"""

operations = ['Sum by rows', 'Sum by columns']

def summarize_data(file):
    data = pd.read_csv(file)
    return data.describe()

def graph_results(file):
    data = pd.read_csv(file)
    # Group by type of algorithm
    grouped_data = data.groupby('operation')
    # In each group, plot the time vs the number of rows and columns (for multiple attempts calculate the average time)
    # Also, add a legend with the name of the algorithm
    for name, group in grouped_data:
        group = group.groupby(['rows', 'cols']).mean()
        group = group.reset_index()
        plt.plot(group['rows'], group['time'], label=operations[name])
    plt.xlabel('Number of rows')
    plt.ylabel('Time (s)')
    plt.legend()
    # Save the plot to a file
    plt.savefig('results.png')

def main():
    file_name = 'results.csv'
    analised_data = summarize_data(file_name)
    print(analised_data)
    graph_results(file_name)

if __name__ == '__main__':
    main()