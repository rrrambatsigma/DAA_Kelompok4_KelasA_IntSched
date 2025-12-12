import pandas as pd

def load_instance(path):
    """
    Loader instance untuk proyek DAA (Interval Scheduling).
    """
    df = pd.read_csv(path)

    df['start_dt'] = pd.to_datetime(df['start'], format="mixed")
    df['finish_dt'] = pd.to_datetime(df['finish'], format="mixed")

    df['profit'] = df['Kapasitas Kelas']

    return df
