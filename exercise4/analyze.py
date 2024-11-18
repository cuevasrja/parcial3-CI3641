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
scale = [100, 1000, 10000, 100000, 1000000]

def summarize_data(file):
    data = pd.read_csv(file)
    return data.describe()

def graph_results(file):
    data = pd.read_csv(file)
    # Group by type of algorithm
    grouped_data = data.groupby('operation')
    # In each group, plot the time vs the number of rows and columns (for multiple attempts calculate the average time)
    # Also, add a legend with the name of the algorithm
    # Show x and y axis in 10^(2, 3, 4, 5, 6)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for name, group in grouped_data:
        group = group.groupby(['rows', 'cols']).mean()
        group = group.reset_index()
        # Remove the 'attempt' column
        group = group.drop(columns=['attempt'])
        group['operation'] = operations[name]
        # Plot the data. In x axis the number of rows, in y axis the number of columns and in z axis the time
        ax.scatter(group['rows'], group['cols'], group['time'], label=operations[name])
        # Print without attempt column and change the name of the operation to the name of the algorithm
        print(group)


    ax.set_xlim(100, 1000000)
    ax.set_ylim(100, 1000000)
    ax.set_zlim(0, 0.7)
    ax.set_xlabel('Rows')
    ax.set_ylabel('Columns')
    ax.set_zlabel('Time (s)')
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