import numpy as np
import pandas as pd

from utils import random_rows


def make_missing(df, column, percent, logger, table):
    """Replace random values with NULL."""

    if column not in df.columns:
        return
    
    rows = random_rows(df, percent)

    df.loc[rows, column] = np.nan

    logger.log(
        table,
        column,
        "Missing Values",
        len(rows)
    )


def add_spaces(df, column, percent, logger, table):
    """Add leading and trailing spaces."""

    if column not in df.columns:
        return
    
    rows = random_rows(df, percent)

    df.loc[rows, column] = (
        df.loc[rows, column]
        .fillna("")
        .astype(str)
        .apply(lambda x: f"   {x}   ")
    )

    logger.log(
        table,
        column,
        "Extra Spaces",
        len(rows)
    )


def uppercase(df, column, percent, logger, table):
    """Convert random text values to uppercase."""

    if column not in df.columns:
        return
    
    rows = random_rows(df, percent)

    df.loc[rows, column] = (
        df.loc[rows, column]
        .fillna("")
        .astype(str)
        .str.upper()
    )

    logger.log(
        table,
        column,
        "Uppercase",
        len(rows)
    )


def duplicate_rows(df, percent, logger, table):
    """Duplicate random rows."""

    rows = random_rows(df, percent)

    duplicated = df.loc[rows]

    df = pd.concat([df, duplicated], ignore_index=True)

    logger.log(
        table,
        "Entire Row",
        "Duplicated Rows",
        len(rows)
    )

    return df


def negative_values(df, column, percent, logger, table):
    """Convert numeric values to negative."""

    if column not in df.columns:
        return

    rows = random_rows(df, percent)

    df.loc[rows, column] = -abs(df.loc[rows, column])

    logger.log(
        table,
        column,
        "Negative Values",
        len(rows)
    )

