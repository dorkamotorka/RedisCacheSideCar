import matplotlib.pyplot as plt
import numpy as np

def plot_response_times(response_times_1, response_times_2):
    # Assuming response_times_1 and response_times_2 are lists of response times

    # Create a range of indices for the x-axis
    x_axis = np.arange(len(response_times_1))

    # Set the width of the bars
    bar_width = 0.35

    # Plot the response times as side-by-side bars with custom colors
    plt.bar(x_axis, response_times_1, width=bar_width, label='Response Time without Cache', color='#1f77b4', alpha=0.7)
    plt.bar(x_axis + bar_width, response_times_2, width=bar_width, label='Response Time with Cache', color='#ff7f0e', alpha=0.7)

    # Add data labels on top of the bars
    for i, (r1, r2) in enumerate(zip(response_times_1, response_times_2)):
        plt.text(i, r1 + 1, str(r1), ha='center', va='bottom', color='#1f77b4', fontweight='bold')
        plt.text(i + bar_width, r2 + 1, str(r2), ha='center', va='bottom', color='#ff7f0e', fontweight='bold')

    # Add labels and a legend
    plt.xlabel('Request')
    plt.ylabel('Response Time (ms)')
    plt.title('Comparison of Response Times')
    plt.xticks(x_axis + bar_width / 2, x_axis + 1)  # Center the x-axis labels between bars
    plt.legend()

    # Add a grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add a horizontal line at y=0 for reference
    plt.axhline(0, color='black',linewidth=0.5)

    # Customize the appearance of the plot
    plt.tight_layout()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Example response times (replace these with your actual data)
    response_times_1 = [0.396580]
    response_times_2 = [0.003464]

    percentage_speedup = ((response_times_1[0] - response_times_2[0]) / response_times_1[0]) * 100
    print(f"The percentage speedup is: {percentage_speedup:.2f}%")  


    # Plot the response times as a side-by-side bar chart
    plot_response_times(response_times_1, response_times_2)
