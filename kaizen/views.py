from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
from .models import *
from django.shortcuts import redirect
import matplotlib
import pandas as pd
matplotlib.use('Agg')
import japanize_matplotlib
import matplotlib.pyplot as plt
import io
import seaborn as sns
sns.set(font='IPAexGothic')
import numpy as np
from matplotlib.pyplot import figure
import datetime
from django.contrib.auth.decorators import login_required
 

today=datetime.date.today()
nen=today.year
now=datetime.datetime.now()
# Create your views here.

team_kaizen1_kijun=team_kaizen1.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
team_kaizen1_kijun2=team_kaizen1_kijun[0]
#チームネーム1    
team_kaizen1_kijun_team_name=team_kaizen1_kijun2['team_name']
#改善必要枚数
team_kaizen1_kijun_kaizen_teian_hituyou_maisuu=team_kaizen1_kijun2['kaizen_teian_hituyou_maisuu']
#年間目標の金額
team_kaizen1_kijun_nenkan_mokuhyou_kingaku=team_kaizen1_kijun2['nenkan_mokuhyou_kingaku']
#チームメンバー人数
team_kaizen1_kijun_team_member_ninzuu=team_kaizen1_kijun2['team_member_ninzuu']
team_kaizen2_kijun=team_kaizen2.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
team_kaizen2_kijun2=team_kaizen2_kijun[0]
#チームネーム2    
team_kaizen2_kijun_team_name=team_kaizen2_kijun2['team_name']
#改善必要枚数
team_kaizen2_kijun_kaizen_teian_hituyou_maisuu=team_kaizen2_kijun2['kaizen_teian_hituyou_maisuu']
#年間目標の金額
team_kaizen2_kijun_nenkan_mokuhyou_kingaku=team_kaizen2_kijun2['nenkan_mokuhyou_kingaku']
#チームメンバー人数
team_kaizen2_kijun_team_member_ninzuu=team_kaizen2_kijun2['team_member_ninzuu']

team_kaizen3_kijun=team_kaizen3.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
team_kaizen3_kijun2=team_kaizen3_kijun[0]
#チームネーム3    
team_kaizen3_kijun_team_name=team_kaizen3_kijun2['team_name']
#改善必要枚数
team_kaizen3_kijun_kaizen_teian_hituyou_maisuu=team_kaizen3_kijun2['kaizen_teian_hituyou_maisuu']
#年間目標の金額
team_kaizen3_kijun_nenkan_mokuhyou_kingaku=team_kaizen3_kijun2['nenkan_mokuhyou_kingaku']
#チームメンバー人数
team_kaizen3_kijun_team_member_ninzuu=team_kaizen3_kijun2['team_member_ninzuu']

team_kaizen4_kijun=team_kaizen4.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
team_kaizen4_kijun2=team_kaizen4_kijun[0]
#チームネーム4    
team_kaizen4_kijun_team_name=team_kaizen4_kijun2['team_name']
#改善必要枚数
team_kaizen4_kijun_kaizen_teian_hituyou_maisuu=team_kaizen4_kijun2['kaizen_teian_hituyou_maisuu']
#年間目標の金額
team_kaizen4_kijun_nenkan_mokuhyou_kingaku=team_kaizen4_kijun2['nenkan_mokuhyou_kingaku']
#チームメンバー人数
team_kaizen4_kijun_team_member_ninzuu=team_kaizen4_kijun2['team_member_ninzuu']

team_kaizen5_kijun=team_kaizen5.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
team_kaizen5_kijun2=team_kaizen5_kijun[0]
#チームネーム5    
team_kaizen5_kijun_team_name=team_kaizen5_kijun2['team_name']
#改善必要枚数
team_kaizen5_kijun_kaizen_teian_hituyou_maisuu=team_kaizen5_kijun2['kaizen_teian_hituyou_maisuu']
#年間目標の金額
team_kaizen5_kijun_nenkan_mokuhyou_kingaku=team_kaizen5_kijun2['nenkan_mokuhyou_kingaku']
#チームメンバー人数
team_kaizen5_kijun_team_member_ninzuu=team_kaizen5_kijun2['team_member_ninzuu']

team_kaizen6_kijun=team_kaizen6.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
team_kaizen6_kijun2=team_kaizen6_kijun[0]
#チームネーム6    
team_kaizen6_kijun_team_name=team_kaizen6_kijun2['team_name']
#改善必要枚数
team_kaizen6_kijun_kaizen_teian_hituyou_maisuu=team_kaizen6_kijun2['kaizen_teian_hituyou_maisuu']
#年間目標の金額
team_kaizen6_kijun_nenkan_mokuhyou_kingaku=team_kaizen6_kijun2['nenkan_mokuhyou_kingaku']
#チームメンバー人数
team_kaizen6_kijun_team_member_ninzuu=team_kaizen6_kijun2['team_member_ninzuu']


#チーム１
team_kaizen1_kiroku2=team_kaizen1_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
team1_kiroku1=team_kaizen1_kiroku2[0]
team1_kiroku2=team_kaizen1_kiroku2[1]
team1_kiroku3=team_kaizen1_kiroku2[2]
team1_kiroku4=team_kaizen1_kiroku2[3]
team1_kiroku5=team_kaizen1_kiroku2[4]
team1_kiroku6=team_kaizen1_kiroku2[5]
team1_kiroku7=team_kaizen1_kiroku2[6]
team1_kiroku8=team_kaizen1_kiroku2[7]
team1_kiroku9=team_kaizen1_kiroku2[8]
team1_kiroku10=team_kaizen1_kiroku2[9]
team1_kiroku11=team_kaizen1_kiroku2[10]
team1_kiroku12=team_kaizen1_kiroku2[11]

team1_kiroku1_output_kaizenteian=team1_kiroku1['output_kaizenteian']
team1_kiroku2_output_kaizenteian=team1_kiroku2['output_kaizenteian']
team1_kiroku3_output_kaizenteian=team1_kiroku3['output_kaizenteian']
team1_kiroku4_output_kaizenteian=team1_kiroku4['output_kaizenteian']
team1_kiroku5_output_kaizenteian=team1_kiroku5['output_kaizenteian']
team1_kiroku6_output_kaizenteian=team1_kiroku6['output_kaizenteian']
team1_kiroku7_output_kaizenteian=team1_kiroku7['output_kaizenteian']
team1_kiroku8_output_kaizenteian=team1_kiroku8['output_kaizenteian']
team1_kiroku9_output_kaizenteian=team1_kiroku9['output_kaizenteian']
team1_kiroku10_output_kaizenteian=team1_kiroku10['output_kaizenteian']
team1_kiroku11_output_kaizenteian=team1_kiroku11['output_kaizenteian']
team1_kiroku12_output_kaizenteian=team1_kiroku12['output_kaizenteian']

team1_kiroku1_output_kingaku=team1_kiroku1['output_kingaku']
team1_kiroku2_output_kingaku=team1_kiroku2['output_kingaku']
team1_kiroku3_output_kingaku=team1_kiroku3['output_kingaku']
team1_kiroku4_output_kingaku=team1_kiroku4['output_kingaku']
team1_kiroku5_output_kingaku=team1_kiroku5['output_kingaku']
team1_kiroku6_output_kingaku=team1_kiroku6['output_kingaku']
team1_kiroku7_output_kingaku=team1_kiroku7['output_kingaku']
team1_kiroku8_output_kingaku=team1_kiroku8['output_kingaku']
team1_kiroku9_output_kingaku=team1_kiroku9['output_kingaku']
team1_kiroku10_output_kingaku=team1_kiroku10['output_kingaku']
team1_kiroku11_output_kingaku=team1_kiroku11['output_kingaku']
team1_kiroku12_output_kingaku=team1_kiroku12['output_kingaku']



#チーム2
team_kaizen2_kiroku2=team_kaizen2_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
team2_kiroku1=team_kaizen2_kiroku2[0]
team2_kiroku2=team_kaizen2_kiroku2[1]
team2_kiroku3=team_kaizen2_kiroku2[2]
team2_kiroku4=team_kaizen2_kiroku2[3]
team2_kiroku5=team_kaizen2_kiroku2[4]
team2_kiroku6=team_kaizen2_kiroku2[5]
team2_kiroku7=team_kaizen2_kiroku2[6]
team2_kiroku8=team_kaizen2_kiroku2[7]
team2_kiroku9=team_kaizen2_kiroku2[8]
team2_kiroku10=team_kaizen2_kiroku2[9]
team2_kiroku11=team_kaizen2_kiroku2[10]
team2_kiroku12=team_kaizen2_kiroku2[11]

team2_kiroku1_output_kaizenteian=team2_kiroku1['output_kaizenteian']
team2_kiroku2_output_kaizenteian=team2_kiroku2['output_kaizenteian']
team2_kiroku3_output_kaizenteian=team2_kiroku3['output_kaizenteian']
team2_kiroku4_output_kaizenteian=team2_kiroku4['output_kaizenteian']
team2_kiroku5_output_kaizenteian=team2_kiroku5['output_kaizenteian']
team2_kiroku6_output_kaizenteian=team2_kiroku6['output_kaizenteian']
team2_kiroku7_output_kaizenteian=team2_kiroku7['output_kaizenteian']
team2_kiroku8_output_kaizenteian=team2_kiroku8['output_kaizenteian']
team2_kiroku9_output_kaizenteian=team2_kiroku9['output_kaizenteian']
team2_kiroku10_output_kaizenteian=team2_kiroku10['output_kaizenteian']
team2_kiroku11_output_kaizenteian=team2_kiroku11['output_kaizenteian']
team2_kiroku12_output_kaizenteian=team2_kiroku12['output_kaizenteian']

team2_kiroku1_output_kingaku=team2_kiroku1['output_kingaku']
team2_kiroku2_output_kingaku=team2_kiroku2['output_kingaku']
team2_kiroku3_output_kingaku=team2_kiroku3['output_kingaku']
team2_kiroku4_output_kingaku=team2_kiroku4['output_kingaku']
team2_kiroku5_output_kingaku=team2_kiroku5['output_kingaku']
team2_kiroku6_output_kingaku=team2_kiroku6['output_kingaku']
team2_kiroku7_output_kingaku=team2_kiroku7['output_kingaku']
team2_kiroku8_output_kingaku=team2_kiroku8['output_kingaku']
team2_kiroku9_output_kingaku=team2_kiroku9['output_kingaku']
team2_kiroku10_output_kingaku=team2_kiroku10['output_kingaku']
team2_kiroku11_output_kingaku=team2_kiroku11['output_kingaku']
team2_kiroku12_output_kingaku=team2_kiroku12['output_kingaku']




#チーム3
team_kaizen3_kiroku2=team_kaizen3_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
team3_kiroku1=team_kaizen3_kiroku2[0]
team3_kiroku2=team_kaizen3_kiroku2[1]
team3_kiroku3=team_kaizen3_kiroku2[2]
team3_kiroku4=team_kaizen3_kiroku2[3]
team3_kiroku5=team_kaizen3_kiroku2[4]
team3_kiroku6=team_kaizen3_kiroku2[5]
team3_kiroku7=team_kaizen3_kiroku2[6]
team3_kiroku8=team_kaizen3_kiroku2[7]
team3_kiroku9=team_kaizen3_kiroku2[8]
team3_kiroku10=team_kaizen3_kiroku2[9]
team3_kiroku11=team_kaizen3_kiroku2[10]
team3_kiroku12=team_kaizen3_kiroku2[11]

team3_kiroku1_output_kaizenteian=team3_kiroku1['output_kaizenteian']
team3_kiroku2_output_kaizenteian=team3_kiroku2['output_kaizenteian']
team3_kiroku3_output_kaizenteian=team3_kiroku3['output_kaizenteian']
team3_kiroku4_output_kaizenteian=team3_kiroku4['output_kaizenteian']
team3_kiroku5_output_kaizenteian=team3_kiroku5['output_kaizenteian']
team3_kiroku6_output_kaizenteian=team3_kiroku6['output_kaizenteian']
team3_kiroku7_output_kaizenteian=team3_kiroku7['output_kaizenteian']
team3_kiroku8_output_kaizenteian=team3_kiroku8['output_kaizenteian']
team3_kiroku9_output_kaizenteian=team3_kiroku9['output_kaizenteian']
team3_kiroku10_output_kaizenteian=team3_kiroku10['output_kaizenteian']
team3_kiroku11_output_kaizenteian=team3_kiroku11['output_kaizenteian']
team3_kiroku12_output_kaizenteian=team3_kiroku12['output_kaizenteian']

team3_kiroku1_output_kingaku=team3_kiroku1['output_kingaku']
team3_kiroku2_output_kingaku=team3_kiroku2['output_kingaku']
team3_kiroku3_output_kingaku=team3_kiroku3['output_kingaku']
team3_kiroku4_output_kingaku=team3_kiroku4['output_kingaku']
team3_kiroku5_output_kingaku=team3_kiroku5['output_kingaku']
team3_kiroku6_output_kingaku=team3_kiroku6['output_kingaku']
team3_kiroku7_output_kingaku=team3_kiroku7['output_kingaku']
team3_kiroku8_output_kingaku=team3_kiroku8['output_kingaku']
team3_kiroku9_output_kingaku=team3_kiroku9['output_kingaku']
team3_kiroku10_output_kingaku=team3_kiroku10['output_kingaku']
team3_kiroku11_output_kingaku=team3_kiroku11['output_kingaku']
team3_kiroku12_output_kingaku=team3_kiroku12['output_kingaku']




#チーム4
team_kaizen4_kiroku2=team_kaizen4_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
team4_kiroku1=team_kaizen4_kiroku2[0]
team4_kiroku2=team_kaizen4_kiroku2[1]
team4_kiroku3=team_kaizen4_kiroku2[2]
team4_kiroku4=team_kaizen4_kiroku2[3]
team4_kiroku5=team_kaizen4_kiroku2[4]
team4_kiroku6=team_kaizen4_kiroku2[5]
team4_kiroku7=team_kaizen4_kiroku2[6]
team4_kiroku8=team_kaizen4_kiroku2[7]
team4_kiroku9=team_kaizen4_kiroku2[8]
team4_kiroku10=team_kaizen4_kiroku2[9]
team4_kiroku11=team_kaizen4_kiroku2[10]
team4_kiroku12=team_kaizen4_kiroku2[11]

team4_kiroku1_output_kaizenteian=team4_kiroku1['output_kaizenteian']
team4_kiroku2_output_kaizenteian=team4_kiroku2['output_kaizenteian']
team4_kiroku3_output_kaizenteian=team4_kiroku3['output_kaizenteian']
team4_kiroku4_output_kaizenteian=team4_kiroku4['output_kaizenteian']
team4_kiroku5_output_kaizenteian=team4_kiroku5['output_kaizenteian']
team4_kiroku6_output_kaizenteian=team4_kiroku6['output_kaizenteian']
team4_kiroku7_output_kaizenteian=team4_kiroku7['output_kaizenteian']
team4_kiroku8_output_kaizenteian=team4_kiroku8['output_kaizenteian']
team4_kiroku9_output_kaizenteian=team4_kiroku9['output_kaizenteian']
team4_kiroku10_output_kaizenteian=team4_kiroku10['output_kaizenteian']
team4_kiroku11_output_kaizenteian=team4_kiroku11['output_kaizenteian']
team4_kiroku12_output_kaizenteian=team4_kiroku12['output_kaizenteian']

team4_kiroku1_output_kingaku=team4_kiroku1['output_kingaku']
team4_kiroku2_output_kingaku=team4_kiroku2['output_kingaku']
team4_kiroku3_output_kingaku=team4_kiroku3['output_kingaku']
team4_kiroku4_output_kingaku=team4_kiroku4['output_kingaku']
team4_kiroku5_output_kingaku=team4_kiroku5['output_kingaku']
team4_kiroku6_output_kingaku=team4_kiroku6['output_kingaku']
team4_kiroku7_output_kingaku=team4_kiroku7['output_kingaku']
team4_kiroku8_output_kingaku=team4_kiroku8['output_kingaku']
team4_kiroku9_output_kingaku=team4_kiroku9['output_kingaku']
team4_kiroku10_output_kingaku=team4_kiroku10['output_kingaku']
team4_kiroku11_output_kingaku=team4_kiroku11['output_kingaku']
team4_kiroku12_output_kingaku=team4_kiroku12['output_kingaku']




#チーム5
team_kaizen5_kiroku2=team_kaizen5_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
team5_kiroku1=team_kaizen5_kiroku2[0]
team5_kiroku2=team_kaizen5_kiroku2[1]
team5_kiroku3=team_kaizen5_kiroku2[2]
team5_kiroku4=team_kaizen5_kiroku2[3]
team5_kiroku5=team_kaizen5_kiroku2[4]
team5_kiroku6=team_kaizen5_kiroku2[5]
team5_kiroku7=team_kaizen5_kiroku2[6]
team5_kiroku8=team_kaizen5_kiroku2[7]
team5_kiroku9=team_kaizen5_kiroku2[8]
team5_kiroku10=team_kaizen5_kiroku2[9]
team5_kiroku11=team_kaizen5_kiroku2[10]
team5_kiroku12=team_kaizen5_kiroku2[11]

