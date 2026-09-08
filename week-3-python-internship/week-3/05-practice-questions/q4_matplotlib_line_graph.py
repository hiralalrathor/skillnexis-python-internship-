"""
Practice Q4: Use Matplotlib to plot a line graph.
"""

import matplotlib
matplotlib.use("Agg")  # allows saving the plot without a display
import matplotlib.pyplot as plt


def main():
    print("=== Matplotlib Line Graph ===")

    # Sample data: days vs temperature
    days = [1, 2, 3, 4, 5, 6, 7]
    temperature = [30, 32, 29, 35, 33, 31, 34]

    plt.figure(figsize=(8, 5))
    plt.plot(days, temperature, marker="o", color="blue", linestyle="-")
    plt.title("Temperature Over a Week")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)

    output_file = "line_graph.png"
    plt.savefig(output_file)
    print(f"Line graph saved as '{output_file}'.")


if __name__ == "__main__":
    main()
