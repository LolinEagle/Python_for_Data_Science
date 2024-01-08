from load_csv import load
import matplotlib.pyplot as plt
import seaborn


def main():
    p = "Population"
    y = "Year"
    pop = load("population_total.csv")

    # Melt
    pop_melt = pop.melt(id_vars=["country"], var_name=y, value_name=p)
    pop_fr = pop_melt[(pop_melt["country"] == "France") &
                      (pop_melt[y].astype(int).between(1800, 2050))]
    pop_be = pop_melt[(pop_melt["country"] == "Belgium") &
                      (pop_melt[y].astype(int).between(1800, 2050))]

    # Parsing
    pop_fr.loc[:, p] = pop_fr[p].str.replace('M', '').astype(float)
    pop_be.loc[:, p] = pop_be[p].str.replace('M', '').astype(float)

    # Lineplot
    pop_lineplot = seaborn.lineplot(data=pop_be, x=y, y=p, color="blue")
    pop_lineplot = seaborn.lineplot(data=pop_fr, x=y, y=p, color="green")
    pop_lineplot.set_xlabel(y)
    pop_lineplot.set_ylabel(p)
    pop_lineplot.set_title("Population Projections")
    pop_lineplot.set_xticks(range(0, 251, 40))
    pop_lineplot.set_yticks(range(0, 61, 20))
    pop_lineplot.set_yticklabels([None, "20M", "40M", "60M"])
    line2d = [plt.Line2D([0], [0], color='blue'),
              plt.Line2D([0], [0], color='green')]
    plt.legend(labels=["Belgium", "France"], loc="lower right", handles=line2d)
    plt.show()


if __name__ == "__main__":
    main()
