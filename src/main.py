import matplotlib.pyplot as plt
from plot import create_plot

# from data import get_data
from data import get_data

def main(save: bool = False, file_path: str = "img/bitcoin_rainbow_chart.png"):
    # Load data
    raw_data,popt=get_data("data/newadadata.csv")

    # Create plot
    create_plot(raw_data, popt)

    # Show plot
    if save:
        plt.savefig(file_path, bbox_inches="tight", dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    main()
