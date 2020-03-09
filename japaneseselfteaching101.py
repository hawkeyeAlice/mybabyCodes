'''
Fri, 6th March 2020, Japan.
Author: hawkeyeAlice.
Topic: A program to make the learning of Hiragana and Katakana easy-peasy for beginners like me.
'''
#learn hiragana and katakana simultaneously for users made easy
import os

class Japanese:
    def __init__(self):
        self.list_romaji=['a','i','u','e','o',
        'ka','ki','ku','ke','ke',
        'sa','shi','su','se','so',
        'ta','chi','tsu','te','to',
        'na','ni','nu','ne','no',
        'ha','hi','fu','he','ho',
        'ma','mi','mu','me','mo',
        'ya','-','yu','-','yo',
        'ra','ri','ru','re','ro',
        'wa','-','-','-','o(wo)',
        'n','-','-','-','-',
        'ga','gi','gu','ge','go',
        'za','ji(zi)','zu','ze','zo',
        'da','ji(di)','zu(du)','de','do',
        'ba','bi','bu','be','bo',
        'pa','pi','pu','pe','po',
        'kya','-','kyu','','kyo',
        'sha','-','shu','-','sho',
        'cha','-','chu','-','cho',
        'nya','-','nyu','','nyo',
        'hya','-','hyu','','hyo',
        'mya','-','myu','','myo',
        'rya','-','ryu','','ryo',
        'gya','-','gyu','','gyo',
        'ja','-','ju','-','jo',
        'bya','-','byu','','byo',
        'pya','-','pyu','','pyo']
        self.list_hiragana=['あ','い','う','え','お',
        'か','き','く','け','こ',
        'さ','し','す','せ','そ',
        'た','ち','つ','て','と',
        'な','に','ぬ','ね','の',
        'は','ひ','ふ','へ','ほ',
        'ま','み','む','め','も',
        'や','－','ゆ','－','よ',
        'ら','り','る','れ','ろ',
        'わ','－','－','－','を',
        'ん','-','-','-','-',
        'が','ぎ','ぐ','げ','ご',
        'ざ','じ','ず','ぜ','ぞ',
        'だ','ぢ','づ','で','ど',
        'ば','び','ぶ','べ','ぼ',
        'ぱ','ぴ','ぷ','ぺ','ぽ',
        'きゃ','-','きゅ','-','きょ',
        'しゃ','-','しゅ','-','しょ',
        'ちゃ','-','ちゅ','-','ちょ',
        'にゃ','-','にゅ','-','にょ',
        'ひゃ','-','ひゅ','-','ひょ',
        'みゃ','-','みゅ','-','みょ',
        'りゃ','-','りゅ','-','りょ',
        'ぎゃ','-','ぎゅ','-','ぎょ',
        'じゃ','-','じゅ','-','じょ',
        'びゃ','-','びゅ','-','びょ',
        'ぴゃ','-','ぴゅ','-','ぴょ']
        self.list_katakana=['ア','イ','ウ','エ','オ',
        'カ','キ','ク','ケ','コ',
        'サ','シ','ス','セ','ソ',
        'タ','チ','ツ','テ','ト',
        'ナ','ニ','ヌ','ネ','ノ',
        'ハ','ヒ','フ','ヘ','ホ',
        'マ','ミ','ム','メ','モ',
        'ヤ','－','ユ','－','ヨ',
        'ラ','リ','ル','レ','ロ',
        'ワ','－','－','－','ヲ',
        'ン','－','－','－','－',
        'ガ','ギ','グ','ゲ','ゴ',
        'ザ','ジ','ズ','ゼ','ゾ',
        'ダ','ヂ','ヅ','デ','ド',
        'バ','ビ','ブ','ベ','ボ',
        'パ','ピ','プ','ペ','ポ',
        'キャ','-','キュ','-','キョ',
        'シャ','-','シュ','-','ショ',
        'チャ','-','チュ','-','チョ',
        'ニャ','-','ニュ','-','ニョ',
        'ヒャ','-','ヒュ','-','ヒョ',
        'ミャ','-','ミュ','-','ミョ',
        'リャ','-','リュ','-','リョ',
        'ギャ','-','ギュ','-','ギョ',
        'ジャ','-','ジュ','-','ジョ',
        'ビャ','-','ビュ','-','ビョ',
        'ピャ','-','ピュ','-','ピョ']
    def dict_creation(self):
        self.romaji_to_hiragana=dict(zip(self.list_romaji,self.list_hiragana))
        self.romaji_to_katakana=dict(zip(self.list_romaji,self.list_katakana))
        self.dictionary_overall=dict(zip(self.list_romaji,zip(self.list_hiragana,self.list_katakana)))
        return self.dictionary_overall
    def checkchr(self,inp):
        result=self.dictionary_overall.get(inp)
        print("ROMAJI          HIRAGANA          KATAKANA")
        print("------------------------------------------")
        row="{:18} {:18} {:18}".format(inp,result[0],result[1])
        print(row)


Object=Japanese() #instance of class Japanese
res=Object.dict_creation()
while True:
    val = input("Enter romaji to get the equivalent Hiragana & Katakana or type PREVIEW to see the character table: ")
    if val=="PREVIEW":
        print("ROMAJI          HIRAGANA          KATAKANA")
        print("------------------------------------------")
        for keys,values in res.items():
            row="{:18} {:18} {:18}".format(keys,values[0],values[1])
            print(row)
    else:
        if(val.islower()):
            Object.checkchr(val)
    choice = input("Enter 0 to continue, 1 to exit")
    if choice!="1" and choice!="0":
        print(choice+" is a wrong choice. Exit.")
        break
    elif choice=="1":
        break
