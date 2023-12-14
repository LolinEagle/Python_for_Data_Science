import os
import pandas


def load(path: str):
    """def load(path: str)"""
    try:
        if not (os.path.exists(path)):
            raise FileNotFoundError("File not found")
        if not (os.access(path, os.R_OK)):
            raise PermissionError("Permission denied")
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        return
    df = pandas.read_csv(path)
    df.reset_index(drop=True)
    print(f"Loading dataset of dimensions {df.shape}")
    return (df)


def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
