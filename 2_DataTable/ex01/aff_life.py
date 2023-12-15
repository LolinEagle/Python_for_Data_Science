from load_csv import load
import matplotlib.pyplot as plt
import seaborn


def main():
    le = "Life Expectancy"
    ley = load("../ex00/life_expectancy_years.csv")
    ley_melt = ley.melt(id_vars=["country"], var_name="Year", value_name=le)
    ley_france = ley_melt[ley_melt["country"] == "France"]

    # Lineplot
    ley_lineplot = seaborn.lineplot(data=ley_france, x="Year", y=le)
    ley_lineplot.set_xlabel("Year")
    ley_lineplot.set_ylabel("Life Expectancy")
    ley_lineplot.set_title("France Life Expectancy Projections")
    ley_lineplot.set_xticks(range(0, 300, 40))
    plt.show()


if __name__ == "__main__":
    main()
