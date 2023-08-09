import numpy as np
import pandas as pd

def main():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df = pd.DataFrame(data, columns=["A", "B", "C"])

    df["Sum"] = df["A"] + df["B"] + df["C"]
    df["Product"] = df["A"] * df["B"] * df["C"]

    print("Processed DataFrame:")
    print(df)

if __name__ == "__main__":
    main()
