import datetime 

def get_period(start_day: str, n_days: int) -> list:
    ''' get the list of string dates from <start_date> <n_days> backwards '''
    datelst = [datetime.datetime.strptime(start_day, '%Y-%m-%d') - datetime.timedelta(days=x) for x in range(n_days)]
    datelst = [x.strftime('%Y-%m-%d') for x in datelst]
    
    return datelst


def convert_datetime(df, sin_cos=False):
    start_time = time.time()
    sh = df.shape

    print("datetime conversion started...")
    df['hour'] = df.created_ts.apply(get_hour)
    df['weekday'] = df.created_ts.apply(get_weekday)
    df['day'] = df.created_ts.apply(get_day)
    
    if sin_cos:
        df = sin_cos_encoding(df, 'hour', 24)
        df = sin_cos_encoding(df, 'weekday', 7)
        df = sin_cos_encoding(df, 'day', 30)
        tests.test_df_shape(sh, 3*2, df.shape)
    else:
        tests.test_df_shape(sh, 3, df.shape)
  
    print(f"datetime conversion completed, time : {int(time.time() - start_time)}s")

    return df


def dt_string_converter(df, dt_column, fmt="datetime"):
    '''convert string to datetime & vice versa,
    fmt: [datetime/string]'''
    if all([fmt == "datetime", df[dt_column].dtype == "object"]):
            df[dt_column] = df[dt_column].apply(lambda v: datetime.datetime.strptime(v, "%Y-%m-%d %H:%M:%S"))
    if all([fmt == "string", df[dt_column].dtype == "<M8[ns]"]):
            df[dt_column] = df[dt_column].apply(lambda v: datetime.datetime.strftime(v, "%Y-%m-%d %H:%M:%S"))
    
    try:
        assert df[dt_column].dtype == {"datetime":"<M8[ns]", "string":"object"}[fmt]
    except AssertionError:
        print(f"datetime string converter failed")
    
    return df
