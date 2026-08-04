import random
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


def corrupt_dates(df, percent, logger, table):
    """
    Introduce realistic date quality issues into orders dataset.
    """

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    missing = [c for c in date_columns if c not in df.columns]

    if missing:
        print(f"[WARNING] {table}: missing date columns: {missing}")
        return
    
    rows = random_rows(df, percent)

    issue_counter = {
        "Future Purchase Date": 0,
        "Approved Before Purchase": 0,
        "Delivered Before Shipped": 0,
        "Missing Delivery Date": 0,
        "Extreme Delivery Delay": 0,
    }

    for row in rows:

        issue = random.choice([
            "future",
            "approved_before_purchase",
            "delivered_before_shipped",
            "missing_delivery",
            "long_delivery",
        ])

        purchase = pd.to_datetime(
            df.at[row, "order_approved_at"],
            errors="coerce"
        )

        approved = pd.to_datetime(
            df.at[row, "order_approved_at"],
            errors="coerce"
        )

        shipped = pd.to_datetime(
            df.at[row, "order_delivered_carrier_date"],
            errors="coerce"
        )

        delivered = pd.to_datetime(
            df.at[row, "order_delivered_customer_date"],
            errors="coerce"
        )

        if pd.isna(purchase):
            continue
        
        # ------------------------------------------------

        if issue == "future":

            df.at[row, "order_purchase_timestamp"] = (
                purchase + pd.Timedelta(days=3650)
            )

            issue_counter["Future Purchase Date"] += 1
        
        # ------------------------------------------------
        
        elif issue == "approved_before_purchase":

            if pd.notna(approved):

                df.at[row, "order_approved_at"] = (
                    purchase - pd.Timedelta(days=2)
                )

                issue_counter["Approved Before Purchase"] += 1
        
        # ------------------------------------------------
        
        elif issue == "delivered_before_shipped":

            if pd.notna(shipped):

                df.at[row, "order_delivered_carrier_date"] = (
                    shipped - pd.Timedelta(days=2)
                )

                issue_counter["Delivered Before Shipped"] += 1
        
        # ------------------------------------------------
        
        elif issue == "missing_delivery":

            df.at[row, "order_delivered_customer_date"] = pd.NaT

            issue_counter["Missing Delivery Date"] += 1
 
        # ------------------------------------------------
        
        elif issue == "long_delivery":

            df.at[row, "order_delivered_customer_date"] = (
                purchase - pd.Timedelta(days=500)
            )

            issue_counter["Extreme Delivery Delay"] += 1
    
    for issue, count in issue_counter.items():

        if count > 0:

            logger.log(
                table,
                "Date Columns",
                issue,
                count
            )