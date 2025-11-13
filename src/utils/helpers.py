def safe_group_median_impute(df, group_col, target_col):
    col_median = df[target_col].median()
    group_median = df.groupby(group_col)[target_col].median()
    group_median = group_median.fillna(col_median)
    return df[target_col].fillna(df[group_col].map(group_median))
