import pandas as pd

# beauty basic info 합치기
df1 = pd.read_csv('beauty_influencer_basic_info150.csv')
df2 = pd.read_csv('beauty_influencer_basic_info300.csv')
df3 = pd.read_csv('beauty_influencer_basic_info400.csv')
df4 = pd.read_csv('beauty_influencer_basic_info500.csv')
df5 = pd.read_csv('beauty_influencer_basic_info600.csv')
df6 = pd.read_csv('beauty_influencer_basic_info750.csv')
df7 = pd.read_csv('beauty_influencer_basic_info1000.csv')

df_temp1 = pd.concat([df1, df2, df3, df4, df5, df6, df7])
print(len(df_temp1))
df_temp2 = df_temp1.drop_duplicates(["0"])
print(len(df_temp2))

df_temp2.columns = ['index', 'account', 'post', 'follower', 'follow', 'open_account', 'official_account']
df_result = df_temp2.set_index('account')

del df_result['index']
df_result.to_csv('beauty_basic_info.csv', encoding='utf-8-sig')


# # beauty post info 합치기
# df1 = pd.read_csv('beauty_influencer_post_info100.csv')
# df2 = pd.read_csv('beauty_influencer_post_info200.csv')
# df3 = pd.read_csv('beauty_influencer_post_info300.csv')
# df4 = pd.read_csv('beauty_influencer_post_info400.csv')
# df5 = pd.read_csv('beauty_influencer_post_info500.csv')
# df6 = pd.read_csv('beauty_influencer_post_info600.csv')
# df7 = pd.read_csv('beauty_influencer_post_info700.csv')
# df8 = pd.read_csv('beauty_influencer_post_info900.csv')
# df9 = pd.read_csv('beauty_influencer_post_info939.csv')
#
# df_temp1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9])
# print(len(df_temp1))
# df_temp2 = df_temp1.drop_duplicates(["0"])
# print(len(df_temp2))
#
# df_temp2.columns = ['index', 'account', 'image_love', 'image_comment', 'video_love', 'video_comment', 'igtv_love',
#                     'igtv_comment']
# df_result = df_temp2.set_index('account')
# del df_result['index']
# df_result.to_csv('beauty_post_info.csv', encoding='utf-8-sig')

