def handle_missing(df):
    df['children'] = df['children'].fillna(0)
    return df
