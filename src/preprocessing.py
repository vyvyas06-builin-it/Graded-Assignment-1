def handle_missing(df):
    df['children'] = df['children'].fillna(0)
    df['country'] = df['country'].fillna('Unknown')
    return df
