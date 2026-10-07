"""A2 · MEMBER 2 · Summarise the deliveries for the manager."""

import pandas as pd


def summary_by_sector(df: pd.DataFrame) -> pd.DataFrame:
    """Return summary statistics for each sector."""

    result = (
        df.groupby("sector")
        .agg(
            deliveries=("delivery_id", "count"),
            total_litres=("litres", "sum"),
            rejection_rate=("rejected", "mean"),
        )
        .reset_index()
    )

    result["total_litres"] = result["total_litres"].round(1)
    result["rejection_rate"] = result["rejection_rate"].round(2)

    result = result.sort_values(
        ["total_litres", "sector"],
        ascending=[False, True],
    )

    return result.reset_index(drop=True)


def litres_by_day(df: pd.DataFrame) -> pd.DataFrame:
    """Return total litres collected for each day."""

    result = (
        df.groupby(df["date"].dt.date)["litres"]
        .sum()
        .round(1)
        .reset_index()
    )

    result.columns = ["date", "total_litres"]

    return result.reset_index(drop=True)