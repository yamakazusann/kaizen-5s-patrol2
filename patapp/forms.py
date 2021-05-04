from django import forms
from .models import *

class kakutukiForm(forms.ModelForm):
    class Meta:
        model=kakutuki
        fields=['seiri_in','seiton_in','seisou_in','seiketu_in','situke_in']

class kakutukiForm_a(forms.ModelForm):
    class Meta:
        model=kakutuki_a
        fields=['seiri_in','seiton_in','seisou_in','seiketu_in','situke_in']

class kakutukiForm_b(forms.ModelForm):
    class Meta:
        model=kakutuki_b
        fields=['seiri_in','seiton_in','seisou_in','seiketu_in','situke_in']

class kakutukiForm_c(forms.ModelForm):
    class Meta:
        model=kakutuki_c
        fields=['seiri_in','seiton_in','seisou_in','seiketu_in','situke_in']

class kakutukiForm_d(forms.ModelForm):
    class Meta:
        model=kakutuki_d
        fields=['seiri_in','seiton_in','seisou_in','seiketu_in','situke_in']

class kakutukiForm_e(forms.ModelForm):
    class Meta:
        model=kakutuki_e
        fields=['seiri_in','seiton_in','seisou_in','seiketu_in','situke_in']





class teamForm(forms.ModelForm):
    class Meta:
        model=team
        fields=['team_name']



class goukakuForm(forms.ModelForm):
    class Meta:
        model=goukaku
        fields=['kijunten_in']

















