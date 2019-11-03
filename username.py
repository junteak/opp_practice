'''
データ型宣言: UserName
    属性:
        実際のユーザー名
    ルール:
        ・4文字以上20文字以下である
    できること
        ・ユーザー名を大文字に変換する
'''


class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}は文字数のルール違反です！')

        self.name = name

    def screen_name(self):
        return self.name.upper()


# UserNameクラス(自分で作った型)のインスタンス化
hibiki = UserName('hibiki')
print(hibiki.screen_name())
# print(hibiki)
# print.type(hibiki)
print(hibiki.name)

# sho = UserName('sho')
# print('sho')
# print(sho.name)
