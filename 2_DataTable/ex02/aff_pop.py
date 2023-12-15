from load_csv import load
import matplotlib.pyplot as plt
import seaborn


def main():
    p = "Population"
    pop = load("population_total.csv")

    # Melt
    pop_melt = pop.melt(id_vars=["country"], var_name="Year", value_name=p)
    pop_france = pop_melt[pop_melt["country"] == "France"]
    pop_belgium = pop_melt[pop_melt["country"] == "Belgium"]

    # Parsing
    pop_france.loc[:, p] = pop_france[p].str.replace('M', '').astype(float)
    pop_belgium.loc[:, p] = pop_belgium[p].str.replace('M', '').astype(float)

    # Lineplot
    pop_lineplot = seaborn.lineplot(data=pop_france, x="Year", y=p)
    pop_lineplot = seaborn.lineplot(data=pop_belgium, x="Year", y=p)
    pop_lineplot.set_xlabel("Year")
    pop_lineplot.set_ylabel(p)
    pop_lineplot.set_title("Population Projections")
    pop_lineplot.set_xticks(range(0, 251, 40))
    pop_lineplot.set_yticks(range(0, 61, 20))
    pop_lineplot.set_yticklabels([None, "20M", "40M", "60M"])
    # plt.legend(labels=["Belgium", "France"])
    plt.show()


if __name__ == "__main__":
    main()
