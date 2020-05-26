
# coding: UTF-8

import pynder
import pandas as pd
# "456900714360021"
# token = '483b353a-89df-4ec7-9eaa-1055fcb0fb81' # 取得したFBアクセストークンを入力

token = '8833432f-2f8e-4ba5-b227-98f6fbcc42a2' # 取得したFBアクセストークンを入力
session=pynder.Session("kurosaiyak",token)

# token = 'b45be1ba-53dd-48c7-8cb1-5a6ca5960d0c' # 取得したFBアクセストークンを入力
# session=pynder.Session("100010261097863",token)
# session.matches()  # 既にマッチしたユーザー情報を取得
# # LAT = 40
# # LON = -75
# # session.update_location(LAT, LON)
# # session.update_location(LAT, LON) # 位置情報を更新（緯度、経度）
# session.profile  # 自分のプロフィール。更新すると本体の方も更新される。
users = session.nearby_users()  # 近くにいるユーザーを取得。
# print(int(session.profile.ping_time[:4]))
listlist = []
people = 0
for user in users:
    # if int(user.ping_time[:4]) == 2019:
    # if user.jobs == ['看護師']:
        print('画像'),
        print(user.photos)

        print('名前'),

        print(user.name)

        print('年齢'),
        print(user.age)

        print('BIO'),
        print(user.bio)

        print('誕生日'),
        print(user.birth_date)

        print('最終ログイン時刻'),
        print(user.ping_time)

        print('距離'),
        print(user.distance_km)

        print('学校名'),
        print(user.schools)

        print('職業'),
        print(user.jobs)

        print('共通の友人数'),
        print(user.common_connections)

        if user.common_connections == []: # 共通の知り合いがいるユーザーはLIKEしないようにしてます。
            user.like()
            print('LIKE!!!!!')

        print('==============================================================================')
        list = []
        list.append("名前")
        list.append(user.name)
        list.append("年齢")
        list.append(user.age)
        list.append("自己紹介")
        list.append(user.bio)
        list.append("誕生日")
        list.append(user.birth_date)
        list.append("距離")
        list.append(user.distance_km)
        list.append("学校名")
        list.append(user.schools)
        list.append("職業")
        list.append(user.jobs)
        people += 1
        listlist.append(list)
        if people == 100:
            break
filename = "like_list.tsv"
print("100人にライクを送った")
pd.DataFrame(listlist).to_csv(filename,sep='\t',index =False)

        # else:
            # print('画像'),
            # print(user.photos)
            #
            # print('名前'),
            #
            # print(user.name)
            #
            # print('年齢'),
            # print(user.age)
            #
            # print('BIO'),
            # print(user.bio)
            #
            # print('誕生日'),
            # print(user.birth_date)
            #
            # print('最終ログイン時刻'),
            # print(user.ping_time)
            #
            # print('距離'),
            # print(user.distance_km)
            #
            # print('学校名'),
            # print(user.schools)
            #
            # print('職業'),
            # print(user.jobs)
            #
            # print('共通の友人数'),
            # print(user.common_connections)
            #
            # if user.common_connections == []: # 共通の知り合いがいるユーザーはLIKEしないようにしてます。
            #     user.dislike()
            #     print('dislike!!!!!')

            # print('==============================================================================')
