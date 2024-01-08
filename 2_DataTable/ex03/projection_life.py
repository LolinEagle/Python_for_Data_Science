from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    ley = load("../ex00/life_expectancy_years.csv")
    life = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    plt.show()


if __name__ == "__main__":
    main()