class saiten_form(forms.Form):
    data1=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice1=forms.ChoiceField(label='整理:⑴不必要、故障している設備・測定器・治工具の放置はないか？',choices=data1,widget=forms.RadioSelect())

    data2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'曖昧な管理')
    ]
    choice2=forms.ChoiceField(label='整理:⑵製品・不良品・仕掛品の管理状態はわかるか？',choices=data2,widget=forms.RadioSelect())

    data3=[
        (2,'置いている'),
        (1,'場所は決まっている'),
        (0,'置かれていない')
    ]
    choice3=forms.ChoiceField(label='整理:⑶部品・備品・工具・文具は決められた場所に必要量のみ置いているか？',choices=data3,widget=forms.RadioSelect())

    data4=[
        (2,'一目で分かる'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice4=forms.ChoiceField(label='整理:⑷識別表示が製品・不良品・仕掛品にされているか？',choices=data4,widget=forms.RadioSelect())

    data5=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5=forms.ChoiceField(label='整理:⑸原材料・資材・素材・製品の保管環境は品質管理上、問題ないか？',choices=data5,widget=forms.RadioSelect())

    data6=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice6=forms.ChoiceField(label='整理:⑹エリアメンバーで処置判断ができないものはないか？',choices=data6,widget=forms.RadioSelect())

    data7=[
        (2,'していない'),
        (0,'している')
    ]
    choice7=forms.ChoiceField(label='整理:⑺設備・装置・測定器・治工具を一部破損/故障したまま使用してないか？',choices=data7,widget=forms.RadioSelect())

    data8=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8=forms.ChoiceField(label='整理:⑻仮置き等、一時的に非定常な状況を分かる化（表示）しているか？',choices=data8,widget=forms.RadioSelect())

    data9=[
        (2,'管理している'),
        (0,'管理してない')
    ]
    choice9=forms.ChoiceField(label='整理:⑼掲示物に古いものは無く、きちんと見える位置に貼られているか？',choices=data9,widget=forms.RadioSelect())

    data10=[
        (2,'ない'),
        (0,'ある')
    ]
    choice10=forms.ChoiceField(label='整理:⑽作業/避難通路内、配電盤前、消化設備前、非常口前に物を置いていないか？',choices=data10,widget=forms.RadioSelect())


    data1_2=[
        (2,'ない'),
        (0,'ある')
    ]
    choice1_2=forms.ChoiceField(label='整頓:⑴治工具類や書類が設備や測定器、机の上へ放置されていないか？',choices=data1_2,widget=forms.RadioSelect())

    data2_2=[
        (2,'常時徹底'),
        (1,'意識はしている'),
        (0,'意識は薄い')
    ]
    choice2_2=forms.ChoiceField(label='整頓:⑵物の置き方、掲示物の貼り方、区画線の引き方は「真っ直ぐ」を意識しているか？',choices=data2_2,widget=forms.RadioSelect())

    data3_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice3_2=forms.ChoiceField(label='整頓:⑶ストック品と使用品を区別している状況がわかるか？',choices=data3_2,widget=forms.RadioSelect())

    data4_2=[
        (2,'混在なし'),
        (0,'混在あり')
    ]
    choice4_2=forms.ChoiceField(label='整頓:⑷種類の異なる備品、製品が混雑して保管されていないか？',choices=data4_2,widget=forms.RadioSelect())

    data5_2=[
        (2,'容易にできる'),
        (1,'支障はなし'),
        (0,'やり難い')
    ]
    choice5_2=forms.ChoiceField(label='整頓:⑸設備や測定器周りは、支障なくメンテナンスができているか？',choices=data5_2,widget=forms.RadioSelect())

    data6_2=[
        (2,'している'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice6_2=forms.ChoiceField(label='整頓:⑹通路と設備・作業場・置き場は区分され、区画線で表記しているか？',choices=data6_2,widget=forms.RadioSelect())

    data7_2=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice7_2=forms.ChoiceField(label='整頓:⑺製品や資材・備品の直置きや立てかけはないか？',choices=data7_2,widget=forms.RadioSelect())

    data8_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_2=forms.ChoiceField(label='整頓:⑻良品・不良品・仕掛品が区分けされ、識別管理できているか？',choices=data8_2,widget=forms.RadioSelect())

    data9_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice9_2=forms.ChoiceField(label='整頓:⑼保管物は番地管理（置き場所管理）されて、数量等の情報が把握できるか？',choices=data9_2,widget=forms.RadioSelect())

    data10_2=[
        (2,'滞留なし'),
        (1,'適量のみ'),
        (0,'溜まっている')
    ]
    choice10_2=forms.ChoiceField(label='整頓:⑽工程内に仕掛品・保留品が留まっていないか？',choices=data10_2,widget=forms.RadioSelect())








    data1_3=[
        (2,'している'),
        (0,'曖昧な管理')
    ]
    choice1_3=forms.ChoiceField(label='清掃:⑴清掃ルールを決めて維持管理を行っているか？',choices=data1_3,widget=forms.RadioSelect())

    data2_3=[
        (2,'出さない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice2_3=forms.ChoiceField(label='清掃:⑵床に水・油・薬液・素材屑が落ちていないか？',choices=data2_3,widget=forms.RadioSelect())

    data3_3=[
        (2,'汚れない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice3_3=forms.ChoiceField(label='清掃:⑶床・机・ラック・設備・装置・測定器に埃や汚れがないか？',choices=data3_3,widget=forms.RadioSelect())

    data4_3=[
        (2,'している'),
        (0,'考慮不足')
    ]
    choice4_3=forms.ChoiceField(label='清掃:⑷ゴミ箱は必要以上に配置せず、必要最低限の数としているか？',choices=data4_3,widget=forms.RadioSelect())

    data5_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice5_3=forms.ChoiceField(label='清掃:⑸設備周辺や作業エリアに備品類が落ちていないか？',choices=data5_3,widget=forms.RadioSelect())

    data6_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice6_3=forms.ChoiceField(label='清掃:⑹製品を入れる容器や運搬代が埃等で汚れていないか？',choices=data6_3,widget=forms.RadioSelect())

    data7_3=[
        (2,'している'),
        (0,'していない')
    ]
    choice7_3=forms.ChoiceField(label='清掃:⑺清掃用具は決められた場所に必要なものと数だけ保管しているか？',choices=data7_3,widget=forms.RadioSelect())

    data8_3=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_3=forms.ChoiceField(label='清掃:⑻廃棄物（ゴミ）は分別容器などで正しく分けているか？',choices=data8_3,widget=forms.RadioSelect())

    data9_3=[
        (2,'適切に処理'),
        (0,'溢れあり')
    ]
    choice9_3=forms.ChoiceField(label='清掃:⑼ゴミ箱から溢れることなく、ゴミの廃棄タイミングは適切な状況か？',choices=data9_3,widget=forms.RadioSelect())

    data10_3=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice10_3=forms.ChoiceField(label='清掃:⑽部屋の換気や作業時の換気は正しく行われ、環境に問題はないか？',choices=data10_3,widget=forms.RadioSelect())






    data1_4=[
        (2,'清潔感あり'),
        (1,'不快感あり'),
        (0,'不快感なし')
    ]
    choice1_4=forms.ChoiceField(label='清潔:⑴作業者の保護手袋、作業着に著しい汚れはなく清潔感があるか？',choices=data1_4,widget=forms.RadioSelect())

    

    data2_4=[
        (2,'している'),
        (0,'していない')
    ]
    choice2_4=forms.ChoiceField(label='清潔:⑵作業着、作業靴、保護具はきちんとした決められた物を使用しているか？',choices=data2_4,widget=forms.RadioSelect())

    data3_4=[
        (2,'積極的に参加'),
        (1,'必要に応じ参加'),
        (0,'担当任せ')
    ]
    choice3_4=forms.ChoiceField(label='清潔:⑶共有エリア（倉庫・休憩室・トイレ・喫煙室・廃棄物置き場等）の５S活動もしているか？',choices=data3_4,widget=forms.RadioSelect())

    data4_4=[
        (2,'問題なし'),
        (1,'安全は考慮'),
        (0,'考慮不足')
    ]
    choice4_4=forms.ChoiceField(label='清潔:⑷設備・装置・測定器・PCの配線の仕舞は安全や清掃を考慮しているか？',choices=data4_4,widget=forms.RadioSelect())

    data5_4=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5_4=forms.ChoiceField(label='清潔:⑸床や壁が損傷していたり、照明器具が切れていたり、タコ足配線がないか？',choices=data5_4,widget=forms.RadioSelect())

    data6_4=[
        (2,'日々管理'),
        (1,'適時管理'),
        (0,'管理不足')
    ]
    choice6_4=forms.ChoiceField(label='清潔:⑹活動版は常設され、史料に破れ。垂れ・剥がれ・汚れがないか？',choices=data6_4,widget=forms.RadioSelect())

    data7_4=[
        (2,'なっている'),
        (0,'なっていない')
    ]
    choice7_4=forms.ChoiceField(label='清潔:⑺５Sパトロールの結果、連続で不合格の状態となっていないか？',choices=data7_4,widget=forms.RadioSelect())

    data8_4=[
        (2,'ない'),
        (0,'ある')
    ]
    choice8_4=forms.ChoiceField(label='清潔:⑻作業エリアに落下の危険のあるもの、燃えやすいものの放置はないか？',choices=data8_4,widget=forms.RadioSelect())

    data9_4=[
        (2,'自信あり'),
        (1,'言える'),
        (0,'改善要')
    ]
    choice9_4=forms.ChoiceField(label='清潔:⑼作業エリアはお客様が見て不安を与えない状況と言えるか？',choices=data9_4,widget=forms.RadioSelect())

    data10_4=[
        (2,'点検記録あり'),
        (1,'点検はしている'),
        (0,'点検不備')
    ]
    choice10_4=forms.ChoiceField(label='清潔:⑽設備や測定器の保守点検は実施され、必要能力を発揮できているか？',choices=data10_4,widget=forms.RadioSelect())


    data1_5=[
        (2,'自信あり'),
        (1,'できている'),
        (0,'できていない')
    ]
    choice1_5=forms.ChoiceField(label='躾:⑴社内・社外の人に対して気持ちの良い挨拶ができているか？',choices=data1_5,widget=forms.RadioSelect())

    data2_5=[
        (2,'遵守徹底が浸透'),
        (1,'遵守している'),
        (0,'遵守不足')
    ]
    choice2_5=forms.ChoiceField(label='躾:⑵決められた社内ルールを理解し厳守しているか？',choices=data2_5,widget=forms.RadioSelect())

    data3_5=[
        (2,'守っている'),
        (0,'一部不足')
    ]
    choice3_5=forms.ChoiceField(label='躾:⑶廃棄物の処理ルールを全員が正しく理解しているか？',choices=data3_5,widget=forms.RadioSelect())

    data4_5=[
        (2,'一目で分かる'),
        (1,'共有化はしている'),
        (0,'共有化不足')
    ]
    choice4_5=forms.ChoiceField(label='躾:⑷必要な情報は掲示板等で共有し見える化（周知）されているか？',choices=data4_5,widget=forms.RadioSelect())

    data5_5=[
        (2,'自己チェックもあり'),
        (1,'している'),
        (0,'していない')
    ]
    choice5_5=forms.ChoiceField(label='躾:⑸パトロールによる５Sチェックを１回/月以上は実施しているか？',choices=data5_5,widget=forms.RadioSelect())

    data6_5=[
        (2,'計画的に進行'),
        (1,'進んでいる'),
        (0,'停滞あり')
    ]
    choice6_5=forms.ChoiceField(label='躾:⑹各種パトロールの指摘事項の改善は進んでいるか？',choices=data6_5,widget=forms.RadioSelect())

    data7_5=[
        (2,'率先して対策'),
        (1,'している'),
        (0,'関心低い')
    ]
    choice7_5=forms.ChoiceField(label='躾:⑺共有エリアで気付いた不具合や問題もリーダーや管理職へ報告しているか？',choices=data7_5,widget=forms.RadioSelect())

    data8_5=[
        (2,'守っている'),
        (0,'一部ルーズ')
    ]
    choice8_5=forms.ChoiceField(label='躾:⑻就業時間、休憩時間は守られているか？',choices=data8_5,widget=forms.RadioSelect())

    data9_5=[
        (2,'付けている'),
        (0,'付けていない')
    ]
    choice9_5=forms.ChoiceField(label='躾:⑼名札はきちんと見える場所につけられているか？',choices=data9_5,widget=forms.RadioSelect())

    data10_5=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'できていない')
    ]
    choice10_5=forms.ChoiceField(label='躾:⑽５Sを含めた現場の問題・課題を共有できているか？',choices=data10_5,widget=forms.RadioSelect())

class saiten_form_a(forms.Form):
    data1=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice1=forms.ChoiceField(label='整理:⑴不必要、故障している設備・測定器・治工具の放置はないか？',choices=data1,widget=forms.RadioSelect())

    data2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'曖昧な管理')
    ]
    choice2=forms.ChoiceField(label='整理:⑵製品・不良品・仕掛品の管理状態はわかるか？',choices=data2,widget=forms.RadioSelect())

    data3=[
        (2,'置いている'),
        (1,'場所は決まっている'),
        (0,'置かれていない')
    ]
    choice3=forms.ChoiceField(label='整理:⑶部品・備品・工具・文具は決められた場所に必要量のみ置いているか？',choices=data3,widget=forms.RadioSelect())

    data4=[
        (2,'一目で分かる'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice4=forms.ChoiceField(label='整理:⑷識別表示が製品・不良品・仕掛品にされているか？',choices=data4,widget=forms.RadioSelect())

    data5=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5=forms.ChoiceField(label='整理:⑸原材料・資材・素材・製品の保管環境は品質管理上、問題ないか？',choices=data5,widget=forms.RadioSelect())

    data6=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice6=forms.ChoiceField(label='整理:⑹エリアメンバーで処置判断ができないものはないか？',choices=data6,widget=forms.RadioSelect())

    data7=[
        (2,'していない'),
        (0,'している')
    ]
    choice7=forms.ChoiceField(label='整理:⑺設備・装置・測定器・治工具を一部破損/故障したまま使用してないか？',choices=data7,widget=forms.RadioSelect())

    data8=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8=forms.ChoiceField(label='整理:⑻仮置き等、一時的に非定常な状況を分かる化（表示）しているか？',choices=data8,widget=forms.RadioSelect())

    data9=[
        (2,'管理している'),
        (0,'管理してない')
    ]
    choice9=forms.ChoiceField(label='整理:⑼掲示物に古いものは無く、きちんと見える位置に貼られているか？',choices=data9,widget=forms.RadioSelect())

    data10=[
        (2,'ない'),
        (0,'ある')
    ]
    choice10=forms.ChoiceField(label='整理:⑽作業/避難通路内、配電盤前、消化設備前、非常口前に物を置いていないか？',choices=data10,widget=forms.RadioSelect())


    data1_2=[
        (2,'ない'),
        (0,'ある')
    ]
    choice1_2=forms.ChoiceField(label='整頓:⑴治工具類や書類が設備や測定器、机の上へ放置されていないか？',choices=data1_2,widget=forms.RadioSelect())

    data2_2=[
        (2,'常時徹底'),
        (1,'意識はしている'),
        (0,'意識は薄い')
    ]
    choice2_2=forms.ChoiceField(label='整頓:⑵物の置き方、掲示物の貼り方、区画線の引き方は「真っ直ぐ」を意識しているか？',choices=data2_2,widget=forms.RadioSelect())

    data3_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice3_2=forms.ChoiceField(label='整頓:⑶ストック品と使用品を区別している状況がわかるか？',choices=data3_2,widget=forms.RadioSelect())

    data4_2=[
        (2,'混在なし'),
        (0,'混在あり')
    ]
    choice4_2=forms.ChoiceField(label='整頓:⑷種類の異なる備品、製品が混雑して保管されていないか？',choices=data4_2,widget=forms.RadioSelect())

    data5_2=[
        (2,'容易にできる'),
        (1,'支障はなし'),
        (0,'やり難い')
    ]
    choice5_2=forms.ChoiceField(label='整頓:⑸設備や測定器周りは、支障なくメンテナンスができているか？',choices=data5_2,widget=forms.RadioSelect())

    data6_2=[
        (2,'している'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice6_2=forms.ChoiceField(label='整頓:⑹通路と設備・作業場・置き場は区分され、区画線で表記しているか？',choices=data6_2,widget=forms.RadioSelect())

    data7_2=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice7_2=forms.ChoiceField(label='整頓:⑺製品や資材・備品の直置きや立てかけはないか？',choices=data7_2,widget=forms.RadioSelect())

    data8_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_2=forms.ChoiceField(label='整頓:⑻良品・不良品・仕掛品が区分けされ、識別管理できているか？',choices=data8_2,widget=forms.RadioSelect())

    data9_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice9_2=forms.ChoiceField(label='整頓:⑼保管物は番地管理（置き場所管理）されて、数量等の情報が把握できるか？',choices=data9_2,widget=forms.RadioSelect())

    data10_2=[
        (2,'滞留なし'),
        (1,'適量のみ'),
        (0,'溜まっている')
    ]
    choice10_2=forms.ChoiceField(label='整頓:⑽工程内に仕掛品・保留品が留まっていないか？',choices=data10_2,widget=forms.RadioSelect())








    data1_3=[
        (2,'している'),
        (0,'曖昧な管理')
    ]
    choice1_3=forms.ChoiceField(label='清掃:⑴清掃ルールを決めて維持管理を行っているか？',choices=data1_3,widget=forms.RadioSelect())

    data2_3=[
        (2,'出さない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice2_3=forms.ChoiceField(label='清掃:⑵床に水・油・薬液・素材屑が落ちていないか？',choices=data2_3,widget=forms.RadioSelect())

    data3_3=[
        (2,'汚れない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice3_3=forms.ChoiceField(label='清掃:⑶床・机・ラック・設備・装置・測定器に埃や汚れがないか？',choices=data3_3,widget=forms.RadioSelect())

    data4_3=[
        (2,'している'),
        (0,'考慮不足')
    ]
    choice4_3=forms.ChoiceField(label='清掃:⑷ゴミ箱は必要以上に配置せず、必要最低限の数としているか？',choices=data4_3,widget=forms.RadioSelect())

    data5_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice5_3=forms.ChoiceField(label='清掃:⑸設備周辺や作業エリアに備品類が落ちていないか？',choices=data5_3,widget=forms.RadioSelect())

    data6_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice6_3=forms.ChoiceField(label='清掃:⑹製品を入れる容器や運搬代が埃等で汚れていないか？',choices=data6_3,widget=forms.RadioSelect())

    data7_3=[
        (2,'している'),
        (0,'していない')
    ]
    choice7_3=forms.ChoiceField(label='清掃:⑺清掃用具は決められた場所に必要なものと数だけ保管しているか？',choices=data7_3,widget=forms.RadioSelect())

    data8_3=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_3=forms.ChoiceField(label='清掃:⑻廃棄物（ゴミ）は分別容器などで正しく分けているか？',choices=data8_3,widget=forms.RadioSelect())

    data9_3=[
        (2,'適切に処理'),
        (0,'溢れあり')
    ]
    choice9_3=forms.ChoiceField(label='清掃:⑼ゴミ箱から溢れることなく、ゴミの廃棄タイミングは適切な状況か？',choices=data9_3,widget=forms.RadioSelect())

    data10_3=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice10_3=forms.ChoiceField(label='清掃:⑽部屋の換気や作業時の換気は正しく行われ、環境に問題はないか？',choices=data10_3,widget=forms.RadioSelect())






    data1_4=[
        (2,'清潔感あり'),
        (1,'不快感あり'),
        (0,'不快感なし')
    ]
    choice1_4=forms.ChoiceField(label='清潔:⑴作業者の保護手袋、作業着に著しい汚れはなく清潔感があるか？',choices=data1_4,widget=forms.RadioSelect())

    

    data2_4=[
        (2,'している'),
        (0,'していない')
    ]
    choice2_4=forms.ChoiceField(label='清潔:⑵作業着、作業靴、保護具はきちんとした決められた物を使用しているか？',choices=data2_4,widget=forms.RadioSelect())

    data3_4=[
        (2,'積極的に参加'),
        (1,'必要に応じ参加'),
        (0,'担当任せ')
    ]
    choice3_4=forms.ChoiceField(label='清潔:⑶共有エリア（倉庫・休憩室・トイレ・喫煙室・廃棄物置き場等）の５S活動もしているか？',choices=data3_4,widget=forms.RadioSelect())

    data4_4=[
        (2,'問題なし'),
        (1,'安全は考慮'),
        (0,'考慮不足')
    ]
    choice4_4=forms.ChoiceField(label='清潔:⑷設備・装置・測定器・PCの配線の仕舞は安全や清掃を考慮しているか？',choices=data4_4,widget=forms.RadioSelect())

    data5_4=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5_4=forms.ChoiceField(label='清潔:⑸床や壁が損傷していたり、照明器具が切れていたり、タコ足配線がないか？',choices=data5_4,widget=forms.RadioSelect())

    data6_4=[
        (2,'日々管理'),
        (1,'適時管理'),
        (0,'管理不足')
    ]
    choice6_4=forms.ChoiceField(label='清潔:⑹活動版は常設され、史料に破れ。垂れ・剥がれ・汚れがないか？',choices=data6_4,widget=forms.RadioSelect())

    data7_4=[
        (2,'なっている'),
        (0,'なっていない')
    ]
    choice7_4=forms.ChoiceField(label='清潔:⑺５Sパトロールの結果、連続で不合格の状態となっていないか？',choices=data7_4,widget=forms.RadioSelect())

    data8_4=[
        (2,'ない'),
        (0,'ある')
    ]
    choice8_4=forms.ChoiceField(label='清潔:⑻作業エリアに落下の危険のあるもの、燃えやすいものの放置はないか？',choices=data8_4,widget=forms.RadioSelect())

    data9_4=[
        (2,'自信あり'),
        (1,'言える'),
        (0,'改善要')
    ]
    choice9_4=forms.ChoiceField(label='清潔:⑼作業エリアはお客様が見て不安を与えない状況と言えるか？',choices=data9_4,widget=forms.RadioSelect())

    data10_4=[
        (2,'点検記録あり'),
        (1,'点検はしている'),
        (0,'点検不備')
    ]
    choice10_4=forms.ChoiceField(label='清潔:⑽設備や測定器の保守点検は実施され、必要能力を発揮できているか？',choices=data10_4,widget=forms.RadioSelect())


    data1_5=[
        (2,'自信あり'),
        (1,'できている'),
        (0,'できていない')
    ]
    choice1_5=forms.ChoiceField(label='躾:⑴社内・社外の人に対して気持ちの良い挨拶ができているか？',choices=data1_5,widget=forms.RadioSelect())

    data2_5=[
        (2,'遵守徹底が浸透'),
        (1,'遵守している'),
        (0,'遵守不足')
    ]
    choice2_5=forms.ChoiceField(label='躾:⑵決められた社内ルールを理解し厳守しているか？',choices=data2_5,widget=forms.RadioSelect())

    data3_5=[
        (2,'守っている'),
        (0,'一部不足')
    ]
    choice3_5=forms.ChoiceField(label='躾:⑶廃棄物の処理ルールを全員が正しく理解しているか？',choices=data3_5,widget=forms.RadioSelect())

    data4_5=[
        (2,'一目で分かる'),
        (1,'共有化はしている'),
        (0,'共有化不足')
    ]
    choice4_5=forms.ChoiceField(label='躾:⑷必要な情報は掲示板等で共有し見える化（周知）されているか？',choices=data4_5,widget=forms.RadioSelect())

    data5_5=[
        (2,'自己チェックもあり'),
        (1,'している'),
        (0,'していない')
    ]
    choice5_5=forms.ChoiceField(label='躾:⑸パトロールによる５Sチェックを１回/月以上は実施しているか？',choices=data5_5,widget=forms.RadioSelect())

    data6_5=[
        (2,'計画的に進行'),
        (1,'進んでいる'),
        (0,'停滞あり')
    ]
    choice6_5=forms.ChoiceField(label='躾:⑹各種パトロールの指摘事項の改善は進んでいるか？',choices=data6_5,widget=forms.RadioSelect())

    data7_5=[
        (2,'率先して対策'),
        (1,'している'),
        (0,'関心低い')
    ]
    choice7_5=forms.ChoiceField(label='躾:⑺共有エリアで気付いた不具合や問題もリーダーや管理職へ報告しているか？',choices=data7_5,widget=forms.RadioSelect())

    data8_5=[
        (2,'守っている'),
        (0,'一部ルーズ')
    ]
    choice8_5=forms.ChoiceField(label='躾:⑻就業時間、休憩時間は守られているか？',choices=data8_5,widget=forms.RadioSelect())

    data9_5=[
        (2,'付けている'),
        (0,'付けていない')
    ]
    choice9_5=forms.ChoiceField(label='躾:⑼名札はきちんと見える場所につけられているか？',choices=data9_5,widget=forms.RadioSelect())

    data10_5=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'できていない')
    ]
    choice10_5=forms.ChoiceField(label='躾:⑽５Sを含めた現場の問題・課題を共有できているか？',choices=data10_5,widget=forms.RadioSelect())

class saiten_form_b(forms.Form):
    data1=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice1=forms.ChoiceField(label='整理:⑴不必要、故障している設備・測定器・治工具の放置はないか？',choices=data1,widget=forms.RadioSelect())

    data2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'曖昧な管理')
    ]
    choice2=forms.ChoiceField(label='整理:⑵製品・不良品・仕掛品の管理状態はわかるか？',choices=data2,widget=forms.RadioSelect())

    data3=[
        (2,'置いている'),
        (1,'場所は決まっている'),
        (0,'置かれていない')
    ]
    choice3=forms.ChoiceField(label='整理:⑶部品・備品・工具・文具は決められた場所に必要量のみ置いているか？',choices=data3,widget=forms.RadioSelect())

    data4=[
        (2,'一目で分かる'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice4=forms.ChoiceField(label='整理:⑷識別表示が製品・不良品・仕掛品にされているか？',choices=data4,widget=forms.RadioSelect())

    data5=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5=forms.ChoiceField(label='整理:⑸原材料・資材・素材・製品の保管環境は品質管理上、問題ないか？',choices=data5,widget=forms.RadioSelect())

    data6=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice6=forms.ChoiceField(label='整理:⑹エリアメンバーで処置判断ができないものはないか？',choices=data6,widget=forms.RadioSelect())

    data7=[
        (2,'していない'),
        (0,'している')
    ]
    choice7=forms.ChoiceField(label='整理:⑺設備・装置・測定器・治工具を一部破損/故障したまま使用してないか？',choices=data7,widget=forms.RadioSelect())

    data8=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8=forms.ChoiceField(label='整理:⑻仮置き等、一時的に非定常な状況を分かる化（表示）しているか？',choices=data8,widget=forms.RadioSelect())

    data9=[
        (2,'管理している'),
        (0,'管理してない')
    ]
    choice9=forms.ChoiceField(label='整理:⑼掲示物に古いものは無く、きちんと見える位置に貼られているか？',choices=data9,widget=forms.RadioSelect())

    data10=[
        (2,'ない'),
        (0,'ある')
    ]
    choice10=forms.ChoiceField(label='整理:⑽作業/避難通路内、配電盤前、消化設備前、非常口前に物を置いていないか？',choices=data10,widget=forms.RadioSelect())


    data1_2=[
        (2,'ない'),
        (0,'ある')
    ]
    choice1_2=forms.ChoiceField(label='整頓:⑴治工具類や書類が設備や測定器、机の上へ放置されていないか？',choices=data1_2,widget=forms.RadioSelect())

    data2_2=[
        (2,'常時徹底'),
        (1,'意識はしている'),
        (0,'意識は薄い')
    ]
    choice2_2=forms.ChoiceField(label='整頓:⑵物の置き方、掲示物の貼り方、区画線の引き方は「真っ直ぐ」を意識しているか？',choices=data2_2,widget=forms.RadioSelect())

    data3_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice3_2=forms.ChoiceField(label='整頓:⑶ストック品と使用品を区別している状況がわかるか？',choices=data3_2,widget=forms.RadioSelect())

    data4_2=[
        (2,'混在なし'),
        (0,'混在あり')
    ]
    choice4_2=forms.ChoiceField(label='整頓:⑷種類の異なる備品、製品が混雑して保管されていないか？',choices=data4_2,widget=forms.RadioSelect())

    data5_2=[
        (2,'容易にできる'),
        (1,'支障はなし'),
        (0,'やり難い')
    ]
    choice5_2=forms.ChoiceField(label='整頓:⑸設備や測定器周りは、支障なくメンテナンスができているか？',choices=data5_2,widget=forms.RadioSelect())

    data6_2=[
        (2,'している'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice6_2=forms.ChoiceField(label='整頓:⑹通路と設備・作業場・置き場は区分され、区画線で表記しているか？',choices=data6_2,widget=forms.RadioSelect())

    data7_2=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice7_2=forms.ChoiceField(label='整頓:⑺製品や資材・備品の直置きや立てかけはないか？',choices=data7_2,widget=forms.RadioSelect())

    data8_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_2=forms.ChoiceField(label='整頓:⑻良品・不良品・仕掛品が区分けされ、識別管理できているか？',choices=data8_2,widget=forms.RadioSelect())

    data9_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice9_2=forms.ChoiceField(label='整頓:⑼保管物は番地管理（置き場所管理）されて、数量等の情報が把握できるか？',choices=data9_2,widget=forms.RadioSelect())

    data10_2=[
        (2,'滞留なし'),
        (1,'適量のみ'),
        (0,'溜まっている')
    ]
    choice10_2=forms.ChoiceField(label='整頓:⑽工程内に仕掛品・保留品が留まっていないか？',choices=data10_2,widget=forms.RadioSelect())








    data1_3=[
        (2,'している'),
        (0,'曖昧な管理')
    ]
    choice1_3=forms.ChoiceField(label='清掃:⑴清掃ルールを決めて維持管理を行っているか？',choices=data1_3,widget=forms.RadioSelect())

    data2_3=[
        (2,'出さない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice2_3=forms.ChoiceField(label='清掃:⑵床に水・油・薬液・素材屑が落ちていないか？',choices=data2_3,widget=forms.RadioSelect())

    data3_3=[
        (2,'汚れない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice3_3=forms.ChoiceField(label='清掃:⑶床・机・ラック・設備・装置・測定器に埃や汚れがないか？',choices=data3_3,widget=forms.RadioSelect())

    data4_3=[
        (2,'している'),
        (0,'考慮不足')
    ]
    choice4_3=forms.ChoiceField(label='清掃:⑷ゴミ箱は必要以上に配置せず、必要最低限の数としているか？',choices=data4_3,widget=forms.RadioSelect())

    data5_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice5_3=forms.ChoiceField(label='清掃:⑸設備周辺や作業エリアに備品類が落ちていないか？',choices=data5_3,widget=forms.RadioSelect())

    data6_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice6_3=forms.ChoiceField(label='清掃:⑹製品を入れる容器や運搬代が埃等で汚れていないか？',choices=data6_3,widget=forms.RadioSelect())

    data7_3=[
        (2,'している'),
        (0,'していない')
    ]
    choice7_3=forms.ChoiceField(label='清掃:⑺清掃用具は決められた場所に必要なものと数だけ保管しているか？',choices=data7_3,widget=forms.RadioSelect())

    data8_3=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_3=forms.ChoiceField(label='清掃:⑻廃棄物（ゴミ）は分別容器などで正しく分けているか？',choices=data8_3,widget=forms.RadioSelect())

    data9_3=[
        (2,'適切に処理'),
        (0,'溢れあり')
    ]
    choice9_3=forms.ChoiceField(label='清掃:⑼ゴミ箱から溢れることなく、ゴミの廃棄タイミングは適切な状況か？',choices=data9_3,widget=forms.RadioSelect())

    data10_3=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice10_3=forms.ChoiceField(label='清掃:⑽部屋の換気や作業時の換気は正しく行われ、環境に問題はないか？',choices=data10_3,widget=forms.RadioSelect())






    data1_4=[
        (2,'清潔感あり'),
        (1,'不快感あり'),
        (0,'不快感なし')
    ]
    choice1_4=forms.ChoiceField(label='清潔:⑴作業者の保護手袋、作業着に著しい汚れはなく清潔感があるか？',choices=data1_4,widget=forms.RadioSelect())

    

    data2_4=[
        (2,'している'),
        (0,'していない')
    ]
    choice2_4=forms.ChoiceField(label='清潔:⑵作業着、作業靴、保護具はきちんとした決められた物を使用しているか？',choices=data2_4,widget=forms.RadioSelect())

    data3_4=[
        (2,'積極的に参加'),
        (1,'必要に応じ参加'),
        (0,'担当任せ')
    ]
    choice3_4=forms.ChoiceField(label='清潔:⑶共有エリア（倉庫・休憩室・トイレ・喫煙室・廃棄物置き場等）の５S活動もしているか？',choices=data3_4,widget=forms.RadioSelect())

    data4_4=[
        (2,'問題なし'),
        (1,'安全は考慮'),
        (0,'考慮不足')
    ]
    choice4_4=forms.ChoiceField(label='清潔:⑷設備・装置・測定器・PCの配線の仕舞は安全や清掃を考慮しているか？',choices=data4_4,widget=forms.RadioSelect())

    data5_4=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5_4=forms.ChoiceField(label='清潔:⑸床や壁が損傷していたり、照明器具が切れていたり、タコ足配線がないか？',choices=data5_4,widget=forms.RadioSelect())

    data6_4=[
        (2,'日々管理'),
        (1,'適時管理'),
        (0,'管理不足')
    ]
    choice6_4=forms.ChoiceField(label='清潔:⑹活動版は常設され、史料に破れ。垂れ・剥がれ・汚れがないか？',choices=data6_4,widget=forms.RadioSelect())

    data7_4=[
        (2,'なっている'),
        (0,'なっていない')
    ]
    choice7_4=forms.ChoiceField(label='清潔:⑺５Sパトロールの結果、連続で不合格の状態となっていないか？',choices=data7_4,widget=forms.RadioSelect())

    data8_4=[
        (2,'ない'),
        (0,'ある')
    ]
    choice8_4=forms.ChoiceField(label='清潔:⑻作業エリアに落下の危険のあるもの、燃えやすいものの放置はないか？',choices=data8_4,widget=forms.RadioSelect())

    data9_4=[
        (2,'自信あり'),
        (1,'言える'),
        (0,'改善要')
    ]
    choice9_4=forms.ChoiceField(label='清潔:⑼作業エリアはお客様が見て不安を与えない状況と言えるか？',choices=data9_4,widget=forms.RadioSelect())

    data10_4=[
        (2,'点検記録あり'),
        (1,'点検はしている'),
        (0,'点検不備')
    ]
    choice10_4=forms.ChoiceField(label='清潔:⑽設備や測定器の保守点検は実施され、必要能力を発揮できているか？',choices=data10_4,widget=forms.RadioSelect())


    data1_5=[
        (2,'自信あり'),
        (1,'できている'),
        (0,'できていない')
    ]
    choice1_5=forms.ChoiceField(label='躾:⑴社内・社外の人に対して気持ちの良い挨拶ができているか？',choices=data1_5,widget=forms.RadioSelect())

    data2_5=[
        (2,'遵守徹底が浸透'),
        (1,'遵守している'),
        (0,'遵守不足')
    ]
    choice2_5=forms.ChoiceField(label='躾:⑵決められた社内ルールを理解し厳守しているか？',choices=data2_5,widget=forms.RadioSelect())

    data3_5=[
        (2,'守っている'),
        (0,'一部不足')
    ]
    choice3_5=forms.ChoiceField(label='躾:⑶廃棄物の処理ルールを全員が正しく理解しているか？',choices=data3_5,widget=forms.RadioSelect())

    data4_5=[
        (2,'一目で分かる'),
        (1,'共有化はしている'),
        (0,'共有化不足')
    ]
    choice4_5=forms.ChoiceField(label='躾:⑷必要な情報は掲示板等で共有し見える化（周知）されているか？',choices=data4_5,widget=forms.RadioSelect())

    data5_5=[
        (2,'自己チェックもあり'),
        (1,'している'),
        (0,'していない')
    ]
    choice5_5=forms.ChoiceField(label='躾:⑸パトロールによる５Sチェックを１回/月以上は実施しているか？',choices=data5_5,widget=forms.RadioSelect())

    data6_5=[
        (2,'計画的に進行'),
        (1,'進んでいる'),
        (0,'停滞あり')
    ]
    choice6_5=forms.ChoiceField(label='躾:⑹各種パトロールの指摘事項の改善は進んでいるか？',choices=data6_5,widget=forms.RadioSelect())

    data7_5=[
        (2,'率先して対策'),
        (1,'している'),
        (0,'関心低い')
    ]
    choice7_5=forms.ChoiceField(label='躾:⑺共有エリアで気付いた不具合や問題もリーダーや管理職へ報告しているか？',choices=data7_5,widget=forms.RadioSelect())

    data8_5=[
        (2,'守っている'),
        (0,'一部ルーズ')
    ]
    choice8_5=forms.ChoiceField(label='躾:⑻就業時間、休憩時間は守られているか？',choices=data8_5,widget=forms.RadioSelect())

    data9_5=[
        (2,'付けている'),
        (0,'付けていない')
    ]
    choice9_5=forms.ChoiceField(label='躾:⑼名札はきちんと見える場所につけられているか？',choices=data9_5,widget=forms.RadioSelect())

    data10_5=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'できていない')
    ]
    choice10_5=forms.ChoiceField(label='躾:⑽５Sを含めた現場の問題・課題を共有できているか？',choices=data10_5,widget=forms.RadioSelect())

class saiten_form_c(forms.Form):
    data1=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice1=forms.ChoiceField(label='整理:⑴不必要、故障している設備・測定器・治工具の放置はないか？',choices=data1,widget=forms.RadioSelect())

    data2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'曖昧な管理')
    ]
    choice2=forms.ChoiceField(label='整理:⑵製品・不良品・仕掛品の管理状態はわかるか？',choices=data2,widget=forms.RadioSelect())

    data3=[
        (2,'置いている'),
        (1,'場所は決まっている'),
        (0,'置かれていない')
    ]
    choice3=forms.ChoiceField(label='整理:⑶部品・備品・工具・文具は決められた場所に必要量のみ置いているか？',choices=data3,widget=forms.RadioSelect())

    data4=[
        (2,'一目で分かる'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice4=forms.ChoiceField(label='整理:⑷識別表示が製品・不良品・仕掛品にされているか？',choices=data4,widget=forms.RadioSelect())

    data5=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5=forms.ChoiceField(label='整理:⑸原材料・資材・素材・製品の保管環境は品質管理上、問題ないか？',choices=data5,widget=forms.RadioSelect())

    data6=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice6=forms.ChoiceField(label='整理:⑹エリアメンバーで処置判断ができないものはないか？',choices=data6,widget=forms.RadioSelect())

    data7=[
        (2,'していない'),
        (0,'している')
    ]
    choice7=forms.ChoiceField(label='整理:⑺設備・装置・測定器・治工具を一部破損/故障したまま使用してないか？',choices=data7,widget=forms.RadioSelect())

    data8=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8=forms.ChoiceField(label='整理:⑻仮置き等、一時的に非定常な状況を分かる化（表示）しているか？',choices=data8,widget=forms.RadioSelect())

    data9=[
        (2,'管理している'),
        (0,'管理してない')
    ]
    choice9=forms.ChoiceField(label='整理:⑼掲示物に古いものは無く、きちんと見える位置に貼られているか？',choices=data9,widget=forms.RadioSelect())

    data10=[
        (2,'ない'),
        (0,'ある')
    ]
    choice10=forms.ChoiceField(label='整理:⑽作業/避難通路内、配電盤前、消化設備前、非常口前に物を置いていないか？',choices=data10,widget=forms.RadioSelect())


    data1_2=[
        (2,'ない'),
        (0,'ある')
    ]
    choice1_2=forms.ChoiceField(label='整頓:⑴治工具類や書類が設備や測定器、机の上へ放置されていないか？',choices=data1_2,widget=forms.RadioSelect())

    data2_2=[
        (2,'常時徹底'),
        (1,'意識はしている'),
        (0,'意識は薄い')
    ]
    choice2_2=forms.ChoiceField(label='整頓:⑵物の置き方、掲示物の貼り方、区画線の引き方は「真っ直ぐ」を意識しているか？',choices=data2_2,widget=forms.RadioSelect())

    data3_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice3_2=forms.ChoiceField(label='整頓:⑶ストック品と使用品を区別している状況がわかるか？',choices=data3_2,widget=forms.RadioSelect())

    data4_2=[
        (2,'混在なし'),
        (0,'混在あり')
    ]
    choice4_2=forms.ChoiceField(label='整頓:⑷種類の異なる備品、製品が混雑して保管されていないか？',choices=data4_2,widget=forms.RadioSelect())

    data5_2=[
        (2,'容易にできる'),
        (1,'支障はなし'),
        (0,'やり難い')
    ]
    choice5_2=forms.ChoiceField(label='整頓:⑸設備や測定器周りは、支障なくメンテナンスができているか？',choices=data5_2,widget=forms.RadioSelect())

    data6_2=[
        (2,'している'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice6_2=forms.ChoiceField(label='整頓:⑹通路と設備・作業場・置き場は区分され、区画線で表記しているか？',choices=data6_2,widget=forms.RadioSelect())

    data7_2=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice7_2=forms.ChoiceField(label='整頓:⑺製品や資材・備品の直置きや立てかけはないか？',choices=data7_2,widget=forms.RadioSelect())

    data8_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_2=forms.ChoiceField(label='整頓:⑻良品・不良品・仕掛品が区分けされ、識別管理できているか？',choices=data8_2,widget=forms.RadioSelect())

    data9_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice9_2=forms.ChoiceField(label='整頓:⑼保管物は番地管理（置き場所管理）されて、数量等の情報が把握できるか？',choices=data9_2,widget=forms.RadioSelect())

    data10_2=[
        (2,'滞留なし'),
        (1,'適量のみ'),
        (0,'溜まっている')
    ]
    choice10_2=forms.ChoiceField(label='整頓:⑽工程内に仕掛品・保留品が留まっていないか？',choices=data10_2,widget=forms.RadioSelect())








    data1_3=[
        (2,'している'),
        (0,'曖昧な管理')
    ]
    choice1_3=forms.ChoiceField(label='清掃:⑴清掃ルールを決めて維持管理を行っているか？',choices=data1_3,widget=forms.RadioSelect())

    data2_3=[
        (2,'出さない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice2_3=forms.ChoiceField(label='清掃:⑵床に水・油・薬液・素材屑が落ちていないか？',choices=data2_3,widget=forms.RadioSelect())

    data3_3=[
        (2,'汚れない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice3_3=forms.ChoiceField(label='清掃:⑶床・机・ラック・設備・装置・測定器に埃や汚れがないか？',choices=data3_3,widget=forms.RadioSelect())

    data4_3=[
        (2,'している'),
        (0,'考慮不足')
    ]
    choice4_3=forms.ChoiceField(label='清掃:⑷ゴミ箱は必要以上に配置せず、必要最低限の数としているか？',choices=data4_3,widget=forms.RadioSelect())

    data5_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice5_3=forms.ChoiceField(label='清掃:⑸設備周辺や作業エリアに備品類が落ちていないか？',choices=data5_3,widget=forms.RadioSelect())

    data6_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice6_3=forms.ChoiceField(label='清掃:⑹製品を入れる容器や運搬代が埃等で汚れていないか？',choices=data6_3,widget=forms.RadioSelect())

    data7_3=[
        (2,'している'),
        (0,'していない')
    ]
    choice7_3=forms.ChoiceField(label='清掃:⑺清掃用具は決められた場所に必要なものと数だけ保管しているか？',choices=data7_3,widget=forms.RadioSelect())

    data8_3=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_3=forms.ChoiceField(label='清掃:⑻廃棄物（ゴミ）は分別容器などで正しく分けているか？',choices=data8_3,widget=forms.RadioSelect())

    data9_3=[
        (2,'適切に処理'),
        (0,'溢れあり')
    ]
    choice9_3=forms.ChoiceField(label='清掃:⑼ゴミ箱から溢れることなく、ゴミの廃棄タイミングは適切な状況か？',choices=data9_3,widget=forms.RadioSelect())

    data10_3=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice10_3=forms.ChoiceField(label='清掃:⑽部屋の換気や作業時の換気は正しく行われ、環境に問題はないか？',choices=data10_3,widget=forms.RadioSelect())






    data1_4=[
        (2,'清潔感あり'),
        (1,'不快感あり'),
        (0,'不快感なし')
    ]
    choice1_4=forms.ChoiceField(label='清潔:⑴作業者の保護手袋、作業着に著しい汚れはなく清潔感があるか？',choices=data1_4,widget=forms.RadioSelect())

    

    data2_4=[
        (2,'している'),
        (0,'していない')
    ]
    choice2_4=forms.ChoiceField(label='清潔:⑵作業着、作業靴、保護具はきちんとした決められた物を使用しているか？',choices=data2_4,widget=forms.RadioSelect())

    data3_4=[
        (2,'積極的に参加'),
        (1,'必要に応じ参加'),
        (0,'担当任せ')
    ]
    choice3_4=forms.ChoiceField(label='清潔:⑶共有エリア（倉庫・休憩室・トイレ・喫煙室・廃棄物置き場等）の５S活動もしているか？',choices=data3_4,widget=forms.RadioSelect())

    data4_4=[
        (2,'問題なし'),
        (1,'安全は考慮'),
        (0,'考慮不足')
    ]
    choice4_4=forms.ChoiceField(label='清潔:⑷設備・装置・測定器・PCの配線の仕舞は安全や清掃を考慮しているか？',choices=data4_4,widget=forms.RadioSelect())

    data5_4=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5_4=forms.ChoiceField(label='清潔:⑸床や壁が損傷していたり、照明器具が切れていたり、タコ足配線がないか？',choices=data5_4,widget=forms.RadioSelect())

    data6_4=[
        (2,'日々管理'),
        (1,'適時管理'),
        (0,'管理不足')
    ]
    choice6_4=forms.ChoiceField(label='清潔:⑹活動版は常設され、史料に破れ。垂れ・剥がれ・汚れがないか？',choices=data6_4,widget=forms.RadioSelect())

    data7_4=[
        (2,'なっている'),
        (0,'なっていない')
    ]
    choice7_4=forms.ChoiceField(label='清潔:⑺５Sパトロールの結果、連続で不合格の状態となっていないか？',choices=data7_4,widget=forms.RadioSelect())

    data8_4=[
        (2,'ない'),
        (0,'ある')
    ]
    choice8_4=forms.ChoiceField(label='清潔:⑻作業エリアに落下の危険のあるもの、燃えやすいものの放置はないか？',choices=data8_4,widget=forms.RadioSelect())

    data9_4=[
        (2,'自信あり'),
        (1,'言える'),
        (0,'改善要')
    ]
    choice9_4=forms.ChoiceField(label='清潔:⑼作業エリアはお客様が見て不安を与えない状況と言えるか？',choices=data9_4,widget=forms.RadioSelect())

    data10_4=[
        (2,'点検記録あり'),
        (1,'点検はしている'),
        (0,'点検不備')
    ]
    choice10_4=forms.ChoiceField(label='清潔:⑽設備や測定器の保守点検は実施され、必要能力を発揮できているか？',choices=data10_4,widget=forms.RadioSelect())


    data1_5=[
        (2,'自信あり'),
        (1,'できている'),
        (0,'できていない')
    ]
    choice1_5=forms.ChoiceField(label='躾:⑴社内・社外の人に対して気持ちの良い挨拶ができているか？',choices=data1_5,widget=forms.RadioSelect())

    data2_5=[
        (2,'遵守徹底が浸透'),
        (1,'遵守している'),
        (0,'遵守不足')
    ]
    choice2_5=forms.ChoiceField(label='躾:⑵決められた社内ルールを理解し厳守しているか？',choices=data2_5,widget=forms.RadioSelect())

    data3_5=[
        (2,'守っている'),
        (0,'一部不足')
    ]
    choice3_5=forms.ChoiceField(label='躾:⑶廃棄物の処理ルールを全員が正しく理解しているか？',choices=data3_5,widget=forms.RadioSelect())

    data4_5=[
        (2,'一目で分かる'),
        (1,'共有化はしている'),
        (0,'共有化不足')
    ]
    choice4_5=forms.ChoiceField(label='躾:⑷必要な情報は掲示板等で共有し見える化（周知）されているか？',choices=data4_5,widget=forms.RadioSelect())

    data5_5=[
        (2,'自己チェックもあり'),
        (1,'している'),
        (0,'していない')
    ]
    choice5_5=forms.ChoiceField(label='躾:⑸パトロールによる５Sチェックを１回/月以上は実施しているか？',choices=data5_5,widget=forms.RadioSelect())

    data6_5=[
        (2,'計画的に進行'),
        (1,'進んでいる'),
        (0,'停滞あり')
    ]
    choice6_5=forms.ChoiceField(label='躾:⑹各種パトロールの指摘事項の改善は進んでいるか？',choices=data6_5,widget=forms.RadioSelect())

    data7_5=[
        (2,'率先して対策'),
        (1,'している'),
        (0,'関心低い')
    ]
    choice7_5=forms.ChoiceField(label='躾:⑺共有エリアで気付いた不具合や問題もリーダーや管理職へ報告しているか？',choices=data7_5,widget=forms.RadioSelect())

    data8_5=[
        (2,'守っている'),
        (0,'一部ルーズ')
    ]
    choice8_5=forms.ChoiceField(label='躾:⑻就業時間、休憩時間は守られているか？',choices=data8_5,widget=forms.RadioSelect())

    data9_5=[
        (2,'付けている'),
        (0,'付けていない')
    ]
    choice9_5=forms.ChoiceField(label='躾:⑼名札はきちんと見える場所につけられているか？',choices=data9_5,widget=forms.RadioSelect())

    data10_5=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'できていない')
    ]
    choice10_5=forms.ChoiceField(label='躾:⑽５Sを含めた現場の問題・課題を共有できているか？',choices=data10_5,widget=forms.RadioSelect())

class saiten_form_d(forms.Form):
    data1=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice1=forms.ChoiceField(label='整理:⑴不必要、故障している設備・測定器・治工具の放置はないか？',choices=data1,widget=forms.RadioSelect())

    data2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'曖昧な管理')
    ]
    choice2=forms.ChoiceField(label='整理:⑵製品・不良品・仕掛品の管理状態はわかるか？',choices=data2,widget=forms.RadioSelect())

    data3=[
        (2,'置いている'),
        (1,'場所は決まっている'),
        (0,'置かれていない')
    ]
    choice3=forms.ChoiceField(label='整理:⑶部品・備品・工具・文具は決められた場所に必要量のみ置いているか？',choices=data3,widget=forms.RadioSelect())

    data4=[
        (2,'一目で分かる'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice4=forms.ChoiceField(label='整理:⑷識別表示が製品・不良品・仕掛品にされているか？',choices=data4,widget=forms.RadioSelect())

    data5=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5=forms.ChoiceField(label='整理:⑸原材料・資材・素材・製品の保管環境は品質管理上、問題ないか？',choices=data5,widget=forms.RadioSelect())

    data6=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice6=forms.ChoiceField(label='整理:⑹エリアメンバーで処置判断ができないものはないか？',choices=data6,widget=forms.RadioSelect())

    data7=[
        (2,'していない'),
        (0,'している')
    ]
    choice7=forms.ChoiceField(label='整理:⑺設備・装置・測定器・治工具を一部破損/故障したまま使用してないか？',choices=data7,widget=forms.RadioSelect())

    data8=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8=forms.ChoiceField(label='整理:⑻仮置き等、一時的に非定常な状況を分かる化（表示）しているか？',choices=data8,widget=forms.RadioSelect())

    data9=[
        (2,'管理している'),
        (0,'管理してない')
    ]
    choice9=forms.ChoiceField(label='整理:⑼掲示物に古いものは無く、きちんと見える位置に貼られているか？',choices=data9,widget=forms.RadioSelect())

    data10=[
        (2,'ない'),
        (0,'ある')
    ]
    choice10=forms.ChoiceField(label='整理:⑽作業/避難通路内、配電盤前、消化設備前、非常口前に物を置いていないか？',choices=data10,widget=forms.RadioSelect())


    data1_2=[
        (2,'ない'),
        (0,'ある')
    ]
    choice1_2=forms.ChoiceField(label='整頓:⑴治工具類や書類が設備や測定器、机の上へ放置されていないか？',choices=data1_2,widget=forms.RadioSelect())

    data2_2=[
        (2,'常時徹底'),
        (1,'意識はしている'),
        (0,'意識は薄い')
    ]
    choice2_2=forms.ChoiceField(label='整頓:⑵物の置き方、掲示物の貼り方、区画線の引き方は「真っ直ぐ」を意識しているか？',choices=data2_2,widget=forms.RadioSelect())

    data3_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice3_2=forms.ChoiceField(label='整頓:⑶ストック品と使用品を区別している状況がわかるか？',choices=data3_2,widget=forms.RadioSelect())

    data4_2=[
        (2,'混在なし'),
        (0,'混在あり')
    ]
    choice4_2=forms.ChoiceField(label='整頓:⑷種類の異なる備品、製品が混雑して保管されていないか？',choices=data4_2,widget=forms.RadioSelect())

    data5_2=[
        (2,'容易にできる'),
        (1,'支障はなし'),
        (0,'やり難い')
    ]
    choice5_2=forms.ChoiceField(label='整頓:⑸設備や測定器周りは、支障なくメンテナンスができているか？',choices=data5_2,widget=forms.RadioSelect())

    data6_2=[
        (2,'している'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice6_2=forms.ChoiceField(label='整頓:⑹通路と設備・作業場・置き場は区分され、区画線で表記しているか？',choices=data6_2,widget=forms.RadioSelect())

    data7_2=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice7_2=forms.ChoiceField(label='整頓:⑺製品や資材・備品の直置きや立てかけはないか？',choices=data7_2,widget=forms.RadioSelect())

    data8_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_2=forms.ChoiceField(label='整頓:⑻良品・不良品・仕掛品が区分けされ、識別管理できているか？',choices=data8_2,widget=forms.RadioSelect())

    data9_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice9_2=forms.ChoiceField(label='整頓:⑼保管物は番地管理（置き場所管理）されて、数量等の情報が把握できるか？',choices=data9_2,widget=forms.RadioSelect())

    data10_2=[
        (2,'滞留なし'),
        (1,'適量のみ'),
        (0,'溜まっている')
    ]
    choice10_2=forms.ChoiceField(label='整頓:⑽工程内に仕掛品・保留品が留まっていないか？',choices=data10_2,widget=forms.RadioSelect())








    data1_3=[
        (2,'している'),
        (0,'曖昧な管理')
    ]
    choice1_3=forms.ChoiceField(label='清掃:⑴清掃ルールを決めて維持管理を行っているか？',choices=data1_3,widget=forms.RadioSelect())

    data2_3=[
        (2,'出さない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice2_3=forms.ChoiceField(label='清掃:⑵床に水・油・薬液・素材屑が落ちていないか？',choices=data2_3,widget=forms.RadioSelect())

    data3_3=[
        (2,'汚れない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice3_3=forms.ChoiceField(label='清掃:⑶床・机・ラック・設備・装置・測定器に埃や汚れがないか？',choices=data3_3,widget=forms.RadioSelect())

    data4_3=[
        (2,'している'),
        (0,'考慮不足')
    ]
    choice4_3=forms.ChoiceField(label='清掃:⑷ゴミ箱は必要以上に配置せず、必要最低限の数としているか？',choices=data4_3,widget=forms.RadioSelect())

    data5_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice5_3=forms.ChoiceField(label='清掃:⑸設備周辺や作業エリアに備品類が落ちていないか？',choices=data5_3,widget=forms.RadioSelect())

    data6_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice6_3=forms.ChoiceField(label='清掃:⑹製品を入れる容器や運搬代が埃等で汚れていないか？',choices=data6_3,widget=forms.RadioSelect())

    data7_3=[
        (2,'している'),
        (0,'していない')
    ]
    choice7_3=forms.ChoiceField(label='清掃:⑺清掃用具は決められた場所に必要なものと数だけ保管しているか？',choices=data7_3,widget=forms.RadioSelect())

    data8_3=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_3=forms.ChoiceField(label='清掃:⑻廃棄物（ゴミ）は分別容器などで正しく分けているか？',choices=data8_3,widget=forms.RadioSelect())

    data9_3=[
        (2,'適切に処理'),
        (0,'溢れあり')
    ]
    choice9_3=forms.ChoiceField(label='清掃:⑼ゴミ箱から溢れることなく、ゴミの廃棄タイミングは適切な状況か？',choices=data9_3,widget=forms.RadioSelect())

    data10_3=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice10_3=forms.ChoiceField(label='清掃:⑽部屋の換気や作業時の換気は正しく行われ、環境に問題はないか？',choices=data10_3,widget=forms.RadioSelect())






    data1_4=[
        (2,'清潔感あり'),
        (1,'不快感あり'),
        (0,'不快感なし')
    ]
    choice1_4=forms.ChoiceField(label='清潔:⑴作業者の保護手袋、作業着に著しい汚れはなく清潔感があるか？',choices=data1_4,widget=forms.RadioSelect())

    

    data2_4=[
        (2,'している'),
        (0,'していない')
    ]
    choice2_4=forms.ChoiceField(label='清潔:⑵作業着、作業靴、保護具はきちんとした決められた物を使用しているか？',choices=data2_4,widget=forms.RadioSelect())

    data3_4=[
        (2,'積極的に参加'),
        (1,'必要に応じ参加'),
        (0,'担当任せ')
    ]
    choice3_4=forms.ChoiceField(label='清潔:⑶共有エリア（倉庫・休憩室・トイレ・喫煙室・廃棄物置き場等）の５S活動もしているか？',choices=data3_4,widget=forms.RadioSelect())

    data4_4=[
        (2,'問題なし'),
        (1,'安全は考慮'),
        (0,'考慮不足')
    ]
    choice4_4=forms.ChoiceField(label='清潔:⑷設備・装置・測定器・PCの配線の仕舞は安全や清掃を考慮しているか？',choices=data4_4,widget=forms.RadioSelect())

    data5_4=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5_4=forms.ChoiceField(label='清潔:⑸床や壁が損傷していたり、照明器具が切れていたり、タコ足配線がないか？',choices=data5_4,widget=forms.RadioSelect())

    data6_4=[
        (2,'日々管理'),
        (1,'適時管理'),
        (0,'管理不足')
    ]
    choice6_4=forms.ChoiceField(label='清潔:⑹活動版は常設され、史料に破れ。垂れ・剥がれ・汚れがないか？',choices=data6_4,widget=forms.RadioSelect())

    data7_4=[
        (2,'なっている'),
        (0,'なっていない')
    ]
    choice7_4=forms.ChoiceField(label='清潔:⑺５Sパトロールの結果、連続で不合格の状態となっていないか？',choices=data7_4,widget=forms.RadioSelect())

    data8_4=[
        (2,'ない'),
        (0,'ある')
    ]
    choice8_4=forms.ChoiceField(label='清潔:⑻作業エリアに落下の危険のあるもの、燃えやすいものの放置はないか？',choices=data8_4,widget=forms.RadioSelect())

    data9_4=[
        (2,'自信あり'),
        (1,'言える'),
        (0,'改善要')
    ]
    choice9_4=forms.ChoiceField(label='清潔:⑼作業エリアはお客様が見て不安を与えない状況と言えるか？',choices=data9_4,widget=forms.RadioSelect())

    data10_4=[
        (2,'点検記録あり'),
        (1,'点検はしている'),
        (0,'点検不備')
    ]
    choice10_4=forms.ChoiceField(label='清潔:⑽設備や測定器の保守点検は実施され、必要能力を発揮できているか？',choices=data10_4,widget=forms.RadioSelect())


    data1_5=[
        (2,'自信あり'),
        (1,'できている'),
        (0,'できていない')
    ]
    choice1_5=forms.ChoiceField(label='躾:⑴社内・社外の人に対して気持ちの良い挨拶ができているか？',choices=data1_5,widget=forms.RadioSelect())

    data2_5=[
        (2,'遵守徹底が浸透'),
        (1,'遵守している'),
        (0,'遵守不足')
    ]
    choice2_5=forms.ChoiceField(label='躾:⑵決められた社内ルールを理解し厳守しているか？',choices=data2_5,widget=forms.RadioSelect())

    data3_5=[
        (2,'守っている'),
        (0,'一部不足')
    ]
    choice3_5=forms.ChoiceField(label='躾:⑶廃棄物の処理ルールを全員が正しく理解しているか？',choices=data3_5,widget=forms.RadioSelect())

    data4_5=[
        (2,'一目で分かる'),
        (1,'共有化はしている'),
        (0,'共有化不足')
    ]
    choice4_5=forms.ChoiceField(label='躾:⑷必要な情報は掲示板等で共有し見える化（周知）されているか？',choices=data4_5,widget=forms.RadioSelect())

    data5_5=[
        (2,'自己チェックもあり'),
        (1,'している'),
        (0,'していない')
    ]
    choice5_5=forms.ChoiceField(label='躾:⑸パトロールによる５Sチェックを１回/月以上は実施しているか？',choices=data5_5,widget=forms.RadioSelect())

    data6_5=[
        (2,'計画的に進行'),
        (1,'進んでいる'),
        (0,'停滞あり')
    ]
    choice6_5=forms.ChoiceField(label='躾:⑹各種パトロールの指摘事項の改善は進んでいるか？',choices=data6_5,widget=forms.RadioSelect())

    data7_5=[
        (2,'率先して対策'),
        (1,'している'),
        (0,'関心低い')
    ]
    choice7_5=forms.ChoiceField(label='躾:⑺共有エリアで気付いた不具合や問題もリーダーや管理職へ報告しているか？',choices=data7_5,widget=forms.RadioSelect())

    data8_5=[
        (2,'守っている'),
        (0,'一部ルーズ')
    ]
    choice8_5=forms.ChoiceField(label='躾:⑻就業時間、休憩時間は守られているか？',choices=data8_5,widget=forms.RadioSelect())

    data9_5=[
        (2,'付けている'),
        (0,'付けていない')
    ]
    choice9_5=forms.ChoiceField(label='躾:⑼名札はきちんと見える場所につけられているか？',choices=data9_5,widget=forms.RadioSelect())

    data10_5=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'できていない')
    ]
    choice10_5=forms.ChoiceField(label='躾:⑽５Sを含めた現場の問題・課題を共有できているか？',choices=data10_5,widget=forms.RadioSelect())

class saiten_form_e(forms.Form):
    data1=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice1=forms.ChoiceField(label='整理:⑴不必要、故障している設備・測定器・治工具の放置はないか？',choices=data1,widget=forms.RadioSelect())

    data2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'曖昧な管理')
    ]
    choice2=forms.ChoiceField(label='整理:⑵製品・不良品・仕掛品の管理状態はわかるか？',choices=data2,widget=forms.RadioSelect())

    data3=[
        (2,'置いている'),
        (1,'場所は決まっている'),
        (0,'置かれていない')
    ]
    choice3=forms.ChoiceField(label='整理:⑶部品・備品・工具・文具は決められた場所に必要量のみ置いているか？',choices=data3,widget=forms.RadioSelect())

    data4=[
        (2,'一目で分かる'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice4=forms.ChoiceField(label='整理:⑷識別表示が製品・不良品・仕掛品にされているか？',choices=data4,widget=forms.RadioSelect())

    data5=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5=forms.ChoiceField(label='整理:⑸原材料・資材・素材・製品の保管環境は品質管理上、問題ないか？',choices=data5,widget=forms.RadioSelect())

    data6=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice6=forms.ChoiceField(label='整理:⑹エリアメンバーで処置判断ができないものはないか？',choices=data6,widget=forms.RadioSelect())

    data7=[
        (2,'していない'),
        (0,'している')
    ]
    choice7=forms.ChoiceField(label='整理:⑺設備・装置・測定器・治工具を一部破損/故障したまま使用してないか？',choices=data7,widget=forms.RadioSelect())

    data8=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8=forms.ChoiceField(label='整理:⑻仮置き等、一時的に非定常な状況を分かる化（表示）しているか？',choices=data8,widget=forms.RadioSelect())

    data9=[
        (2,'管理している'),
        (0,'管理してない')
    ]
    choice9=forms.ChoiceField(label='整理:⑼掲示物に古いものは無く、きちんと見える位置に貼られているか？',choices=data9,widget=forms.RadioSelect())

    data10=[
        (2,'ない'),
        (0,'ある')
    ]
    choice10=forms.ChoiceField(label='整理:⑽作業/避難通路内、配電盤前、消化設備前、非常口前に物を置いていないか？',choices=data10,widget=forms.RadioSelect())


    data1_2=[
        (2,'ない'),
        (0,'ある')
    ]
    choice1_2=forms.ChoiceField(label='整頓:⑴治工具類や書類が設備や測定器、机の上へ放置されていないか？',choices=data1_2,widget=forms.RadioSelect())

    data2_2=[
        (2,'常時徹底'),
        (1,'意識はしている'),
        (0,'意識は薄い')
    ]
    choice2_2=forms.ChoiceField(label='整頓:⑵物の置き方、掲示物の貼り方、区画線の引き方は「真っ直ぐ」を意識しているか？',choices=data2_2,widget=forms.RadioSelect())

    data3_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice3_2=forms.ChoiceField(label='整頓:⑶ストック品と使用品を区別している状況がわかるか？',choices=data3_2,widget=forms.RadioSelect())

    data4_2=[
        (2,'混在なし'),
        (0,'混在あり')
    ]
    choice4_2=forms.ChoiceField(label='整頓:⑷種類の異なる備品、製品が混雑して保管されていないか？',choices=data4_2,widget=forms.RadioSelect())

    data5_2=[
        (2,'容易にできる'),
        (1,'支障はなし'),
        (0,'やり難い')
    ]
    choice5_2=forms.ChoiceField(label='整頓:⑸設備や測定器周りは、支障なくメンテナンスができているか？',choices=data5_2,widget=forms.RadioSelect())

    data6_2=[
        (2,'している'),
        (1,'様子はわかる'),
        (0,'分からない')
    ]
    choice6_2=forms.ChoiceField(label='整頓:⑹通路と設備・作業場・置き場は区分され、区画線で表記しているか？',choices=data6_2,widget=forms.RadioSelect())

    data7_2=[
        (2,'ない'),
        (1,'あるが明記あり'),
        (0,'ある')
    ]
    choice7_2=forms.ChoiceField(label='整頓:⑺製品や資材・備品の直置きや立てかけはないか？',choices=data7_2,widget=forms.RadioSelect())

    data8_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_2=forms.ChoiceField(label='整頓:⑻良品・不良品・仕掛品が区分けされ、識別管理できているか？',choices=data8_2,widget=forms.RadioSelect())

    data9_2=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice9_2=forms.ChoiceField(label='整頓:⑼保管物は番地管理（置き場所管理）されて、数量等の情報が把握できるか？',choices=data9_2,widget=forms.RadioSelect())

    data10_2=[
        (2,'滞留なし'),
        (1,'適量のみ'),
        (0,'溜まっている')
    ]
    choice10_2=forms.ChoiceField(label='整頓:⑽工程内に仕掛品・保留品が留まっていないか？',choices=data10_2,widget=forms.RadioSelect())








    data1_3=[
        (2,'している'),
        (0,'曖昧な管理')
    ]
    choice1_3=forms.ChoiceField(label='清掃:⑴清掃ルールを決めて維持管理を行っているか？',choices=data1_3,widget=forms.RadioSelect())

    data2_3=[
        (2,'出さない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice2_3=forms.ChoiceField(label='清掃:⑵床に水・油・薬液・素材屑が落ちていないか？',choices=data2_3,widget=forms.RadioSelect())

    data3_3=[
        (2,'汚れない工夫あり'),
        (1,'ない'),
        (0,'ある')
    ]
    choice3_3=forms.ChoiceField(label='清掃:⑶床・机・ラック・設備・装置・測定器に埃や汚れがないか？',choices=data3_3,widget=forms.RadioSelect())

    data4_3=[
        (2,'している'),
        (0,'考慮不足')
    ]
    choice4_3=forms.ChoiceField(label='清掃:⑷ゴミ箱は必要以上に配置せず、必要最低限の数としているか？',choices=data4_3,widget=forms.RadioSelect())

    data5_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice5_3=forms.ChoiceField(label='清掃:⑸設備周辺や作業エリアに備品類が落ちていないか？',choices=data5_3,widget=forms.RadioSelect())

    data6_3=[
        (2,'ない'),
        (0,'ある')
    ]
    choice6_3=forms.ChoiceField(label='清掃:⑹製品を入れる容器や運搬代が埃等で汚れていないか？',choices=data6_3,widget=forms.RadioSelect())

    data7_3=[
        (2,'している'),
        (0,'していない')
    ]
    choice7_3=forms.ChoiceField(label='清掃:⑺清掃用具は決められた場所に必要なものと数だけ保管しているか？',choices=data7_3,widget=forms.RadioSelect())

    data8_3=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'分からない')
    ]
    choice8_3=forms.ChoiceField(label='清掃:⑻廃棄物（ゴミ）は分別容器などで正しく分けているか？',choices=data8_3,widget=forms.RadioSelect())

    data9_3=[
        (2,'適切に処理'),
        (0,'溢れあり')
    ]
    choice9_3=forms.ChoiceField(label='清掃:⑼ゴミ箱から溢れることなく、ゴミの廃棄タイミングは適切な状況か？',choices=data9_3,widget=forms.RadioSelect())

    data10_3=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice10_3=forms.ChoiceField(label='清掃:⑽部屋の換気や作業時の換気は正しく行われ、環境に問題はないか？',choices=data10_3,widget=forms.RadioSelect())






    data1_4=[
        (2,'清潔感あり'),
        (1,'不快感あり'),
        (0,'不快感なし')
    ]
    choice1_4=forms.ChoiceField(label='清潔:⑴作業者の保護手袋、作業着に著しい汚れはなく清潔感があるか？',choices=data1_4,widget=forms.RadioSelect())

    

    data2_4=[
        (2,'している'),
        (0,'していない')
    ]
    choice2_4=forms.ChoiceField(label='清潔:⑵作業着、作業靴、保護具はきちんとした決められた物を使用しているか？',choices=data2_4,widget=forms.RadioSelect())

    data3_4=[
        (2,'積極的に参加'),
        (1,'必要に応じ参加'),
        (0,'担当任せ')
    ]
    choice3_4=forms.ChoiceField(label='清潔:⑶共有エリア（倉庫・休憩室・トイレ・喫煙室・廃棄物置き場等）の５S活動もしているか？',choices=data3_4,widget=forms.RadioSelect())

    data4_4=[
        (2,'問題なし'),
        (1,'安全は考慮'),
        (0,'考慮不足')
    ]
    choice4_4=forms.ChoiceField(label='清潔:⑷設備・装置・測定器・PCの配線の仕舞は安全や清掃を考慮しているか？',choices=data4_4,widget=forms.RadioSelect())

    data5_4=[
        (2,'問題なし'),
        (0,'問題あり')
    ]
    choice5_4=forms.ChoiceField(label='清潔:⑸床や壁が損傷していたり、照明器具が切れていたり、タコ足配線がないか？',choices=data5_4,widget=forms.RadioSelect())

    data6_4=[
        (2,'日々管理'),
        (1,'適時管理'),
        (0,'管理不足')
    ]
    choice6_4=forms.ChoiceField(label='清潔:⑹活動版は常設され、史料に破れ。垂れ・剥がれ・汚れがないか？',choices=data6_4,widget=forms.RadioSelect())

    data7_4=[
        (2,'なっている'),
        (0,'なっていない')
    ]
    choice7_4=forms.ChoiceField(label='清潔:⑺５Sパトロールの結果、連続で不合格の状態となっていないか？',choices=data7_4,widget=forms.RadioSelect())

    data8_4=[
        (2,'ない'),
        (0,'ある')
    ]
    choice8_4=forms.ChoiceField(label='清潔:⑻作業エリアに落下の危険のあるもの、燃えやすいものの放置はないか？',choices=data8_4,widget=forms.RadioSelect())

    data9_4=[
        (2,'自信あり'),
        (1,'言える'),
        (0,'改善要')
    ]
    choice9_4=forms.ChoiceField(label='清潔:⑼作業エリアはお客様が見て不安を与えない状況と言えるか？',choices=data9_4,widget=forms.RadioSelect())

    data10_4=[
        (2,'点検記録あり'),
        (1,'点検はしている'),
        (0,'点検不備')
    ]
    choice10_4=forms.ChoiceField(label='清潔:⑽設備や測定器の保守点検は実施され、必要能力を発揮できているか？',choices=data10_4,widget=forms.RadioSelect())


    data1_5=[
        (2,'自信あり'),
        (1,'できている'),
        (0,'できていない')
    ]
    choice1_5=forms.ChoiceField(label='躾:⑴社内・社外の人に対して気持ちの良い挨拶ができているか？',choices=data1_5,widget=forms.RadioSelect())

    data2_5=[
        (2,'遵守徹底が浸透'),
        (1,'遵守している'),
        (0,'遵守不足')
    ]
    choice2_5=forms.ChoiceField(label='躾:⑵決められた社内ルールを理解し厳守しているか？',choices=data2_5,widget=forms.RadioSelect())

    data3_5=[
        (2,'守っている'),
        (0,'一部不足')
    ]
    choice3_5=forms.ChoiceField(label='躾:⑶廃棄物の処理ルールを全員が正しく理解しているか？',choices=data3_5,widget=forms.RadioSelect())

    data4_5=[
        (2,'一目で分かる'),
        (1,'共有化はしている'),
        (0,'共有化不足')
    ]
    choice4_5=forms.ChoiceField(label='躾:⑷必要な情報は掲示板等で共有し見える化（周知）されているか？',choices=data4_5,widget=forms.RadioSelect())

    data5_5=[
        (2,'自己チェックもあり'),
        (1,'している'),
        (0,'していない')
    ]
    choice5_5=forms.ChoiceField(label='躾:⑸パトロールによる５Sチェックを１回/月以上は実施しているか？',choices=data5_5,widget=forms.RadioSelect())

    data6_5=[
        (2,'計画的に進行'),
        (1,'進んでいる'),
        (0,'停滞あり')
    ]
    choice6_5=forms.ChoiceField(label='躾:⑹各種パトロールの指摘事項の改善は進んでいるか？',choices=data6_5,widget=forms.RadioSelect())

    data7_5=[
        (2,'率先して対策'),
        (1,'している'),
        (0,'関心低い')
    ]
    choice7_5=forms.ChoiceField(label='躾:⑺共有エリアで気付いた不具合や問題もリーダーや管理職へ報告しているか？',choices=data7_5,widget=forms.RadioSelect())

    data8_5=[
        (2,'守っている'),
        (0,'一部ルーズ')
    ]
    choice8_5=forms.ChoiceField(label='躾:⑻就業時間、休憩時間は守られているか？',choices=data8_5,widget=forms.RadioSelect())

    data9_5=[
        (2,'付けている'),
        (0,'付けていない')
    ]
    choice9_5=forms.ChoiceField(label='躾:⑼名札はきちんと見える場所につけられているか？',choices=data9_5,widget=forms.RadioSelect())

    data10_5=[
        (2,'一目で分かる'),
        (1,'様子は分かる'),
        (0,'できていない')
    ]
    choice10_5=forms.ChoiceField(label='躾:⑽５Sを含めた現場の問題・課題を共有できているか？',choices=data10_5,widget=forms.RadioSelect())