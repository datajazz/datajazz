import pandas as pd

def timeoftime(df, drop_original=True, measures=["hour", "dayofweek", "weekofyear", "month"], infer_datetime_format=True, utc=True):
    for col in df.select_dtypes(include='datetime64').columns:
        for m in measures:
            df[f"{col}_{m}"] = getattr(pd.to_datetime(df[col], infer_datetime_format=infer_datetime_format, utc=utc).dt, m)
        if drop_original:
            df = df.drop(col, inplace=False, axis=1, errors='ignore')
    return df

def onehot_categories(df, drop_original=True, min_ones=1, max_categories=100):
    for col in df.columns:
        if df[col].nunique() > max_categories:
            continue
        one_hot = pd.get_dummies(df[col], prefix=col, dummy_na=False)
        one_hot.drop([col for col, val in one_hot.sum().iteritems() if val < min_ones], axis=1, inplace=True)
        if drop_original:
            df = df.drop(col, inplace=False, axis=1, errors='ignore')
        df = df.join(one_hot, lsuffix='', rsuffix='_'+col)
    return df

def remove_redundancies(df):
    return df.T.drop_duplicates().T