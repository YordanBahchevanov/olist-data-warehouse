import random

import numpy as np
import pandas as pd

from config import *
from logger import ReportLogger

from dirty_data import *

# -----------------------------
# Random seed
# -----------------------------

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

logger = ReportLogger()


def save(df, filename):
    """Save dataframe to the messy folder."""
    df.to_csv(MESSY_DATA / filename, index=False)


print("=" * 60)
print("Generating Dirty Dataset...")
print("=" * 60)

# -----------------------------
# Customers
# -----------------------------

print("Processing customers...")

customers = pd.read_csv(ORIGINAL_DATA / "olist_customers_dataset.csv")

make_missing(
    customers, 
    "customer_city", 
    MISSING_RATE,
    logger,
    "customers"
)

add_spaces(
    customers,
    "customer_city",
    SPACE_RATE,
    logger,
    "customers"
)

uppercase(
    customers,
    "customer_city", 
    UPPERCASE_RATE,
    logger,
    "customers"   
)

customers = duplicate_rows(
    customers, 
    DUPLICATE_RATE,
    logger,
    "customers" 
)

save(customers, "messy_olist_customers_dataset.csv")

print("Customers ✓")

# -----------------------------
# Products
# -----------------------------

print("Processing products...")

products = pd.read_csv(ORIGINAL_DATA / "olist_products_dataset.csv")

make_missing(
    products, 
    "product_category_name", 
    MISSING_RATE,
    logger,
    "products"
)

add_spaces(
    products,
    "product_category_name",
    SPACE_RATE,
    logger,
    "products"
)

negative_values(
    products,
    "product_weigth_g",
    NEGATIVE_VALUE_RATE,
    logger,
    "products"
)

uppercase(
    products,
    "product_category_name", 
    UPPERCASE_RATE,
    logger,
    "products"   
)

save(products, "messy_olist_products_dataset.csv")

print("Products ✓")

# -----------------------------
# Payments
# -----------------------------

print("Processing payments...")

payments = pd.read_csv(ORIGINAL_DATA / "olist_order_payments_dataset.csv")

negative_values(
    payments,
    "payment_value",
    NEGATIVE_VALUE_RATE,
    logger,
    "payments"
)

payments = duplicate_rows(
    payments, 
    DUPLICATE_RATE,
    logger,
    "payments" 
)

save(payments, "messy_olist_order_payments_dataset.csv")

print("Payments ✓")

# -----------------------------
# Save Report
# -----------------------------

report = logger.to_dataframe()

report.to_csv(
    MESSY_DATA / "dirty_data_report.csv",
    index=False
)

print("\nDone!")
print(f"Files saved to: {MESSY_DATA}.")

logger.print_summary()