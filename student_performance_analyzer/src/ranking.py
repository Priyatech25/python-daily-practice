import pandas as pd

def rank_students(df: pd.DataFrame) -> pd.DataFrame:
    ranked_df = df.copy()

    ranked_df["rank"] = ranked_df["marks"].rank(
        method="dense", ascending=False
    ).astype(int)

    ranked_df.sort_values("rank", inplace=True)

    return ranked_df

def calculate_percentile(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["percentile"] = df["marks"].rank(pct=True) * 100
    return df
