"""
    7.	Write a python function that receives a random number of numerical parameters 
        and displays a normal distribution graph based on the parameter values. 
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_normal_distribution(*values):
    # Convert the parameters to a NumPy array
    data = np.array(values)

    # Create the normal distribution curve
    mean = np.mean(data)
    std = np.std(data)
    
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    y = (1/(std * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mean)/std)**2)

    # Plot the graph
    plt.plot(x, y)
    plt.title("Normal Distribution Curve")
    plt.xlabel("Values")
    plt.ylabel("Probability Density")
    plt.grid(True)
    plt.show()

# Example (you can pass ANY number of values)
plot_normal_distribution(2, 5, 7, 9, 12, 15)