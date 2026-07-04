import pandas as pd
from collections import defaultdict


class ReportLogger:
    def __init__(self):
        self.records = []
    
    def log(self, table, column, issue, count):
        self.records.append({
            "Table": table,
            "Column": column,
            "Issue": issue,
            "Rows Affected": count,
        })
    
    def print_summary(self):
        grouped = defaultdict(list)

        for record in self.records:
            grouped[record["Table"]].append(record)
        
        print("\n" + "=" * 70)

        for table, records in grouped.items():
            
            print(f"\n{table.upper()}")

            print("-" * 70)

            for r in records:
                print(
                    f"{r['Issue']:<25}"
                    f"{r['Column']:<30}"
                    f"{r['Rows Affected']:>8}"
                )
    
    def to_dataframe(self):
        return pd.DataFrame(self.records)