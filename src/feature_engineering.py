def create_features(df):
    df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
    df['price_per_person'] = df['adr'] / (df['adults'] + df['children'] + 1)
    return df