team5_kiroku1_output_kaizenteian=team5_kiroku1['output_kaizenteian']
team5_kiroku2_output_kaizenteian=team5_kiroku2['output_kaizenteian']
team5_kiroku3_output_kaizenteian=team5_kiroku3['output_kaizenteian']
team5_kiroku4_output_kaizenteian=team5_kiroku4['output_kaizenteian']
team5_kiroku5_output_kaizenteian=team5_kiroku5['output_kaizenteian']
team5_kiroku6_output_kaizenteian=team5_kiroku6['output_kaizenteian']
team5_kiroku7_output_kaizenteian=team5_kiroku7['output_kaizenteian']
team5_kiroku8_output_kaizenteian=team5_kiroku8['output_kaizenteian']
team5_kiroku9_output_kaizenteian=team5_kiroku9['output_kaizenteian']
team5_kiroku10_output_kaizenteian=team5_kiroku10['output_kaizenteian']
team5_kiroku11_output_kaizenteian=team5_kiroku11['output_kaizenteian']
team5_kiroku12_output_kaizenteian=team5_kiroku12['output_kaizenteian']

team5_kiroku1_output_kingaku=team5_kiroku1['output_kingaku']
team5_kiroku2_output_kingaku=team5_kiroku2['output_kingaku']
team5_kiroku3_output_kingaku=team5_kiroku3['output_kingaku']
team5_kiroku4_output_kingaku=team5_kiroku4['output_kingaku']
team5_kiroku5_output_kingaku=team5_kiroku5['output_kingaku']
team5_kiroku6_output_kingaku=team5_kiroku6['output_kingaku']
team5_kiroku7_output_kingaku=team5_kiroku7['output_kingaku']
team5_kiroku8_output_kingaku=team5_kiroku8['output_kingaku']
team5_kiroku9_output_kingaku=team5_kiroku9['output_kingaku']
team5_kiroku10_output_kingaku=team5_kiroku10['output_kingaku']
team5_kiroku11_output_kingaku=team5_kiroku11['output_kingaku']
team5_kiroku12_output_kingaku=team5_kiroku12['output_kingaku']




#チーム6
team_kaizen6_kiroku2=team_kaizen6_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
team6_kiroku1=team_kaizen6_kiroku2[0]
team6_kiroku2=team_kaizen6_kiroku2[1]
team6_kiroku3=team_kaizen6_kiroku2[2]
team6_kiroku4=team_kaizen6_kiroku2[3]
team6_kiroku5=team_kaizen6_kiroku2[4]
team6_kiroku6=team_kaizen6_kiroku2[5]
team6_kiroku7=team_kaizen6_kiroku2[6]
team6_kiroku8=team_kaizen6_kiroku2[7]
team6_kiroku9=team_kaizen6_kiroku2[8]
team6_kiroku10=team_kaizen6_kiroku2[9]
team6_kiroku11=team_kaizen6_kiroku2[10]
team6_kiroku12=team_kaizen6_kiroku2[11]

team6_kiroku1_output_kaizenteian=team6_kiroku1['output_kaizenteian']
team6_kiroku2_output_kaizenteian=team6_kiroku2['output_kaizenteian']
team6_kiroku3_output_kaizenteian=team6_kiroku3['output_kaizenteian']
team6_kiroku4_output_kaizenteian=team6_kiroku4['output_kaizenteian']
team6_kiroku5_output_kaizenteian=team6_kiroku5['output_kaizenteian']
team6_kiroku6_output_kaizenteian=team6_kiroku6['output_kaizenteian']
team6_kiroku7_output_kaizenteian=team6_kiroku7['output_kaizenteian']
team6_kiroku8_output_kaizenteian=team6_kiroku8['output_kaizenteian']
team6_kiroku9_output_kaizenteian=team6_kiroku9['output_kaizenteian']
team6_kiroku10_output_kaizenteian=team6_kiroku10['output_kaizenteian']
team6_kiroku11_output_kaizenteian=team6_kiroku11['output_kaizenteian']
team6_kiroku12_output_kaizenteian=team6_kiroku12['output_kaizenteian']

team6_kiroku1_output_kingaku=team6_kiroku1['output_kingaku']
team6_kiroku2_output_kingaku=team6_kiroku2['output_kingaku']
team6_kiroku3_output_kingaku=team6_kiroku3['output_kingaku']
team6_kiroku4_output_kingaku=team6_kiroku4['output_kingaku']
team6_kiroku5_output_kingaku=team6_kiroku5['output_kingaku']
team6_kiroku6_output_kingaku=team6_kiroku6['output_kingaku']
team6_kiroku7_output_kingaku=team6_kiroku7['output_kingaku']
team6_kiroku8_output_kingaku=team6_kiroku8['output_kingaku']
team6_kiroku9_output_kingaku=team6_kiroku9['output_kingaku']
team6_kiroku10_output_kingaku=team6_kiroku10['output_kingaku']
team6_kiroku11_output_kingaku=team6_kiroku11['output_kingaku']
team6_kiroku12_output_kingaku=team6_kiroku12['output_kingaku']

@login_required
def kaizen_seika_1(request):
    data=team_kaizen1_kiroku.objects.all()
    
    params={
        'title':'改善提案/合理化',
        'message':'毎月の改善成果を変更してください',
        'data':data,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,

    }
    
    return render(request,'kaizen/kaizen_seika_1.html',params)

