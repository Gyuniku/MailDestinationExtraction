# -*- coding: utf-8 -*-
import re
import difflib

# 出力されるメールアドレス一覧の区切り文字(;)
mailaddress_delimiter = ';'
# 正規表現設定
r = re.compile(r"^[^\(]*")
# 参加者メールリスト
participants_mail_list = []

# 元データ入力
mailaddresses = input('半角セミコロンで分割されたメールリストを入力してください\n →')
participants = input('半角セミコロンで分割された参加者を入力してください\n →')

# 入力データを分割
mail_list = mailaddresses.split(';')
print('メールリスト = ' + str(mail_list) + '\n')
participants_list = participants.split(';')
print('参加者リスト' + str(participants_list) + '\n')

# 参加者リストを見て該当するメールアドレスを抽出(ついでに半角スペースを削除)
for p_num in range(len(participants_list)):
    participant = participants_list[p_num].replace(' ', '')
    print('対象者' + str(p_num + 1) + '人目：' + participant)
    # 抽出した参加者の名前とメールアドレスリストをチェック、類似度が70%以上なら参加者メールリストに追加
    for mail_num in range(len(mail_list)):
        # メールリストから正規表現で ( までの文字列を抜いて半角スペースを削除
        mail = r.search(mail_list[mail_num]).group().replace(' ', '')
        # 類似度確認
        match_ratio = difflib.SequenceMatcher(None, participant, mail).ratio()
        print(participant + 'と' + mail + 'の類似度 = ' + str(match_ratio))
        # 70％以上合ってたら参加者リストに入れる
        if match_ratio >= 0.7:
            participants_mail_list.append(mail_list[mail_num])
            print('参加者リストにインしました')
        # end if
    # end for
# end for

# ファイル出力
file = open('メールリストさん.txt','w')
for i in range(len(participants_mail_list)):
    file.write(participants_mail_list[i] + mailaddress_delimiter)
# end for
print('ファイル出力が完了しました')
file.close()
