from preswald import connect, get_df, table


connect()
df = get_df("test_sb")
table(df)