@login_required
def kaizen_seika_2(request):
    data=team_kaizen2_kiroku.objects.all()
    
    params={
        'title':'改善提案/合理化',
        'message':'毎月の改善成果を変更してください',
        'data':data,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/kaizen_seika_2.html',params)

@login_required
def kaizen_seika_3(request):
    data=team_kaizen3_kiroku.objects.all()
    
    params={
        'title':'改善提案/合理化',
        'message':'毎月の改善成果を変更してください',
        'data':data,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/kaizen_seika_3.html',params)

@login_required
def kaizen_seika_4(request):
    data=team_kaizen4_kiroku.objects.all()
    
    params={
        'title':'改善提案/合理化',
        'message':'毎月の改善成果を変更してください',
        'data':data,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/kaizen_seika_4.html',params)

@login_required
def kaizen_seika_5(request):
    data=team_kaizen5_kiroku.objects.all()
    
    params={
        'title':'改善提案/合理化',
        'message':'毎月の改善成果を変更してください',
        'data':data,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/kaizen_seika_5.html',params)

@login_required
def kaizen_seika_6(request):
    data=team_kaizen6_kiroku.objects.all()
    
    params={
        'title':'改善提案/合理化',
        'message':'毎月の改善成果を変更してください',
        'data':data,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/kaizen_seika_6.html',params)

@login_required
def kaizen_seika_1edit(request,num):
    obj=team_kaizen1_kiroku.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=team_kaizen1_kiroku_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/kaizen_seika_1')
    params={
        'title':'Output kaizenteian=提出した改善提案枚数　Output kingaku=合理化した金額',
        'tuki':num,
        'form':team_kaizen1_kiroku_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/kaizen_seika_1edit.html',params)

@login_required
def kaizen_seika_2edit(request,num):
    obj=team_kaizen2_kiroku.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=team_kaizen2_kiroku_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/kaizen_seika_2')
    params={
        'title':'Output kaizenteian=提出した改善提案枚数　Output kingaku=合理化した金額',
        'tuki':num,
        'form':team_kaizen2_kiroku_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/kaizen_seika_2edit.html',params)

@login_required
def kaizen_seika_3edit(request,num):
    obj=team_kaizen3_kiroku.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=team_kaizen3_kiroku_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/kaizen_seika_3')
    params={
        'title':'Output kaizenteian=提出した改善提案枚数　Output kingaku=合理化した金額',
        'tuki':num,
        'form':team_kaizen3_kiroku_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/kaizen_seika_3edit.html',params)

@login_required
def kaizen_seika_4edit(request,num):
    obj=team_kaizen4_kiroku.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=team_kaizen4_kiroku_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/kaizen_seika_4')
    params={
        'title':'Output kaizenteian=提出した改善提案枚数　Output kingaku=合理化した金額',
        'tuki':num,
        'form':team_kaizen4_kiroku_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/kaizen_seika_4edit.html',params)

@login_required
def kaizen_seika_5edit(request,num):
    obj=team_kaizen5_kiroku.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=team_kaizen5_kiroku_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/kaizen_seika_5')
    params={
        'title':'Output kaizenteian=提出した改善提案枚数　Output kingaku=合理化した金額',
        'tuki':num,
        'form':team_kaizen5_kiroku_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/kaizen_seika_5edit.html',params)

@login_required
def kaizen_seika_6edit(request,num):
    obj=team_kaizen6_kiroku.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=team_kaizen6_kiroku_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/kaizen_seika_6')
    params={
        'title':'Output kaizenteian=提出した改善提案枚数　Output kingaku=合理化した金額',
        'tuki':num,
        'form':team_kaizen6_kiroku_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/kaizen_seika_6edit.html',params)


@login_required
def team_kaizen1_1(request):
    
    team_kaizen=team_kaizen1.objects.all()

    
    params={
        'title':'チーム名変更',
        'message':'チーム名を変更した場合は変更を押して記入してください',
        'team_kaizen':team_kaizen,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/team_kaizen1.html',params)

@login_required
def team_kaizen2_2(request):
    
    team_kaizen=team_kaizen2.objects.all()

    
    params={
        'title':'チーム名変更',
        'message':'チーム名を変更した場合は変更を押して記入してください',
        'team_kaizen':team_kaizen,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/team_kaizen2.html',params)

@login_required
def team_kaizen3_3(request):
    
    team_kaizen=team_kaizen3.objects.all()

    
    params={
        'title':'チーム名変更',
        'message':'チーム名を変更した場合は変更を押して記入してください',
        'team_kaizen':team_kaizen,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/team_kaizen3.html',params)

@login_required
def team_kaizen4_4(request):
    
    team_kaizen=team_kaizen4.objects.all()

    
    params={
        'title':'チーム名変更',
        'message':'チーム名を変更した場合は変更を押して記入してください',
        'team_kaizen':team_kaizen,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/team_kaizen4.html',params)

@login_required
def team_kaizen5_5(request):
    
    team_kaizen=team_kaizen5.objects.all()

    
    params={
        'title':'チーム名変更',
        'message':'チーム名を変更した場合は変更を押して記入してください',
        'team_kaizen':team_kaizen,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/team_kaizen5.html',params)

@login_required
def team_kaizen6_6(request):
    
    team_kaizen=team_kaizen6.objects.all()

    
    params={
        'title':'チーム名変更',
        'message':'チーム名を変更した場合は変更を押して記入してください',
        'team_kaizen':team_kaizen,
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    
    return render(request,'kaizen/team_kaizen6.html',params)

@login_required
def team_kaizen1_1edit(request,num):
    obj=team_kaizen1.objects.get(id=num)
    if(request.method=='POST'):
        kaku=team_kaizen1_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/team_kaizen1_1')
    params={
        'title1':'Team name=チーム名',
        'title2':'Kaizen teian hituyou maisuu=改善提案必要枚数/月',
        'title3':'Nenkan mokuhyou kingaku=合理化目的金額/年',
        'title4':'Team member ninzuu=チーム人数',
        'id':num,
        'form':team_kaizen1_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/team_kaizen1_1edit.html',params)

@login_required
def team_kaizen2_2edit(request,num):
    obj=team_kaizen2.objects.get(id=num)
    if(request.method=='POST'):
        kaku=team_kaizen2_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/team_kaizen2_2')
    params={
        'title1':'Team name=チーム名',
        'title2':'Kaizen teian hituyou maisuu=改善提案必要枚数/月',
        'title3':'Nenkan mokuhyou kingaku=合理化目的金額/年',
        'title4':'Team member ninzuu=チーム人数',
        'id':num,
        'form':team_kaizen2_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/team_kaizen2_2edit.html',params)

@login_required
def team_kaizen3_3edit(request,num):
    obj=team_kaizen3.objects.get(id=num)
    if(request.method=='POST'):
        kaku=team_kaizen3_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/team_kaizen3_3')
    params={
        'title1':'Team name=チーム名',
        'title2':'Kaizen teian hituyou maisuu=改善提案必要枚数/月',
        'title3':'Nenkan mokuhyou kingaku=合理化目的金額/年',
        'title4':'Team member ninzuu=チーム人数',
        'id':num,
        'form':team_kaizen3_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/team_kaizen3_3edit.html',params)

@login_required
def team_kaizen4_4edit(request,num):
    obj=team_kaizen4.objects.get(id=num)
    if(request.method=='POST'):
        kaku=team_kaizen4_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/team_kaizen4_4')
    params={
        'title1':'Team name=チーム名',
        'title2':'Kaizen teian hituyou maisuu=改善提案必要枚数/月',
        'title3':'Nenkan mokuhyou kingaku=合理化目的金額/年',
        'title4':'Team member ninzuu=チーム人数',
        'id':num,
        'form':team_kaizen4_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/team_kaizen4_4edit.html',params)

@login_required
def team_kaizen5_5edit(request,num):
    obj=team_kaizen5.objects.get(id=num)
    if(request.method=='POST'):
        kaku=team_kaizen5_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/team_kaizen5_5')
    params={
        'title1':'Team name=チーム名',
        'title2':'Kaizen teian hituyou maisuu=改善提案必要枚数/月',
        'title3':'Nenkan mokuhyou kingaku=合理化目的金額/年',
        'title4':'Team member ninzuu=チーム人数',
        'id':num,
        'form':team_kaizen5_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/team_kaizen5_5edit.html',params)

@login_required
def team_kaizen6_6edit(request,num):
    obj=team_kaizen6.objects.get(id=num)
    if(request.method=='POST'):
        kaku=team_kaizen6_Form(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/kaizen/team_kaizen6_6')
    params={
        'title1':'Team name=チーム名',
        'title2':'Kaizen teian hituyou maisuu=改善提案必要枚数/月',
        'title3':'Nenkan mokuhyou kingaku=合理化目的金額/年',
        'title4':'Team member ninzuu=チーム人数',
        'id':num,
        'form':team_kaizen6_Form(instance=obj),
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,
    }
    return render(request,'kaizen/team_kaizen6_6edit.html',params)

def setplt_k1():

    team_kaizen1_kijun=team_kaizen1.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen1_kijun2=team_kaizen1_kijun[0]
    #チームネーム1    
    team_kaizen1_kijun_team_name=team_kaizen1_kijun2['team_name']
    #改善必要枚数
    team_kaizen1_kijun_kaizen_teian_hituyou_maisuu=team_kaizen1_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen1_kijun_nenkan_mokuhyou_kingaku=team_kaizen1_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen1_kijun_team_member_ninzuu=team_kaizen1_kijun2['team_member_ninzuu']

    #チーム１
    team_kaizen1_kiroku2=team_kaizen1_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team1_kiroku1=team_kaizen1_kiroku2[0]
    team1_kiroku2=team_kaizen1_kiroku2[1]
    team1_kiroku3=team_kaizen1_kiroku2[2]
    team1_kiroku4=team_kaizen1_kiroku2[3]
    team1_kiroku5=team_kaizen1_kiroku2[4]
    team1_kiroku6=team_kaizen1_kiroku2[5]
    team1_kiroku7=team_kaizen1_kiroku2[6]
    team1_kiroku8=team_kaizen1_kiroku2[7]
    team1_kiroku9=team_kaizen1_kiroku2[8]
    team1_kiroku10=team_kaizen1_kiroku2[9]
    team1_kiroku11=team_kaizen1_kiroku2[10]
    team1_kiroku12=team_kaizen1_kiroku2[11]

    team1_kiroku1_output_kaizenteian=team1_kiroku1['output_kaizenteian']
    team1_kiroku2_output_kaizenteian=team1_kiroku2['output_kaizenteian']
    team1_kiroku3_output_kaizenteian=team1_kiroku3['output_kaizenteian']
    team1_kiroku4_output_kaizenteian=team1_kiroku4['output_kaizenteian']
    team1_kiroku5_output_kaizenteian=team1_kiroku5['output_kaizenteian']
    team1_kiroku6_output_kaizenteian=team1_kiroku6['output_kaizenteian']
    team1_kiroku7_output_kaizenteian=team1_kiroku7['output_kaizenteian']
    team1_kiroku8_output_kaizenteian=team1_kiroku8['output_kaizenteian']
    team1_kiroku9_output_kaizenteian=team1_kiroku9['output_kaizenteian']
    team1_kiroku10_output_kaizenteian=team1_kiroku10['output_kaizenteian']
    team1_kiroku11_output_kaizenteian=team1_kiroku11['output_kaizenteian']
    team1_kiroku12_output_kaizenteian=team1_kiroku12['output_kaizenteian']

    team1_kiroku1_output_kingaku=team1_kiroku1['output_kingaku']
    team1_kiroku2_output_kingaku=team1_kiroku2['output_kingaku']
    team1_kiroku3_output_kingaku=team1_kiroku3['output_kingaku']
    team1_kiroku4_output_kingaku=team1_kiroku4['output_kingaku']
    team1_kiroku5_output_kingaku=team1_kiroku5['output_kingaku']
    team1_kiroku6_output_kingaku=team1_kiroku6['output_kingaku']
    team1_kiroku7_output_kingaku=team1_kiroku7['output_kingaku']
    team1_kiroku8_output_kingaku=team1_kiroku8['output_kingaku']
    team1_kiroku9_output_kingaku=team1_kiroku9['output_kingaku']
    team1_kiroku10_output_kingaku=team1_kiroku10['output_kingaku']
    team1_kiroku11_output_kingaku=team1_kiroku11['output_kingaku']
    team1_kiroku12_output_kingaku=team1_kiroku12['output_kingaku']

    a=team_kaizen1_kijun_nenkan_mokuhyou_kingaku/12



    
    a_a=f'年間目標金額{team_kaizen1_kijun_nenkan_mokuhyou_kingaku}円'
    b_b=f'チーム:{team_kaizen1_kijun_team_name}達成金額'

    aa=f'4月+{team1_kiroku1_output_kingaku}円'
    bb=f'5月+{team1_kiroku2_output_kingaku}円'
    cc=f'6月+{team1_kiroku3_output_kingaku}円'
    dd=f'7月+{team1_kiroku4_output_kingaku}円'
    ee=f'8月+{team1_kiroku5_output_kingaku}円'
    ff=f'9月+{team1_kiroku6_output_kingaku}円'
    gg=f'10月+{team1_kiroku7_output_kingaku}円'
    hh=f'11月+{team1_kiroku8_output_kingaku}円'
    ii=f'12月+{team1_kiroku9_output_kingaku}円'
    jj=f'1月+{team1_kiroku10_output_kingaku}円'
    kk=f'2月+{team1_kiroku11_output_kingaku}円'
    ll=f'3月+{team1_kiroku12_output_kingaku}円'

    columns=[a_a,b_b]
    index=index=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll]

    a1=a
    a2=team1_kiroku1_output_kingaku

    b1=a*2
    b2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku

    c1=a*3
    c2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku

    d1=a*4
    d2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku+team1_kiroku4_output_kingaku

    e1=a*5
    e2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku+team1_kiroku4_output_kingaku+team1_kiroku5_output_kingaku

    f1=a*6
    f2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku+team1_kiroku4_output_kingaku+team1_kiroku5_output_kingaku+team1_kiroku6_output_kingaku

    g1=a*7
    g2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku+team1_kiroku4_output_kingaku+team1_kiroku5_output_kingaku+team1_kiroku6_output_kingaku+team1_kiroku7_output_kingaku

    h1=a*8
    h2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku+team1_kiroku4_output_kingaku+team1_kiroku5_output_kingaku+team1_kiroku6_output_kingaku+team1_kiroku7_output_kingaku+team1_kiroku8_output_kingaku

    i1=a*9
    i2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku+team1_kiroku4_output_kingaku+team1_kiroku5_output_kingaku+team1_kiroku6_output_kingaku+team1_kiroku7_output_kingaku+team1_kiroku8_output_kingaku+team1_kiroku9_output_kingaku

    j1=a*10
    j2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku+team1_kiroku4_output_kingaku+team1_kiroku5_output_kingaku+team1_kiroku6_output_kingaku+team1_kiroku7_output_kingaku+team1_kiroku8_output_kingaku+team1_kiroku9_output_kingaku+team1_kiroku10_output_kingaku
    
    k1=a*11
    k2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku+team1_kiroku4_output_kingaku+team1_kiroku5_output_kingaku+team1_kiroku6_output_kingaku+team1_kiroku7_output_kingaku+team1_kiroku8_output_kingaku+team1_kiroku9_output_kingaku+team1_kiroku10_output_kingaku+team1_kiroku11_output_kingaku
    
    l1=a*12
    l2=team1_kiroku1_output_kingaku+team1_kiroku2_output_kingaku+team1_kiroku3_output_kingaku+team1_kiroku4_output_kingaku+team1_kiroku5_output_kingaku+team1_kiroku6_output_kingaku+team1_kiroku7_output_kingaku+team1_kiroku8_output_kingaku+team1_kiroku9_output_kingaku+team1_kiroku10_output_kingaku+team1_kiroku11_output_kingaku+team1_kiroku12_output_kingaku
    

    df_a=pd.DataFrame([[a1,a2],[b1,b2],[c1,c2],[d1,d2],[e1,e2],[f1,f2],[g1,g2],[h1,h2],[i1,i2],[j1,j2],[k1,k2],[l1,l2]],index=index,columns=columns)
    figure(num=None, figsize=(18.5, 9))
    plt.title(f'合理化達成金額[チーム:{team_kaizen1_kijun_team_name}]',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=20)
    plt.ylabel('金額単位【100万円】',fontsize=20)
    plt.plot(list(df_a.index),df_a[a_a],marker='s',label=a_a)
    plt.plot(list(df_a.index),df_a[b_b],marker='o',label=b_b)
    plt.legend()


def plt2svg_k1():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k1(request):
    setplt_k1()
    svg=plt2svg_k1()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response

def setplt_k2():

    team_kaizen2_kijun=team_kaizen2.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen2_kijun2=team_kaizen2_kijun[0]
    #チームネーム2    
    team_kaizen2_kijun_team_name=team_kaizen2_kijun2['team_name']
    #改善必要枚数
    team_kaizen2_kijun_kaizen_teian_hituyou_maisuu=team_kaizen2_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen2_kijun_nenkan_mokuhyou_kingaku=team_kaizen2_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen2_kijun_team_member_ninzuu=team_kaizen2_kijun2['team_member_ninzuu']

    #チーム2
    team_kaizen2_kiroku2=team_kaizen2_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team2_kiroku1=team_kaizen2_kiroku2[0]
    team2_kiroku2=team_kaizen2_kiroku2[1]
    team2_kiroku3=team_kaizen2_kiroku2[2]
    team2_kiroku4=team_kaizen2_kiroku2[3]
    team2_kiroku5=team_kaizen2_kiroku2[4]
    team2_kiroku6=team_kaizen2_kiroku2[5]
    team2_kiroku7=team_kaizen2_kiroku2[6]
    team2_kiroku8=team_kaizen2_kiroku2[7]
    team2_kiroku9=team_kaizen2_kiroku2[8]
    team2_kiroku10=team_kaizen2_kiroku2[9]
    team2_kiroku11=team_kaizen2_kiroku2[10]
    team2_kiroku12=team_kaizen2_kiroku2[11]

    team2_kiroku1_output_kaizenteian=team2_kiroku1['output_kaizenteian']
    team2_kiroku2_output_kaizenteian=team2_kiroku2['output_kaizenteian']
    team2_kiroku3_output_kaizenteian=team2_kiroku3['output_kaizenteian']
    team2_kiroku4_output_kaizenteian=team2_kiroku4['output_kaizenteian']
    team2_kiroku5_output_kaizenteian=team2_kiroku5['output_kaizenteian']
    team2_kiroku6_output_kaizenteian=team2_kiroku6['output_kaizenteian']
    team2_kiroku7_output_kaizenteian=team2_kiroku7['output_kaizenteian']
    team2_kiroku8_output_kaizenteian=team2_kiroku8['output_kaizenteian']
    team2_kiroku9_output_kaizenteian=team2_kiroku9['output_kaizenteian']
    team2_kiroku10_output_kaizenteian=team2_kiroku10['output_kaizenteian']
    team2_kiroku11_output_kaizenteian=team2_kiroku11['output_kaizenteian']
    team2_kiroku12_output_kaizenteian=team2_kiroku12['output_kaizenteian']

    team2_kiroku1_output_kingaku=team2_kiroku1['output_kingaku']
    team2_kiroku2_output_kingaku=team2_kiroku2['output_kingaku']
    team2_kiroku3_output_kingaku=team2_kiroku3['output_kingaku']
    team2_kiroku4_output_kingaku=team2_kiroku4['output_kingaku']
    team2_kiroku5_output_kingaku=team2_kiroku5['output_kingaku']
    team2_kiroku6_output_kingaku=team2_kiroku6['output_kingaku']
    team2_kiroku7_output_kingaku=team2_kiroku7['output_kingaku']
    team2_kiroku8_output_kingaku=team2_kiroku8['output_kingaku']
    team2_kiroku9_output_kingaku=team2_kiroku9['output_kingaku']
    team2_kiroku10_output_kingaku=team2_kiroku10['output_kingaku']
    team2_kiroku11_output_kingaku=team2_kiroku11['output_kingaku']
    team2_kiroku12_output_kingaku=team2_kiroku12['output_kingaku']



    a=team_kaizen2_kijun_nenkan_mokuhyou_kingaku/12



    
    a_a=f'年間目標金額{team_kaizen2_kijun_nenkan_mokuhyou_kingaku}円'
    b_b=f'チーム:{team_kaizen2_kijun_team_name}達成金額'

    aa=f'4月+{team2_kiroku1_output_kingaku}円'
    bb=f'5月+{team2_kiroku2_output_kingaku}円'
    cc=f'6月+{team2_kiroku3_output_kingaku}円'
    dd=f'7月+{team2_kiroku4_output_kingaku}円'
    ee=f'8月+{team2_kiroku5_output_kingaku}円'
    ff=f'9月+{team2_kiroku6_output_kingaku}円'
    gg=f'10月+{team2_kiroku7_output_kingaku}円'
    hh=f'11月+{team2_kiroku8_output_kingaku}円'
    ii=f'12月+{team2_kiroku9_output_kingaku}円'
    jj=f'1月+{team2_kiroku10_output_kingaku}円'
    kk=f'2月+{team2_kiroku11_output_kingaku}円'
    ll=f'3月+{team2_kiroku12_output_kingaku}円'

    columns=[a_a,b_b]
    index=index=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll]

    a1=a
    a2=team2_kiroku1_output_kingaku

    b1=a*2
    b2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku

    c1=a*3
    c2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku

    d1=a*4
    d2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku+team2_kiroku4_output_kingaku

    e1=a*5
    e2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku+team2_kiroku4_output_kingaku+team2_kiroku5_output_kingaku

    f1=a*6
    f2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku+team2_kiroku4_output_kingaku+team2_kiroku5_output_kingaku+team2_kiroku6_output_kingaku

    g1=a*7
    g2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku+team2_kiroku4_output_kingaku+team2_kiroku5_output_kingaku+team2_kiroku6_output_kingaku+team2_kiroku7_output_kingaku

    h1=a*8
    h2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku+team2_kiroku4_output_kingaku+team2_kiroku5_output_kingaku+team2_kiroku6_output_kingaku+team2_kiroku7_output_kingaku+team2_kiroku8_output_kingaku

    i1=a*9
    i2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku+team2_kiroku4_output_kingaku+team2_kiroku5_output_kingaku+team2_kiroku6_output_kingaku+team2_kiroku7_output_kingaku+team2_kiroku8_output_kingaku+team2_kiroku9_output_kingaku

    j1=a*10
    j2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku+team2_kiroku4_output_kingaku+team2_kiroku5_output_kingaku+team2_kiroku6_output_kingaku+team2_kiroku7_output_kingaku+team2_kiroku8_output_kingaku+team2_kiroku9_output_kingaku+team2_kiroku10_output_kingaku
    
    k1=a*11
    k2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku+team2_kiroku4_output_kingaku+team2_kiroku5_output_kingaku+team2_kiroku6_output_kingaku+team2_kiroku7_output_kingaku+team2_kiroku8_output_kingaku+team2_kiroku9_output_kingaku+team2_kiroku10_output_kingaku+team2_kiroku11_output_kingaku
    
    l1=a*12
    l2=team2_kiroku1_output_kingaku+team2_kiroku2_output_kingaku+team2_kiroku3_output_kingaku+team2_kiroku4_output_kingaku+team2_kiroku5_output_kingaku+team2_kiroku6_output_kingaku+team2_kiroku7_output_kingaku+team2_kiroku8_output_kingaku+team2_kiroku9_output_kingaku+team2_kiroku10_output_kingaku+team2_kiroku11_output_kingaku+team2_kiroku12_output_kingaku
    

    df_a=pd.DataFrame([[a1,a2],[b1,b2],[c1,c2],[d1,d2],[e1,e2],[f1,f2],[g1,g2],[h1,h2],[i1,i2],[j1,j2],[k1,k2],[l1,l2]],index=index,columns=columns)
    figure(num=None, figsize=(18.5, 9))
    plt.title(f'合理化達成金額[チーム:{team_kaizen2_kijun_team_name}]',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=20)
    plt.ylabel('金額単位【100万円】',fontsize=20)
    plt.plot(list(df_a.index),df_a[a_a],marker='s',label=a_a)
    plt.plot(list(df_a.index),df_a[b_b],marker='o',label=b_b)
    plt.legend()


def plt2svg_k2():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k2(request):
    setplt_k2()
    svg=plt2svg_k2()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response

def setplt_k3():

    team_kaizen3_kijun=team_kaizen3.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen3_kijun2=team_kaizen3_kijun[0]
    #チームネーム3    
    team_kaizen3_kijun_team_name=team_kaizen3_kijun2['team_name']
    #改善必要枚数
    team_kaizen3_kijun_kaizen_teian_hituyou_maisuu=team_kaizen3_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen3_kijun_nenkan_mokuhyou_kingaku=team_kaizen3_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen3_kijun_team_member_ninzuu=team_kaizen3_kijun2['team_member_ninzuu']

    #チーム3
    team_kaizen3_kiroku2=team_kaizen3_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team3_kiroku1=team_kaizen3_kiroku2[0]
    team3_kiroku2=team_kaizen3_kiroku2[1]
    team3_kiroku3=team_kaizen3_kiroku2[2]
    team3_kiroku4=team_kaizen3_kiroku2[3]
    team3_kiroku5=team_kaizen3_kiroku2[4]
    team3_kiroku6=team_kaizen3_kiroku2[5]
    team3_kiroku7=team_kaizen3_kiroku2[6]
    team3_kiroku8=team_kaizen3_kiroku2[7]
    team3_kiroku9=team_kaizen3_kiroku2[8]
    team3_kiroku10=team_kaizen3_kiroku2[9]
    team3_kiroku11=team_kaizen3_kiroku2[10]
    team3_kiroku12=team_kaizen3_kiroku2[11]

    team3_kiroku1_output_kaizenteian=team3_kiroku1['output_kaizenteian']
    team3_kiroku2_output_kaizenteian=team3_kiroku2['output_kaizenteian']
    team3_kiroku3_output_kaizenteian=team3_kiroku3['output_kaizenteian']
    team3_kiroku4_output_kaizenteian=team3_kiroku4['output_kaizenteian']
    team3_kiroku5_output_kaizenteian=team3_kiroku5['output_kaizenteian']
    team3_kiroku6_output_kaizenteian=team3_kiroku6['output_kaizenteian']
    team3_kiroku7_output_kaizenteian=team3_kiroku7['output_kaizenteian']
    team3_kiroku8_output_kaizenteian=team3_kiroku8['output_kaizenteian']
    team3_kiroku9_output_kaizenteian=team3_kiroku9['output_kaizenteian']
    team3_kiroku10_output_kaizenteian=team3_kiroku10['output_kaizenteian']
    team3_kiroku11_output_kaizenteian=team3_kiroku11['output_kaizenteian']
    team3_kiroku12_output_kaizenteian=team3_kiroku12['output_kaizenteian']

    team3_kiroku1_output_kingaku=team3_kiroku1['output_kingaku']
    team3_kiroku2_output_kingaku=team3_kiroku2['output_kingaku']
    team3_kiroku3_output_kingaku=team3_kiroku3['output_kingaku']
    team3_kiroku4_output_kingaku=team3_kiroku4['output_kingaku']
    team3_kiroku5_output_kingaku=team3_kiroku5['output_kingaku']
    team3_kiroku6_output_kingaku=team3_kiroku6['output_kingaku']
    team3_kiroku7_output_kingaku=team3_kiroku7['output_kingaku']
    team3_kiroku8_output_kingaku=team3_kiroku8['output_kingaku']
    team3_kiroku9_output_kingaku=team3_kiroku9['output_kingaku']
    team3_kiroku10_output_kingaku=team3_kiroku10['output_kingaku']
    team3_kiroku11_output_kingaku=team3_kiroku11['output_kingaku']
    team3_kiroku12_output_kingaku=team3_kiroku12['output_kingaku']



    a=team_kaizen3_kijun_nenkan_mokuhyou_kingaku/12



    
    a_a=f'年間目標金額{team_kaizen3_kijun_nenkan_mokuhyou_kingaku}円'
    b_b=f'チーム:{team_kaizen3_kijun_team_name}達成金額'

    aa=f'4月+{team3_kiroku1_output_kingaku}円'
    bb=f'5月+{team3_kiroku2_output_kingaku}円'
    cc=f'6月+{team3_kiroku3_output_kingaku}円'
    dd=f'7月+{team3_kiroku4_output_kingaku}円'
    ee=f'8月+{team3_kiroku5_output_kingaku}円'
    ff=f'9月+{team3_kiroku6_output_kingaku}円'
    gg=f'10月+{team3_kiroku7_output_kingaku}円'
    hh=f'11月+{team3_kiroku8_output_kingaku}円'
    ii=f'12月+{team3_kiroku9_output_kingaku}円'
    jj=f'1月+{team3_kiroku10_output_kingaku}円'
    kk=f'2月+{team3_kiroku11_output_kingaku}円'
    ll=f'3月+{team3_kiroku12_output_kingaku}円'

    columns=[a_a,b_b]
    index=index=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll]

    a1=a
    a2=team3_kiroku1_output_kingaku

    b1=a*2
    b2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku

    c1=a*3
    c2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku

    d1=a*4
    d2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku+team3_kiroku4_output_kingaku

    e1=a*5
    e2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku+team3_kiroku4_output_kingaku+team3_kiroku5_output_kingaku

    f1=a*6
    f2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku+team3_kiroku4_output_kingaku+team3_kiroku5_output_kingaku+team3_kiroku6_output_kingaku

    g1=a*7
    g2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku+team3_kiroku4_output_kingaku+team3_kiroku5_output_kingaku+team3_kiroku6_output_kingaku+team3_kiroku7_output_kingaku

    h1=a*8
    h2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku+team3_kiroku4_output_kingaku+team3_kiroku5_output_kingaku+team3_kiroku6_output_kingaku+team3_kiroku7_output_kingaku+team3_kiroku8_output_kingaku

    i1=a*9
    i2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku+team3_kiroku4_output_kingaku+team3_kiroku5_output_kingaku+team3_kiroku6_output_kingaku+team3_kiroku7_output_kingaku+team3_kiroku8_output_kingaku+team3_kiroku9_output_kingaku

    j1=a*10
    j2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku+team3_kiroku4_output_kingaku+team3_kiroku5_output_kingaku+team3_kiroku6_output_kingaku+team3_kiroku7_output_kingaku+team3_kiroku8_output_kingaku+team3_kiroku9_output_kingaku+team3_kiroku10_output_kingaku
    
    k1=a*11
    k2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku+team3_kiroku4_output_kingaku+team3_kiroku5_output_kingaku+team3_kiroku6_output_kingaku+team3_kiroku7_output_kingaku+team3_kiroku8_output_kingaku+team3_kiroku9_output_kingaku+team3_kiroku10_output_kingaku+team3_kiroku11_output_kingaku
    
    l1=a*12
    l2=team3_kiroku1_output_kingaku+team3_kiroku2_output_kingaku+team3_kiroku3_output_kingaku+team3_kiroku4_output_kingaku+team3_kiroku5_output_kingaku+team3_kiroku6_output_kingaku+team3_kiroku7_output_kingaku+team3_kiroku8_output_kingaku+team3_kiroku9_output_kingaku+team3_kiroku10_output_kingaku+team3_kiroku11_output_kingaku+team3_kiroku12_output_kingaku
    

    df_a=pd.DataFrame([[a1,a2],[b1,b2],[c1,c2],[d1,d2],[e1,e2],[f1,f2],[g1,g2],[h1,h2],[i1,i2],[j1,j2],[k1,k2],[l1,l2]],index=index,columns=columns)
    figure(num=None, figsize=(18.5, 9))
    plt.title(f'合理化達成金額[チーム:{team_kaizen3_kijun_team_name}]',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=20)
    plt.ylabel('金額単位【100万円】',fontsize=20)
    plt.plot(list(df_a.index),df_a[a_a],marker='s',label=a_a)
    plt.plot(list(df_a.index),df_a[b_b],marker='o',label=b_b)
    plt.legend()


def plt2svg_k3():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k3(request):
    setplt_k3()
    svg=plt2svg_k3()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response

def setplt_k4():

    team_kaizen4_kijun=team_kaizen4.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen4_kijun2=team_kaizen4_kijun[0]
    #チームネーム4    
    team_kaizen4_kijun_team_name=team_kaizen4_kijun2['team_name']
    #改善必要枚数
    team_kaizen4_kijun_kaizen_teian_hituyou_maisuu=team_kaizen4_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen4_kijun_nenkan_mokuhyou_kingaku=team_kaizen4_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen4_kijun_team_member_ninzuu=team_kaizen4_kijun2['team_member_ninzuu']

    #チーム4
    team_kaizen4_kiroku2=team_kaizen4_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team4_kiroku1=team_kaizen4_kiroku2[0]
    team4_kiroku2=team_kaizen4_kiroku2[1]
    team4_kiroku3=team_kaizen4_kiroku2[2]
    team4_kiroku4=team_kaizen4_kiroku2[3]
    team4_kiroku5=team_kaizen4_kiroku2[4]
    team4_kiroku6=team_kaizen4_kiroku2[5]
    team4_kiroku7=team_kaizen4_kiroku2[6]
    team4_kiroku8=team_kaizen4_kiroku2[7]
    team4_kiroku9=team_kaizen4_kiroku2[8]
    team4_kiroku10=team_kaizen4_kiroku2[9]
    team4_kiroku11=team_kaizen4_kiroku2[10]
    team4_kiroku12=team_kaizen4_kiroku2[11]

    team4_kiroku1_output_kaizenteian=team4_kiroku1['output_kaizenteian']
    team4_kiroku2_output_kaizenteian=team4_kiroku2['output_kaizenteian']
    team4_kiroku3_output_kaizenteian=team4_kiroku3['output_kaizenteian']
    team4_kiroku4_output_kaizenteian=team4_kiroku4['output_kaizenteian']
    team4_kiroku5_output_kaizenteian=team4_kiroku5['output_kaizenteian']
    team4_kiroku6_output_kaizenteian=team4_kiroku6['output_kaizenteian']
    team4_kiroku7_output_kaizenteian=team4_kiroku7['output_kaizenteian']
    team4_kiroku8_output_kaizenteian=team4_kiroku8['output_kaizenteian']
    team4_kiroku9_output_kaizenteian=team4_kiroku9['output_kaizenteian']
    team4_kiroku10_output_kaizenteian=team4_kiroku10['output_kaizenteian']
    team4_kiroku11_output_kaizenteian=team4_kiroku11['output_kaizenteian']
    team4_kiroku12_output_kaizenteian=team4_kiroku12['output_kaizenteian']

    team4_kiroku1_output_kingaku=team4_kiroku1['output_kingaku']
    team4_kiroku2_output_kingaku=team4_kiroku2['output_kingaku']
    team4_kiroku3_output_kingaku=team4_kiroku3['output_kingaku']
    team4_kiroku4_output_kingaku=team4_kiroku4['output_kingaku']
    team4_kiroku5_output_kingaku=team4_kiroku5['output_kingaku']
    team4_kiroku6_output_kingaku=team4_kiroku6['output_kingaku']
    team4_kiroku7_output_kingaku=team4_kiroku7['output_kingaku']
    team4_kiroku8_output_kingaku=team4_kiroku8['output_kingaku']
    team4_kiroku9_output_kingaku=team4_kiroku9['output_kingaku']
    team4_kiroku10_output_kingaku=team4_kiroku10['output_kingaku']
    team4_kiroku11_output_kingaku=team4_kiroku11['output_kingaku']
    team4_kiroku12_output_kingaku=team4_kiroku12['output_kingaku']


    a=team_kaizen4_kijun_nenkan_mokuhyou_kingaku/12



    
    a_a=f'年間目標金額{team_kaizen4_kijun_nenkan_mokuhyou_kingaku}円'
    b_b=f'チーム:{team_kaizen4_kijun_team_name}達成金額'

    aa=f'4月+{team4_kiroku1_output_kingaku}円'
    bb=f'5月+{team4_kiroku2_output_kingaku}円'
    cc=f'6月+{team4_kiroku3_output_kingaku}円'
    dd=f'7月+{team4_kiroku4_output_kingaku}円'
    ee=f'8月+{team4_kiroku5_output_kingaku}円'
    ff=f'9月+{team4_kiroku6_output_kingaku}円'
    gg=f'10月+{team4_kiroku7_output_kingaku}円'
    hh=f'11月+{team4_kiroku8_output_kingaku}円'
    ii=f'12月+{team4_kiroku9_output_kingaku}円'
    jj=f'1月+{team4_kiroku10_output_kingaku}円'
    kk=f'2月+{team4_kiroku11_output_kingaku}円'
    ll=f'3月+{team4_kiroku12_output_kingaku}円'

    columns=[a_a,b_b]
    index=index=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll]

    a1=a
    a2=team4_kiroku1_output_kingaku

    b1=a*2
    b2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku

    c1=a*3
    c2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku

    d1=a*4
    d2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku+team4_kiroku4_output_kingaku

    e1=a*5
    e2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku+team4_kiroku4_output_kingaku+team4_kiroku5_output_kingaku

    f1=a*6
    f2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku+team4_kiroku4_output_kingaku+team4_kiroku5_output_kingaku+team4_kiroku6_output_kingaku

    g1=a*7
    g2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku+team4_kiroku4_output_kingaku+team4_kiroku5_output_kingaku+team4_kiroku6_output_kingaku+team4_kiroku7_output_kingaku

    h1=a*8
    h2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku+team4_kiroku4_output_kingaku+team4_kiroku5_output_kingaku+team4_kiroku6_output_kingaku+team4_kiroku7_output_kingaku+team4_kiroku8_output_kingaku

    i1=a*9
    i2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku+team4_kiroku4_output_kingaku+team4_kiroku5_output_kingaku+team4_kiroku6_output_kingaku+team4_kiroku7_output_kingaku+team4_kiroku8_output_kingaku+team4_kiroku9_output_kingaku

    j1=a*10
    j2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku+team4_kiroku4_output_kingaku+team4_kiroku5_output_kingaku+team4_kiroku6_output_kingaku+team4_kiroku7_output_kingaku+team4_kiroku8_output_kingaku+team4_kiroku9_output_kingaku+team4_kiroku10_output_kingaku
    
    k1=a*11
    k2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku+team4_kiroku4_output_kingaku+team4_kiroku5_output_kingaku+team4_kiroku6_output_kingaku+team4_kiroku7_output_kingaku+team4_kiroku8_output_kingaku+team4_kiroku9_output_kingaku+team4_kiroku10_output_kingaku+team4_kiroku11_output_kingaku
    
    l1=a*12
    l2=team4_kiroku1_output_kingaku+team4_kiroku2_output_kingaku+team4_kiroku3_output_kingaku+team4_kiroku4_output_kingaku+team4_kiroku5_output_kingaku+team4_kiroku6_output_kingaku+team4_kiroku7_output_kingaku+team4_kiroku8_output_kingaku+team4_kiroku9_output_kingaku+team4_kiroku10_output_kingaku+team4_kiroku11_output_kingaku+team4_kiroku12_output_kingaku
    

    df_a=pd.DataFrame([[a1,a2],[b1,b2],[c1,c2],[d1,d2],[e1,e2],[f1,f2],[g1,g2],[h1,h2],[i1,i2],[j1,j2],[k1,k2],[l1,l2]],index=index,columns=columns)
    figure(num=None, figsize=(18.5, 9))
    plt.title(f'合理化達成金額[チーム:{team_kaizen4_kijun_team_name}]',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=20)
    plt.ylabel('金額単位【100万円】',fontsize=20)
    plt.plot(list(df_a.index),df_a[a_a],marker='s',label=a_a)
    plt.plot(list(df_a.index),df_a[b_b],marker='o',label=b_b)
    plt.legend()


def plt2svg_k4():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k4(request):
    setplt_k4()
    svg=plt2svg_k4()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response

def setplt_k5():

    team_kaizen5_kijun=team_kaizen5.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen5_kijun2=team_kaizen5_kijun[0]
    #チームネーム5    
    team_kaizen5_kijun_team_name=team_kaizen5_kijun2['team_name']
    #改善必要枚数
    team_kaizen5_kijun_kaizen_teian_hituyou_maisuu=team_kaizen5_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen5_kijun_nenkan_mokuhyou_kingaku=team_kaizen5_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen5_kijun_team_member_ninzuu=team_kaizen5_kijun2['team_member_ninzuu']


    #チーム5
    team_kaizen5_kiroku2=team_kaizen5_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team5_kiroku1=team_kaizen5_kiroku2[0]
    team5_kiroku2=team_kaizen5_kiroku2[1]
    team5_kiroku3=team_kaizen5_kiroku2[2]
    team5_kiroku4=team_kaizen5_kiroku2[3]
    team5_kiroku5=team_kaizen5_kiroku2[4]
    team5_kiroku6=team_kaizen5_kiroku2[5]
    team5_kiroku7=team_kaizen5_kiroku2[6]
    team5_kiroku8=team_kaizen5_kiroku2[7]
    team5_kiroku9=team_kaizen5_kiroku2[8]
    team5_kiroku10=team_kaizen5_kiroku2[9]
    team5_kiroku11=team_kaizen5_kiroku2[10]
    team5_kiroku12=team_kaizen5_kiroku2[11]

    team5_kiroku1_output_kaizenteian=team5_kiroku1['output_kaizenteian']
    team5_kiroku2_output_kaizenteian=team5_kiroku2['output_kaizenteian']
    team5_kiroku3_output_kaizenteian=team5_kiroku3['output_kaizenteian']
    team5_kiroku4_output_kaizenteian=team5_kiroku4['output_kaizenteian']
    team5_kiroku5_output_kaizenteian=team5_kiroku5['output_kaizenteian']
    team5_kiroku6_output_kaizenteian=team5_kiroku6['output_kaizenteian']
    team5_kiroku7_output_kaizenteian=team5_kiroku7['output_kaizenteian']
    team5_kiroku8_output_kaizenteian=team5_kiroku8['output_kaizenteian']
    team5_kiroku9_output_kaizenteian=team5_kiroku9['output_kaizenteian']
    team5_kiroku10_output_kaizenteian=team5_kiroku10['output_kaizenteian']
    team5_kiroku11_output_kaizenteian=team5_kiroku11['output_kaizenteian']
    team5_kiroku12_output_kaizenteian=team5_kiroku12['output_kaizenteian']

    team5_kiroku1_output_kingaku=team5_kiroku1['output_kingaku']
    team5_kiroku2_output_kingaku=team5_kiroku2['output_kingaku']
    team5_kiroku3_output_kingaku=team5_kiroku3['output_kingaku']
    team5_kiroku4_output_kingaku=team5_kiroku4['output_kingaku']
    team5_kiroku5_output_kingaku=team5_kiroku5['output_kingaku']
    team5_kiroku6_output_kingaku=team5_kiroku6['output_kingaku']
    team5_kiroku7_output_kingaku=team5_kiroku7['output_kingaku']
    team5_kiroku8_output_kingaku=team5_kiroku8['output_kingaku']
    team5_kiroku9_output_kingaku=team5_kiroku9['output_kingaku']
    team5_kiroku10_output_kingaku=team5_kiroku10['output_kingaku']
    team5_kiroku11_output_kingaku=team5_kiroku11['output_kingaku']
    team5_kiroku12_output_kingaku=team5_kiroku12['output_kingaku']


    a=team_kaizen5_kijun_nenkan_mokuhyou_kingaku/12



    
    a_a=f'年間目標金額{team_kaizen5_kijun_nenkan_mokuhyou_kingaku}円'
    b_b=f'チーム:{team_kaizen5_kijun_team_name}達成金額'

    aa=f'4月+{team5_kiroku1_output_kingaku}円'
    bb=f'5月+{team5_kiroku2_output_kingaku}円'
    cc=f'6月+{team5_kiroku3_output_kingaku}円'
    dd=f'7月+{team5_kiroku4_output_kingaku}円'
    ee=f'8月+{team5_kiroku5_output_kingaku}円'
    ff=f'9月+{team5_kiroku6_output_kingaku}円'
    gg=f'10月+{team5_kiroku7_output_kingaku}円'
    hh=f'11月+{team5_kiroku8_output_kingaku}円'
    ii=f'12月+{team5_kiroku9_output_kingaku}円'
    jj=f'1月+{team5_kiroku10_output_kingaku}円'
    kk=f'2月+{team5_kiroku11_output_kingaku}円'
    ll=f'3月+{team5_kiroku12_output_kingaku}円'

    columns=[a_a,b_b]
    index=index=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll]

    a1=a
    a2=team5_kiroku1_output_kingaku

    b1=a*2
    b2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku

    c1=a*3
    c2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku

    d1=a*4
    d2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku+team5_kiroku4_output_kingaku

    e1=a*5
    e2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku+team5_kiroku4_output_kingaku+team5_kiroku5_output_kingaku

    f1=a*6
    f2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku+team5_kiroku4_output_kingaku+team5_kiroku5_output_kingaku+team5_kiroku6_output_kingaku

    g1=a*7
    g2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku+team5_kiroku4_output_kingaku+team5_kiroku5_output_kingaku+team5_kiroku6_output_kingaku+team5_kiroku7_output_kingaku

    h1=a*8
    h2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku+team5_kiroku4_output_kingaku+team5_kiroku5_output_kingaku+team5_kiroku6_output_kingaku+team5_kiroku7_output_kingaku+team5_kiroku8_output_kingaku

    i1=a*9
    i2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku+team5_kiroku4_output_kingaku+team5_kiroku5_output_kingaku+team5_kiroku6_output_kingaku+team5_kiroku7_output_kingaku+team5_kiroku8_output_kingaku+team5_kiroku9_output_kingaku

    j1=a*10
    j2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku+team5_kiroku4_output_kingaku+team5_kiroku5_output_kingaku+team5_kiroku6_output_kingaku+team5_kiroku7_output_kingaku+team5_kiroku8_output_kingaku+team5_kiroku9_output_kingaku+team5_kiroku10_output_kingaku
    
    k1=a*11
    k2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku+team5_kiroku4_output_kingaku+team5_kiroku5_output_kingaku+team5_kiroku6_output_kingaku+team5_kiroku7_output_kingaku+team5_kiroku8_output_kingaku+team5_kiroku9_output_kingaku+team5_kiroku10_output_kingaku+team5_kiroku11_output_kingaku
    
    l1=a*12
    l2=team5_kiroku1_output_kingaku+team5_kiroku2_output_kingaku+team5_kiroku3_output_kingaku+team5_kiroku4_output_kingaku+team5_kiroku5_output_kingaku+team5_kiroku6_output_kingaku+team5_kiroku7_output_kingaku+team5_kiroku8_output_kingaku+team5_kiroku9_output_kingaku+team5_kiroku10_output_kingaku+team5_kiroku11_output_kingaku+team5_kiroku12_output_kingaku
    

    df_a=pd.DataFrame([[a1,a2],[b1,b2],[c1,c2],[d1,d2],[e1,e2],[f1,f2],[g1,g2],[h1,h2],[i1,i2],[j1,j2],[k1,k2],[l1,l2]],index=index,columns=columns)
    figure(num=None, figsize=(18.5, 9))
    plt.title(f'合理化達成金額[チーム:{team_kaizen5_kijun_team_name}]',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=20)
    plt.ylabel('金額単位【100万円】',fontsize=20)
    plt.plot(list(df_a.index),df_a[a_a],marker='s',label=a_a)
    plt.plot(list(df_a.index),df_a[b_b],marker='o',label=b_b)
    plt.legend()


def plt2svg_k5():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k5(request):
    setplt_k5()
    svg=plt2svg_k5()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_k6():

    team_kaizen6_kijun=team_kaizen6.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen6_kijun2=team_kaizen6_kijun[0]
    #チームネーム6    
    team_kaizen6_kijun_team_name=team_kaizen6_kijun2['team_name']
    #改善必要枚数
    team_kaizen6_kijun_kaizen_teian_hituyou_maisuu=team_kaizen6_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen6_kijun_nenkan_mokuhyou_kingaku=team_kaizen6_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen6_kijun_team_member_ninzuu=team_kaizen6_kijun2['team_member_ninzuu']
    

    #チーム6
    team_kaizen6_kiroku2=team_kaizen6_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team6_kiroku1=team_kaizen6_kiroku2[0]
    team6_kiroku2=team_kaizen6_kiroku2[1]
    team6_kiroku3=team_kaizen6_kiroku2[2]
    team6_kiroku4=team_kaizen6_kiroku2[3]
    team6_kiroku5=team_kaizen6_kiroku2[4]
    team6_kiroku6=team_kaizen6_kiroku2[5]
    team6_kiroku7=team_kaizen6_kiroku2[6]
    team6_kiroku8=team_kaizen6_kiroku2[7]
    team6_kiroku9=team_kaizen6_kiroku2[8]
    team6_kiroku10=team_kaizen6_kiroku2[9]
    team6_kiroku11=team_kaizen6_kiroku2[10]
    team6_kiroku12=team_kaizen6_kiroku2[11]

    team6_kiroku1_output_kaizenteian=team6_kiroku1['output_kaizenteian']
    team6_kiroku2_output_kaizenteian=team6_kiroku2['output_kaizenteian']
    team6_kiroku3_output_kaizenteian=team6_kiroku3['output_kaizenteian']
    team6_kiroku4_output_kaizenteian=team6_kiroku4['output_kaizenteian']
    team6_kiroku5_output_kaizenteian=team6_kiroku5['output_kaizenteian']
    team6_kiroku6_output_kaizenteian=team6_kiroku6['output_kaizenteian']
    team6_kiroku7_output_kaizenteian=team6_kiroku7['output_kaizenteian']
    team6_kiroku8_output_kaizenteian=team6_kiroku8['output_kaizenteian']
    team6_kiroku9_output_kaizenteian=team6_kiroku9['output_kaizenteian']
    team6_kiroku10_output_kaizenteian=team6_kiroku10['output_kaizenteian']
    team6_kiroku11_output_kaizenteian=team6_kiroku11['output_kaizenteian']
    team6_kiroku12_output_kaizenteian=team6_kiroku12['output_kaizenteian']

    team6_kiroku1_output_kingaku=team6_kiroku1['output_kingaku']
    team6_kiroku2_output_kingaku=team6_kiroku2['output_kingaku']
    team6_kiroku3_output_kingaku=team6_kiroku3['output_kingaku']
    team6_kiroku4_output_kingaku=team6_kiroku4['output_kingaku']
    team6_kiroku5_output_kingaku=team6_kiroku5['output_kingaku']
    team6_kiroku6_output_kingaku=team6_kiroku6['output_kingaku']
    team6_kiroku7_output_kingaku=team6_kiroku7['output_kingaku']
    team6_kiroku8_output_kingaku=team6_kiroku8['output_kingaku']
    team6_kiroku9_output_kingaku=team6_kiroku9['output_kingaku']
    team6_kiroku10_output_kingaku=team6_kiroku10['output_kingaku']
    team6_kiroku11_output_kingaku=team6_kiroku11['output_kingaku']
    team6_kiroku12_output_kingaku=team6_kiroku12['output_kingaku']





    a=team_kaizen6_kijun_nenkan_mokuhyou_kingaku/12

    a_a=f'年間目標金額{team_kaizen6_kijun_nenkan_mokuhyou_kingaku}円'
    b_b=f'チーム:{team_kaizen6_kijun_team_name}達成金額'

    aa=f'4月+{team6_kiroku1_output_kingaku}円'
    bb=f'5月+{team6_kiroku2_output_kingaku}円'
    cc=f'6月+{team6_kiroku3_output_kingaku}円'
    dd=f'7月+{team6_kiroku4_output_kingaku}円'
    ee=f'8月+{team6_kiroku5_output_kingaku}円'
    ff=f'9月+{team6_kiroku6_output_kingaku}円'
    gg=f'10月+{team6_kiroku7_output_kingaku}円'
    hh=f'11月+{team6_kiroku8_output_kingaku}円'
    ii=f'12月+{team6_kiroku9_output_kingaku}円'
    jj=f'1月+{team6_kiroku10_output_kingaku}円'
    kk=f'2月+{team6_kiroku11_output_kingaku}円'
    ll=f'3月+{team6_kiroku12_output_kingaku}円'

    columns=[a_a,b_b]
    index=index=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll]

    a1=a
    a2=team6_kiroku1_output_kingaku

    b1=a*2
    b2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku

    c1=a*3
    c2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku

    d1=a*4
    d2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku+team6_kiroku4_output_kingaku

    e1=a*5
    e2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku+team6_kiroku4_output_kingaku+team6_kiroku5_output_kingaku

    f1=a*6
    f2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku+team6_kiroku4_output_kingaku+team6_kiroku5_output_kingaku+team6_kiroku6_output_kingaku

    g1=a*7
    g2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku+team6_kiroku4_output_kingaku+team6_kiroku5_output_kingaku+team6_kiroku6_output_kingaku+team6_kiroku7_output_kingaku

    h1=a*8
    h2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku+team6_kiroku4_output_kingaku+team6_kiroku5_output_kingaku+team6_kiroku6_output_kingaku+team6_kiroku7_output_kingaku+team6_kiroku8_output_kingaku

    i1=a*9
    i2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku+team6_kiroku4_output_kingaku+team6_kiroku5_output_kingaku+team6_kiroku6_output_kingaku+team6_kiroku7_output_kingaku+team6_kiroku8_output_kingaku+team6_kiroku9_output_kingaku

    j1=a*10
    j2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku+team6_kiroku4_output_kingaku+team6_kiroku5_output_kingaku+team6_kiroku6_output_kingaku+team6_kiroku7_output_kingaku+team6_kiroku8_output_kingaku+team6_kiroku9_output_kingaku+team6_kiroku10_output_kingaku
    
    k1=a*11
    k2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku+team6_kiroku4_output_kingaku+team6_kiroku5_output_kingaku+team6_kiroku6_output_kingaku+team6_kiroku7_output_kingaku+team6_kiroku8_output_kingaku+team6_kiroku9_output_kingaku+team6_kiroku10_output_kingaku+team6_kiroku11_output_kingaku
    
    l1=a*12
    l2=team6_kiroku1_output_kingaku+team6_kiroku2_output_kingaku+team6_kiroku3_output_kingaku+team6_kiroku4_output_kingaku+team6_kiroku5_output_kingaku+team6_kiroku6_output_kingaku+team6_kiroku7_output_kingaku+team6_kiroku8_output_kingaku+team6_kiroku9_output_kingaku+team6_kiroku10_output_kingaku+team6_kiroku11_output_kingaku+team6_kiroku12_output_kingaku
    

    df_a=pd.DataFrame([[a1,a2],[b1,b2],[c1,c2],[d1,d2],[e1,e2],[f1,f2],[g1,g2],[h1,h2],[i1,i2],[j1,j2],[k1,k2],[l1,l2]],index=index,columns=columns)
    figure(num=None, figsize=(18.5, 9))
    plt.title(f'合理化達成金額[チーム:{team_kaizen6_kijun_team_name}]',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=20)
    plt.ylabel('金額単位【100万円】',fontsize=20)
    plt.plot(list(df_a.index),df_a[a_a],marker='s',label=a_a)
    plt.plot(list(df_a.index),df_a[b_b],marker='o',label=b_b)
    plt.legend()


def plt2svg_k6():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k6(request):
    setplt_k6()
    svg=plt2svg_k6()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response








def setplt_k1t():

    team_kaizen1_kijun=team_kaizen1.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen1_kijun2=team_kaizen1_kijun[0]
    #チームネーム1    
    team_kaizen1_kijun_team_name=team_kaizen1_kijun2['team_name']
    #改善必要枚数
    team_kaizen1_kijun_kaizen_teian_hituyou_maisuu=team_kaizen1_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen1_kijun_nenkan_mokuhyou_kingaku=team_kaizen1_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen1_kijun_team_member_ninzuu=team_kaizen1_kijun2['team_member_ninzuu']
    if team_kaizen1_kijun_team_member_ninzuu==0:
        team_kaizen1_kijun_team_member_ninzuu=1


    #チーム１
    team_kaizen1_kiroku2=team_kaizen1_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team1_kiroku1=team_kaizen1_kiroku2[0]
    team1_kiroku2=team_kaizen1_kiroku2[1]
    team1_kiroku3=team_kaizen1_kiroku2[2]
    team1_kiroku4=team_kaizen1_kiroku2[3]
    team1_kiroku5=team_kaizen1_kiroku2[4]
    team1_kiroku6=team_kaizen1_kiroku2[5]
    team1_kiroku7=team_kaizen1_kiroku2[6]
    team1_kiroku8=team_kaizen1_kiroku2[7]
    team1_kiroku9=team_kaizen1_kiroku2[8]
    team1_kiroku10=team_kaizen1_kiroku2[9]
    team1_kiroku11=team_kaizen1_kiroku2[10]
    team1_kiroku12=team_kaizen1_kiroku2[11]

    team1_kiroku1_output_kaizenteian=team1_kiroku1['output_kaizenteian']
    team1_kiroku2_output_kaizenteian=team1_kiroku2['output_kaizenteian']
    team1_kiroku3_output_kaizenteian=team1_kiroku3['output_kaizenteian']
    team1_kiroku4_output_kaizenteian=team1_kiroku4['output_kaizenteian']
    team1_kiroku5_output_kaizenteian=team1_kiroku5['output_kaizenteian']
    team1_kiroku6_output_kaizenteian=team1_kiroku6['output_kaizenteian']
    team1_kiroku7_output_kaizenteian=team1_kiroku7['output_kaizenteian']
    team1_kiroku8_output_kaizenteian=team1_kiroku8['output_kaizenteian']
    team1_kiroku9_output_kaizenteian=team1_kiroku9['output_kaizenteian']
    team1_kiroku10_output_kaizenteian=team1_kiroku10['output_kaizenteian']
    team1_kiroku11_output_kaizenteian=team1_kiroku11['output_kaizenteian']
    team1_kiroku12_output_kaizenteian=team1_kiroku12['output_kaizenteian']

    team1_kiroku1_output_kingaku=team1_kiroku1['output_kingaku']
    team1_kiroku2_output_kingaku=team1_kiroku2['output_kingaku']
    team1_kiroku3_output_kingaku=team1_kiroku3['output_kingaku']
    team1_kiroku4_output_kingaku=team1_kiroku4['output_kingaku']
    team1_kiroku5_output_kingaku=team1_kiroku5['output_kingaku']
    team1_kiroku6_output_kingaku=team1_kiroku6['output_kingaku']
    team1_kiroku7_output_kingaku=team1_kiroku7['output_kingaku']
    team1_kiroku8_output_kingaku=team1_kiroku8['output_kingaku']
    team1_kiroku9_output_kingaku=team1_kiroku9['output_kingaku']
    team1_kiroku10_output_kingaku=team1_kiroku10['output_kingaku']
    team1_kiroku11_output_kingaku=team1_kiroku11['output_kingaku']
    team1_kiroku12_output_kingaku=team1_kiroku12['output_kingaku']




    g4=team1_kiroku1_output_kaizenteian
    g5=team1_kiroku2_output_kaizenteian
    g6=team1_kiroku3_output_kaizenteian
    g7=team1_kiroku4_output_kaizenteian
    g8=team1_kiroku5_output_kaizenteian
    g9=team1_kiroku6_output_kaizenteian
    g10=team1_kiroku7_output_kaizenteian
    g11=team1_kiroku8_output_kaizenteian
    g12=team1_kiroku9_output_kaizenteian
    g1=team1_kiroku10_output_kaizenteian
    g2=team1_kiroku11_output_kaizenteian
    g3=team1_kiroku12_output_kaizenteian

    g4a=team1_kiroku1_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g5a=team1_kiroku2_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g6a=team1_kiroku3_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g7a=team1_kiroku4_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g8a=team1_kiroku5_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g9a=team1_kiroku6_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g10a=team1_kiroku7_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g11a=team1_kiroku8_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g12a=team1_kiroku9_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g1a=team1_kiroku10_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g2a=team1_kiroku11_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu
    g3a=team1_kiroku12_output_kaizenteian/team_kaizen1_kijun_team_member_ninzuu

    g4a=round(g4a, 1)
    g5a=round(g5a, 1)
    g6a=round(g6a, 1)
    g7a=round(g7a, 1)
    g8a=round(g8a, 1)
    g9a=round(g9a, 1)
    g10a=round(g10a, 1)
    g11a=round(g11a, 1)
    g12a=round(g12a, 1)
    g1a=round(g1a, 1)
    g2a=round(g2a, 1)
    g3a=round(g3a, 1)







    nin=team_kaizen1_kijun_team_member_ninzuu
    mokuhyou=team_kaizen1_kijun_kaizen_teian_hituyou_maisuu
    zen_mokuhyou=team_kaizen1_kijun_team_member_ninzuu*team_kaizen1_kijun_kaizen_teian_hituyou_maisuu
    index='改善提案提出枚数'
    

    

    
    
    

    x = np.array([f'4月(平均{g4a})',f'5月(平均{g5a})',f'6月(平均{g6a})',f'7月(平均{g7a})',f'8月(平均{g8a})',f'9月(平均{g9a})',f'10月(平均{g10a})',f'11月(平均{g11a})',f'12月(平均{g12a})',f'1月(平均{g1a})',f'２月(平均{g2a})',f'３月(平均{g3a})'])
    y = np.array([g4,g5,g6,g7,g8,g9,g10,g11,g12,g1,g2,g3])

   
    x_position = np.arange(len(x))
    fig = plt.figure()
    fig,ax=plt.subplots(figsize=(18,9))
    
    ax.bar(x_position, y, tick_label=x)
    ax.axhline(y=zen_mokuhyou,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)
    plt.title(f'改善提案提出記録:チーム{team_kaizen1_kijun_team_name}({nin}人)',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'提出目標{zen_mokuhyou}枚以上【枚】',fontsize=23)
    fig.show()


def plt2svg_k1t():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k1t(request):
    setplt_k1t()
    svg=plt2svg_k1t()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_k2t():
    team_kaizen2_kijun=team_kaizen2.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen2_kijun2=team_kaizen2_kijun[0]
    #チームネーム2    
    team_kaizen2_kijun_team_name=team_kaizen2_kijun2['team_name']
    #改善必要枚数
    team_kaizen2_kijun_kaizen_teian_hituyou_maisuu=team_kaizen2_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen2_kijun_nenkan_mokuhyou_kingaku=team_kaizen2_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen2_kijun_team_member_ninzuu=team_kaizen2_kijun2['team_member_ninzuu']


    
    if team_kaizen2_kijun_team_member_ninzuu==0:
        team_kaizen2_kijun_team_member_ninzuu=1


    #チーム2
    team_kaizen2_kiroku2=team_kaizen2_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team2_kiroku1=team_kaizen2_kiroku2[0]
    team2_kiroku2=team_kaizen2_kiroku2[1]
    team2_kiroku3=team_kaizen2_kiroku2[2]
    team2_kiroku4=team_kaizen2_kiroku2[3]
    team2_kiroku5=team_kaizen2_kiroku2[4]
    team2_kiroku6=team_kaizen2_kiroku2[5]
    team2_kiroku7=team_kaizen2_kiroku2[6]
    team2_kiroku8=team_kaizen2_kiroku2[7]
    team2_kiroku9=team_kaizen2_kiroku2[8]
    team2_kiroku10=team_kaizen2_kiroku2[9]
    team2_kiroku11=team_kaizen2_kiroku2[10]
    team2_kiroku12=team_kaizen2_kiroku2[11]

    team2_kiroku1_output_kaizenteian=team2_kiroku1['output_kaizenteian']
    team2_kiroku2_output_kaizenteian=team2_kiroku2['output_kaizenteian']
    team2_kiroku3_output_kaizenteian=team2_kiroku3['output_kaizenteian']
    team2_kiroku4_output_kaizenteian=team2_kiroku4['output_kaizenteian']
    team2_kiroku5_output_kaizenteian=team2_kiroku5['output_kaizenteian']
    team2_kiroku6_output_kaizenteian=team2_kiroku6['output_kaizenteian']
    team2_kiroku7_output_kaizenteian=team2_kiroku7['output_kaizenteian']
    team2_kiroku8_output_kaizenteian=team2_kiroku8['output_kaizenteian']
    team2_kiroku9_output_kaizenteian=team2_kiroku9['output_kaizenteian']
    team2_kiroku10_output_kaizenteian=team2_kiroku10['output_kaizenteian']
    team2_kiroku11_output_kaizenteian=team2_kiroku11['output_kaizenteian']
    team2_kiroku12_output_kaizenteian=team2_kiroku12['output_kaizenteian']

    team2_kiroku1_output_kingaku=team2_kiroku1['output_kingaku']
    team2_kiroku2_output_kingaku=team2_kiroku2['output_kingaku']
    team2_kiroku3_output_kingaku=team2_kiroku3['output_kingaku']
    team2_kiroku4_output_kingaku=team2_kiroku4['output_kingaku']
    team2_kiroku5_output_kingaku=team2_kiroku5['output_kingaku']
    team2_kiroku6_output_kingaku=team2_kiroku6['output_kingaku']
    team2_kiroku7_output_kingaku=team2_kiroku7['output_kingaku']
    team2_kiroku8_output_kingaku=team2_kiroku8['output_kingaku']
    team2_kiroku9_output_kingaku=team2_kiroku9['output_kingaku']
    team2_kiroku10_output_kingaku=team2_kiroku10['output_kingaku']
    team2_kiroku11_output_kingaku=team2_kiroku11['output_kingaku']
    team2_kiroku12_output_kingaku=team2_kiroku12['output_kingaku']




    g4=team2_kiroku1_output_kaizenteian
    g5=team2_kiroku2_output_kaizenteian
    g6=team2_kiroku3_output_kaizenteian
    g7=team2_kiroku4_output_kaizenteian
    g8=team2_kiroku5_output_kaizenteian
    g9=team2_kiroku6_output_kaizenteian
    g10=team2_kiroku7_output_kaizenteian
    g11=team2_kiroku8_output_kaizenteian
    g12=team2_kiroku9_output_kaizenteian
    g1=team2_kiroku10_output_kaizenteian
    g2=team2_kiroku11_output_kaizenteian
    g3=team2_kiroku12_output_kaizenteian

    g4a=team2_kiroku1_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g5a=team2_kiroku2_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g6a=team2_kiroku3_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g7a=team2_kiroku4_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g8a=team2_kiroku5_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g9a=team2_kiroku6_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g10a=team2_kiroku7_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g11a=team2_kiroku8_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g12a=team2_kiroku9_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g1a=team2_kiroku10_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g2a=team2_kiroku11_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu
    g3a=team2_kiroku12_output_kaizenteian/team_kaizen2_kijun_team_member_ninzuu





    g4a=round(g4a, 1)
    g5a=round(g5a, 1)
    g6a=round(g6a, 1)
    g7a=round(g7a, 1)
    g8a=round(g8a, 1)
    g9a=round(g9a, 1)
    g10a=round(g10a, 1)
    g11a=round(g11a, 1)
    g12a=round(g12a, 1)
    g1a=round(g1a, 1)
    g2a=round(g2a, 1)
    g3a=round(g3a, 1)








    nin=team_kaizen2_kijun_team_member_ninzuu
    mokuhyou=team_kaizen2_kijun_kaizen_teian_hituyou_maisuu
    zen_mokuhyou=team_kaizen2_kijun_team_member_ninzuu*team_kaizen2_kijun_kaizen_teian_hituyou_maisuu
    index='改善提案提出枚数'
    

    

    
    
    

    x = np.array([f'4月(平均{g4a})',f'5月(平均{g5a})',f'6月(平均{g6a})',f'7月(平均{g7a})',f'8月(平均{g8a})',f'9月(平均{g9a})',f'10月(平均{g10a})',f'11月(平均{g11a})',f'12月(平均{g12a})',f'1月(平均{g1a})',f'２月(平均{g2a})',f'３月(平均{g3a})'])
    y = np.array([g4,g5,g6,g7,g8,g9,g10,g11,g12,g1,g2,g3])

   
    x_position = np.arange(len(x))
    fig = plt.figure()
    fig,ax=plt.subplots(figsize=(18,9))
    
    ax.bar(x_position, y, tick_label=x)
    ax.axhline(y=zen_mokuhyou,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)
    plt.title(f'改善提案提出記録:チーム{team_kaizen2_kijun_team_name}({nin}人)',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'提出目標{zen_mokuhyou}枚以上【枚】',fontsize=23)
    fig.show()


def plt2svg_k2t():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k2t(request):
    setplt_k2t()
    svg=plt2svg_k2t()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_k3t():

    team_kaizen3_kijun=team_kaizen3.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen3_kijun2=team_kaizen3_kijun[0]
    #チームネーム3    
    team_kaizen3_kijun_team_name=team_kaizen3_kijun2['team_name']
    #改善必要枚数
    team_kaizen3_kijun_kaizen_teian_hituyou_maisuu=team_kaizen3_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen3_kijun_nenkan_mokuhyou_kingaku=team_kaizen3_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen3_kijun_team_member_ninzuu=team_kaizen3_kijun2['team_member_ninzuu']
    
    if team_kaizen3_kijun_team_member_ninzuu==0:
        team_kaizen3_kijun_team_member_ninzuu=1

    #チーム3
    team_kaizen3_kiroku2=team_kaizen3_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team3_kiroku1=team_kaizen3_kiroku2[0]
    team3_kiroku2=team_kaizen3_kiroku2[1]
    team3_kiroku3=team_kaizen3_kiroku2[2]
    team3_kiroku4=team_kaizen3_kiroku2[3]
    team3_kiroku5=team_kaizen3_kiroku2[4]
    team3_kiroku6=team_kaizen3_kiroku2[5]
    team3_kiroku7=team_kaizen3_kiroku2[6]
    team3_kiroku8=team_kaizen3_kiroku2[7]
    team3_kiroku9=team_kaizen3_kiroku2[8]
    team3_kiroku10=team_kaizen3_kiroku2[9]
    team3_kiroku11=team_kaizen3_kiroku2[10]
    team3_kiroku12=team_kaizen3_kiroku2[11]

    team3_kiroku1_output_kaizenteian=team3_kiroku1['output_kaizenteian']
    team3_kiroku2_output_kaizenteian=team3_kiroku2['output_kaizenteian']
    team3_kiroku3_output_kaizenteian=team3_kiroku3['output_kaizenteian']
    team3_kiroku4_output_kaizenteian=team3_kiroku4['output_kaizenteian']
    team3_kiroku5_output_kaizenteian=team3_kiroku5['output_kaizenteian']
    team3_kiroku6_output_kaizenteian=team3_kiroku6['output_kaizenteian']
    team3_kiroku7_output_kaizenteian=team3_kiroku7['output_kaizenteian']
    team3_kiroku8_output_kaizenteian=team3_kiroku8['output_kaizenteian']
    team3_kiroku9_output_kaizenteian=team3_kiroku9['output_kaizenteian']
    team3_kiroku10_output_kaizenteian=team3_kiroku10['output_kaizenteian']
    team3_kiroku11_output_kaizenteian=team3_kiroku11['output_kaizenteian']
    team3_kiroku12_output_kaizenteian=team3_kiroku12['output_kaizenteian']

    team3_kiroku1_output_kingaku=team3_kiroku1['output_kingaku']
    team3_kiroku2_output_kingaku=team3_kiroku2['output_kingaku']
    team3_kiroku3_output_kingaku=team3_kiroku3['output_kingaku']
    team3_kiroku4_output_kingaku=team3_kiroku4['output_kingaku']
    team3_kiroku5_output_kingaku=team3_kiroku5['output_kingaku']
    team3_kiroku6_output_kingaku=team3_kiroku6['output_kingaku']
    team3_kiroku7_output_kingaku=team3_kiroku7['output_kingaku']
    team3_kiroku8_output_kingaku=team3_kiroku8['output_kingaku']
    team3_kiroku9_output_kingaku=team3_kiroku9['output_kingaku']
    team3_kiroku10_output_kingaku=team3_kiroku10['output_kingaku']
    team3_kiroku11_output_kingaku=team3_kiroku11['output_kingaku']
    team3_kiroku12_output_kingaku=team3_kiroku12['output_kingaku']



   



    g4=team3_kiroku1_output_kaizenteian
    g5=team3_kiroku2_output_kaizenteian
    g6=team3_kiroku3_output_kaizenteian
    g7=team3_kiroku4_output_kaizenteian
    g8=team3_kiroku5_output_kaizenteian
    g9=team3_kiroku6_output_kaizenteian
    g10=team3_kiroku7_output_kaizenteian
    g11=team3_kiroku8_output_kaizenteian
    g12=team3_kiroku9_output_kaizenteian
    g1=team3_kiroku10_output_kaizenteian
    g2=team3_kiroku11_output_kaizenteian
    g3=team3_kiroku12_output_kaizenteian

    g4a=team3_kiroku1_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g5a=team3_kiroku2_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g6a=team3_kiroku3_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g7a=team3_kiroku4_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g8a=team3_kiroku5_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g9a=team3_kiroku6_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g10a=team3_kiroku7_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g11a=team3_kiroku8_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g12a=team3_kiroku9_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g1a=team3_kiroku10_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g2a=team3_kiroku11_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu
    g3a=team3_kiroku12_output_kaizenteian/team_kaizen3_kijun_team_member_ninzuu

    g4a=round(g4a, 1)
    g5a=round(g5a, 1)
    g6a=round(g6a, 1)
    g7a=round(g7a, 1)
    g8a=round(g8a, 1)
    g9a=round(g9a, 1)
    g10a=round(g10a, 1)
    g11a=round(g11a, 1)
    g12a=round(g12a, 1)
    g1a=round(g1a, 1)
    g2a=round(g2a, 1)
    g3a=round(g3a, 1)







    nin=team_kaizen3_kijun_team_member_ninzuu
    mokuhyou=team_kaizen3_kijun_kaizen_teian_hituyou_maisuu
    zen_mokuhyou=team_kaizen3_kijun_team_member_ninzuu*team_kaizen3_kijun_kaizen_teian_hituyou_maisuu
    index='改善提案提出枚数'
    

    

    
    
    

    x = np.array([f'4月(平均{g4a})',f'5月(平均{g5a})',f'6月(平均{g6a})',f'7月(平均{g7a})',f'8月(平均{g8a})',f'9月(平均{g9a})',f'10月(平均{g10a})',f'11月(平均{g11a})',f'12月(平均{g12a})',f'1月(平均{g1a})',f'２月(平均{g2a})',f'３月(平均{g3a})'])
    y = np.array([g4,g5,g6,g7,g8,g9,g10,g11,g12,g1,g2,g3])

   
    x_position = np.arange(len(x))
    fig = plt.figure()
    fig,ax=plt.subplots(figsize=(18,9))
    
    ax.bar(x_position, y, tick_label=x)
    ax.axhline(y=zen_mokuhyou,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)
    plt.title(f'改善提案提出記録:チーム{team_kaizen3_kijun_team_name}({nin}人)',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'提出目標{zen_mokuhyou}枚以上【枚】',fontsize=23)
    fig.show()


def plt2svg_k3t():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k3t(request):
    setplt_k3t()
    svg=plt2svg_k3t()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_k4t():

    team_kaizen4_kijun=team_kaizen4.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen4_kijun2=team_kaizen4_kijun[0]
    #チームネーム4    
    team_kaizen4_kijun_team_name=team_kaizen4_kijun2['team_name']
    #改善必要枚数
    team_kaizen4_kijun_kaizen_teian_hituyou_maisuu=team_kaizen4_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen4_kijun_nenkan_mokuhyou_kingaku=team_kaizen4_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen4_kijun_team_member_ninzuu=team_kaizen4_kijun2['team_member_ninzuu']

    if team_kaizen4_kijun_team_member_ninzuu==0:
        team_kaizen4_kijun_team_member_ninzuu=1

    #チーム4
    team_kaizen4_kiroku2=team_kaizen4_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team4_kiroku1=team_kaizen4_kiroku2[0]
    team4_kiroku2=team_kaizen4_kiroku2[1]
    team4_kiroku3=team_kaizen4_kiroku2[2]
    team4_kiroku4=team_kaizen4_kiroku2[3]
    team4_kiroku5=team_kaizen4_kiroku2[4]
    team4_kiroku6=team_kaizen4_kiroku2[5]
    team4_kiroku7=team_kaizen4_kiroku2[6]
    team4_kiroku8=team_kaizen4_kiroku2[7]
    team4_kiroku9=team_kaizen4_kiroku2[8]
    team4_kiroku10=team_kaizen4_kiroku2[9]
    team4_kiroku11=team_kaizen4_kiroku2[10]
    team4_kiroku12=team_kaizen4_kiroku2[11]

    team4_kiroku1_output_kaizenteian=team4_kiroku1['output_kaizenteian']
    team4_kiroku2_output_kaizenteian=team4_kiroku2['output_kaizenteian']
    team4_kiroku3_output_kaizenteian=team4_kiroku3['output_kaizenteian']
    team4_kiroku4_output_kaizenteian=team4_kiroku4['output_kaizenteian']
    team4_kiroku5_output_kaizenteian=team4_kiroku5['output_kaizenteian']
    team4_kiroku6_output_kaizenteian=team4_kiroku6['output_kaizenteian']
    team4_kiroku7_output_kaizenteian=team4_kiroku7['output_kaizenteian']
    team4_kiroku8_output_kaizenteian=team4_kiroku8['output_kaizenteian']
    team4_kiroku9_output_kaizenteian=team4_kiroku9['output_kaizenteian']
    team4_kiroku10_output_kaizenteian=team4_kiroku10['output_kaizenteian']
    team4_kiroku11_output_kaizenteian=team4_kiroku11['output_kaizenteian']
    team4_kiroku12_output_kaizenteian=team4_kiroku12['output_kaizenteian']

    team4_kiroku1_output_kingaku=team4_kiroku1['output_kingaku']
    team4_kiroku2_output_kingaku=team4_kiroku2['output_kingaku']
    team4_kiroku3_output_kingaku=team4_kiroku3['output_kingaku']
    team4_kiroku4_output_kingaku=team4_kiroku4['output_kingaku']
    team4_kiroku5_output_kingaku=team4_kiroku5['output_kingaku']
    team4_kiroku6_output_kingaku=team4_kiroku6['output_kingaku']
    team4_kiroku7_output_kingaku=team4_kiroku7['output_kingaku']
    team4_kiroku8_output_kingaku=team4_kiroku8['output_kingaku']
    team4_kiroku9_output_kingaku=team4_kiroku9['output_kingaku']
    team4_kiroku10_output_kingaku=team4_kiroku10['output_kingaku']
    team4_kiroku11_output_kingaku=team4_kiroku11['output_kingaku']
    team4_kiroku12_output_kingaku=team4_kiroku12['output_kingaku']




    g4=team4_kiroku1_output_kaizenteian
    g5=team4_kiroku2_output_kaizenteian
    g6=team4_kiroku3_output_kaizenteian
    g7=team4_kiroku4_output_kaizenteian
    g8=team4_kiroku5_output_kaizenteian
    g9=team4_kiroku6_output_kaizenteian
    g10=team4_kiroku7_output_kaizenteian
    g11=team4_kiroku8_output_kaizenteian
    g12=team4_kiroku9_output_kaizenteian
    g1=team4_kiroku10_output_kaizenteian
    g2=team4_kiroku11_output_kaizenteian
    g3=team4_kiroku12_output_kaizenteian

    g4a=team4_kiroku1_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g5a=team4_kiroku2_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g6a=team4_kiroku3_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g7a=team4_kiroku4_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g8a=team4_kiroku5_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g9a=team4_kiroku6_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g10a=team4_kiroku7_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g11a=team4_kiroku8_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g12a=team4_kiroku9_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g1a=team4_kiroku10_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g2a=team4_kiroku11_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu
    g3a=team4_kiroku12_output_kaizenteian/team_kaizen4_kijun_team_member_ninzuu

    g4a=round(g4a, 1)
    g5a=round(g5a, 1)
    g6a=round(g6a, 1)
    g7a=round(g7a, 1)
    g8a=round(g8a, 1)
    g9a=round(g9a, 1)
    g10a=round(g10a, 1)
    g11a=round(g11a, 1)
    g12a=round(g12a, 1)
    g1a=round(g1a, 1)
    g2a=round(g2a, 1)
    g3a=round(g3a, 1)







    nin=team_kaizen4_kijun_team_member_ninzuu
    mokuhyou=team_kaizen4_kijun_kaizen_teian_hituyou_maisuu
    zen_mokuhyou=team_kaizen4_kijun_team_member_ninzuu*team_kaizen4_kijun_kaizen_teian_hituyou_maisuu
    index='改善提案提出枚数'
    

    

    
    
    

    x = np.array([f'4月(平均{g4a})',f'5月(平均{g5a})',f'6月(平均{g6a})',f'7月(平均{g7a})',f'8月(平均{g8a})',f'9月(平均{g9a})',f'10月(平均{g10a})',f'11月(平均{g11a})',f'12月(平均{g12a})',f'1月(平均{g1a})',f'２月(平均{g2a})',f'３月(平均{g3a})'])
    y = np.array([g4,g5,g6,g7,g8,g9,g10,g11,g12,g1,g2,g3])

   
    x_position = np.arange(len(x))
    fig = plt.figure()
    fig,ax=plt.subplots(figsize=(18,9))
    
    ax.bar(x_position, y, tick_label=x)
    ax.axhline(y=zen_mokuhyou,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)
    plt.title(f'改善提案提出記録:チーム{team_kaizen4_kijun_team_name}({nin}人)',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'提出目標{zen_mokuhyou}枚以上【枚】',fontsize=23)
    fig.show()


def plt2svg_k4t():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k4t(request):
    setplt_k4t()
    svg=plt2svg_k4t()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_k5t():

    team_kaizen5_kijun=team_kaizen5.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen5_kijun2=team_kaizen5_kijun[0]
    #チームネーム5    
    team_kaizen5_kijun_team_name=team_kaizen5_kijun2['team_name']
    #改善必要枚数
    team_kaizen5_kijun_kaizen_teian_hituyou_maisuu=team_kaizen5_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen5_kijun_nenkan_mokuhyou_kingaku=team_kaizen5_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen5_kijun_team_member_ninzuu=team_kaizen5_kijun2['team_member_ninzuu']

    if team_kaizen5_kijun_team_member_ninzuu==0:
        team_kaizen5_kijun_team_member_ninzuu=1


    #チーム5
    team_kaizen5_kiroku2=team_kaizen5_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team5_kiroku1=team_kaizen5_kiroku2[0]
    team5_kiroku2=team_kaizen5_kiroku2[1]
    team5_kiroku3=team_kaizen5_kiroku2[2]
    team5_kiroku4=team_kaizen5_kiroku2[3]
    team5_kiroku5=team_kaizen5_kiroku2[4]
    team5_kiroku6=team_kaizen5_kiroku2[5]
    team5_kiroku7=team_kaizen5_kiroku2[6]
    team5_kiroku8=team_kaizen5_kiroku2[7]
    team5_kiroku9=team_kaizen5_kiroku2[8]
    team5_kiroku10=team_kaizen5_kiroku2[9]
    team5_kiroku11=team_kaizen5_kiroku2[10]
    team5_kiroku12=team_kaizen5_kiroku2[11]

    team5_kiroku1_output_kaizenteian=team5_kiroku1['output_kaizenteian']
    team5_kiroku2_output_kaizenteian=team5_kiroku2['output_kaizenteian']
    team5_kiroku3_output_kaizenteian=team5_kiroku3['output_kaizenteian']
    team5_kiroku4_output_kaizenteian=team5_kiroku4['output_kaizenteian']
    team5_kiroku5_output_kaizenteian=team5_kiroku5['output_kaizenteian']
    team5_kiroku6_output_kaizenteian=team5_kiroku6['output_kaizenteian']
    team5_kiroku7_output_kaizenteian=team5_kiroku7['output_kaizenteian']
    team5_kiroku8_output_kaizenteian=team5_kiroku8['output_kaizenteian']
    team5_kiroku9_output_kaizenteian=team5_kiroku9['output_kaizenteian']
    team5_kiroku10_output_kaizenteian=team5_kiroku10['output_kaizenteian']
    team5_kiroku11_output_kaizenteian=team5_kiroku11['output_kaizenteian']
    team5_kiroku12_output_kaizenteian=team5_kiroku12['output_kaizenteian']

    team5_kiroku1_output_kingaku=team5_kiroku1['output_kingaku']
    team5_kiroku2_output_kingaku=team5_kiroku2['output_kingaku']
    team5_kiroku3_output_kingaku=team5_kiroku3['output_kingaku']
    team5_kiroku4_output_kingaku=team5_kiroku4['output_kingaku']
    team5_kiroku5_output_kingaku=team5_kiroku5['output_kingaku']
    team5_kiroku6_output_kingaku=team5_kiroku6['output_kingaku']
    team5_kiroku7_output_kingaku=team5_kiroku7['output_kingaku']
    team5_kiroku8_output_kingaku=team5_kiroku8['output_kingaku']
    team5_kiroku9_output_kingaku=team5_kiroku9['output_kingaku']
    team5_kiroku10_output_kingaku=team5_kiroku10['output_kingaku']
    team5_kiroku11_output_kingaku=team5_kiroku11['output_kingaku']
    team5_kiroku12_output_kingaku=team5_kiroku12['output_kingaku']




    g4=team5_kiroku1_output_kaizenteian
    g5=team5_kiroku2_output_kaizenteian
    g6=team5_kiroku3_output_kaizenteian
    g7=team5_kiroku4_output_kaizenteian
    g8=team5_kiroku5_output_kaizenteian
    g9=team5_kiroku6_output_kaizenteian
    g10=team5_kiroku7_output_kaizenteian
    g11=team5_kiroku8_output_kaizenteian
    g12=team5_kiroku9_output_kaizenteian
    g1=team5_kiroku10_output_kaizenteian
    g2=team5_kiroku11_output_kaizenteian
    g3=team5_kiroku12_output_kaizenteian

    g4a=team5_kiroku1_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g5a=team5_kiroku2_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g6a=team5_kiroku3_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g7a=team5_kiroku4_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g8a=team5_kiroku5_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g9a=team5_kiroku6_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g10a=team5_kiroku7_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g11a=team5_kiroku8_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g12a=team5_kiroku9_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g1a=team5_kiroku10_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g2a=team5_kiroku11_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu
    g3a=team5_kiroku12_output_kaizenteian/team_kaizen5_kijun_team_member_ninzuu


    g4a=round(g4a, 1)
    g5a=round(g5a, 1)
    g6a=round(g6a, 1)
    g7a=round(g7a, 1)
    g8a=round(g8a, 1)
    g9a=round(g9a, 1)
    g10a=round(g10a, 1)
    g11a=round(g11a, 1)
    g12a=round(g12a, 1)
    g1a=round(g1a, 1)
    g2a=round(g2a, 1)
    g3a=round(g3a, 1)







    nin=team_kaizen5_kijun_team_member_ninzuu
    mokuhyou=team_kaizen5_kijun_kaizen_teian_hituyou_maisuu
    zen_mokuhyou=team_kaizen5_kijun_team_member_ninzuu*team_kaizen5_kijun_kaizen_teian_hituyou_maisuu
    index='改善提案提出枚数'
    

    

    
    
    

    x = np.array([f'4月(平均{g4a})',f'5月(平均{g5a})',f'6月(平均{g6a})',f'7月(平均{g7a})',f'8月(平均{g8a})',f'9月(平均{g9a})',f'10月(平均{g10a})',f'11月(平均{g11a})',f'12月(平均{g12a})',f'1月(平均{g1a})',f'２月(平均{g2a})',f'３月(平均{g3a})'])
    y = np.array([g4,g5,g6,g7,g8,g9,g10,g11,g12,g1,g2,g3])

   
    x_position = np.arange(len(x))
    fig = plt.figure()
    fig,ax=plt.subplots(figsize=(18,9))
    
    ax.bar(x_position, y, tick_label=x)
    ax.axhline(y=zen_mokuhyou,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)
    plt.title(f'改善提案提出記録:チーム{team_kaizen5_kijun_team_name}({nin}人)',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'提出目標{zen_mokuhyou}枚以上【枚】',fontsize=23)
    fig.show()


def plt2svg_k5t():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k5t(request):
    setplt_k5t()
    svg=plt2svg_k5t()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_k6t():

    team_kaizen6_kijun=team_kaizen6.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen6_kijun2=team_kaizen6_kijun[0]
    #チームネーム6    
    team_kaizen6_kijun_team_name=team_kaizen6_kijun2['team_name']
    #改善必要枚数
    team_kaizen6_kijun_kaizen_teian_hituyou_maisuu=team_kaizen6_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen6_kijun_nenkan_mokuhyou_kingaku=team_kaizen6_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen6_kijun_team_member_ninzuu=team_kaizen6_kijun2['team_member_ninzuu']

    if team_kaizen6_kijun_team_member_ninzuu==0:
        team_kaizen6_kijun_team_member_ninzuu=1


    #チーム6
    team_kaizen6_kiroku2=team_kaizen6_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team6_kiroku1=team_kaizen6_kiroku2[0]
    team6_kiroku2=team_kaizen6_kiroku2[1]
    team6_kiroku3=team_kaizen6_kiroku2[2]
    team6_kiroku4=team_kaizen6_kiroku2[3]
    team6_kiroku5=team_kaizen6_kiroku2[4]
    team6_kiroku6=team_kaizen6_kiroku2[5]
    team6_kiroku7=team_kaizen6_kiroku2[6]
    team6_kiroku8=team_kaizen6_kiroku2[7]
    team6_kiroku9=team_kaizen6_kiroku2[8]
    team6_kiroku10=team_kaizen6_kiroku2[9]
    team6_kiroku11=team_kaizen6_kiroku2[10]
    team6_kiroku12=team_kaizen6_kiroku2[11]

    team6_kiroku1_output_kaizenteian=team6_kiroku1['output_kaizenteian']
    team6_kiroku2_output_kaizenteian=team6_kiroku2['output_kaizenteian']
    team6_kiroku3_output_kaizenteian=team6_kiroku3['output_kaizenteian']
    team6_kiroku4_output_kaizenteian=team6_kiroku4['output_kaizenteian']
    team6_kiroku5_output_kaizenteian=team6_kiroku5['output_kaizenteian']
    team6_kiroku6_output_kaizenteian=team6_kiroku6['output_kaizenteian']
    team6_kiroku7_output_kaizenteian=team6_kiroku7['output_kaizenteian']
    team6_kiroku8_output_kaizenteian=team6_kiroku8['output_kaizenteian']
    team6_kiroku9_output_kaizenteian=team6_kiroku9['output_kaizenteian']
    team6_kiroku10_output_kaizenteian=team6_kiroku10['output_kaizenteian']
    team6_kiroku11_output_kaizenteian=team6_kiroku11['output_kaizenteian']
    team6_kiroku12_output_kaizenteian=team6_kiroku12['output_kaizenteian']

    team6_kiroku1_output_kingaku=team6_kiroku1['output_kingaku']
    team6_kiroku2_output_kingaku=team6_kiroku2['output_kingaku']
    team6_kiroku3_output_kingaku=team6_kiroku3['output_kingaku']
    team6_kiroku4_output_kingaku=team6_kiroku4['output_kingaku']
    team6_kiroku5_output_kingaku=team6_kiroku5['output_kingaku']
    team6_kiroku6_output_kingaku=team6_kiroku6['output_kingaku']
    team6_kiroku7_output_kingaku=team6_kiroku7['output_kingaku']
    team6_kiroku8_output_kingaku=team6_kiroku8['output_kingaku']
    team6_kiroku9_output_kingaku=team6_kiroku9['output_kingaku']
    team6_kiroku10_output_kingaku=team6_kiroku10['output_kingaku']
    team6_kiroku11_output_kingaku=team6_kiroku11['output_kingaku']
    team6_kiroku12_output_kingaku=team6_kiroku12['output_kingaku']




    g4=team6_kiroku1_output_kaizenteian
    g5=team6_kiroku2_output_kaizenteian
    g6=team6_kiroku3_output_kaizenteian
    g7=team6_kiroku4_output_kaizenteian
    g8=team6_kiroku5_output_kaizenteian
    g9=team6_kiroku6_output_kaizenteian
    g10=team6_kiroku7_output_kaizenteian
    g11=team6_kiroku8_output_kaizenteian
    g12=team6_kiroku9_output_kaizenteian
    g1=team6_kiroku10_output_kaizenteian
    g2=team6_kiroku11_output_kaizenteian
    g3=team6_kiroku12_output_kaizenteian

    g4a=team6_kiroku1_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g5a=team6_kiroku2_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g6a=team6_kiroku3_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g7a=team6_kiroku4_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g8a=team6_kiroku5_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g9a=team6_kiroku6_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g10a=team6_kiroku7_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g11a=team6_kiroku8_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g12a=team6_kiroku9_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g1a=team6_kiroku10_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g2a=team6_kiroku11_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu
    g3a=team6_kiroku12_output_kaizenteian/team_kaizen6_kijun_team_member_ninzuu


    g4a=round(g4a, 1)
    g5a=round(g5a, 1)
    g6a=round(g6a, 1)
    g7a=round(g7a, 1)
    g8a=round(g8a, 1)
    g9a=round(g9a, 1)
    g10a=round(g10a, 1)
    g11a=round(g11a, 1)
    g12a=round(g12a, 1)
    g1a=round(g1a, 1)
    g2a=round(g2a, 1)
    g3a=round(g3a, 1)







    nin=team_kaizen6_kijun_team_member_ninzuu
    mokuhyou=team_kaizen6_kijun_kaizen_teian_hituyou_maisuu
    zen_mokuhyou=team_kaizen6_kijun_team_member_ninzuu*team_kaizen6_kijun_kaizen_teian_hituyou_maisuu
    index='改善提案提出枚数'
    

    

    
    
    

    x = np.array([f'4月(平均{g4a})',f'5月(平均{g5a})',f'6月(平均{g6a})',f'7月(平均{g7a})',f'8月(平均{g8a})',f'9月(平均{g9a})',f'10月(平均{g10a})',f'11月(平均{g11a})',f'12月(平均{g12a})',f'1月(平均{g1a})',f'２月(平均{g2a})',f'３月(平均{g3a})'])
    y = np.array([g4,g5,g6,g7,g8,g9,g10,g11,g12,g1,g2,g3])

   
    x_position = np.arange(len(x))
    fig = plt.figure()
    fig,ax=plt.subplots(figsize=(18,9))
    
    ax.bar(x_position, y, tick_label=x)
    ax.axhline(y=zen_mokuhyou,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)
    plt.title(f'改善提案提出記録:チーム{team_kaizen6_kijun_team_name}({nin}人)',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'提出目標{zen_mokuhyou}枚以上【枚】',fontsize=23)
    fig.show()


def plt2svg_k6t():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_k6t(request):
    setplt_k6t()
    svg=plt2svg_k6t()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response




@login_required
def kaizen_zentai(request):
    team_kaizen1_kijun=team_kaizen1.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen1_kijun2=team_kaizen1_kijun[0]
    #チームネーム1    
    team_kaizen1_kijun_team_name=team_kaizen1_kijun2['team_name']
    #改善必要枚数
    team_kaizen1_kijun_kaizen_teian_hituyou_maisuu=team_kaizen1_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen1_kijun_nenkan_mokuhyou_kingaku=team_kaizen1_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen1_kijun_team_member_ninzuu=team_kaizen1_kijun2['team_member_ninzuu']

    team_kaizen2_kijun=team_kaizen2.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen2_kijun2=team_kaizen2_kijun[0]
    #チームネーム2    
    team_kaizen2_kijun_team_name=team_kaizen2_kijun2['team_name']
    #改善必要枚数
    team_kaizen2_kijun_kaizen_teian_hituyou_maisuu=team_kaizen2_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen2_kijun_nenkan_mokuhyou_kingaku=team_kaizen2_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen2_kijun_team_member_ninzuu=team_kaizen2_kijun2['team_member_ninzuu']

    team_kaizen3_kijun=team_kaizen3.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen3_kijun2=team_kaizen3_kijun[0]
    #チームネーム3    
    team_kaizen3_kijun_team_name=team_kaizen3_kijun2['team_name']
    #改善必要枚数
    team_kaizen3_kijun_kaizen_teian_hituyou_maisuu=team_kaizen3_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen3_kijun_nenkan_mokuhyou_kingaku=team_kaizen3_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen3_kijun_team_member_ninzuu=team_kaizen3_kijun2['team_member_ninzuu']

    team_kaizen4_kijun=team_kaizen4.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen4_kijun2=team_kaizen4_kijun[0]
    #チームネーム4    
    team_kaizen4_kijun_team_name=team_kaizen4_kijun2['team_name']
    #改善必要枚数
    team_kaizen4_kijun_kaizen_teian_hituyou_maisuu=team_kaizen4_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen4_kijun_nenkan_mokuhyou_kingaku=team_kaizen4_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen4_kijun_team_member_ninzuu=team_kaizen4_kijun2['team_member_ninzuu']

    team_kaizen5_kijun=team_kaizen5.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen5_kijun2=team_kaizen5_kijun[0]
    #チームネーム5    
    team_kaizen5_kijun_team_name=team_kaizen5_kijun2['team_name']
    #改善必要枚数
    team_kaizen5_kijun_kaizen_teian_hituyou_maisuu=team_kaizen5_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen5_kijun_nenkan_mokuhyou_kingaku=team_kaizen5_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen5_kijun_team_member_ninzuu=team_kaizen5_kijun2['team_member_ninzuu']

    team_kaizen6_kijun=team_kaizen6.objects.all().values('team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu')
    team_kaizen6_kijun2=team_kaizen6_kijun[0]
    #チームネーム6    
    team_kaizen6_kijun_team_name=team_kaizen6_kijun2['team_name']
    #改善必要枚数
    team_kaizen6_kijun_kaizen_teian_hituyou_maisuu=team_kaizen6_kijun2['kaizen_teian_hituyou_maisuu']
    #年間目標の金額
    team_kaizen6_kijun_nenkan_mokuhyou_kingaku=team_kaizen6_kijun2['nenkan_mokuhyou_kingaku']
    #チームメンバー人数
    team_kaizen6_kijun_team_member_ninzuu=team_kaizen6_kijun2['team_member_ninzuu']


    #チーム１
    team_kaizen1_kiroku2=team_kaizen1_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team1_kiroku1=team_kaizen1_kiroku2[0]
    team1_kiroku2=team_kaizen1_kiroku2[1]
    team1_kiroku3=team_kaizen1_kiroku2[2]
    team1_kiroku4=team_kaizen1_kiroku2[3]
    team1_kiroku5=team_kaizen1_kiroku2[4]
    team1_kiroku6=team_kaizen1_kiroku2[5]
    team1_kiroku7=team_kaizen1_kiroku2[6]
    team1_kiroku8=team_kaizen1_kiroku2[7]
    team1_kiroku9=team_kaizen1_kiroku2[8]
    team1_kiroku10=team_kaizen1_kiroku2[9]
    team1_kiroku11=team_kaizen1_kiroku2[10]
    team1_kiroku12=team_kaizen1_kiroku2[11]

    team1_kiroku1_output_kaizenteian=team1_kiroku1['output_kaizenteian']
    team1_kiroku2_output_kaizenteian=team1_kiroku2['output_kaizenteian']
    team1_kiroku3_output_kaizenteian=team1_kiroku3['output_kaizenteian']
    team1_kiroku4_output_kaizenteian=team1_kiroku4['output_kaizenteian']
    team1_kiroku5_output_kaizenteian=team1_kiroku5['output_kaizenteian']
    team1_kiroku6_output_kaizenteian=team1_kiroku6['output_kaizenteian']
    team1_kiroku7_output_kaizenteian=team1_kiroku7['output_kaizenteian']
    team1_kiroku8_output_kaizenteian=team1_kiroku8['output_kaizenteian']
    team1_kiroku9_output_kaizenteian=team1_kiroku9['output_kaizenteian']
    team1_kiroku10_output_kaizenteian=team1_kiroku10['output_kaizenteian']
    team1_kiroku11_output_kaizenteian=team1_kiroku11['output_kaizenteian']
    team1_kiroku12_output_kaizenteian=team1_kiroku12['output_kaizenteian']

    team1_kiroku1_output_kingaku=team1_kiroku1['output_kingaku']
    team1_kiroku2_output_kingaku=team1_kiroku2['output_kingaku']
    team1_kiroku3_output_kingaku=team1_kiroku3['output_kingaku']
    team1_kiroku4_output_kingaku=team1_kiroku4['output_kingaku']
    team1_kiroku5_output_kingaku=team1_kiroku5['output_kingaku']
    team1_kiroku6_output_kingaku=team1_kiroku6['output_kingaku']
    team1_kiroku7_output_kingaku=team1_kiroku7['output_kingaku']
    team1_kiroku8_output_kingaku=team1_kiroku8['output_kingaku']
    team1_kiroku9_output_kingaku=team1_kiroku9['output_kingaku']
    team1_kiroku10_output_kingaku=team1_kiroku10['output_kingaku']
    team1_kiroku11_output_kingaku=team1_kiroku11['output_kingaku']
    team1_kiroku12_output_kingaku=team1_kiroku12['output_kingaku']



    #チーム2
    team_kaizen2_kiroku2=team_kaizen2_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team2_kiroku1=team_kaizen2_kiroku2[0]
    team2_kiroku2=team_kaizen2_kiroku2[1]
    team2_kiroku3=team_kaizen2_kiroku2[2]
    team2_kiroku4=team_kaizen2_kiroku2[3]
    team2_kiroku5=team_kaizen2_kiroku2[4]
    team2_kiroku6=team_kaizen2_kiroku2[5]
    team2_kiroku7=team_kaizen2_kiroku2[6]
    team2_kiroku8=team_kaizen2_kiroku2[7]
    team2_kiroku9=team_kaizen2_kiroku2[8]
    team2_kiroku10=team_kaizen2_kiroku2[9]
    team2_kiroku11=team_kaizen2_kiroku2[10]
    team2_kiroku12=team_kaizen2_kiroku2[11]

    team2_kiroku1_output_kaizenteian=team2_kiroku1['output_kaizenteian']
    team2_kiroku2_output_kaizenteian=team2_kiroku2['output_kaizenteian']
    team2_kiroku3_output_kaizenteian=team2_kiroku3['output_kaizenteian']
    team2_kiroku4_output_kaizenteian=team2_kiroku4['output_kaizenteian']
    team2_kiroku5_output_kaizenteian=team2_kiroku5['output_kaizenteian']
    team2_kiroku6_output_kaizenteian=team2_kiroku6['output_kaizenteian']
    team2_kiroku7_output_kaizenteian=team2_kiroku7['output_kaizenteian']
    team2_kiroku8_output_kaizenteian=team2_kiroku8['output_kaizenteian']
    team2_kiroku9_output_kaizenteian=team2_kiroku9['output_kaizenteian']
    team2_kiroku10_output_kaizenteian=team2_kiroku10['output_kaizenteian']
    team2_kiroku11_output_kaizenteian=team2_kiroku11['output_kaizenteian']
    team2_kiroku12_output_kaizenteian=team2_kiroku12['output_kaizenteian']

    team2_kiroku1_output_kingaku=team2_kiroku1['output_kingaku']
    team2_kiroku2_output_kingaku=team2_kiroku2['output_kingaku']
    team2_kiroku3_output_kingaku=team2_kiroku3['output_kingaku']
    team2_kiroku4_output_kingaku=team2_kiroku4['output_kingaku']
    team2_kiroku5_output_kingaku=team2_kiroku5['output_kingaku']
    team2_kiroku6_output_kingaku=team2_kiroku6['output_kingaku']
    team2_kiroku7_output_kingaku=team2_kiroku7['output_kingaku']
    team2_kiroku8_output_kingaku=team2_kiroku8['output_kingaku']
    team2_kiroku9_output_kingaku=team2_kiroku9['output_kingaku']
    team2_kiroku10_output_kingaku=team2_kiroku10['output_kingaku']
    team2_kiroku11_output_kingaku=team2_kiroku11['output_kingaku']
    team2_kiroku12_output_kingaku=team2_kiroku12['output_kingaku']




    #チーム3
    team_kaizen3_kiroku2=team_kaizen3_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team3_kiroku1=team_kaizen3_kiroku2[0]
    team3_kiroku2=team_kaizen3_kiroku2[1]
    team3_kiroku3=team_kaizen3_kiroku2[2]
    team3_kiroku4=team_kaizen3_kiroku2[3]
    team3_kiroku5=team_kaizen3_kiroku2[4]
    team3_kiroku6=team_kaizen3_kiroku2[5]
    team3_kiroku7=team_kaizen3_kiroku2[6]
    team3_kiroku8=team_kaizen3_kiroku2[7]
    team3_kiroku9=team_kaizen3_kiroku2[8]
    team3_kiroku10=team_kaizen3_kiroku2[9]
    team3_kiroku11=team_kaizen3_kiroku2[10]
    team3_kiroku12=team_kaizen3_kiroku2[11]

    team3_kiroku1_output_kaizenteian=team3_kiroku1['output_kaizenteian']
    team3_kiroku2_output_kaizenteian=team3_kiroku2['output_kaizenteian']
    team3_kiroku3_output_kaizenteian=team3_kiroku3['output_kaizenteian']
    team3_kiroku4_output_kaizenteian=team3_kiroku4['output_kaizenteian']
    team3_kiroku5_output_kaizenteian=team3_kiroku5['output_kaizenteian']
    team3_kiroku6_output_kaizenteian=team3_kiroku6['output_kaizenteian']
    team3_kiroku7_output_kaizenteian=team3_kiroku7['output_kaizenteian']
    team3_kiroku8_output_kaizenteian=team3_kiroku8['output_kaizenteian']
    team3_kiroku9_output_kaizenteian=team3_kiroku9['output_kaizenteian']
    team3_kiroku10_output_kaizenteian=team3_kiroku10['output_kaizenteian']
    team3_kiroku11_output_kaizenteian=team3_kiroku11['output_kaizenteian']
    team3_kiroku12_output_kaizenteian=team3_kiroku12['output_kaizenteian']

    team3_kiroku1_output_kingaku=team3_kiroku1['output_kingaku']
    team3_kiroku2_output_kingaku=team3_kiroku2['output_kingaku']
    team3_kiroku3_output_kingaku=team3_kiroku3['output_kingaku']
    team3_kiroku4_output_kingaku=team3_kiroku4['output_kingaku']
    team3_kiroku5_output_kingaku=team3_kiroku5['output_kingaku']
    team3_kiroku6_output_kingaku=team3_kiroku6['output_kingaku']
    team3_kiroku7_output_kingaku=team3_kiroku7['output_kingaku']
    team3_kiroku8_output_kingaku=team3_kiroku8['output_kingaku']
    team3_kiroku9_output_kingaku=team3_kiroku9['output_kingaku']
    team3_kiroku10_output_kingaku=team3_kiroku10['output_kingaku']
    team3_kiroku11_output_kingaku=team3_kiroku11['output_kingaku']
    team3_kiroku12_output_kingaku=team3_kiroku12['output_kingaku']




    #チーム4
    team_kaizen4_kiroku2=team_kaizen4_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team4_kiroku1=team_kaizen4_kiroku2[0]
    team4_kiroku2=team_kaizen4_kiroku2[1]
    team4_kiroku3=team_kaizen4_kiroku2[2]
    team4_kiroku4=team_kaizen4_kiroku2[3]
    team4_kiroku5=team_kaizen4_kiroku2[4]
    team4_kiroku6=team_kaizen4_kiroku2[5]
    team4_kiroku7=team_kaizen4_kiroku2[6]
    team4_kiroku8=team_kaizen4_kiroku2[7]
    team4_kiroku9=team_kaizen4_kiroku2[8]
    team4_kiroku10=team_kaizen4_kiroku2[9]
    team4_kiroku11=team_kaizen4_kiroku2[10]
    team4_kiroku12=team_kaizen4_kiroku2[11]

    team4_kiroku1_output_kaizenteian=team4_kiroku1['output_kaizenteian']
    team4_kiroku2_output_kaizenteian=team4_kiroku2['output_kaizenteian']
    team4_kiroku3_output_kaizenteian=team4_kiroku3['output_kaizenteian']
    team4_kiroku4_output_kaizenteian=team4_kiroku4['output_kaizenteian']
    team4_kiroku5_output_kaizenteian=team4_kiroku5['output_kaizenteian']
    team4_kiroku6_output_kaizenteian=team4_kiroku6['output_kaizenteian']
    team4_kiroku7_output_kaizenteian=team4_kiroku7['output_kaizenteian']
    team4_kiroku8_output_kaizenteian=team4_kiroku8['output_kaizenteian']
    team4_kiroku9_output_kaizenteian=team4_kiroku9['output_kaizenteian']
    team4_kiroku10_output_kaizenteian=team4_kiroku10['output_kaizenteian']
    team4_kiroku11_output_kaizenteian=team4_kiroku11['output_kaizenteian']
    team4_kiroku12_output_kaizenteian=team4_kiroku12['output_kaizenteian']

    team4_kiroku1_output_kingaku=team4_kiroku1['output_kingaku']
    team4_kiroku2_output_kingaku=team4_kiroku2['output_kingaku']
    team4_kiroku3_output_kingaku=team4_kiroku3['output_kingaku']
    team4_kiroku4_output_kingaku=team4_kiroku4['output_kingaku']
    team4_kiroku5_output_kingaku=team4_kiroku5['output_kingaku']
    team4_kiroku6_output_kingaku=team4_kiroku6['output_kingaku']
    team4_kiroku7_output_kingaku=team4_kiroku7['output_kingaku']
    team4_kiroku8_output_kingaku=team4_kiroku8['output_kingaku']
    team4_kiroku9_output_kingaku=team4_kiroku9['output_kingaku']
    team4_kiroku10_output_kingaku=team4_kiroku10['output_kingaku']
    team4_kiroku11_output_kingaku=team4_kiroku11['output_kingaku']
    team4_kiroku12_output_kingaku=team4_kiroku12['output_kingaku']




    #チーム5
    team_kaizen5_kiroku2=team_kaizen5_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team5_kiroku1=team_kaizen5_kiroku2[0]
    team5_kiroku2=team_kaizen5_kiroku2[1]
    team5_kiroku3=team_kaizen5_kiroku2[2]
    team5_kiroku4=team_kaizen5_kiroku2[3]
    team5_kiroku5=team_kaizen5_kiroku2[4]
    team5_kiroku6=team_kaizen5_kiroku2[5]
    team5_kiroku7=team_kaizen5_kiroku2[6]
    team5_kiroku8=team_kaizen5_kiroku2[7]
    team5_kiroku9=team_kaizen5_kiroku2[8]
    team5_kiroku10=team_kaizen5_kiroku2[9]
    team5_kiroku11=team_kaizen5_kiroku2[10]
    team5_kiroku12=team_kaizen5_kiroku2[11]

    team5_kiroku1_output_kaizenteian=team5_kiroku1['output_kaizenteian']
    team5_kiroku2_output_kaizenteian=team5_kiroku2['output_kaizenteian']
    team5_kiroku3_output_kaizenteian=team5_kiroku3['output_kaizenteian']
    team5_kiroku4_output_kaizenteian=team5_kiroku4['output_kaizenteian']
    team5_kiroku5_output_kaizenteian=team5_kiroku5['output_kaizenteian']
    team5_kiroku6_output_kaizenteian=team5_kiroku6['output_kaizenteian']
    team5_kiroku7_output_kaizenteian=team5_kiroku7['output_kaizenteian']
    team5_kiroku8_output_kaizenteian=team5_kiroku8['output_kaizenteian']
    team5_kiroku9_output_kaizenteian=team5_kiroku9['output_kaizenteian']
    team5_kiroku10_output_kaizenteian=team5_kiroku10['output_kaizenteian']
    team5_kiroku11_output_kaizenteian=team5_kiroku11['output_kaizenteian']
    team5_kiroku12_output_kaizenteian=team5_kiroku12['output_kaizenteian']

    team5_kiroku1_output_kingaku=team5_kiroku1['output_kingaku']
    team5_kiroku2_output_kingaku=team5_kiroku2['output_kingaku']
    team5_kiroku3_output_kingaku=team5_kiroku3['output_kingaku']
    team5_kiroku4_output_kingaku=team5_kiroku4['output_kingaku']
    team5_kiroku5_output_kingaku=team5_kiroku5['output_kingaku']
    team5_kiroku6_output_kingaku=team5_kiroku6['output_kingaku']
    team5_kiroku7_output_kingaku=team5_kiroku7['output_kingaku']
    team5_kiroku8_output_kingaku=team5_kiroku8['output_kingaku']
    team5_kiroku9_output_kingaku=team5_kiroku9['output_kingaku']
    team5_kiroku10_output_kingaku=team5_kiroku10['output_kingaku']
    team5_kiroku11_output_kingaku=team5_kiroku11['output_kingaku']
    team5_kiroku12_output_kingaku=team5_kiroku12['output_kingaku']




    #チーム6
    team_kaizen6_kiroku2=team_kaizen6_kiroku.objects.all().values('output_kaizenteian','output_kingaku')
    team6_kiroku1=team_kaizen6_kiroku2[0]
    team6_kiroku2=team_kaizen6_kiroku2[1]
    team6_kiroku3=team_kaizen6_kiroku2[2]
    team6_kiroku4=team_kaizen6_kiroku2[3]
    team6_kiroku5=team_kaizen6_kiroku2[4]
    team6_kiroku6=team_kaizen6_kiroku2[5]
    team6_kiroku7=team_kaizen6_kiroku2[6]
    team6_kiroku8=team_kaizen6_kiroku2[7]
    team6_kiroku9=team_kaizen6_kiroku2[8]
    team6_kiroku10=team_kaizen6_kiroku2[9]
    team6_kiroku11=team_kaizen6_kiroku2[10]
    team6_kiroku12=team_kaizen6_kiroku2[11]

    team6_kiroku1_output_kaizenteian=team6_kiroku1['output_kaizenteian']
    team6_kiroku2_output_kaizenteian=team6_kiroku2['output_kaizenteian']
    team6_kiroku3_output_kaizenteian=team6_kiroku3['output_kaizenteian']
    team6_kiroku4_output_kaizenteian=team6_kiroku4['output_kaizenteian']
    team6_kiroku5_output_kaizenteian=team6_kiroku5['output_kaizenteian']
    team6_kiroku6_output_kaizenteian=team6_kiroku6['output_kaizenteian']
    team6_kiroku7_output_kaizenteian=team6_kiroku7['output_kaizenteian']
    team6_kiroku8_output_kaizenteian=team6_kiroku8['output_kaizenteian']
    team6_kiroku9_output_kaizenteian=team6_kiroku9['output_kaizenteian']
    team6_kiroku10_output_kaizenteian=team6_kiroku10['output_kaizenteian']
    team6_kiroku11_output_kaizenteian=team6_kiroku11['output_kaizenteian']
    team6_kiroku12_output_kaizenteian=team6_kiroku12['output_kaizenteian']

    team6_kiroku1_output_kingaku=team6_kiroku1['output_kingaku']
    team6_kiroku2_output_kingaku=team6_kiroku2['output_kingaku']
    team6_kiroku3_output_kingaku=team6_kiroku3['output_kingaku']
    team6_kiroku4_output_kingaku=team6_kiroku4['output_kingaku']
    team6_kiroku5_output_kingaku=team6_kiroku5['output_kingaku']
    team6_kiroku6_output_kingaku=team6_kiroku6['output_kingaku']
    team6_kiroku7_output_kingaku=team6_kiroku7['output_kingaku']
    team6_kiroku8_output_kingaku=team6_kiroku8['output_kingaku']
    team6_kiroku9_output_kingaku=team6_kiroku9['output_kingaku']
    team6_kiroku10_output_kingaku=team6_kiroku10['output_kingaku']
    team6_kiroku11_output_kingaku=team6_kiroku11['output_kingaku']
    team6_kiroku12_output_kingaku=team6_kiroku12['output_kingaku']

    params={
        'title':'改善提案/合理化 JFC・受託加工製造部　愛知',
        'message1':'▼チーム成果を記入してください▼',
        'team_kaizen1_kijun_team_name':team_kaizen1_kijun_team_name,
        'team_kaizen2_kijun_team_name':team_kaizen2_kijun_team_name,
        'team_kaizen3_kijun_team_name':team_kaizen3_kijun_team_name,
        'team_kaizen4_kijun_team_name':team_kaizen4_kijun_team_name,
        'team_kaizen5_kijun_team_name':team_kaizen5_kijun_team_name,
        'team_kaizen6_kijun_team_name':team_kaizen6_kijun_team_name,

        
    }
    
    return render(request,'kaizen/kaizen_zentai.html',params)
