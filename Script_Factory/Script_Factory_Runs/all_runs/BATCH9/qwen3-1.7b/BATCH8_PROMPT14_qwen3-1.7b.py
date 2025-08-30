```python
import pandas as pd

def main():
    df = pd.read_csv('input.csv')
    column_name = 'category'
    counts = df[column_name].value_counts()
    max_count = counts.max()
    top_value = counts.idxmax()
    adjusted_counts = {k: v if k != top_value else (v * 5) for k, v in counts.items()}
    print(adjusted_counts)

if __name__ == "__main__":
    main()