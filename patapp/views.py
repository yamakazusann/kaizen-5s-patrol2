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
team_name_ch=team.objects.all()
team_all=team.objects.all().values('team_name')
team_all_1=team_all[0]
team_all_2=team_all[1]
team_all_3=team_all[2]
team_all_4=team_all[3]
team_all_5=team_all[4]
team_all_6=team_all[5]

team_all_1z=team_all_1['team_name']
team_all_2z=team_all_2['team_name']
team_all_3z=team_all_3['team_name']
team_all_4z=team_all_4['team_name']
team_all_5z=team_all_5['team_name']
team_all_6z=team_all_6['team_name']
    
@login_required
def goukakuten_change(request):
    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    goukakuten_tuki_1z=goukakuten1['tuki']
    goukakuten_tuki_2z=goukakuten2['tuki']
    goukakuten_tuki_3z=goukakuten3['tuki']
    goukakuten_tuki_4z=goukakuten4['tuki']
    goukakuten_tuki_5z=goukakuten5['tuki']
    goukakuten_tuki_6z=goukakuten6['tuki']
    goukakuten_tuki_7z=goukakuten7['tuki']
    goukakuten_tuki_8z=goukakuten8['tuki']
    goukakuten_tuki_9z=goukakuten9['tuki']
    goukakuten_tuki_10z=goukakuten10['tuki']
    goukakuten_tuki_11z=goukakuten11['tuki']
    goukakuten_tuki_12z=goukakuten12['tuki']

    





    params={
        'title':'合格点変更',
        'message':'合格点が更新した場合は変更を押して記入してください',
        'goukakuten_all':goukakuten_all,
        'goukakuten_tuki_1z':goukakuten_tuki_1z,
        'goukakuten_tuki_2z':goukakuten_tuki_2z,
        'goukakuten_tuki_3z':goukakuten_tuki_3z,
        'goukakuten_tuki_4z':goukakuten_tuki_4z,
        'goukakuten_tuki_5z':goukakuten_tuki_5z,
        'goukakuten_tuki_6z':goukakuten_tuki_6z,
        'goukakuten_tuki_7z':goukakuten_tuki_7z,
        'goukakuten_tuki_8z':goukakuten_tuki_8z,
        'goukakuten_tuki_9z':goukakuten_tuki_9z,
        'goukakuten_tuki_10z':goukakuten_tuki_10z,
        'goukakuten_tuki_11z':goukakuten_tuki_11z,
        'goukakuten_tuki_12z':goukakuten_tuki_12z,

        'goukakuten_all_1z':goukakuten_all_1z,
        'goukakuten_all_2z':goukakuten_all_2z,
        'goukakuten_all_3z':goukakuten_all_3z,
        'goukakuten_all_4z':goukakuten_all_4z,
        'goukakuten_all_5z':goukakuten_all_5z,
        'goukakuten_all_6z':goukakuten_all_6z,
        'goukakuten_all_7z':goukakuten_all_7z,
        'goukakuten_all_8z':goukakuten_all_8z,
        'goukakuten_all_9z':goukakuten_all_9z,
        'goukakuten_all_10z':goukakuten_all_10z,
        'goukakuten_all_11z':goukakuten_all_11z,
        'goukakuten_all_12z':goukakuten_all_12z,

        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,


    }
    
    return render(request,'patapp/goukakuten_change.html',params)


@login_required
def edit_goukakuten(request,num):
    obj=goukaku.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=goukakuForm(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/patrol/goukakuten_change')
    params={
        'title':'合格点を記入し直してください',
        'tuki':num,
        'form':goukakuForm(instance=obj),
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    return render(request,'patapp/edit_goukakuten.html',params)



@login_required
def team_name_change(request):
    team_name_ch=team.objects.all()
    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    
    params={
        'title':'チーム名変更',
        'message':'チーム名を変更した場合は変更を押して記入してください',
        'team_name_ch':team_name_ch,
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    
    return render(request,'patapp/team_name_change.html',params)


@login_required
def edit_name(request,num):
    obj=team.objects.get(id=num)
    if(request.method=='POST'):
        kaku=teamForm(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/patrol/team_name_change')
    params={
        'title':'チーム名を記入し直してください',
        'tuki':num,
        'form':teamForm(instance=obj),
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    return render(request,'patapp/edit_name.html',params)



@login_required
def zentai(request):
    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    data=kakutuki.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_1=data[0]
    data_2=data[1]
    data_3=data[2]
    data_4=data[3]
    data_5=data[4]
    data_6=data[5]
    data_7=data[6]
    data_8=data[7]
    data_9=data[8]
    data_10=data[9]
    data_11=data[10]
    data_12=data[11]

    data_a=kakutuki_a.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_a_1=data_a[0]
    data_a_2=data_a[1]
    data_a_3=data_a[2]
    data_a_4=data_a[3]
    data_a_5=data_a[4]
    data_a_6=data_a[5]
    data_a_7=data_a[6]
    data_a_8=data_a[7]
    data_a_9=data_a[8]
    data_a_10=data_a[9]
    data_a_11=data_a[10]
    data_a_12=data_a[11]

    data_b=kakutuki_b.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_b_1=data_b[0]
    data_b_2=data_b[1]
    data_b_3=data_b[2]
    data_b_4=data_b[3]
    data_b_5=data_b[4]
    data_b_6=data_b[5]
    data_b_7=data_b[6]
    data_b_8=data_b[7]
    data_b_9=data_b[8]
    data_b_10=data_b[9]
    data_b_11=data_b[10]
    data_b_12=data_b[11]

    data_c=kakutuki_c.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_c_1=data_c[0]
    data_c_2=data_c[1]
    data_c_3=data_c[2]
    data_c_4=data_c[3]
    data_c_5=data_c[4]
    data_c_6=data_c[5]
    data_c_7=data_c[6]
    data_c_8=data_c[7]
    data_c_9=data_c[8]
    data_c_10=data_c[9]
    data_c_11=data_c[10]
    data_c_12=data_c[11]

    data_d=kakutuki_d.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_d_1=data_d[0]
    data_d_2=data_d[1]
    data_d_3=data_d[2]
    data_d_4=data_d[3]
    data_d_5=data_d[4]
    data_d_6=data_d[5]
    data_d_7=data_d[6]
    data_d_8=data_d[7]
    data_d_9=data_d[8]
    data_d_10=data_d[9]
    data_d_11=data_d[10]
    data_d_12=data_d[11]
    
    data_e=kakutuki_e.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_e_1=data_e[0]
    data_e_2=data_e[1]
    data_e_3=data_e[2]
    data_e_4=data_e[3]
    data_e_5=data_e[4]
    data_e_6=data_e[5]
    data_e_7=data_e[6]
    data_e_8=data_e[7]
    data_e_9=data_e[8]
    data_e_10=data_e[9]
    data_e_11=data_e[10]
    data_e_12=data_e[11]




    team_a_1=data_1['seiri_in']+data_1['seiton_in']+data_1['seisou_in']+data_1['seiketu_in']+data_1['situke_in']
    team_a_2=data_2['seiri_in']+data_2['seiton_in']+data_2['seisou_in']+data_2['seiketu_in']+data_2['situke_in']
    team_a_3=data_3['seiri_in']+data_3['seiton_in']+data_3['seisou_in']+data_3['seiketu_in']+data_3['situke_in']
    team_a_4=data_4['seiri_in']+data_4['seiton_in']+data_4['seisou_in']+data_4['seiketu_in']+data_4['situke_in']
    team_a_5=data_5['seiri_in']+data_5['seiton_in']+data_5['seisou_in']+data_5['seiketu_in']+data_5['situke_in']
    team_a_6=data_6['seiri_in']+data_6['seiton_in']+data_6['seisou_in']+data_6['seiketu_in']+data_6['situke_in']
    team_a_7=data_7['seiri_in']+data_7['seiton_in']+data_7['seisou_in']+data_7['seiketu_in']+data_7['situke_in']
    team_a_8=data_8['seiri_in']+data_8['seiton_in']+data_8['seisou_in']+data_8['seiketu_in']+data_8['situke_in']
    team_a_9=data_9['seiri_in']+data_9['seiton_in']+data_9['seisou_in']+data_9['seiketu_in']+data_9['situke_in']
    team_a_10=data_10['seiri_in']+data_10['seiton_in']+data_10['seisou_in']+data_10['seiketu_in']+data_10['situke_in']
    team_a_11=data_11['seiri_in']+data_11['seiton_in']+data_11['seisou_in']+data_11['seiketu_in']+data_11['situke_in']
    team_a_12=data_12['seiri_in']+data_12['seiton_in']+data_12['seisou_in']+data_12['seiketu_in']+data_12['situke_in']

    team_b_1=data_a_1['seiri_in']+data_a_1['seiton_in']+data_a_1['seisou_in']+data_a_1['seiketu_in']+data_a_1['situke_in']
    team_b_2=data_a_2['seiri_in']+data_a_2['seiton_in']+data_a_2['seisou_in']+data_a_2['seiketu_in']+data_a_2['situke_in']
    team_b_3=data_a_3['seiri_in']+data_a_3['seiton_in']+data_a_3['seisou_in']+data_a_3['seiketu_in']+data_a_3['situke_in']
    team_b_4=data_a_4['seiri_in']+data_a_4['seiton_in']+data_a_4['seisou_in']+data_a_4['seiketu_in']+data_a_4['situke_in']
    team_b_5=data_a_5['seiri_in']+data_a_5['seiton_in']+data_a_5['seisou_in']+data_a_5['seiketu_in']+data_a_5['situke_in']
    team_b_6=data_a_6['seiri_in']+data_a_6['seiton_in']+data_a_6['seisou_in']+data_a_6['seiketu_in']+data_a_6['situke_in']
    team_b_7=data_a_7['seiri_in']+data_a_7['seiton_in']+data_a_7['seisou_in']+data_a_7['seiketu_in']+data_a_7['situke_in']
    team_b_8=data_a_8['seiri_in']+data_a_8['seiton_in']+data_a_8['seisou_in']+data_a_8['seiketu_in']+data_a_8['situke_in']
    team_b_9=data_a_9['seiri_in']+data_a_9['seiton_in']+data_a_9['seisou_in']+data_a_9['seiketu_in']+data_a_9['situke_in']
    team_b_10=data_a_10['seiri_in']+data_a_10['seiton_in']+data_a_10['seisou_in']+data_a_10['seiketu_in']+data_a_10['situke_in']
    team_b_11=data_a_11['seiri_in']+data_a_11['seiton_in']+data_a_11['seisou_in']+data_a_11['seiketu_in']+data_a_11['situke_in']
    team_b_12=data_a_12['seiri_in']+data_a_12['seiton_in']+data_a_12['seisou_in']+data_a_12['seiketu_in']+data_a_12['situke_in']

    team_c_1=data_b_1['seiri_in']+data_b_1['seiton_in']+data_b_1['seisou_in']+data_b_1['seiketu_in']+data_b_1['situke_in']
    team_c_2=data_b_2['seiri_in']+data_b_2['seiton_in']+data_b_2['seisou_in']+data_b_2['seiketu_in']+data_b_2['situke_in']
    team_c_3=data_b_3['seiri_in']+data_b_3['seiton_in']+data_b_3['seisou_in']+data_b_3['seiketu_in']+data_b_3['situke_in']
    team_c_4=data_b_4['seiri_in']+data_b_4['seiton_in']+data_b_4['seisou_in']+data_b_4['seiketu_in']+data_b_4['situke_in']
    team_c_5=data_b_5['seiri_in']+data_b_5['seiton_in']+data_b_5['seisou_in']+data_b_5['seiketu_in']+data_b_5['situke_in']
    team_c_6=data_b_6['seiri_in']+data_b_6['seiton_in']+data_b_6['seisou_in']+data_b_6['seiketu_in']+data_b_6['situke_in']
    team_c_7=data_b_7['seiri_in']+data_b_7['seiton_in']+data_b_7['seisou_in']+data_b_7['seiketu_in']+data_b_7['situke_in']
    team_c_8=data_b_8['seiri_in']+data_b_8['seiton_in']+data_b_8['seisou_in']+data_b_8['seiketu_in']+data_b_8['situke_in']
    team_c_9=data_b_9['seiri_in']+data_b_9['seiton_in']+data_b_9['seisou_in']+data_b_9['seiketu_in']+data_b_9['situke_in']
    team_c_10=data_b_10['seiri_in']+data_b_10['seiton_in']+data_b_10['seisou_in']+data_b_10['seiketu_in']+data_b_10['situke_in']
    team_c_11=data_b_11['seiri_in']+data_b_11['seiton_in']+data_b_11['seisou_in']+data_b_11['seiketu_in']+data_b_11['situke_in']
    team_c_12=data_b_12['seiri_in']+data_b_12['seiton_in']+data_b_12['seisou_in']+data_b_12['seiketu_in']+data_b_12['situke_in']

    team_d_1=data_c_1['seiri_in']+data_c_1['seiton_in']+data_c_1['seisou_in']+data_c_1['seiketu_in']+data_c_1['situke_in']
    team_d_2=data_c_2['seiri_in']+data_c_2['seiton_in']+data_c_2['seisou_in']+data_c_2['seiketu_in']+data_c_2['situke_in']
    team_d_3=data_c_3['seiri_in']+data_c_3['seiton_in']+data_c_3['seisou_in']+data_c_3['seiketu_in']+data_c_3['situke_in']
    team_d_4=data_c_4['seiri_in']+data_c_4['seiton_in']+data_c_4['seisou_in']+data_c_4['seiketu_in']+data_c_4['situke_in']
    team_d_5=data_c_5['seiri_in']+data_c_5['seiton_in']+data_c_5['seisou_in']+data_c_5['seiketu_in']+data_c_5['situke_in']
    team_d_6=data_c_6['seiri_in']+data_c_6['seiton_in']+data_c_6['seisou_in']+data_c_6['seiketu_in']+data_c_6['situke_in']
    team_d_7=data_c_7['seiri_in']+data_c_7['seiton_in']+data_c_7['seisou_in']+data_c_7['seiketu_in']+data_c_7['situke_in']
    team_d_8=data_c_8['seiri_in']+data_c_8['seiton_in']+data_c_8['seisou_in']+data_c_8['seiketu_in']+data_c_8['situke_in']
    team_d_9=data_c_9['seiri_in']+data_c_9['seiton_in']+data_c_9['seisou_in']+data_c_9['seiketu_in']+data_c_9['situke_in']
    team_d_10=data_c_10['seiri_in']+data_c_10['seiton_in']+data_c_10['seisou_in']+data_c_10['seiketu_in']+data_c_10['situke_in']
    team_d_11=data_c_11['seiri_in']+data_c_11['seiton_in']+data_c_11['seisou_in']+data_c_11['seiketu_in']+data_c_11['situke_in']
    team_d_12=data_c_12['seiri_in']+data_c_12['seiton_in']+data_c_12['seisou_in']+data_c_12['seiketu_in']+data_c_12['situke_in']

    team_e_1=data_d_1['seiri_in']+data_d_1['seiton_in']+data_d_1['seisou_in']+data_d_1['seiketu_in']+data_d_1['situke_in']
    team_e_2=data_d_2['seiri_in']+data_d_2['seiton_in']+data_d_2['seisou_in']+data_d_2['seiketu_in']+data_d_2['situke_in']
    team_e_3=data_d_3['seiri_in']+data_d_3['seiton_in']+data_d_3['seisou_in']+data_d_3['seiketu_in']+data_d_3['situke_in']
    team_e_4=data_d_4['seiri_in']+data_d_4['seiton_in']+data_d_4['seisou_in']+data_d_4['seiketu_in']+data_d_4['situke_in']
    team_e_5=data_d_5['seiri_in']+data_d_5['seiton_in']+data_d_5['seisou_in']+data_d_5['seiketu_in']+data_d_5['situke_in']
    team_e_6=data_d_6['seiri_in']+data_d_6['seiton_in']+data_d_6['seisou_in']+data_d_6['seiketu_in']+data_d_6['situke_in']
    team_e_7=data_d_7['seiri_in']+data_d_7['seiton_in']+data_d_7['seisou_in']+data_d_7['seiketu_in']+data_d_7['situke_in']
    team_e_8=data_d_8['seiri_in']+data_d_8['seiton_in']+data_d_8['seisou_in']+data_d_8['seiketu_in']+data_d_8['situke_in']
    team_e_9=data_d_9['seiri_in']+data_d_9['seiton_in']+data_d_9['seisou_in']+data_d_9['seiketu_in']+data_d_9['situke_in']
    team_e_10=data_d_10['seiri_in']+data_d_10['seiton_in']+data_d_10['seisou_in']+data_d_10['seiketu_in']+data_d_10['situke_in']
    team_e_11=data_d_11['seiri_in']+data_d_11['seiton_in']+data_d_11['seisou_in']+data_d_11['seiketu_in']+data_d_11['situke_in']
    team_e_12=data_d_12['seiri_in']+data_d_12['seiton_in']+data_d_12['seisou_in']+data_d_12['seiketu_in']+data_d_12['situke_in']

    team_f_1=data_e_1['seiri_in']+data_e_1['seiton_in']+data_e_1['seisou_in']+data_e_1['seiketu_in']+data_e_1['situke_in']
    team_f_2=data_e_2['seiri_in']+data_e_2['seiton_in']+data_e_2['seisou_in']+data_e_2['seiketu_in']+data_e_2['situke_in']
    team_f_3=data_e_3['seiri_in']+data_e_3['seiton_in']+data_e_3['seisou_in']+data_e_3['seiketu_in']+data_e_3['situke_in']
    team_f_4=data_e_4['seiri_in']+data_e_4['seiton_in']+data_e_4['seisou_in']+data_e_4['seiketu_in']+data_e_4['situke_in']
    team_f_5=data_e_5['seiri_in']+data_e_5['seiton_in']+data_e_5['seisou_in']+data_e_5['seiketu_in']+data_e_5['situke_in']
    team_f_6=data_e_6['seiri_in']+data_e_6['seiton_in']+data_e_6['seisou_in']+data_e_6['seiketu_in']+data_e_6['situke_in']
    team_f_7=data_e_7['seiri_in']+data_e_7['seiton_in']+data_e_7['seisou_in']+data_e_7['seiketu_in']+data_e_7['situke_in']
    team_f_8=data_e_8['seiri_in']+data_e_8['seiton_in']+data_e_8['seisou_in']+data_e_8['seiketu_in']+data_e_8['situke_in']
    team_f_9=data_e_9['seiri_in']+data_e_9['seiton_in']+data_e_9['seisou_in']+data_e_9['seiketu_in']+data_e_9['situke_in']
    team_f_10=data_e_10['seiri_in']+data_e_10['seiton_in']+data_e_10['seisou_in']+data_e_10['seiketu_in']+data_e_10['situke_in']
    team_f_11=data_e_11['seiri_in']+data_e_11['seiton_in']+data_e_11['seisou_in']+data_e_11['seiketu_in']+data_e_11['situke_in']
    team_f_12=data_e_12['seiri_in']+data_e_12['seiton_in']+data_e_12['seisou_in']+data_e_12['seiketu_in']+data_e_12['situke_in']


    

    


    team_a_len=[team_a_1,team_a_2,team_a_3,team_a_4,team_a_5,team_a_6,team_a_7,team_a_8,team_a_9,team_a_10,team_a_11,team_a_12]
    team_b_len=[team_b_1,team_b_2,team_b_3,team_b_4,team_b_5,team_b_6,team_b_7,team_b_8,team_b_9,team_b_10,team_b_11,team_b_12]
    team_c_len=[team_c_1,team_c_2,team_c_3,team_c_4,team_c_5,team_c_6,team_c_7,team_c_8,team_c_9,team_c_10,team_c_11,team_c_12]
    team_d_len=[team_d_1,team_d_2,team_d_3,team_d_4,team_d_5,team_d_6,team_d_7,team_d_8,team_d_9,team_d_10,team_d_11,team_d_12]
    team_e_len=[team_e_1,team_e_2,team_e_3,team_e_4,team_e_5,team_e_6,team_e_7,team_e_8,team_e_9,team_e_10,team_e_11,team_e_12]
    team_f_len=[team_f_1,team_f_2,team_f_3,team_f_4,team_f_5,team_f_6,team_f_7,team_f_8,team_f_9,team_f_10,team_f_11,team_f_12]

    team_a_len_2=[ai for ai in team_a_len if ai > 0]
    team_b_len_2=[bi for bi in team_b_len if bi > 0]
    team_c_len_2=[ci for ci in team_c_len if ci > 0]
    team_d_len_2=[di for di in team_d_len if di > 0]
    team_e_len_2=[ei for ei in team_e_len if ei > 0]
    team_f_len_2=[fi for fi in team_f_len if fi > 0]

    team_a_len_3=len(team_a_len_2)
    if team_a_len_3 == 0:
        team_a_len_3=1

    team_b_len_3=len(team_b_len_2)
    if team_b_len_3 == 0:
        team_b_len_3=1

    team_c_len_3=len(team_c_len_2)
    if team_c_len_3 == 0:
        team_c_len_3=1

    team_d_len_3=len(team_d_len_2)
    if team_d_len_3 == 0:
        team_d_len_3=1

    team_e_len_3=len(team_e_len_2)
    if team_e_len_3 == 0:
        team_e_len_3=1
    
    team_f_len_3=len(team_f_len_2)
    if team_f_len_3 == 0:
        team_f_len_3=1

    #チーム名順の年度平均
    team_score_ave_1=int(team_a_1+team_a_2+team_a_3+team_a_4+team_a_5+team_a_6+team_a_7+team_a_8+team_a_9+team_a_10+team_a_11+team_a_12)/team_a_len_3
    team_score_ave_2=int(team_b_1+team_b_2+team_b_3+team_b_4+team_b_5+team_b_6+team_b_7+team_b_8+team_b_9+team_b_10+team_b_11+team_b_12)/team_b_len_3
    team_score_ave_3=int(team_c_1+team_c_2+team_c_3+team_c_4+team_c_5+team_c_6+team_c_7+team_c_8+team_c_9+team_c_10+team_c_11+team_c_12)/team_c_len_3
    team_score_ave_4=int(team_d_1+team_d_2+team_d_3+team_d_4+team_d_5+team_d_6+team_d_7+team_d_8+team_d_9+team_d_10+team_d_11+team_d_12)/team_d_len_3
    team_score_ave_5=int(team_e_1+team_e_2+team_e_3+team_e_4+team_e_5+team_e_6+team_e_7+team_e_8+team_e_9+team_e_10+team_e_11+team_e_12)/team_e_len_3
    team_score_ave_6=int(team_f_1+team_f_2+team_f_3+team_f_4+team_f_5+team_f_6+team_f_7+team_f_8+team_f_9+team_f_10+team_f_11+team_f_12)/team_f_len_3
    



    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']
    params={
        'title':'５sパトロール JFC・受託加工製造部　愛知',
        'message':'▼チーム別データの記入はこちらから▼',
        'message_2':'▼全データとデータ推移の確認はこちらから▼',
        'message_3':'▼チーム名と合格基準点を変更したい時はこちらから▼',
        'message_4':f'【JFC・受託加工製造部（愛知加工課/第一,第二）】{ten}以上で合格！{nen}年{now.month}月{now.day}日現在',
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,

        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
        'team_a_1':team_a_1,
        'team_a_2':team_a_2,
        'team_a_3':team_a_3,
        'team_a_4':team_a_4,
        'team_a_5':team_a_5,
        'team_a_6':team_a_6,
        'team_a_7':team_a_7,
        'team_a_8':team_a_8,
        'team_a_9':team_a_9,
        'team_a_10':team_a_10,
        'team_a_11':team_a_11,
        'team_a_12':team_a_12,

        'team_b_1':team_b_1,
        'team_b_2':team_b_2,
        'team_b_3':team_b_3,
        'team_b_4':team_b_4,
        'team_b_5':team_b_5,
        'team_b_6':team_b_6,
        'team_b_7':team_b_7,
        'team_b_8':team_b_8,
        'team_b_9':team_b_9,
        'team_b_10':team_b_10,
        'team_b_11':team_b_11,
        'team_b_12':team_b_12,

        'team_c_1':team_c_1,
        'team_c_2':team_c_2,
        'team_c_3':team_c_3,
        'team_c_4':team_c_4,
        'team_c_5':team_c_5,
        'team_c_6':team_c_6,
        'team_c_7':team_c_7,
        'team_c_8':team_c_8,
        'team_c_9':team_c_9,
        'team_c_10':team_c_10,
        'team_c_11':team_c_11,
        'team_c_12':team_c_12,

        'team_d_1':team_d_1,
        'team_d_2':team_d_2,
        'team_d_3':team_d_3,
        'team_d_4':team_d_4,
        'team_d_5':team_d_5,
        'team_d_6':team_d_6,
        'team_d_7':team_d_7,
        'team_d_8':team_d_8,
        'team_d_9':team_d_9,
        'team_d_10':team_d_10,
        'team_d_11':team_d_11,
        'team_d_12':team_d_12,

        'team_e_1':team_e_1,
        'team_e_2':team_e_2,
        'team_e_3':team_e_3,
        'team_e_4':team_e_4,
        'team_e_5':team_e_5,
        'team_e_6':team_e_6,
        'team_e_7':team_e_7,
        'team_e_8':team_e_8,
        'team_e_9':team_e_9,
        'team_e_10':team_e_10,
        'team_e_11':team_e_11,
        'team_e_12':team_e_12,

        'team_f_1':team_f_1,
        'team_f_2':team_f_2,
        'team_f_3':team_f_3,
        'team_f_4':team_f_4,
        'team_f_5':team_f_5,
        'team_f_6':team_f_6,
        'team_f_7':team_f_7,
        'team_f_8':team_f_8,
        'team_f_9':team_f_9,
        'team_f_10':team_f_10,
        'team_f_11':team_f_11,
        'team_f_12':team_f_12,

        'team_score_ave_1':team_score_ave_1,
        'team_score_ave_2':team_score_ave_2,
        'team_score_ave_3':team_score_ave_3,
        'team_score_ave_4':team_score_ave_4,
        'team_score_ave_5':team_score_ave_5,
        'team_score_ave_6':team_score_ave_6,

        
    }
    
    return render(request,'patapp/zentai.html',params)



@login_required
def index(request):
    data=kakutuki.objects.all()
    data1=kakutuki.objects.all().values('seiri_in','seiton_in','seisou_in','seiketu_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]
    




    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']
    
        
    
    params={
        'title':'５sパトロール結果',
        'message':'毎月の点数を数値変更を押して記入してください',
        'data':data,
        'data2_1':data2_1,
        'data2_2':data2_2,
        'data2_3':data2_3,
        'data2_4':data2_4,
        'data2_5':data2_5,
        'data2_6':data2_6,
        'data2_7':data2_7,
        'data2_8':data2_8,
        'data2_9':data2_9,
        'data2_10':data2_10,
        'data2_11':data2_11,
        'data2_12':data2_12,
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    
    return render(request,'patapp/index.html',params)


@login_required
def index_a(request):
    data=kakutuki_a.objects.all()
    data1=kakutuki_a.objects.all().values('seiri_in','seiton_in','seisou_in','seiketu_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']
    
    params={
        'title':'５sパトロール結果',
        'message':'毎月の点数を数値変更を押して記入してください',
        'data':data,
        'data2_1':data2_1,
        'data2_2':data2_2,
        'data2_3':data2_3,
        'data2_4':data2_4,
        'data2_5':data2_5,
        'data2_6':data2_6,
        'data2_7':data2_7,
        'data2_8':data2_8,
        'data2_9':data2_9,
        'data2_10':data2_10,
        'data2_11':data2_11,
        'data2_12':data2_12,
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    
    return render(request,'patapp/index_a.html',params)

@login_required
def index_b(request):
    data=kakutuki_b.objects.all()
    data1=kakutuki_b.objects.all().values('seiri_in','seiton_in','seisou_in','seiketu_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    
    params={
        'title':'５sパトロール結果',
        'message':'毎月の点数を数値変更を押して記入してください',
        'data':data,
        'data2_1':data2_1,
        'data2_2':data2_2,
        'data2_3':data2_3,
        'data2_4':data2_4,
        'data2_5':data2_5,
        'data2_6':data2_6,
        'data2_7':data2_7,
        'data2_8':data2_8,
        'data2_9':data2_9,
        'data2_10':data2_10,
        'data2_11':data2_11,
        'data2_12':data2_12,
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    
    return render(request,'patapp/index_b.html',params)

@login_required
def index_c(request):
    data=kakutuki_c.objects.all()
    data1=kakutuki_c.objects.all().values('seiri_in','seiton_in','seisou_in','seiketu_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    
    params={
        'title':'５sパトロール結果',
        'message':'毎月の点数を数値変更を押して記入してください',
        'data':data,
        'data2_1':data2_1,
        'data2_2':data2_2,
        'data2_3':data2_3,
        'data2_4':data2_4,
        'data2_5':data2_5,
        'data2_6':data2_6,
        'data2_7':data2_7,
        'data2_8':data2_8,
        'data2_9':data2_9,
        'data2_10':data2_10,
        'data2_11':data2_11,
        'data2_12':data2_12,
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    
    return render(request,'patapp/index_c.html',params)

@login_required
def index_d(request):
    data=kakutuki_d.objects.all()
    data1=kakutuki_d.objects.all().values('seiri_in','seiton_in','seisou_in','seiketu_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    
    params={
        'title':'５sパトロール結果',
        'message':'毎月の点数を数値変更を押して記入してください',
        'data':data,
        'data2_1':data2_1,
        'data2_2':data2_2,
        'data2_3':data2_3,
        'data2_4':data2_4,
        'data2_5':data2_5,
        'data2_6':data2_6,
        'data2_7':data2_7,
        'data2_8':data2_8,
        'data2_9':data2_9,
        'data2_10':data2_10,
        'data2_11':data2_11,
        'data2_12':data2_12,
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    
    return render(request,'patapp/index_d.html',params)

@login_required
def index_e(request):
    data=kakutuki_e.objects.all()
    data1=kakutuki_e.objects.all().values('seiri_in','seiton_in','seisou_in','seiketu_in','situke_in','total_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    
    params={
        'title':'５sパトロール結果',
        'message':'毎月の点数を数値変更を押して記入してください',
        'data':data,
        'data2_1':data2_1,
        'data2_2':data2_2,
        'data2_3':data2_3,
        'data2_4':data2_4,
        'data2_5':data2_5,
        'data2_6':data2_6,
        'data2_7':data2_7,
        'data2_8':data2_8,
        'data2_9':data2_9,
        'data2_10':data2_10,
        'data2_11':data2_11,
        'data2_12':data2_12,
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    
    return render(request,'patapp/index_e.html',params)

@login_required
def edit(request,num):
    obj=kakutuki.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=kakutukiForm(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/patrol/index')
    params={
        'title':'半角数字0~20で点数を記入してください',
        'tuki':num,
        'form':kakutukiForm(instance=obj),
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    return render(request,'patapp/edit.html',params)

@login_required
def edit_a(request,num):
    obj=kakutuki_a.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=kakutukiForm_a(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/patrol/index_a')
    params={
        'title':'半角数字0~20で点数を記入してください',
        'tuki':num,
        'form':kakutukiForm_a(instance=obj),
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    return render(request,'patapp/edit_a.html',params)

@login_required
def edit_b(request,num):
    obj=kakutuki_b.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=kakutukiForm_b(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/patrol/index_b')
    params={
        'title':'半角数字0~20で点数を記入してください',
        'tuki':num,
        'form':kakutukiForm_b(instance=obj),
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    return render(request,'patapp/edit_b.html',params)

@login_required
def edit_c(request,num):
    obj=kakutuki_c.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=kakutukiForm_c(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/patrol/index_c')
    params={
        'title':'半角数字0~20で点数を記入してください',
        'tuki':num,
        'form':kakutukiForm_c(instance=obj),
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    return render(request,'patapp/edit_c.html',params)

@login_required
def edit_d(request,num):
    obj=kakutuki_d.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=kakutukiForm_d(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/patrol/index_d')
    params={
        'title':'半角数字0~20で点数を記入してください',
        'tuki':num,
        'form':kakutukiForm_d(instance=obj),
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }
    return render(request,'patapp/edit_d.html',params)

@login_required
def edit_e(request,num):
    obj=kakutuki_e.objects.get(tuki=num)
    if(request.method=='POST'):
        kaku=kakutukiForm_e(request.POST,instance=obj)
        kaku.save()
        return redirect(to='/patrol/index_e')
    params={
        'title':'半角数字0~20で点数を記入してください',
        'tuki':num,
        'form':kakutukiForm_e(instance=obj),'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,

    }
    return render(request,'patapp/edit_e.html',params)


@login_required
def saiten(request):
    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z
    params={
        'title':f'5Sパトロール採点機能_{ten}点以上で合格！',
        'form':saiten_form(),
        'kekka':'【結果】 ▶️    ',
        'sum':'【合計】 ▶️　 /100点',
        'seiri':'【整理】　▶️ 　/20点',
        'seiton':'【整頓】　▶️ 　/20点',
        'seisou':'【清掃】　▶️ 　/20点',
        'seiketu':'【清潔】　▶️ 　/20点',
        'situke':'【躾】　　▶️ 　/20点',
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }

    if(request.method=='POST'):
        s1_1=int(request.POST['choice1'])
        s1_2=int(request.POST['choice2'])
        s1_3=int(request.POST['choice3'])
        s1_4=int(request.POST['choice4'])
        s1_5=int(request.POST['choice5'])
        s1_6=int(request.POST['choice6'])
        s1_7=int(request.POST['choice7'])
        s1_8=int(request.POST['choice8'])
        s1_9=int(request.POST['choice9'])
        s1_10=int(request.POST['choice10'])

        s2_1=int(request.POST['choice1_2'])
        s2_2=int(request.POST['choice2_2'])
        s2_3=int(request.POST['choice3_2'])
        s2_4=int(request.POST['choice4_2'])
        s2_5=int(request.POST['choice5_2'])
        s2_6=int(request.POST['choice6_2'])
        s2_7=int(request.POST['choice7_2'])
        s2_8=int(request.POST['choice8_2'])
        s2_9=int(request.POST['choice9_2'])
        s2_10=int(request.POST['choice10_2'])

        s3_1=int(request.POST['choice1_3'])
        s3_2=int(request.POST['choice2_3'])
        s3_3=int(request.POST['choice3_3'])
        s3_4=int(request.POST['choice4_3'])
        s3_5=int(request.POST['choice5_3'])
        s3_6=int(request.POST['choice6_3'])
        s3_7=int(request.POST['choice7_3'])
        s3_8=int(request.POST['choice8_3'])
        s3_9=int(request.POST['choice9_3'])
        s3_10=int(request.POST['choice10_3'])

        s4_1=int(request.POST['choice1_4'])
        s4_2=int(request.POST['choice2_4'])
        s4_3=int(request.POST['choice3_4'])
        s4_4=int(request.POST['choice4_4'])
        s4_5=int(request.POST['choice5_4'])
        s4_6=int(request.POST['choice6_4'])
        s4_7=int(request.POST['choice7_4'])
        s4_8=int(request.POST['choice8_4'])
        s4_9=int(request.POST['choice9_4'])
        s4_10=int(request.POST['choice10_4'])

        s5_1=int(request.POST['choice1_5'])
        s5_2=int(request.POST['choice2_5'])
        s5_3=int(request.POST['choice3_5'])
        s5_4=int(request.POST['choice4_5'])
        s5_5=int(request.POST['choice5_5'])
        s5_6=int(request.POST['choice6_5'])
        s5_7=int(request.POST['choice7_5'])
        s5_8=int(request.POST['choice8_5'])
        s5_9=int(request.POST['choice9_5'])
        s5_10=int(request.POST['choice10_5'])


        sm1=s1_1 + s1_2 + s1_3 + s1_4 + s1_5 + s1_6 + s1_7 + s1_8 + s1_9 + s1_10
        sm2=s2_1 + s2_2 + s2_3 + s2_4 + s2_5 + s2_6 + s2_7 + s2_8 + s2_9 + s2_10
        sm3=s3_1 + s3_2 + s3_3 + s3_4 + s3_5 + s3_6 + s3_7 + s3_8 + s3_9 + s3_10
        sm4=s4_1 + s4_2 + s4_3 + s4_4 + s4_5 + s4_6 + s4_7 + s4_8 + s4_9 + s4_10
        sm5=s5_1 + s5_2 + s5_3 + s5_4 + s5_5 + s5_6 + s5_7 + s5_8 + s5_9 + s5_10
        sm_sum=sm1+sm2+sm3+sm4+sm5
        
        
        
        if sm_sum >= ten:
            params['kekka']='【結果】 ▶️　"合格！" '
        else:
            params['kekka']='【結果】 ▶️　"不合格" '
        
        
        
        
        
        sm1=str(sm1)
        sm2=str(sm2)
        sm3=str(sm3)
        sm4=str(sm4)
        sm5=str(sm5)
        sm_sum=str(sm_sum)



        




        params['sum']='【合計】 ▶️  '+sm_sum+'/100点'
        params['seiri']='【整理】　▶️ ' +sm1+'/20点'
        params['seiton']='【整頓】　▶️  ' +sm2+'/20点'
        params['seisou']='【清掃】　▶️  ' +sm3+'/20点'
        params['seiketu']='【清潔】　▶️  ' +sm4+'/20点'
        params['situke']='【躾】　　▶️  ' +sm5+'/20点'





        params['form']=saiten_form(request.POST)
    return render(request,'patapp/saiten.html',params)

@login_required
def saiten_a(request):
    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z
    params={
        'title':f'5Sパトロール採点機能_{ten}点以上で合格！',
        'form':saiten_form_a(),
        'kekka':'【結果】 ▶️    ',
        'sum':'【合計】 ▶️　 /100点',
        'seiri':'【整理】　▶️ 　/20点',
        'seiton':'【整頓】　▶️ 　/20点',
        'seisou':'【清掃】　▶️ 　/20点',
        'seiketu':'【清潔】　▶️ 　/20点',
        'situke':'【躾】　　▶️ 　/20点',
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }

    if(request.method=='POST'):
        s1_1=int(request.POST['choice1'])
        s1_2=int(request.POST['choice2'])
        s1_3=int(request.POST['choice3'])
        s1_4=int(request.POST['choice4'])
        s1_5=int(request.POST['choice5'])
        s1_6=int(request.POST['choice6'])
        s1_7=int(request.POST['choice7'])
        s1_8=int(request.POST['choice8'])
        s1_9=int(request.POST['choice9'])
        s1_10=int(request.POST['choice10'])

        s2_1=int(request.POST['choice1_2'])
        s2_2=int(request.POST['choice2_2'])
        s2_3=int(request.POST['choice3_2'])
        s2_4=int(request.POST['choice4_2'])
        s2_5=int(request.POST['choice5_2'])
        s2_6=int(request.POST['choice6_2'])
        s2_7=int(request.POST['choice7_2'])
        s2_8=int(request.POST['choice8_2'])
        s2_9=int(request.POST['choice9_2'])
        s2_10=int(request.POST['choice10_2'])

        s3_1=int(request.POST['choice1_3'])
        s3_2=int(request.POST['choice2_3'])
        s3_3=int(request.POST['choice3_3'])
        s3_4=int(request.POST['choice4_3'])
        s3_5=int(request.POST['choice5_3'])
        s3_6=int(request.POST['choice6_3'])
        s3_7=int(request.POST['choice7_3'])
        s3_8=int(request.POST['choice8_3'])
        s3_9=int(request.POST['choice9_3'])
        s3_10=int(request.POST['choice10_3'])

        s4_1=int(request.POST['choice1_4'])
        s4_2=int(request.POST['choice2_4'])
        s4_3=int(request.POST['choice3_4'])
        s4_4=int(request.POST['choice4_4'])
        s4_5=int(request.POST['choice5_4'])
        s4_6=int(request.POST['choice6_4'])
        s4_7=int(request.POST['choice7_4'])
        s4_8=int(request.POST['choice8_4'])
        s4_9=int(request.POST['choice9_4'])
        s4_10=int(request.POST['choice10_4'])

        s5_1=int(request.POST['choice1_5'])
        s5_2=int(request.POST['choice2_5'])
        s5_3=int(request.POST['choice3_5'])
        s5_4=int(request.POST['choice4_5'])
        s5_5=int(request.POST['choice5_5'])
        s5_6=int(request.POST['choice6_5'])
        s5_7=int(request.POST['choice7_5'])
        s5_8=int(request.POST['choice8_5'])
        s5_9=int(request.POST['choice9_5'])
        s5_10=int(request.POST['choice10_5'])


        sm1=s1_1 + s1_2 + s1_3 + s1_4 + s1_5 + s1_6 + s1_7 + s1_8 + s1_9 + s1_10
        sm2=s2_1 + s2_2 + s2_3 + s2_4 + s2_5 + s2_6 + s2_7 + s2_8 + s2_9 + s2_10
        sm3=s3_1 + s3_2 + s3_3 + s3_4 + s3_5 + s3_6 + s3_7 + s3_8 + s3_9 + s3_10
        sm4=s4_1 + s4_2 + s4_3 + s4_4 + s4_5 + s4_6 + s4_7 + s4_8 + s4_9 + s4_10
        sm5=s5_1 + s5_2 + s5_3 + s5_4 + s5_5 + s5_6 + s5_7 + s5_8 + s5_9 + s5_10
        sm_sum=sm1+sm2+sm3+sm4+sm5
        
        
        
        if sm_sum>= ten:
            params['kekka']='【結果】 ▶️　"合格！" '
        else:
            params['kekka']='【結果】 ▶️　"不合格" '
        
        
        
        
        
        sm1=str(sm1)
        sm2=str(sm2)
        sm3=str(sm3)
        sm4=str(sm4)
        sm5=str(sm5)
        sm_sum=str(sm_sum)



        




        params['sum']='【合計】 ▶️  '+sm_sum+'/100点'
        params['seiri']='【整理】　▶️ ' +sm1+'/20点'
        params['seiton']='【整頓】　▶️  ' +sm2+'/20点'
        params['seisou']='【清掃】　▶️  ' +sm3+'/20点'
        params['seiketu']='【清潔】　▶️  ' +sm4+'/20点'
        params['situke']='【躾】　　▶️  ' +sm5+'/20点'





        params['form']=saiten_form_a(request.POST)
    return render(request,'patapp/saiten_a.html',params)

@login_required
def saiten_b(request):
    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z
    params={
        'title':f'5Sパトロール採点機能_{ten}点以上で合格！',
        'form':saiten_form_b(),
        'kekka':'【結果】 ▶️    ',
        'sum':'【合計】 ▶️　 /100点',
        'seiri':'【整理】　▶️ 　/20点',
        'seiton':'【整頓】　▶️ 　/20点',
        'seisou':'【清掃】　▶️ 　/20点',
        'seiketu':'【清潔】　▶️ 　/20点',
        'situke':'【躾】　　▶️ 　/20点',
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }

    if(request.method=='POST'):
        s1_1=int(request.POST['choice1'])
        s1_2=int(request.POST['choice2'])
        s1_3=int(request.POST['choice3'])
        s1_4=int(request.POST['choice4'])
        s1_5=int(request.POST['choice5'])
        s1_6=int(request.POST['choice6'])
        s1_7=int(request.POST['choice7'])
        s1_8=int(request.POST['choice8'])
        s1_9=int(request.POST['choice9'])
        s1_10=int(request.POST['choice10'])

        s2_1=int(request.POST['choice1_2'])
        s2_2=int(request.POST['choice2_2'])
        s2_3=int(request.POST['choice3_2'])
        s2_4=int(request.POST['choice4_2'])
        s2_5=int(request.POST['choice5_2'])
        s2_6=int(request.POST['choice6_2'])
        s2_7=int(request.POST['choice7_2'])
        s2_8=int(request.POST['choice8_2'])
        s2_9=int(request.POST['choice9_2'])
        s2_10=int(request.POST['choice10_2'])

        s3_1=int(request.POST['choice1_3'])
        s3_2=int(request.POST['choice2_3'])
        s3_3=int(request.POST['choice3_3'])
        s3_4=int(request.POST['choice4_3'])
        s3_5=int(request.POST['choice5_3'])
        s3_6=int(request.POST['choice6_3'])
        s3_7=int(request.POST['choice7_3'])
        s3_8=int(request.POST['choice8_3'])
        s3_9=int(request.POST['choice9_3'])
        s3_10=int(request.POST['choice10_3'])

        s4_1=int(request.POST['choice1_4'])
        s4_2=int(request.POST['choice2_4'])
        s4_3=int(request.POST['choice3_4'])
        s4_4=int(request.POST['choice4_4'])
        s4_5=int(request.POST['choice5_4'])
        s4_6=int(request.POST['choice6_4'])
        s4_7=int(request.POST['choice7_4'])
        s4_8=int(request.POST['choice8_4'])
        s4_9=int(request.POST['choice9_4'])
        s4_10=int(request.POST['choice10_4'])

        s5_1=int(request.POST['choice1_5'])
        s5_2=int(request.POST['choice2_5'])
        s5_3=int(request.POST['choice3_5'])
        s5_4=int(request.POST['choice4_5'])
        s5_5=int(request.POST['choice5_5'])
        s5_6=int(request.POST['choice6_5'])
        s5_7=int(request.POST['choice7_5'])
        s5_8=int(request.POST['choice8_5'])
        s5_9=int(request.POST['choice9_5'])
        s5_10=int(request.POST['choice10_5'])


        sm1=s1_1 + s1_2 + s1_3 + s1_4 + s1_5 + s1_6 + s1_7 + s1_8 + s1_9 + s1_10
        sm2=s2_1 + s2_2 + s2_3 + s2_4 + s2_5 + s2_6 + s2_7 + s2_8 + s2_9 + s2_10
        sm3=s3_1 + s3_2 + s3_3 + s3_4 + s3_5 + s3_6 + s3_7 + s3_8 + s3_9 + s3_10
        sm4=s4_1 + s4_2 + s4_3 + s4_4 + s4_5 + s4_6 + s4_7 + s4_8 + s4_9 + s4_10
        sm5=s5_1 + s5_2 + s5_3 + s5_4 + s5_5 + s5_6 + s5_7 + s5_8 + s5_9 + s5_10
        sm_sum=sm1+sm2+sm3+sm4+sm5
        
        
        
        if sm_sum>= ten:
            params['kekka']='【結果】 ▶️　"合格！" '
        else:
            params['kekka']='【結果】 ▶️　"不合格" '
        
        
        
        
        
        sm1=str(sm1)
        sm2=str(sm2)
        sm3=str(sm3)
        sm4=str(sm4)
        sm5=str(sm5)
        sm_sum=str(sm_sum)



        




        params['sum']='【合計】 ▶️  '+sm_sum+'/100点'
        params['seiri']='【整理】　▶️ ' +sm1+'/20点'
        params['seiton']='【整頓】　▶️  ' +sm2+'/20点'
        params['seisou']='【清掃】　▶️  ' +sm3+'/20点'
        params['seiketu']='【清潔】　▶️  ' +sm4+'/20点'
        params['situke']='【躾】　　▶️  ' +sm5+'/20点'





        params['form']=saiten_form_b(request.POST)
    return render(request,'patapp/saiten_b.html',params)

@login_required
def saiten_c(request):
    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z
    params={
        'title':f'5Sパトロール採点機能_{ten}点以上で合格！',
        'form':saiten_form_c(),
        'kekka':'【結果】 ▶️    ',
        'sum':'【合計】 ▶️　 /100点',
        'seiri':'【整理】　▶️ 　/20点',
        'seiton':'【整頓】　▶️ 　/20点',
        'seisou':'【清掃】　▶️ 　/20点',
        'seiketu':'【清潔】　▶️ 　/20点',
        'situke':'【躾】　　▶️ 　/20点',
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }

    if(request.method=='POST'):
        s1_1=int(request.POST['choice1'])
        s1_2=int(request.POST['choice2'])
        s1_3=int(request.POST['choice3'])
        s1_4=int(request.POST['choice4'])
        s1_5=int(request.POST['choice5'])
        s1_6=int(request.POST['choice6'])
        s1_7=int(request.POST['choice7'])
        s1_8=int(request.POST['choice8'])
        s1_9=int(request.POST['choice9'])
        s1_10=int(request.POST['choice10'])

        s2_1=int(request.POST['choice1_2'])
        s2_2=int(request.POST['choice2_2'])
        s2_3=int(request.POST['choice3_2'])
        s2_4=int(request.POST['choice4_2'])
        s2_5=int(request.POST['choice5_2'])
        s2_6=int(request.POST['choice6_2'])
        s2_7=int(request.POST['choice7_2'])
        s2_8=int(request.POST['choice8_2'])
        s2_9=int(request.POST['choice9_2'])
        s2_10=int(request.POST['choice10_2'])

        s3_1=int(request.POST['choice1_3'])
        s3_2=int(request.POST['choice2_3'])
        s3_3=int(request.POST['choice3_3'])
        s3_4=int(request.POST['choice4_3'])
        s3_5=int(request.POST['choice5_3'])
        s3_6=int(request.POST['choice6_3'])
        s3_7=int(request.POST['choice7_3'])
        s3_8=int(request.POST['choice8_3'])
        s3_9=int(request.POST['choice9_3'])
        s3_10=int(request.POST['choice10_3'])

        s4_1=int(request.POST['choice1_4'])
        s4_2=int(request.POST['choice2_4'])
        s4_3=int(request.POST['choice3_4'])
        s4_4=int(request.POST['choice4_4'])
        s4_5=int(request.POST['choice5_4'])
        s4_6=int(request.POST['choice6_4'])
        s4_7=int(request.POST['choice7_4'])
        s4_8=int(request.POST['choice8_4'])
        s4_9=int(request.POST['choice9_4'])
        s4_10=int(request.POST['choice10_4'])

        s5_1=int(request.POST['choice1_5'])
        s5_2=int(request.POST['choice2_5'])
        s5_3=int(request.POST['choice3_5'])
        s5_4=int(request.POST['choice4_5'])
        s5_5=int(request.POST['choice5_5'])
        s5_6=int(request.POST['choice6_5'])
        s5_7=int(request.POST['choice7_5'])
        s5_8=int(request.POST['choice8_5'])
        s5_9=int(request.POST['choice9_5'])
        s5_10=int(request.POST['choice10_5'])


        sm1=s1_1 + s1_2 + s1_3 + s1_4 + s1_5 + s1_6 + s1_7 + s1_8 + s1_9 + s1_10
        sm2=s2_1 + s2_2 + s2_3 + s2_4 + s2_5 + s2_6 + s2_7 + s2_8 + s2_9 + s2_10
        sm3=s3_1 + s3_2 + s3_3 + s3_4 + s3_5 + s3_6 + s3_7 + s3_8 + s3_9 + s3_10
        sm4=s4_1 + s4_2 + s4_3 + s4_4 + s4_5 + s4_6 + s4_7 + s4_8 + s4_9 + s4_10
        sm5=s5_1 + s5_2 + s5_3 + s5_4 + s5_5 + s5_6 + s5_7 + s5_8 + s5_9 + s5_10
        sm_sum=sm1+sm2+sm3+sm4+sm5
        
        
        
        if sm_sum>= ten:
            params['kekka']='【結果】 ▶️　"合格！" '
        else:
            params['kekka']='【結果】 ▶️　"不合格" '
        
        
        
        
        
        sm1=str(sm1)
        sm2=str(sm2)
        sm3=str(sm3)
        sm4=str(sm4)
        sm5=str(sm5)
        sm_sum=str(sm_sum)



        params['sum']='【合計】 ▶️  '+sm_sum+'/100点'
        params['seiri']='【整理】　▶️ ' +sm1+'/20点'
        params['seiton']='【整頓】　▶️  ' +sm2+'/20点'
        params['seisou']='【清掃】　▶️  ' +sm3+'/20点'
        params['seiketu']='【清潔】　▶️  ' +sm4+'/20点'
        params['situke']='【躾】　　▶️  ' +sm5+'/20点'





        params['form']=saiten_form_c(request.POST)
    return render(request,'patapp/saiten_c.html',params)

@login_required
def saiten_d(request):
    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z
    params={
        'title':f'5Sパトロール採点機能_{ten}点以上で合格！',
        'form':saiten_form_d(),
        'kekka':'【結果】 ▶️    ',
        'sum':'【合計】 ▶️　 /100点',
        'seiri':'【整理】　▶️ 　/20点',
        'seiton':'【整頓】　▶️ 　/20点',
        'seisou':'【清掃】　▶️ 　/20点',
        'seiketu':'【清潔】　▶️ 　/20点',
        'situke':'【躾】　　▶️ 　/20点',
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }

    if(request.method=='POST'):
        s1_1=int(request.POST['choice1'])
        s1_2=int(request.POST['choice2'])
        s1_3=int(request.POST['choice3'])
        s1_4=int(request.POST['choice4'])
        s1_5=int(request.POST['choice5'])
        s1_6=int(request.POST['choice6'])
        s1_7=int(request.POST['choice7'])
        s1_8=int(request.POST['choice8'])
        s1_9=int(request.POST['choice9'])
        s1_10=int(request.POST['choice10'])

        s2_1=int(request.POST['choice1_2'])
        s2_2=int(request.POST['choice2_2'])
        s2_3=int(request.POST['choice3_2'])
        s2_4=int(request.POST['choice4_2'])
        s2_5=int(request.POST['choice5_2'])
        s2_6=int(request.POST['choice6_2'])
        s2_7=int(request.POST['choice7_2'])
        s2_8=int(request.POST['choice8_2'])
        s2_9=int(request.POST['choice9_2'])
        s2_10=int(request.POST['choice10_2'])

        s3_1=int(request.POST['choice1_3'])
        s3_2=int(request.POST['choice2_3'])
        s3_3=int(request.POST['choice3_3'])
        s3_4=int(request.POST['choice4_3'])
        s3_5=int(request.POST['choice5_3'])
        s3_6=int(request.POST['choice6_3'])
        s3_7=int(request.POST['choice7_3'])
        s3_8=int(request.POST['choice8_3'])
        s3_9=int(request.POST['choice9_3'])
        s3_10=int(request.POST['choice10_3'])

        s4_1=int(request.POST['choice1_4'])
        s4_2=int(request.POST['choice2_4'])
        s4_3=int(request.POST['choice3_4'])
        s4_4=int(request.POST['choice4_4'])
        s4_5=int(request.POST['choice5_4'])
        s4_6=int(request.POST['choice6_4'])
        s4_7=int(request.POST['choice7_4'])
        s4_8=int(request.POST['choice8_4'])
        s4_9=int(request.POST['choice9_4'])
        s4_10=int(request.POST['choice10_4'])

        s5_1=int(request.POST['choice1_5'])
        s5_2=int(request.POST['choice2_5'])
        s5_3=int(request.POST['choice3_5'])
        s5_4=int(request.POST['choice4_5'])
        s5_5=int(request.POST['choice5_5'])
        s5_6=int(request.POST['choice6_5'])
        s5_7=int(request.POST['choice7_5'])
        s5_8=int(request.POST['choice8_5'])
        s5_9=int(request.POST['choice9_5'])
        s5_10=int(request.POST['choice10_5'])


        sm1=s1_1 + s1_2 + s1_3 + s1_4 + s1_5 + s1_6 + s1_7 + s1_8 + s1_9 + s1_10
        sm2=s2_1 + s2_2 + s2_3 + s2_4 + s2_5 + s2_6 + s2_7 + s2_8 + s2_9 + s2_10
        sm3=s3_1 + s3_2 + s3_3 + s3_4 + s3_5 + s3_6 + s3_7 + s3_8 + s3_9 + s3_10
        sm4=s4_1 + s4_2 + s4_3 + s4_4 + s4_5 + s4_6 + s4_7 + s4_8 + s4_9 + s4_10
        sm5=s5_1 + s5_2 + s5_3 + s5_4 + s5_5 + s5_6 + s5_7 + s5_8 + s5_9 + s5_10
        sm_sum=sm1+sm2+sm3+sm4+sm5
        
        
        
        if sm_sum>= ten:
            params['kekka']='【結果】 ▶️　"合格！" '
        else:
            params['kekka']='【結果】 ▶️　"不合格" '
        
        
        
        
        
        sm1=str(sm1)
        sm2=str(sm2)
        sm3=str(sm3)
        sm4=str(sm4)
        sm5=str(sm5)
        sm_sum=str(sm_sum)



        




        params['sum']='【合計】 ▶️  '+sm_sum+'/100点'
        params['seiri']='【整理】　▶️ ' +sm1+'/20点'
        params['seiton']='【整頓】　▶️  ' +sm2+'/20点'
        params['seisou']='【清掃】　▶️  ' +sm3+'/20点'
        params['seiketu']='【清潔】　▶️  ' +sm4+'/20点'
        params['situke']='【躾】　　▶️  ' +sm5+'/20点'





        params['form']=saiten_form_d(request.POST)
    return render(request,'patapp/saiten_d.html',params)

@login_required
def saiten_e(request):
    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z
    params={
        'title':f'5Sパトロール採点機能_{ten}点以上で合格！',
        'form':saiten_form_e(),
        'kekka':'【結果】 ▶️    ',
        'sum':'【合計】 ▶️　 /100点',
        'seiri':'【整理】　▶️ 　/20点',
        'seiton':'【整頓】　▶️ 　/20点',
        'seisou':'【清掃】　▶️ 　/20点',
        'seiketu':'【清潔】　▶️ 　/20点',
        'situke':'【躾】　　▶️ 　/20点',
        'team_all_1z':team_all_1z,
        'team_all_2z':team_all_2z,
        'team_all_3z':team_all_3z,
        'team_all_4z':team_all_4z,
        'team_all_5z':team_all_5z,
        'team_all_6z':team_all_6z,
    }

    if(request.method=='POST'):
        s1_1=int(request.POST['choice1'])
        s1_2=int(request.POST['choice2'])
        s1_3=int(request.POST['choice3'])
        s1_4=int(request.POST['choice4'])
        s1_5=int(request.POST['choice5'])
        s1_6=int(request.POST['choice6'])
        s1_7=int(request.POST['choice7'])
        s1_8=int(request.POST['choice8'])
        s1_9=int(request.POST['choice9'])
        s1_10=int(request.POST['choice10'])

        s2_1=int(request.POST['choice1_2'])
        s2_2=int(request.POST['choice2_2'])
        s2_3=int(request.POST['choice3_2'])
        s2_4=int(request.POST['choice4_2'])
        s2_5=int(request.POST['choice5_2'])
        s2_6=int(request.POST['choice6_2'])
        s2_7=int(request.POST['choice7_2'])
        s2_8=int(request.POST['choice8_2'])
        s2_9=int(request.POST['choice9_2'])
        s2_10=int(request.POST['choice10_2'])

        s3_1=int(request.POST['choice1_3'])
        s3_2=int(request.POST['choice2_3'])
        s3_3=int(request.POST['choice3_3'])
        s3_4=int(request.POST['choice4_3'])
        s3_5=int(request.POST['choice5_3'])
        s3_6=int(request.POST['choice6_3'])
        s3_7=int(request.POST['choice7_3'])
        s3_8=int(request.POST['choice8_3'])
        s3_9=int(request.POST['choice9_3'])
        s3_10=int(request.POST['choice10_3'])

        s4_1=int(request.POST['choice1_4'])
        s4_2=int(request.POST['choice2_4'])
        s4_3=int(request.POST['choice3_4'])
        s4_4=int(request.POST['choice4_4'])
        s4_5=int(request.POST['choice5_4'])
        s4_6=int(request.POST['choice6_4'])
        s4_7=int(request.POST['choice7_4'])
        s4_8=int(request.POST['choice8_4'])
        s4_9=int(request.POST['choice9_4'])
        s4_10=int(request.POST['choice10_4'])

        s5_1=int(request.POST['choice1_5'])
        s5_2=int(request.POST['choice2_5'])
        s5_3=int(request.POST['choice3_5'])
        s5_4=int(request.POST['choice4_5'])
        s5_5=int(request.POST['choice5_5'])
        s5_6=int(request.POST['choice6_5'])
        s5_7=int(request.POST['choice7_5'])
        s5_8=int(request.POST['choice8_5'])
        s5_9=int(request.POST['choice9_5'])
        s5_10=int(request.POST['choice10_5'])


        sm1=s1_1 + s1_2 + s1_3 + s1_4 + s1_5 + s1_6 + s1_7 + s1_8 + s1_9 + s1_10
        sm2=s2_1 + s2_2 + s2_3 + s2_4 + s2_5 + s2_6 + s2_7 + s2_8 + s2_9 + s2_10
        sm3=s3_1 + s3_2 + s3_3 + s3_4 + s3_5 + s3_6 + s3_7 + s3_8 + s3_9 + s3_10
        sm4=s4_1 + s4_2 + s4_3 + s4_4 + s4_5 + s4_6 + s4_7 + s4_8 + s4_9 + s4_10
        sm5=s5_1 + s5_2 + s5_3 + s5_4 + s5_5 + s5_6 + s5_7 + s5_8 + s5_9 + s5_10
        sm_sum=sm1+sm2+sm3+sm4+sm5
        
        
        
        if sm_sum>= ten:
            params['kekka']='【結果】 ▶️　"合格！" '
        else:
            params['kekka']='【結果】 ▶️　"不合格" '
        
        
        
        
        
        sm1=str(sm1)
        sm2=str(sm2)
        sm3=str(sm3)
        sm4=str(sm4)
        sm5=str(sm5)
        sm_sum=str(sm_sum)



        




        params['sum']='【合計】 ▶️  '+sm_sum+'/100点'
        params['seiri']='【整理】　▶️ ' +sm1+'/20点'
        params['seiton']='【整頓】　▶️  ' +sm2+'/20点'
        params['seisou']='【清掃】　▶️  ' +sm3+'/20点'
        params['seiketu']='【清潔】　▶️  ' +sm4+'/20点'
        params['situke']='【躾】　　▶️  ' +sm5+'/20点'





        params['form']=saiten_form_e(request.POST)
    return render(request,'patapp/saiten_e.html',params)


def setplt():

    data=kakutuki.objects.all()
    data1=kakutuki.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]


    g4_1=data2_1['seiri_in']
    g5_1=data2_2['seiri_in']
    g6_1=data2_3['seiri_in']
    g7_1=data2_4['seiri_in']
    g8_1=data2_5['seiri_in']
    g9_1=data2_6['seiri_in']
    g10_1=data2_7['seiri_in']
    g11_1=data2_8['seiri_in']
    g12_1=data2_9['seiri_in']
    g1_1=data2_10['seiri_in']
    g2_1=data2_11['seiri_in']
    g3_1=data2_12['seiri_in']

    g4_2=data2_1['seiton_in']
    g5_2=data2_2['seiton_in']
    g6_2=data2_3['seiton_in']
    g7_2=data2_4['seiton_in']
    g8_2=data2_5['seiton_in']
    g9_2=data2_6['seiton_in']
    g10_2=data2_7['seiton_in']
    g11_2=data2_8['seiton_in']
    g12_2=data2_9['seiton_in']
    g1_2=data2_10['seiton_in']
    g2_2=data2_11['seiton_in']
    g3_2=data2_12['seiton_in']

    g4_3=data2_1['seisou_in']
    g5_3=data2_2['seisou_in']
    g6_3=data2_3['seisou_in']
    g7_3=data2_4['seisou_in']
    g8_3=data2_5['seisou_in']
    g9_3=data2_6['seisou_in']
    g10_3=data2_7['seisou_in']
    g11_3=data2_8['seisou_in']
    g12_3=data2_9['seisou_in']
    g1_3=data2_10['seisou_in']
    g2_3=data2_11['seisou_in']
    g3_3=data2_12['seisou_in']

    g4_4=data2_1['seiketu_in']
    g5_4=data2_2['seiketu_in']
    g6_4=data2_3['seiketu_in']
    g7_4=data2_4['seiketu_in']
    g8_4=data2_5['seiketu_in']
    g9_4=data2_6['seiketu_in']
    g10_4=data2_7['seiketu_in']
    g11_4=data2_8['seiketu_in']
    g12_4=data2_9['seiketu_in']
    g1_4=data2_10['seiketu_in']
    g2_4=data2_11['seiketu_in']
    g3_4=data2_12['seiketu_in']

    g4_5=data2_1['situke_in']
    g5_5=data2_2['situke_in']
    g6_5=data2_3['situke_in']
    g7_5=data2_4['situke_in']
    g8_5=data2_5['situke_in']
    g9_5=data2_6['situke_in']
    g10_5=data2_7['situke_in']
    g11_5=data2_8['situke_in']
    g12_5=data2_9['situke_in']
    g1_5=data2_10['situke_in']
    g2_5=data2_11['situke_in']
    g3_5=data2_12['situke_in']

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z

    dataset=pd.DataFrame([[g4_1,g5_1,g6_1,g7_1,g8_1,g9_1,g10_1,g11_1,g12_1,g1_1,g2_1,g3_1],[g4_2,g5_2,g6_2,g7_2,g8_2,g9_2,g10_2,g11_2,g12_2,g1_2,g2_2,g3_2],
    [g4_3,g5_3,g6_3,g7_3,g8_3,g9_3,g10_3,g11_3,g12_3,g1_3,g2_3,g3_3],[g4_4,g5_4,g6_4,g7_4,g8_4,g9_4,g10_4,g11_4,g12_4,g1_4,g2_4,g3_4],
    [g4_5,g5_5,g6_5,g7_5,g8_5,g9_5,g10_5,g11_5,g12_5,g1_5,g2_5,g3_5]],columns=['4月','5月','6月','7月','8月','9月','10月','11月','12月','1月','２月','３月'],
    index=['整理','整頓','清掃','清潔','躾'])

    fig,ax=plt.subplots(figsize=(17,9))
    for i in range(len(dataset)):
        ax.bar(dataset.columns,dataset.iloc[i],bottom=dataset.iloc[:i].sum())
        for j in range(len(dataset.columns)):
            plt.text(x=j,
            y=dataset.iloc[:i,j].sum()+(dataset.iloc[i,j]/2),
            s=dataset.iloc[i,j],
            ha='center',
            va='bottom'
            )
    plt.title(f'【5Sパトロール結果:チーム{team_all_1z}】',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'{ten}点以上で合格【点】',fontsize=23)
    plt.font='IPAexGothic'
    #ax.set(xlabel='【月】',ylabel='【点】85点以上で合格',title=f'【5Sパトロール結果:チーム{team_all_1z}】',)
    ax.legend(dataset.index)
    ax.axhline(y=ten,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)


def plt2svg():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg(request):
    setplt()
    svg=plt2svg()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_a():

    data=kakutuki_a.objects.all()
    data1=kakutuki_a.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]


    g4_1=data2_1['seiri_in']
    g5_1=data2_2['seiri_in']
    g6_1=data2_3['seiri_in']
    g7_1=data2_4['seiri_in']
    g8_1=data2_5['seiri_in']
    g9_1=data2_6['seiri_in']
    g10_1=data2_7['seiri_in']
    g11_1=data2_8['seiri_in']
    g12_1=data2_9['seiri_in']
    g1_1=data2_10['seiri_in']
    g2_1=data2_11['seiri_in']
    g3_1=data2_12['seiri_in']

    g4_2=data2_1['seiton_in']
    g5_2=data2_2['seiton_in']
    g6_2=data2_3['seiton_in']
    g7_2=data2_4['seiton_in']
    g8_2=data2_5['seiton_in']
    g9_2=data2_6['seiton_in']
    g10_2=data2_7['seiton_in']
    g11_2=data2_8['seiton_in']
    g12_2=data2_9['seiton_in']
    g1_2=data2_10['seiton_in']
    g2_2=data2_11['seiton_in']
    g3_2=data2_12['seiton_in']

    g4_3=data2_1['seisou_in']
    g5_3=data2_2['seisou_in']
    g6_3=data2_3['seisou_in']
    g7_3=data2_4['seisou_in']
    g8_3=data2_5['seisou_in']
    g9_3=data2_6['seisou_in']
    g10_3=data2_7['seisou_in']
    g11_3=data2_8['seisou_in']
    g12_3=data2_9['seisou_in']
    g1_3=data2_10['seisou_in']
    g2_3=data2_11['seisou_in']
    g3_3=data2_12['seisou_in']

    g4_4=data2_1['seiketu_in']
    g5_4=data2_2['seiketu_in']
    g6_4=data2_3['seiketu_in']
    g7_4=data2_4['seiketu_in']
    g8_4=data2_5['seiketu_in']
    g9_4=data2_6['seiketu_in']
    g10_4=data2_7['seiketu_in']
    g11_4=data2_8['seiketu_in']
    g12_4=data2_9['seiketu_in']
    g1_4=data2_10['seiketu_in']
    g2_4=data2_11['seiketu_in']
    g3_4=data2_12['seiketu_in']

    g4_5=data2_1['situke_in']
    g5_5=data2_2['situke_in']
    g6_5=data2_3['situke_in']
    g7_5=data2_4['situke_in']
    g8_5=data2_5['situke_in']
    g9_5=data2_6['situke_in']
    g10_5=data2_7['situke_in']
    g11_5=data2_8['situke_in']
    g12_5=data2_9['situke_in']
    g1_5=data2_10['situke_in']
    g2_5=data2_11['situke_in']
    g3_5=data2_12['situke_in']

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    goukakuten_ch=goukaku.objects.all()
    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z

    dataset=pd.DataFrame([[g4_1,g5_1,g6_1,g7_1,g8_1,g9_1,g10_1,g11_1,g12_1,g1_1,g2_1,g3_1],[g4_2,g5_2,g6_2,g7_2,g8_2,g9_2,g10_2,g11_2,g12_2,g1_2,g2_2,g3_2],
    [g4_3,g5_3,g6_3,g7_3,g8_3,g9_3,g10_3,g11_3,g12_3,g1_3,g2_3,g3_3],[g4_4,g5_4,g6_4,g7_4,g8_4,g9_4,g10_4,g11_4,g12_4,g1_4,g2_4,g3_4],
    [g4_5,g5_5,g6_5,g7_5,g8_5,g9_5,g10_5,g11_5,g12_5,g1_5,g2_5,g3_5]],columns=['4月','5月','6月','7月','8月','9月','10月','11月','12月','1月','２月','３月'],
    index=['整理','整頓','清掃','清潔','躾'])

    fig,ax=plt.subplots(figsize=(17,9))
    for i in range(len(dataset)):
        ax.bar(dataset.columns,dataset.iloc[i],bottom=dataset.iloc[:i].sum())
        for j in range(len(dataset.columns)):
            plt.text(x=j,
            y=dataset.iloc[:i,j].sum()+(dataset.iloc[i,j]/2),
            s=dataset.iloc[i,j],
            ha='center',
            va='bottom'
            )
    plt.title(f'【5Sパトロール結果:チーム{team_all_2z}】',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'{ten}点以上で合格【点】',fontsize=23)
    plt.font='IPAexGothic'
    #ax.set(xlabel='【月】',ylabel='【点】85点以上で合格',title=f'【5Sパトロール結果:チーム{team_all_2z}】')
    ax.legend(dataset.index)
    ax.axhline(y=ten,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)


def plt2svg_a():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_a(request):
    setplt_a()
    svg=plt2svg_a()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_b():

    data=kakutuki_b.objects.all()
    data1=kakutuki_b.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]


    g4_1=data2_1['seiri_in']
    g5_1=data2_2['seiri_in']
    g6_1=data2_3['seiri_in']
    g7_1=data2_4['seiri_in']
    g8_1=data2_5['seiri_in']
    g9_1=data2_6['seiri_in']
    g10_1=data2_7['seiri_in']
    g11_1=data2_8['seiri_in']
    g12_1=data2_9['seiri_in']
    g1_1=data2_10['seiri_in']
    g2_1=data2_11['seiri_in']
    g3_1=data2_12['seiri_in']

    g4_2=data2_1['seiton_in']
    g5_2=data2_2['seiton_in']
    g6_2=data2_3['seiton_in']
    g7_2=data2_4['seiton_in']
    g8_2=data2_5['seiton_in']
    g9_2=data2_6['seiton_in']
    g10_2=data2_7['seiton_in']
    g11_2=data2_8['seiton_in']
    g12_2=data2_9['seiton_in']
    g1_2=data2_10['seiton_in']
    g2_2=data2_11['seiton_in']
    g3_2=data2_12['seiton_in']

    g4_3=data2_1['seisou_in']
    g5_3=data2_2['seisou_in']
    g6_3=data2_3['seisou_in']
    g7_3=data2_4['seisou_in']
    g8_3=data2_5['seisou_in']
    g9_3=data2_6['seisou_in']
    g10_3=data2_7['seisou_in']
    g11_3=data2_8['seisou_in']
    g12_3=data2_9['seisou_in']
    g1_3=data2_10['seisou_in']
    g2_3=data2_11['seisou_in']
    g3_3=data2_12['seisou_in']

    g4_4=data2_1['seiketu_in']
    g5_4=data2_2['seiketu_in']
    g6_4=data2_3['seiketu_in']
    g7_4=data2_4['seiketu_in']
    g8_4=data2_5['seiketu_in']
    g9_4=data2_6['seiketu_in']
    g10_4=data2_7['seiketu_in']
    g11_4=data2_8['seiketu_in']
    g12_4=data2_9['seiketu_in']
    g1_4=data2_10['seiketu_in']
    g2_4=data2_11['seiketu_in']
    g3_4=data2_12['seiketu_in']

    g4_5=data2_1['situke_in']
    g5_5=data2_2['situke_in']
    g6_5=data2_3['situke_in']
    g7_5=data2_4['situke_in']
    g8_5=data2_5['situke_in']
    g9_5=data2_6['situke_in']
    g10_5=data2_7['situke_in']
    g11_5=data2_8['situke_in']
    g12_5=data2_9['situke_in']
    g1_5=data2_10['situke_in']
    g2_5=data2_11['situke_in']
    g3_5=data2_12['situke_in']

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z

    
    
    dataset=pd.DataFrame([[g4_1,g5_1,g6_1,g7_1,g8_1,g9_1,g10_1,g11_1,g12_1,g1_1,g2_1,g3_1],[g4_2,g5_2,g6_2,g7_2,g8_2,g9_2,g10_2,g11_2,g12_2,g1_2,g2_2,g3_2],
    [g4_3,g5_3,g6_3,g7_3,g8_3,g9_3,g10_3,g11_3,g12_3,g1_3,g2_3,g3_3],[g4_4,g5_4,g6_4,g7_4,g8_4,g9_4,g10_4,g11_4,g12_4,g1_4,g2_4,g3_4],
    [g4_5,g5_5,g6_5,g7_5,g8_5,g9_5,g10_5,g11_5,g12_5,g1_5,g2_5,g3_5]],columns=['4月','5月','6月','7月','8月','9月','10月','11月','12月','1月','２月','３月'],
    index=['整理','整頓','清掃','清潔','躾'])

    fig,ax=plt.subplots(figsize=(17,9))
    for i in range(len(dataset)):
        ax.bar(dataset.columns,dataset.iloc[i],bottom=dataset.iloc[:i].sum())
        for j in range(len(dataset.columns)):
            plt.text(x=j,
            y=dataset.iloc[:i,j].sum()+(dataset.iloc[i,j]/2),
            s=dataset.iloc[i,j],
            ha='center',
            va='bottom'
            )
    plt.title(f'【5Sパトロール結果:チーム{team_all_3z}】',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'{ten}点以上で合格【点】',fontsize=23)
    plt.font='IPAexGothic'
    #ax.set(xlabel='【月】',ylabel='【点】85点以上で合格',title=f'【5Sパトロール結果:チーム{team_all_3z}】')
    ax.legend(dataset.index)
    ax.axhline(y=ten,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)


def plt2svg_b():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_b(request):
    setplt_b()
    svg=plt2svg_b()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_c():

    data=kakutuki_c.objects.all()
    data1=kakutuki_c.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]


    g4_1=data2_1['seiri_in']
    g5_1=data2_2['seiri_in']
    g6_1=data2_3['seiri_in']
    g7_1=data2_4['seiri_in']
    g8_1=data2_5['seiri_in']
    g9_1=data2_6['seiri_in']
    g10_1=data2_7['seiri_in']
    g11_1=data2_8['seiri_in']
    g12_1=data2_9['seiri_in']
    g1_1=data2_10['seiri_in']
    g2_1=data2_11['seiri_in']
    g3_1=data2_12['seiri_in']

    g4_2=data2_1['seiton_in']
    g5_2=data2_2['seiton_in']
    g6_2=data2_3['seiton_in']
    g7_2=data2_4['seiton_in']
    g8_2=data2_5['seiton_in']
    g9_2=data2_6['seiton_in']
    g10_2=data2_7['seiton_in']
    g11_2=data2_8['seiton_in']
    g12_2=data2_9['seiton_in']
    g1_2=data2_10['seiton_in']
    g2_2=data2_11['seiton_in']
    g3_2=data2_12['seiton_in']

    g4_3=data2_1['seisou_in']
    g5_3=data2_2['seisou_in']
    g6_3=data2_3['seisou_in']
    g7_3=data2_4['seisou_in']
    g8_3=data2_5['seisou_in']
    g9_3=data2_6['seisou_in']
    g10_3=data2_7['seisou_in']
    g11_3=data2_8['seisou_in']
    g12_3=data2_9['seisou_in']
    g1_3=data2_10['seisou_in']
    g2_3=data2_11['seisou_in']
    g3_3=data2_12['seisou_in']

    g4_4=data2_1['seiketu_in']
    g5_4=data2_2['seiketu_in']
    g6_4=data2_3['seiketu_in']
    g7_4=data2_4['seiketu_in']
    g8_4=data2_5['seiketu_in']
    g9_4=data2_6['seiketu_in']
    g10_4=data2_7['seiketu_in']
    g11_4=data2_8['seiketu_in']
    g12_4=data2_9['seiketu_in']
    g1_4=data2_10['seiketu_in']
    g2_4=data2_11['seiketu_in']
    g3_4=data2_12['seiketu_in']

    g4_5=data2_1['situke_in']
    g5_5=data2_2['situke_in']
    g6_5=data2_3['situke_in']
    g7_5=data2_4['situke_in']
    g8_5=data2_5['situke_in']
    g9_5=data2_6['situke_in']
    g10_5=data2_7['situke_in']
    g11_5=data2_8['situke_in']
    g12_5=data2_9['situke_in']
    g1_5=data2_10['situke_in']
    g2_5=data2_11['situke_in']
    g3_5=data2_12['situke_in']

    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z

    dataset=pd.DataFrame([[g4_1,g5_1,g6_1,g7_1,g8_1,g9_1,g10_1,g11_1,g12_1,g1_1,g2_1,g3_1],[g4_2,g5_2,g6_2,g7_2,g8_2,g9_2,g10_2,g11_2,g12_2,g1_2,g2_2,g3_2],
    [g4_3,g5_3,g6_3,g7_3,g8_3,g9_3,g10_3,g11_3,g12_3,g1_3,g2_3,g3_3],[g4_4,g5_4,g6_4,g7_4,g8_4,g9_4,g10_4,g11_4,g12_4,g1_4,g2_4,g3_4],
    [g4_5,g5_5,g6_5,g7_5,g8_5,g9_5,g10_5,g11_5,g12_5,g1_5,g2_5,g3_5]],columns=['4月','5月','6月','7月','8月','9月','10月','11月','12月','1月','２月','３月'],
    index=['整理','整頓','清掃','清潔','躾'])

    fig,ax=plt.subplots(figsize=(17,9))
    for i in range(len(dataset)):
        ax.bar(dataset.columns,dataset.iloc[i],bottom=dataset.iloc[:i].sum())
        for j in range(len(dataset.columns)):
            plt.text(x=j,
            y=dataset.iloc[:i,j].sum()+(dataset.iloc[i,j]/2),
            s=dataset.iloc[i,j],
            ha='center',
            va='bottom'
            )
    plt.title(f'【5Sパトロール結果:チーム{team_all_4z}】',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'{ten}点以上で合格【点】',fontsize=23)
    plt.font='IPAexGothic'
    #ax.set(xlabel='【月】',ylabel='【点】85点以上で合格',title=f'【5Sパトロール結果:チーム{team_all_4z}】')
    ax.legend(dataset.index)
    ax.axhline(y=ten,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)


def plt2svg_c():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_c(request):
    setplt_c()
    svg=plt2svg_c()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_d():

    data=kakutuki_d.objects.all()
    data1=kakutuki_d.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]


    g4_1=data2_1['seiri_in']
    g5_1=data2_2['seiri_in']
    g6_1=data2_3['seiri_in']
    g7_1=data2_4['seiri_in']
    g8_1=data2_5['seiri_in']
    g9_1=data2_6['seiri_in']
    g10_1=data2_7['seiri_in']
    g11_1=data2_8['seiri_in']
    g12_1=data2_9['seiri_in']
    g1_1=data2_10['seiri_in']
    g2_1=data2_11['seiri_in']
    g3_1=data2_12['seiri_in']

    g4_2=data2_1['seiton_in']
    g5_2=data2_2['seiton_in']
    g6_2=data2_3['seiton_in']
    g7_2=data2_4['seiton_in']
    g8_2=data2_5['seiton_in']
    g9_2=data2_6['seiton_in']
    g10_2=data2_7['seiton_in']
    g11_2=data2_8['seiton_in']
    g12_2=data2_9['seiton_in']
    g1_2=data2_10['seiton_in']
    g2_2=data2_11['seiton_in']
    g3_2=data2_12['seiton_in']

    g4_3=data2_1['seisou_in']
    g5_3=data2_2['seisou_in']
    g6_3=data2_3['seisou_in']
    g7_3=data2_4['seisou_in']
    g8_3=data2_5['seisou_in']
    g9_3=data2_6['seisou_in']
    g10_3=data2_7['seisou_in']
    g11_3=data2_8['seisou_in']
    g12_3=data2_9['seisou_in']
    g1_3=data2_10['seisou_in']
    g2_3=data2_11['seisou_in']
    g3_3=data2_12['seisou_in']

    g4_4=data2_1['seiketu_in']
    g5_4=data2_2['seiketu_in']
    g6_4=data2_3['seiketu_in']
    g7_4=data2_4['seiketu_in']
    g8_4=data2_5['seiketu_in']
    g9_4=data2_6['seiketu_in']
    g10_4=data2_7['seiketu_in']
    g11_4=data2_8['seiketu_in']
    g12_4=data2_9['seiketu_in']
    g1_4=data2_10['seiketu_in']
    g2_4=data2_11['seiketu_in']
    g3_4=data2_12['seiketu_in']

    g4_5=data2_1['situke_in']
    g5_5=data2_2['situke_in']
    g6_5=data2_3['situke_in']
    g7_5=data2_4['situke_in']
    g8_5=data2_5['situke_in']
    g9_5=data2_6['situke_in']
    g10_5=data2_7['situke_in']
    g11_5=data2_8['situke_in']
    g12_5=data2_9['situke_in']
    g1_5=data2_10['situke_in']
    g2_5=data2_11['situke_in']
    g3_5=data2_12['situke_in']


    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z
    dataset=pd.DataFrame([[g4_1,g5_1,g6_1,g7_1,g8_1,g9_1,g10_1,g11_1,g12_1,g1_1,g2_1,g3_1],[g4_2,g5_2,g6_2,g7_2,g8_2,g9_2,g10_2,g11_2,g12_2,g1_2,g2_2,g3_2],
    [g4_3,g5_3,g6_3,g7_3,g8_3,g9_3,g10_3,g11_3,g12_3,g1_3,g2_3,g3_3],[g4_4,g5_4,g6_4,g7_4,g8_4,g9_4,g10_4,g11_4,g12_4,g1_4,g2_4,g3_4],
    [g4_5,g5_5,g6_5,g7_5,g8_5,g9_5,g10_5,g11_5,g12_5,g1_5,g2_5,g3_5]],columns=['4月','5月','6月','7月','8月','9月','10月','11月','12月','1月','２月','３月'],
    index=['整理','整頓','清掃','清潔','躾'])

    fig,ax=plt.subplots(figsize=(17,9))
    for i in range(len(dataset)):
        ax.bar(dataset.columns,dataset.iloc[i],bottom=dataset.iloc[:i].sum())
        for j in range(len(dataset.columns)):
            plt.text(x=j,
            y=dataset.iloc[:i,j].sum()+(dataset.iloc[i,j]/2),
            s=dataset.iloc[i,j],
            ha='center',
            va='bottom'
            )
    plt.title(f'【5Sパトロール結果:チーム{team_all_5z}】',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'{ten}点以上で合格【点】',fontsize=23)
    plt.font='IPAexGothic'
    #ax.set(xlabel='【月】',ylabel='【点】85点以上で合格',title=f'【5Sパトロール結果:チーム{team_all_5z}】')
    ax.legend(dataset.index)
    ax.axhline(y=ten,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)


def plt2svg_d():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_d(request):
    setplt_d()
    svg=plt2svg_d()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_e():

    data=kakutuki_e.objects.all()
    data1=kakutuki_e.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data2_1=data1[0]
    data2_2=data1[1]
    data2_3=data1[2]
    data2_4=data1[3]
    data2_5=data1[4]
    data2_6=data1[5]
    data2_7=data1[6]
    data2_8=data1[7]
    data2_9=data1[8]
    data2_10=data1[9]
    data2_11=data1[10]
    data2_12=data1[11]


    g4_1=data2_1['seiri_in']
    g5_1=data2_2['seiri_in']
    g6_1=data2_3['seiri_in']
    g7_1=data2_4['seiri_in']
    g8_1=data2_5['seiri_in']
    g9_1=data2_6['seiri_in']
    g10_1=data2_7['seiri_in']
    g11_1=data2_8['seiri_in']
    g12_1=data2_9['seiri_in']
    g1_1=data2_10['seiri_in']
    g2_1=data2_11['seiri_in']
    g3_1=data2_12['seiri_in']

    g4_2=data2_1['seiton_in']
    g5_2=data2_2['seiton_in']
    g6_2=data2_3['seiton_in']
    g7_2=data2_4['seiton_in']
    g8_2=data2_5['seiton_in']
    g9_2=data2_6['seiton_in']
    g10_2=data2_7['seiton_in']
    g11_2=data2_8['seiton_in']
    g12_2=data2_9['seiton_in']
    g1_2=data2_10['seiton_in']
    g2_2=data2_11['seiton_in']
    g3_2=data2_12['seiton_in']

    g4_3=data2_1['seisou_in']
    g5_3=data2_2['seisou_in']
    g6_3=data2_3['seisou_in']
    g7_3=data2_4['seisou_in']
    g8_3=data2_5['seisou_in']
    g9_3=data2_6['seisou_in']
    g10_3=data2_7['seisou_in']
    g11_3=data2_8['seisou_in']
    g12_3=data2_9['seisou_in']
    g1_3=data2_10['seisou_in']
    g2_3=data2_11['seisou_in']
    g3_3=data2_12['seisou_in']

    g4_4=data2_1['seiketu_in']
    g5_4=data2_2['seiketu_in']
    g6_4=data2_3['seiketu_in']
    g7_4=data2_4['seiketu_in']
    g8_4=data2_5['seiketu_in']
    g9_4=data2_6['seiketu_in']
    g10_4=data2_7['seiketu_in']
    g11_4=data2_8['seiketu_in']
    g12_4=data2_9['seiketu_in']
    g1_4=data2_10['seiketu_in']
    g2_4=data2_11['seiketu_in']
    g3_4=data2_12['seiketu_in']

    g4_5=data2_1['situke_in']
    g5_5=data2_2['situke_in']
    g6_5=data2_3['situke_in']
    g7_5=data2_4['situke_in']
    g8_5=data2_5['situke_in']
    g9_5=data2_6['situke_in']
    g10_5=data2_7['situke_in']
    g11_5=data2_8['situke_in']
    g12_5=data2_9['situke_in']
    g1_5=data2_10['situke_in']
    g2_5=data2_11['situke_in']
    g3_5=data2_12['situke_in']


    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']

    goukakuten_all=goukaku.objects.all().values('kijunten_in','tuki')
    goukakuten1=goukakuten_all[0]
    goukakuten2=goukakuten_all[1]
    goukakuten3=goukakuten_all[2]
    goukakuten4=goukakuten_all[3]
    goukakuten5=goukakuten_all[4]
    goukakuten6=goukakuten_all[5]
    goukakuten7=goukakuten_all[6]
    goukakuten8=goukakuten_all[7]
    goukakuten9=goukakuten_all[8]
    goukakuten10=goukakuten_all[9]
    goukakuten11=goukakuten_all[10]
    goukakuten12=goukakuten_all[11]

    goukakuten_all_1z=goukakuten1['kijunten_in']
    goukakuten_all_2z=goukakuten2['kijunten_in']
    goukakuten_all_3z=goukakuten3['kijunten_in']
    goukakuten_all_4z=goukakuten4['kijunten_in']
    goukakuten_all_5z=goukakuten5['kijunten_in']
    goukakuten_all_6z=goukakuten6['kijunten_in']
    goukakuten_all_7z=goukakuten7['kijunten_in']
    goukakuten_all_8z=goukakuten8['kijunten_in']
    goukakuten_all_9z=goukakuten9['kijunten_in']
    goukakuten_all_10z=goukakuten10['kijunten_in']
    goukakuten_all_11z=goukakuten11['kijunten_in']
    goukakuten_all_12z=goukakuten12['kijunten_in']

    if now.month == 1:
        ten=goukakuten_all_10z
    elif now.month == 2:
        ten=goukakuten_all_11z
    elif now.month == 3:
        ten=goukakuten_all_12z
    elif now.month == 4:
        ten=goukakuten_all_1z
    elif now.month == 5:
        ten=goukakuten_all_2z
    elif now.month == 6:
        ten=goukakuten_all_3z
    elif now.month == 7:
        ten=goukakuten_all_4z
    elif now.month == 8:
        ten=goukakuten_all_5z
    elif now.month == 9:
        ten=goukakuten_all_6z
    elif now.month == 10:
        ten=goukakuten_all_7z
    elif now.month == 11:
        ten=goukakuten_all_8z
    elif now.month == 12:
        ten=goukakuten_all_9z
    

    dataset=pd.DataFrame([[g4_1,g5_1,g6_1,g7_1,g8_1,g9_1,g10_1,g11_1,g12_1,g1_1,g2_1,g3_1],[g4_2,g5_2,g6_2,g7_2,g8_2,g9_2,g10_2,g11_2,g12_2,g1_2,g2_2,g3_2],
    [g4_3,g5_3,g6_3,g7_3,g8_3,g9_3,g10_3,g11_3,g12_3,g1_3,g2_3,g3_3],[g4_4,g5_4,g6_4,g7_4,g8_4,g9_4,g10_4,g11_4,g12_4,g1_4,g2_4,g3_4],
    [g4_5,g5_5,g6_5,g7_5,g8_5,g9_5,g10_5,g11_5,g12_5,g1_5,g2_5,g3_5]],columns=['4月','5月','6月','7月','8月','9月','10月','11月','12月','1月','２月','３月'],
    index=['整理','整頓','清掃','清潔','躾'])

    fig,ax=plt.subplots(figsize=(17,9))
    for i in range(len(dataset)):
        ax.bar(dataset.columns,dataset.iloc[i],bottom=dataset.iloc[:i].sum())
        for j in range(len(dataset.columns)):
            plt.text(x=j,
            y=dataset.iloc[:i,j].sum()+(dataset.iloc[i,j]/2),
            s=dataset.iloc[i,j],
            ha='center',
            va='bottom'
            )
    plt.title(f'【5Sパトロール結果:チーム{team_all_6z}】',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=23)
    plt.ylabel(f'{ten}点以上で合格【点】',fontsize=23)
    plt.font='IPAexGothic'
    #ax.set(xlabel='【月】',ylabel='【点】85点以上で合格',title=f'【5Sパトロール結果:チーム{team_all_6z}】')
    ax.legend(dataset.index)
    ax.axhline(y=ten,xmin=0,xmax=120,
    color='red',
    lw=2,
    ls='--',
    alpha=0.6)

def plt2svg_e():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_e(request):
    setplt_e()
    svg=plt2svg_e()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response


def setplt_z():



    data=kakutuki.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_1=data[0]
    data_2=data[1]
    data_3=data[2]
    data_4=data[3]
    data_5=data[4]
    data_6=data[5]
    data_7=data[6]
    data_8=data[7]
    data_9=data[8]
    data_10=data[9]
    data_11=data[10]
    data_12=data[11]

    data_a=kakutuki_a.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_a_1=data_a[0]
    data_a_2=data_a[1]
    data_a_3=data_a[2]
    data_a_4=data_a[3]
    data_a_5=data_a[4]
    data_a_6=data_a[5]
    data_a_7=data_a[6]
    data_a_8=data_a[7]
    data_a_9=data_a[8]
    data_a_10=data_a[9]
    data_a_11=data_a[10]
    data_a_12=data_a[11]

    data_b=kakutuki_b.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_b_1=data_b[0]
    data_b_2=data_b[1]
    data_b_3=data_b[2]
    data_b_4=data_b[3]
    data_b_5=data_b[4]
    data_b_6=data_b[5]
    data_b_7=data_b[6]
    data_b_8=data_b[7]
    data_b_9=data_b[8]
    data_b_10=data_b[9]
    data_b_11=data_b[10]
    data_b_12=data_b[11]

    data_c=kakutuki_c.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_c_1=data_c[0]
    data_c_2=data_c[1]
    data_c_3=data_c[2]
    data_c_4=data_c[3]
    data_c_5=data_c[4]
    data_c_6=data_c[5]
    data_c_7=data_c[6]
    data_c_8=data_c[7]
    data_c_9=data_c[8]
    data_c_10=data_c[9]
    data_c_11=data_c[10]
    data_c_12=data_c[11]

    data_d=kakutuki_d.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_d_1=data_d[0]
    data_d_2=data_d[1]
    data_d_3=data_d[2]
    data_d_4=data_d[3]
    data_d_5=data_d[4]
    data_d_6=data_d[5]
    data_d_7=data_d[6]
    data_d_8=data_d[7]
    data_d_9=data_d[8]
    data_d_10=data_d[9]
    data_d_11=data_d[10]
    data_d_12=data_d[11]
    
    data_e=kakutuki_e.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_e_1=data_e[0]
    data_e_2=data_e[1]
    data_e_3=data_e[2]
    data_e_4=data_e[3]
    data_e_5=data_e[4]
    data_e_6=data_e[5]
    data_e_7=data_e[6]
    data_e_8=data_e[7]
    data_e_9=data_e[8]
    data_e_10=data_e[9]
    data_e_11=data_e[10]
    data_e_12=data_e[11]




    team_a_1=data_1['seiri_in']+data_1['seiton_in']+data_1['seisou_in']+data_1['seiketu_in']+data_1['situke_in']
    team_a_2=data_2['seiri_in']+data_2['seiton_in']+data_2['seisou_in']+data_2['seiketu_in']+data_2['situke_in']
    team_a_3=data_3['seiri_in']+data_3['seiton_in']+data_3['seisou_in']+data_3['seiketu_in']+data_3['situke_in']
    team_a_4=data_4['seiri_in']+data_4['seiton_in']+data_4['seisou_in']+data_4['seiketu_in']+data_4['situke_in']
    team_a_5=data_5['seiri_in']+data_5['seiton_in']+data_5['seisou_in']+data_5['seiketu_in']+data_5['situke_in']
    team_a_6=data_6['seiri_in']+data_6['seiton_in']+data_6['seisou_in']+data_6['seiketu_in']+data_6['situke_in']
    team_a_7=data_7['seiri_in']+data_7['seiton_in']+data_7['seisou_in']+data_7['seiketu_in']+data_7['situke_in']
    team_a_8=data_8['seiri_in']+data_8['seiton_in']+data_8['seisou_in']+data_8['seiketu_in']+data_8['situke_in']
    team_a_9=data_9['seiri_in']+data_9['seiton_in']+data_9['seisou_in']+data_9['seiketu_in']+data_9['situke_in']
    team_a_10=data_10['seiri_in']+data_10['seiton_in']+data_10['seisou_in']+data_10['seiketu_in']+data_10['situke_in']
    team_a_11=data_11['seiri_in']+data_11['seiton_in']+data_11['seisou_in']+data_11['seiketu_in']+data_11['situke_in']
    team_a_12=data_12['seiri_in']+data_12['seiton_in']+data_12['seisou_in']+data_12['seiketu_in']+data_12['situke_in']

    team_b_1=data_a_1['seiri_in']+data_a_1['seiton_in']+data_a_1['seisou_in']+data_a_1['seiketu_in']+data_a_1['situke_in']
    team_b_2=data_a_2['seiri_in']+data_a_2['seiton_in']+data_a_2['seisou_in']+data_a_2['seiketu_in']+data_a_2['situke_in']
    team_b_3=data_a_3['seiri_in']+data_a_3['seiton_in']+data_a_3['seisou_in']+data_a_3['seiketu_in']+data_a_3['situke_in']
    team_b_4=data_a_4['seiri_in']+data_a_4['seiton_in']+data_a_4['seisou_in']+data_a_4['seiketu_in']+data_a_4['situke_in']
    team_b_5=data_a_5['seiri_in']+data_a_5['seiton_in']+data_a_5['seisou_in']+data_a_5['seiketu_in']+data_a_5['situke_in']
    team_b_6=data_a_6['seiri_in']+data_a_6['seiton_in']+data_a_6['seisou_in']+data_a_6['seiketu_in']+data_a_6['situke_in']
    team_b_7=data_a_7['seiri_in']+data_a_7['seiton_in']+data_a_7['seisou_in']+data_a_7['seiketu_in']+data_a_7['situke_in']
    team_b_8=data_a_8['seiri_in']+data_a_8['seiton_in']+data_a_8['seisou_in']+data_a_8['seiketu_in']+data_a_8['situke_in']
    team_b_9=data_a_9['seiri_in']+data_a_9['seiton_in']+data_a_9['seisou_in']+data_a_9['seiketu_in']+data_a_9['situke_in']
    team_b_10=data_a_10['seiri_in']+data_a_10['seiton_in']+data_a_10['seisou_in']+data_a_10['seiketu_in']+data_a_10['situke_in']
    team_b_11=data_a_11['seiri_in']+data_a_11['seiton_in']+data_a_11['seisou_in']+data_a_11['seiketu_in']+data_a_11['situke_in']
    team_b_12=data_a_12['seiri_in']+data_a_12['seiton_in']+data_a_12['seisou_in']+data_a_12['seiketu_in']+data_a_12['situke_in']

    team_c_1=data_b_1['seiri_in']+data_b_1['seiton_in']+data_b_1['seisou_in']+data_b_1['seiketu_in']+data_b_1['situke_in']
    team_c_2=data_b_2['seiri_in']+data_b_2['seiton_in']+data_b_2['seisou_in']+data_b_2['seiketu_in']+data_b_2['situke_in']
    team_c_3=data_b_3['seiri_in']+data_b_3['seiton_in']+data_b_3['seisou_in']+data_b_3['seiketu_in']+data_b_3['situke_in']
    team_c_4=data_b_4['seiri_in']+data_b_4['seiton_in']+data_b_4['seisou_in']+data_b_4['seiketu_in']+data_b_4['situke_in']
    team_c_5=data_b_5['seiri_in']+data_b_5['seiton_in']+data_b_5['seisou_in']+data_b_5['seiketu_in']+data_b_5['situke_in']
    team_c_6=data_b_6['seiri_in']+data_b_6['seiton_in']+data_b_6['seisou_in']+data_b_6['seiketu_in']+data_b_6['situke_in']
    team_c_7=data_b_7['seiri_in']+data_b_7['seiton_in']+data_b_7['seisou_in']+data_b_7['seiketu_in']+data_b_7['situke_in']
    team_c_8=data_b_8['seiri_in']+data_b_8['seiton_in']+data_b_8['seisou_in']+data_b_8['seiketu_in']+data_b_8['situke_in']
    team_c_9=data_b_9['seiri_in']+data_b_9['seiton_in']+data_b_9['seisou_in']+data_b_9['seiketu_in']+data_b_9['situke_in']
    team_c_10=data_b_10['seiri_in']+data_b_10['seiton_in']+data_b_10['seisou_in']+data_b_10['seiketu_in']+data_b_10['situke_in']
    team_c_11=data_b_11['seiri_in']+data_b_11['seiton_in']+data_b_11['seisou_in']+data_b_11['seiketu_in']+data_b_11['situke_in']
    team_c_12=data_b_12['seiri_in']+data_b_12['seiton_in']+data_b_12['seisou_in']+data_b_12['seiketu_in']+data_b_12['situke_in']

    team_d_1=data_c_1['seiri_in']+data_c_1['seiton_in']+data_c_1['seisou_in']+data_c_1['seiketu_in']+data_c_1['situke_in']
    team_d_2=data_c_2['seiri_in']+data_c_2['seiton_in']+data_c_2['seisou_in']+data_c_2['seiketu_in']+data_c_2['situke_in']
    team_d_3=data_c_3['seiri_in']+data_c_3['seiton_in']+data_c_3['seisou_in']+data_c_3['seiketu_in']+data_c_3['situke_in']
    team_d_4=data_c_4['seiri_in']+data_c_4['seiton_in']+data_c_4['seisou_in']+data_c_4['seiketu_in']+data_c_4['situke_in']
    team_d_5=data_c_5['seiri_in']+data_c_5['seiton_in']+data_c_5['seisou_in']+data_c_5['seiketu_in']+data_c_5['situke_in']
    team_d_6=data_c_6['seiri_in']+data_c_6['seiton_in']+data_c_6['seisou_in']+data_c_6['seiketu_in']+data_c_6['situke_in']
    team_d_7=data_c_7['seiri_in']+data_c_7['seiton_in']+data_c_7['seisou_in']+data_c_7['seiketu_in']+data_c_7['situke_in']
    team_d_8=data_c_8['seiri_in']+data_c_8['seiton_in']+data_c_8['seisou_in']+data_c_8['seiketu_in']+data_c_8['situke_in']
    team_d_9=data_c_9['seiri_in']+data_c_9['seiton_in']+data_c_9['seisou_in']+data_c_9['seiketu_in']+data_c_9['situke_in']
    team_d_10=data_c_10['seiri_in']+data_c_10['seiton_in']+data_c_10['seisou_in']+data_c_10['seiketu_in']+data_c_10['situke_in']
    team_d_11=data_c_11['seiri_in']+data_c_11['seiton_in']+data_c_11['seisou_in']+data_c_11['seiketu_in']+data_c_11['situke_in']
    team_d_12=data_c_12['seiri_in']+data_c_12['seiton_in']+data_c_12['seisou_in']+data_c_12['seiketu_in']+data_c_12['situke_in']

    team_e_1=data_d_1['seiri_in']+data_d_1['seiton_in']+data_d_1['seisou_in']+data_d_1['seiketu_in']+data_d_1['situke_in']
    team_e_2=data_d_2['seiri_in']+data_d_2['seiton_in']+data_d_2['seisou_in']+data_d_2['seiketu_in']+data_d_2['situke_in']
    team_e_3=data_d_3['seiri_in']+data_d_3['seiton_in']+data_d_3['seisou_in']+data_d_3['seiketu_in']+data_d_3['situke_in']
    team_e_4=data_d_4['seiri_in']+data_d_4['seiton_in']+data_d_4['seisou_in']+data_d_4['seiketu_in']+data_d_4['situke_in']
    team_e_5=data_d_5['seiri_in']+data_d_5['seiton_in']+data_d_5['seisou_in']+data_d_5['seiketu_in']+data_d_5['situke_in']
    team_e_6=data_d_6['seiri_in']+data_d_6['seiton_in']+data_d_6['seisou_in']+data_d_6['seiketu_in']+data_d_6['situke_in']
    team_e_7=data_d_7['seiri_in']+data_d_7['seiton_in']+data_d_7['seisou_in']+data_d_7['seiketu_in']+data_d_7['situke_in']
    team_e_8=data_d_8['seiri_in']+data_d_8['seiton_in']+data_d_8['seisou_in']+data_d_8['seiketu_in']+data_d_8['situke_in']
    team_e_9=data_d_9['seiri_in']+data_d_9['seiton_in']+data_d_9['seisou_in']+data_d_9['seiketu_in']+data_d_9['situke_in']
    team_e_10=data_d_10['seiri_in']+data_d_10['seiton_in']+data_d_10['seisou_in']+data_d_10['seiketu_in']+data_d_10['situke_in']
    team_e_11=data_d_11['seiri_in']+data_d_11['seiton_in']+data_d_11['seisou_in']+data_d_11['seiketu_in']+data_d_11['situke_in']
    team_e_12=data_d_12['seiri_in']+data_d_12['seiton_in']+data_d_12['seisou_in']+data_d_12['seiketu_in']+data_d_12['situke_in']

    team_f_1=data_e_1['seiri_in']+data_e_1['seiton_in']+data_e_1['seisou_in']+data_e_1['seiketu_in']+data_e_1['situke_in']
    team_f_2=data_e_2['seiri_in']+data_e_2['seiton_in']+data_e_2['seisou_in']+data_e_2['seiketu_in']+data_e_2['situke_in']
    team_f_3=data_e_3['seiri_in']+data_e_3['seiton_in']+data_e_3['seisou_in']+data_e_3['seiketu_in']+data_e_3['situke_in']
    team_f_4=data_e_4['seiri_in']+data_e_4['seiton_in']+data_e_4['seisou_in']+data_e_4['seiketu_in']+data_e_4['situke_in']
    team_f_5=data_e_5['seiri_in']+data_e_5['seiton_in']+data_e_5['seisou_in']+data_e_5['seiketu_in']+data_e_5['situke_in']
    team_f_6=data_e_6['seiri_in']+data_e_6['seiton_in']+data_e_6['seisou_in']+data_e_6['seiketu_in']+data_e_6['situke_in']
    team_f_7=data_e_7['seiri_in']+data_e_7['seiton_in']+data_e_7['seisou_in']+data_e_7['seiketu_in']+data_e_7['situke_in']
    team_f_8=data_e_8['seiri_in']+data_e_8['seiton_in']+data_e_8['seisou_in']+data_e_8['seiketu_in']+data_e_8['situke_in']
    team_f_9=data_e_9['seiri_in']+data_e_9['seiton_in']+data_e_9['seisou_in']+data_e_9['seiketu_in']+data_e_9['situke_in']
    team_f_10=data_e_10['seiri_in']+data_e_10['seiton_in']+data_e_10['seisou_in']+data_e_10['seiketu_in']+data_e_10['situke_in']
    team_f_11=data_e_11['seiri_in']+data_e_11['seiton_in']+data_e_11['seisou_in']+data_e_11['seiketu_in']+data_e_11['situke_in']
    team_f_12=data_e_12['seiri_in']+data_e_12['seiton_in']+data_e_12['seisou_in']+data_e_12['seiketu_in']+data_e_12['situke_in']
    



    line_1_list=[team_a_1,team_b_1,team_c_1,team_d_1,team_e_1,team_f_1]
    line_2_list=[team_a_2,team_b_2,team_c_2,team_d_2,team_e_2,team_f_2]
    line_3_list=[team_a_3,team_b_3,team_c_3,team_d_3,team_e_3,team_f_3]
    line_4_list=[team_a_4,team_b_4,team_c_4,team_d_4,team_e_4,team_f_4]
    line_5_list=[team_a_5,team_b_5,team_c_5,team_d_5,team_e_5,team_f_5]
    line_6_list=[team_a_6,team_b_6,team_c_6,team_d_6,team_e_6,team_f_6]
    line_7_list=[team_a_7,team_b_7,team_c_7,team_d_7,team_e_7,team_f_7]
    line_8_list=[team_a_8,team_b_8,team_c_8,team_d_8,team_e_8,team_f_8]
    line_9_list=[team_a_9,team_b_9,team_c_9,team_d_9,team_e_9,team_f_9]
    line_10_list=[team_a_10,team_b_10,team_c_10,team_d_10,team_e_10,team_f_10]
    line_11_list=[team_a_11,team_b_11,team_c_11,team_d_11,team_e_11,team_f_11]
    line_12_list=[team_a_12,team_b_12,team_c_12,team_d_12,team_e_12,team_f_12]

    line_1_list2=[ai for ai in line_1_list if ai > 0 ]
    line_2_list2=[bi for bi in line_2_list if bi > 0 ]
    line_3_list2=[ci for ci in line_3_list if ci > 0 ]
    line_4_list2=[di for di in line_4_list if di > 0 ]
    line_5_list2=[ei for ei in line_5_list if ei > 0 ]
    line_6_list2=[fi for fi in line_6_list if fi > 0 ]
    line_7_list2=[gi for gi in line_7_list if gi > 0 ]
    line_8_list2=[hi for hi in line_8_list if hi > 0 ]
    line_9_list2=[ii for ii in line_9_list if ii > 0 ]
    line_10_list2=[ji for ji in line_10_list if ji > 0 ]
    line_11_list2=[ki for ki in line_11_list if ki > 0 ]
    line_12_list2=[li for li in line_12_list if li > 0 ]
    

    line_1_list3=len(line_1_list2)
    if line_1_list3 == 0:
        line_1_list3=1

    line_2_list3=len(line_2_list2)
    if line_2_list3 == 0:
        line_2_list3=1
    
    line_3_list3=len(line_3_list2)
    if line_3_list3 == 0:
        line_3_list3=1
    
    line_4_list3=len(line_4_list2)
    if line_4_list3 == 0:
        line_4_list3=1
    
    line_5_list3=len(line_5_list2)
    if line_5_list3 == 0:
        line_5_list3=1

    line_6_list3=len(line_6_list2)
    if line_6_list3 == 0:
        line_6_list3=1

    line_7_list3=len(line_7_list2)
    if line_7_list3 == 0:
        line_7_list3=1
    
    line_8_list3=len(line_8_list2)
    if line_8_list3 == 0:
        line_8_list3=1
    
    line_9_list3=len(line_9_list2)
    if line_9_list3 == 0:
        line_9_list3=1
    
    line_10_list3=len(line_10_list2)
    if line_10_list3 == 0:
        line_10_list3=1

    line_11_list3=len(line_11_list2)
    if line_11_list3 == 0:
        line_11_list3=1

    line_12_list3=len(line_12_list2)
    if line_12_list3 == 0:
        line_12_list3=1

    ave_1=(team_a_1+team_b_1+team_c_1+team_d_1+team_e_1+team_f_1) / line_1_list3
    ave_2=(team_a_2+team_b_2+team_c_2+team_d_2+team_e_2+team_f_2) / line_2_list3
    ave_3=(team_a_3+team_b_3+team_c_3+team_d_3+team_e_3+team_f_3) / line_3_list3
    ave_4=(team_a_4+team_b_4+team_c_4+team_d_4+team_e_4+team_f_4) / line_4_list3
    ave_5=(team_a_5+team_b_5+team_c_5+team_d_5+team_e_5+team_f_5) / line_5_list3
    ave_6=(team_a_6+team_b_6+team_c_6+team_d_6+team_e_6+team_f_6) / line_6_list3
    ave_7=(team_a_7+team_b_7+team_c_7+team_d_7+team_e_7+team_f_7) / line_7_list3
    ave_8=(team_a_8+team_b_8+team_c_8+team_d_8+team_e_8+team_f_8) / line_8_list3
    ave_9=(team_a_9+team_b_9+team_c_9+team_d_9+team_e_9+team_f_9) / line_9_list3
    ave_10=(team_a_10+team_b_10+team_c_10+team_d_10+team_e_10+team_f_10) / line_10_list3
    ave_11=(team_a_11+team_b_11+team_c_11+team_d_11+team_e_11+team_f_11) / line_11_list3
    ave_12=(team_a_12+team_b_12+team_c_12+team_d_12+team_e_12+team_f_12) / line_12_list3



    team_all=team.objects.all().values('team_name')
    team_all_1=team_all[0]
    team_all_2=team_all[1]
    team_all_3=team_all[2]
    team_all_4=team_all[3]
    team_all_5=team_all[4]
    team_all_6=team_all[5]

    team_all_1z=team_all_1['team_name']
    team_all_2z=team_all_2['team_name']
    team_all_3z=team_all_3['team_name']
    team_all_4z=team_all_4['team_name']
    team_all_5z=team_all_5['team_name']
    team_all_6z=team_all_6['team_name']


    goukaku_all=goukaku.objects.all().values('kijunten_in')
    goukaku_all_1=goukaku_all[0]
    goukaku_all_2=goukaku_all[1]
    goukaku_all_3=goukaku_all[2]
    goukaku_all_4=goukaku_all[3]
    goukaku_all_5=goukaku_all[4]
    goukaku_all_6=goukaku_all[5]
    goukaku_all_7=goukaku_all[6]
    goukaku_all_8=goukaku_all[7]
    goukaku_all_9=goukaku_all[8]
    goukaku_all_10=goukaku_all[9]
    goukaku_all_11=goukaku_all[10]
    goukaku_all_12=goukaku_all[11]

    goukaku_all_1z=goukaku_all_1['kijunten_in']
    goukaku_all_2z=goukaku_all_2['kijunten_in']
    goukaku_all_3z=goukaku_all_3['kijunten_in']
    goukaku_all_4z=goukaku_all_4['kijunten_in']
    goukaku_all_5z=goukaku_all_5['kijunten_in']
    goukaku_all_6z=goukaku_all_6['kijunten_in']
    goukaku_all_7z=goukaku_all_7['kijunten_in']
    goukaku_all_8z=goukaku_all_8['kijunten_in']
    goukaku_all_9z=goukaku_all_9['kijunten_in']
    goukaku_all_10z=goukaku_all_10['kijunten_in']
    goukaku_all_11z=goukaku_all_11['kijunten_in']
    goukaku_all_12z=goukaku_all_12['kijunten_in']

    a_a=team_all_1z
    b_b=team_all_2z
    c_c=team_all_3z
    d_d=team_all_4z
    e_e=team_all_5z
    f_f=team_all_6z
    g='合格点数'
    h='チーム平均'

    aa='4月'
    bb='5月'
    cc='6月'
    dd='7月'
    ee='8月'
    ff='9月'
    gg='10月'
    hh='11月'
    ii='12月'
    jj='1月'
    kk='2月'
    ll='3月'

    columns=[a_a,b_b,c_c,d_d,e_e,f_f,g,h]
    index=index=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll]

    a1=team_a_1
    a2=team_b_1
    a3=team_c_1
    a4=team_d_1
    a5=team_e_1
    a6=team_f_1
    a85=goukaku_all_1z
    a_h=ave_1

    b7=team_a_2
    b8=team_b_2
    b9=team_c_2
    b10=team_d_2
    b11=team_e_2
    b12=team_f_2
    b85=goukaku_all_2z
    b_h=ave_2

    c13=team_a_3
    c14=team_b_3
    c15=team_c_3
    c16=team_d_3
    c17=team_e_3
    c18=team_f_3
    c85=goukaku_all_3z
    c_h=ave_3

    d19=team_a_4
    d20=team_b_4
    d21=team_c_4
    d22=team_d_4
    d23=team_e_4
    d24=team_f_4
    d85=goukaku_all_4z
    d_h=ave_4

    e25=team_a_5
    e26=team_b_5
    e27=team_c_5
    e28=team_d_5
    e29=team_e_5
    e30=team_f_5
    e85=goukaku_all_5z
    e_h=ave_5

    f31=team_a_6
    f32=team_b_6
    f33=team_c_6
    f34=team_d_6
    f35=team_e_6
    f36=team_f_6
    f85=goukaku_all_6z
    f_h=ave_6

    g37=team_a_7
    g38=team_b_7
    g39=team_c_7
    g40=team_d_7
    g41=team_e_7
    g42=team_f_7
    g85=goukaku_all_7z
    g_h=ave_7

    h43=team_a_8
    h44=team_b_8
    h45=team_c_8
    h46=team_d_8
    h47=team_e_8
    h48=team_f_8
    h85=goukaku_all_8z
    h_h=ave_8

    i49=team_a_9
    i50=team_b_9
    i51=team_c_9
    i52=team_d_9
    i53=team_e_9
    i54=team_f_9
    i85=goukaku_all_9z
    i_h=ave_9

    j55=team_a_10
    j56=team_b_10
    j57=team_c_10
    j58=team_d_10
    j59=team_e_10
    j60=team_f_10
    j85=goukaku_all_10z
    j_h=ave_10

    k61=team_a_11
    k62=team_b_11
    k63=team_c_11
    k64=team_d_11
    k65=team_e_11
    k66=team_f_11
    k85=goukaku_all_11z
    k_h=ave_11

    l67=team_a_12
    l68=team_b_12
    l69=team_c_12
    l70=team_d_12
    l71=team_e_12
    l72=team_f_12
    l85=goukaku_all_12z
    l_h=ave_12

    df_a=pd.DataFrame([[a1,a2,a3,a4,a5,a6,a85,a_h],[b7,b8,b9,b10,b11,b12,b85,b_h],[c13,c14,c15,c16,c17,c18,c85,c_h],[d19,d20,d21,d22,d23,d24,d85,d_h],[e25,e26,e27,e28,e29,e30,e85,e_h],[f31,f32,f33,f34,f35,f36,f85,f_h],[g37,g38,g39,g40,g41,g42,g85,g_h],[h43,h44,h45,h46,h47,h48,h85,h_h],[i49,i50,i51,i52,i53,i54,i85,i_h],[j55,j56,j57,j58,j59,j60,j85,j_h],[k61,k62,k63,k64,k65,k66,k85,k_h],[l67,l68,l69,l70,l71,l72,l85,l_h]],index=index,columns=columns)
    figure(num=None, figsize=(16, 9))
    plt.title('5Sパトロール点数推移[チーム別]',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=25)
    plt.ylabel('点数【点】',fontsize=25)
    plt.plot(list(df_a.index),df_a[a_a],marker='o',label=a_a)
    plt.plot(list(df_a.index),df_a[b_b],marker='o',label=b_b)
    plt.plot(list(df_a.index),df_a[c_c],marker='o',label=c_c)
    plt.plot(list(df_a.index),df_a[d_d],marker='o',label=d_d)
    plt.plot(list(df_a.index),df_a[e_e],marker='o',label=e_e)
    plt.plot(list(df_a.index),df_a[f_f],marker='o',label=f_f)
    plt.plot(list(df_a.index),df_a['合格点数'],marker='x',label='合格点数')
    plt.plot(list(df_a.index),df_a['チーム平均'],marker='s',label='チーム平均')
    plt.legend()


def plt2svg_z():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_z(request):
    setplt_z()
    svg=plt2svg_z()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response

def setplt_zz():
    goukaku_all=goukaku.objects.all().values('kijunten_in')
    goukaku_all_1=goukaku_all[0]
    goukaku_all_2=goukaku_all[1]
    goukaku_all_3=goukaku_all[2]
    goukaku_all_4=goukaku_all[3]
    goukaku_all_5=goukaku_all[4]
    goukaku_all_6=goukaku_all[5]
    goukaku_all_7=goukaku_all[6]
    goukaku_all_8=goukaku_all[7]
    goukaku_all_9=goukaku_all[8]
    goukaku_all_10=goukaku_all[9]
    goukaku_all_11=goukaku_all[10]
    goukaku_all_12=goukaku_all[11]

    goukaku_all_1z=goukaku_all_1['kijunten_in']
    goukaku_all_2z=goukaku_all_2['kijunten_in']
    goukaku_all_3z=goukaku_all_3['kijunten_in']
    goukaku_all_4z=goukaku_all_4['kijunten_in']
    goukaku_all_5z=goukaku_all_5['kijunten_in']
    goukaku_all_6z=goukaku_all_6['kijunten_in']
    goukaku_all_7z=goukaku_all_7['kijunten_in']
    goukaku_all_8z=goukaku_all_8['kijunten_in']
    goukaku_all_9z=goukaku_all_9['kijunten_in']
    goukaku_all_10z=goukaku_all_10['kijunten_in']
    goukaku_all_11z=goukaku_all_11['kijunten_in']
    goukaku_all_12z=goukaku_all_12['kijunten_in']

    data=kakutuki.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_1=data[0]
    data_2=data[1]
    data_3=data[2]
    data_4=data[3]
    data_5=data[4]
    data_6=data[5]
    data_7=data[6]
    data_8=data[7]
    data_9=data[8]
    data_10=data[9]
    data_11=data[10]
    data_12=data[11]

    data_a=kakutuki_a.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_a_1=data_a[0]
    data_a_2=data_a[1]
    data_a_3=data_a[2]
    data_a_4=data_a[3]
    data_a_5=data_a[4]
    data_a_6=data_a[5]
    data_a_7=data_a[6]
    data_a_8=data_a[7]
    data_a_9=data_a[8]
    data_a_10=data_a[9]
    data_a_11=data_a[10]
    data_a_12=data_a[11]

    data_b=kakutuki_b.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_b_1=data_b[0]
    data_b_2=data_b[1]
    data_b_3=data_b[2]
    data_b_4=data_b[3]
    data_b_5=data_b[4]
    data_b_6=data_b[5]
    data_b_7=data_b[6]
    data_b_8=data_b[7]
    data_b_9=data_b[8]
    data_b_10=data_b[9]
    data_b_11=data_b[10]
    data_b_12=data_b[11]

    data_c=kakutuki_c.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_c_1=data_c[0]
    data_c_2=data_c[1]
    data_c_3=data_c[2]
    data_c_4=data_c[3]
    data_c_5=data_c[4]
    data_c_6=data_c[5]
    data_c_7=data_c[6]
    data_c_8=data_c[7]
    data_c_9=data_c[8]
    data_c_10=data_c[9]
    data_c_11=data_c[10]
    data_c_12=data_c[11]

    data_d=kakutuki_d.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_d_1=data_d[0]
    data_d_2=data_d[1]
    data_d_3=data_d[2]
    data_d_4=data_d[3]
    data_d_5=data_d[4]
    data_d_6=data_d[5]
    data_d_7=data_d[6]
    data_d_8=data_d[7]
    data_d_9=data_d[8]
    data_d_10=data_d[9]
    data_d_11=data_d[10]
    data_d_12=data_d[11]
    
    data_e=kakutuki_e.objects.all().values('seiri_in','seiton_in','seiketu_in','seisou_in','situke_in')
    data_e_1=data_e[0]
    data_e_2=data_e[1]
    data_e_3=data_e[2]
    data_e_4=data_e[3]
    data_e_5=data_e[4]
    data_e_6=data_e[5]
    data_e_7=data_e[6]
    data_e_8=data_e[7]
    data_e_9=data_e[8]
    data_e_10=data_e[9]
    data_e_11=data_e[10]
    data_e_12=data_e[11]




    team_a_1=data_1['seiri_in']+data_1['seiton_in']+data_1['seisou_in']+data_1['seiketu_in']+data_1['situke_in']
    team_a_2=data_2['seiri_in']+data_2['seiton_in']+data_2['seisou_in']+data_2['seiketu_in']+data_2['situke_in']
    team_a_3=data_3['seiri_in']+data_3['seiton_in']+data_3['seisou_in']+data_3['seiketu_in']+data_3['situke_in']
    team_a_4=data_4['seiri_in']+data_4['seiton_in']+data_4['seisou_in']+data_4['seiketu_in']+data_4['situke_in']
    team_a_5=data_5['seiri_in']+data_5['seiton_in']+data_5['seisou_in']+data_5['seiketu_in']+data_5['situke_in']
    team_a_6=data_6['seiri_in']+data_6['seiton_in']+data_6['seisou_in']+data_6['seiketu_in']+data_6['situke_in']
    team_a_7=data_7['seiri_in']+data_7['seiton_in']+data_7['seisou_in']+data_7['seiketu_in']+data_7['situke_in']
    team_a_8=data_8['seiri_in']+data_8['seiton_in']+data_8['seisou_in']+data_8['seiketu_in']+data_8['situke_in']
    team_a_9=data_9['seiri_in']+data_9['seiton_in']+data_9['seisou_in']+data_9['seiketu_in']+data_9['situke_in']
    team_a_10=data_10['seiri_in']+data_10['seiton_in']+data_10['seisou_in']+data_10['seiketu_in']+data_10['situke_in']
    team_a_11=data_11['seiri_in']+data_11['seiton_in']+data_11['seisou_in']+data_11['seiketu_in']+data_11['situke_in']
    team_a_12=data_12['seiri_in']+data_12['seiton_in']+data_12['seisou_in']+data_12['seiketu_in']+data_12['situke_in']

    team_b_1=data_a_1['seiri_in']+data_a_1['seiton_in']+data_a_1['seisou_in']+data_a_1['seiketu_in']+data_a_1['situke_in']
    team_b_2=data_a_2['seiri_in']+data_a_2['seiton_in']+data_a_2['seisou_in']+data_a_2['seiketu_in']+data_a_2['situke_in']
    team_b_3=data_a_3['seiri_in']+data_a_3['seiton_in']+data_a_3['seisou_in']+data_a_3['seiketu_in']+data_a_3['situke_in']
    team_b_4=data_a_4['seiri_in']+data_a_4['seiton_in']+data_a_4['seisou_in']+data_a_4['seiketu_in']+data_a_4['situke_in']
    team_b_5=data_a_5['seiri_in']+data_a_5['seiton_in']+data_a_5['seisou_in']+data_a_5['seiketu_in']+data_a_5['situke_in']
    team_b_6=data_a_6['seiri_in']+data_a_6['seiton_in']+data_a_6['seisou_in']+data_a_6['seiketu_in']+data_a_6['situke_in']
    team_b_7=data_a_7['seiri_in']+data_a_7['seiton_in']+data_a_7['seisou_in']+data_a_7['seiketu_in']+data_a_7['situke_in']
    team_b_8=data_a_8['seiri_in']+data_a_8['seiton_in']+data_a_8['seisou_in']+data_a_8['seiketu_in']+data_a_8['situke_in']
    team_b_9=data_a_9['seiri_in']+data_a_9['seiton_in']+data_a_9['seisou_in']+data_a_9['seiketu_in']+data_a_9['situke_in']
    team_b_10=data_a_10['seiri_in']+data_a_10['seiton_in']+data_a_10['seisou_in']+data_a_10['seiketu_in']+data_a_10['situke_in']
    team_b_11=data_a_11['seiri_in']+data_a_11['seiton_in']+data_a_11['seisou_in']+data_a_11['seiketu_in']+data_a_11['situke_in']
    team_b_12=data_a_12['seiri_in']+data_a_12['seiton_in']+data_a_12['seisou_in']+data_a_12['seiketu_in']+data_a_12['situke_in']

    team_c_1=data_b_1['seiri_in']+data_b_1['seiton_in']+data_b_1['seisou_in']+data_b_1['seiketu_in']+data_b_1['situke_in']
    team_c_2=data_b_2['seiri_in']+data_b_2['seiton_in']+data_b_2['seisou_in']+data_b_2['seiketu_in']+data_b_2['situke_in']
    team_c_3=data_b_3['seiri_in']+data_b_3['seiton_in']+data_b_3['seisou_in']+data_b_3['seiketu_in']+data_b_3['situke_in']
    team_c_4=data_b_4['seiri_in']+data_b_4['seiton_in']+data_b_4['seisou_in']+data_b_4['seiketu_in']+data_b_4['situke_in']
    team_c_5=data_b_5['seiri_in']+data_b_5['seiton_in']+data_b_5['seisou_in']+data_b_5['seiketu_in']+data_b_5['situke_in']
    team_c_6=data_b_6['seiri_in']+data_b_6['seiton_in']+data_b_6['seisou_in']+data_b_6['seiketu_in']+data_b_6['situke_in']
    team_c_7=data_b_7['seiri_in']+data_b_7['seiton_in']+data_b_7['seisou_in']+data_b_7['seiketu_in']+data_b_7['situke_in']
    team_c_8=data_b_8['seiri_in']+data_b_8['seiton_in']+data_b_8['seisou_in']+data_b_8['seiketu_in']+data_b_8['situke_in']
    team_c_9=data_b_9['seiri_in']+data_b_9['seiton_in']+data_b_9['seisou_in']+data_b_9['seiketu_in']+data_b_9['situke_in']
    team_c_10=data_b_10['seiri_in']+data_b_10['seiton_in']+data_b_10['seisou_in']+data_b_10['seiketu_in']+data_b_10['situke_in']
    team_c_11=data_b_11['seiri_in']+data_b_11['seiton_in']+data_b_11['seisou_in']+data_b_11['seiketu_in']+data_b_11['situke_in']
    team_c_12=data_b_12['seiri_in']+data_b_12['seiton_in']+data_b_12['seisou_in']+data_b_12['seiketu_in']+data_b_12['situke_in']

    team_d_1=data_c_1['seiri_in']+data_c_1['seiton_in']+data_c_1['seisou_in']+data_c_1['seiketu_in']+data_c_1['situke_in']
    team_d_2=data_c_2['seiri_in']+data_c_2['seiton_in']+data_c_2['seisou_in']+data_c_2['seiketu_in']+data_c_2['situke_in']
    team_d_3=data_c_3['seiri_in']+data_c_3['seiton_in']+data_c_3['seisou_in']+data_c_3['seiketu_in']+data_c_3['situke_in']
    team_d_4=data_c_4['seiri_in']+data_c_4['seiton_in']+data_c_4['seisou_in']+data_c_4['seiketu_in']+data_c_4['situke_in']
    team_d_5=data_c_5['seiri_in']+data_c_5['seiton_in']+data_c_5['seisou_in']+data_c_5['seiketu_in']+data_c_5['situke_in']
    team_d_6=data_c_6['seiri_in']+data_c_6['seiton_in']+data_c_6['seisou_in']+data_c_6['seiketu_in']+data_c_6['situke_in']
    team_d_7=data_c_7['seiri_in']+data_c_7['seiton_in']+data_c_7['seisou_in']+data_c_7['seiketu_in']+data_c_7['situke_in']
    team_d_8=data_c_8['seiri_in']+data_c_8['seiton_in']+data_c_8['seisou_in']+data_c_8['seiketu_in']+data_c_8['situke_in']
    team_d_9=data_c_9['seiri_in']+data_c_9['seiton_in']+data_c_9['seisou_in']+data_c_9['seiketu_in']+data_c_9['situke_in']
    team_d_10=data_c_10['seiri_in']+data_c_10['seiton_in']+data_c_10['seisou_in']+data_c_10['seiketu_in']+data_c_10['situke_in']
    team_d_11=data_c_11['seiri_in']+data_c_11['seiton_in']+data_c_11['seisou_in']+data_c_11['seiketu_in']+data_c_11['situke_in']
    team_d_12=data_c_12['seiri_in']+data_c_12['seiton_in']+data_c_12['seisou_in']+data_c_12['seiketu_in']+data_c_12['situke_in']

    team_e_1=data_d_1['seiri_in']+data_d_1['seiton_in']+data_d_1['seisou_in']+data_d_1['seiketu_in']+data_d_1['situke_in']
    team_e_2=data_d_2['seiri_in']+data_d_2['seiton_in']+data_d_2['seisou_in']+data_d_2['seiketu_in']+data_d_2['situke_in']
    team_e_3=data_d_3['seiri_in']+data_d_3['seiton_in']+data_d_3['seisou_in']+data_d_3['seiketu_in']+data_d_3['situke_in']
    team_e_4=data_d_4['seiri_in']+data_d_4['seiton_in']+data_d_4['seisou_in']+data_d_4['seiketu_in']+data_d_4['situke_in']
    team_e_5=data_d_5['seiri_in']+data_d_5['seiton_in']+data_d_5['seisou_in']+data_d_5['seiketu_in']+data_d_5['situke_in']
    team_e_6=data_d_6['seiri_in']+data_d_6['seiton_in']+data_d_6['seisou_in']+data_d_6['seiketu_in']+data_d_6['situke_in']
    team_e_7=data_d_7['seiri_in']+data_d_7['seiton_in']+data_d_7['seisou_in']+data_d_7['seiketu_in']+data_d_7['situke_in']
    team_e_8=data_d_8['seiri_in']+data_d_8['seiton_in']+data_d_8['seisou_in']+data_d_8['seiketu_in']+data_d_8['situke_in']
    team_e_9=data_d_9['seiri_in']+data_d_9['seiton_in']+data_d_9['seisou_in']+data_d_9['seiketu_in']+data_d_9['situke_in']
    team_e_10=data_d_10['seiri_in']+data_d_10['seiton_in']+data_d_10['seisou_in']+data_d_10['seiketu_in']+data_d_10['situke_in']
    team_e_11=data_d_11['seiri_in']+data_d_11['seiton_in']+data_d_11['seisou_in']+data_d_11['seiketu_in']+data_d_11['situke_in']
    team_e_12=data_d_12['seiri_in']+data_d_12['seiton_in']+data_d_12['seisou_in']+data_d_12['seiketu_in']+data_d_12['situke_in']

    team_f_1=data_e_1['seiri_in']+data_e_1['seiton_in']+data_e_1['seisou_in']+data_e_1['seiketu_in']+data_e_1['situke_in']
    team_f_2=data_e_2['seiri_in']+data_e_2['seiton_in']+data_e_2['seisou_in']+data_e_2['seiketu_in']+data_e_2['situke_in']
    team_f_3=data_e_3['seiri_in']+data_e_3['seiton_in']+data_e_3['seisou_in']+data_e_3['seiketu_in']+data_e_3['situke_in']
    team_f_4=data_e_4['seiri_in']+data_e_4['seiton_in']+data_e_4['seisou_in']+data_e_4['seiketu_in']+data_e_4['situke_in']
    team_f_5=data_e_5['seiri_in']+data_e_5['seiton_in']+data_e_5['seisou_in']+data_e_5['seiketu_in']+data_e_5['situke_in']
    team_f_6=data_e_6['seiri_in']+data_e_6['seiton_in']+data_e_6['seisou_in']+data_e_6['seiketu_in']+data_e_6['situke_in']
    team_f_7=data_e_7['seiri_in']+data_e_7['seiton_in']+data_e_7['seisou_in']+data_e_7['seiketu_in']+data_e_7['situke_in']
    team_f_8=data_e_8['seiri_in']+data_e_8['seiton_in']+data_e_8['seisou_in']+data_e_8['seiketu_in']+data_e_8['situke_in']
    team_f_9=data_e_9['seiri_in']+data_e_9['seiton_in']+data_e_9['seisou_in']+data_e_9['seiketu_in']+data_e_9['situke_in']
    team_f_10=data_e_10['seiri_in']+data_e_10['seiton_in']+data_e_10['seisou_in']+data_e_10['seiketu_in']+data_e_10['situke_in']
    team_f_11=data_e_11['seiri_in']+data_e_11['seiton_in']+data_e_11['seisou_in']+data_e_11['seiketu_in']+data_e_11['situke_in']
    team_f_12=data_e_12['seiri_in']+data_e_12['seiton_in']+data_e_12['seisou_in']+data_e_12['seiketu_in']+data_e_12['situke_in']

    line_1_list=[team_a_1,team_b_1,team_c_1,team_d_1,team_e_1,team_f_1]
    line_2_list=[team_a_2,team_b_2,team_c_2,team_d_2,team_e_2,team_f_2]
    line_3_list=[team_a_3,team_b_3,team_c_3,team_d_3,team_e_3,team_f_3]
    line_4_list=[team_a_4,team_b_4,team_c_4,team_d_4,team_e_4,team_f_4]
    line_5_list=[team_a_5,team_b_5,team_c_5,team_d_5,team_e_5,team_f_5]
    line_6_list=[team_a_6,team_b_6,team_c_6,team_d_6,team_e_6,team_f_6]
    line_7_list=[team_a_7,team_b_7,team_c_7,team_d_7,team_e_7,team_f_7]
    line_8_list=[team_a_8,team_b_8,team_c_8,team_d_8,team_e_8,team_f_8]
    line_9_list=[team_a_9,team_b_9,team_c_9,team_d_9,team_e_9,team_f_9]
    line_10_list=[team_a_10,team_b_10,team_c_10,team_d_10,team_e_10,team_f_10]
    line_11_list=[team_a_11,team_b_11,team_c_11,team_d_11,team_e_11,team_f_11]
    line_12_list=[team_a_12,team_b_12,team_c_12,team_d_12,team_e_12,team_f_12]

    line_1_list2=[ai for ai in line_1_list if ai >= goukaku_all_1z]
    line_2_list2=[bi for bi in line_2_list if bi >= goukaku_all_2z]
    line_3_list2=[ci for ci in line_3_list if ci >= goukaku_all_3z]
    line_4_list2=[di for di in line_4_list if di >= goukaku_all_4z]
    line_5_list2=[ei for ei in line_5_list if ei >= goukaku_all_5z]
    line_6_list2=[fi for fi in line_6_list if fi >= goukaku_all_6z]
    line_7_list2=[gi for gi in line_7_list if gi >= goukaku_all_7z]
    line_8_list2=[hi for hi in line_8_list if hi >= goukaku_all_8z]
    line_9_list2=[ii for ii in line_9_list if ii >= goukaku_all_9z]
    line_10_list2=[ji for ji in line_10_list if ji >= goukaku_all_10z]
    line_11_list2=[ki for ki in line_11_list if ki >= goukaku_all_11z]
    line_12_list2=[li for li in line_12_list if li >= goukaku_all_12z]


    line_1_list2_len=len(line_1_list2)*100
    line_2_list2_len=len(line_2_list2)*100
    line_3_list2_len=len(line_3_list2)*100
    line_4_list2_len=len(line_4_list2)*100
    line_5_list2_len=len(line_5_list2)*100
    line_6_list2_len=len(line_6_list2)*100
    line_7_list2_len=len(line_7_list2)*100
    line_8_list2_len=len(line_8_list2)*100
    line_9_list2_len=len(line_9_list2)*100
    line_10_list2_len=len(line_10_list2)*100
    line_11_list2_len=len(line_11_list2)*100
    line_12_list2_len=len(line_12_list2)*100




    

    line_1_list_len=[x1 for x1 in line_1_list if x1 > 0]
    line_2_list_len=[x2 for x2 in line_2_list if x2 > 0]
    line_3_list_len=[x3 for x3 in line_3_list if x3 > 0]
    line_4_list_len=[x4 for x4 in line_4_list if x4 > 0]
    line_5_list_len=[x5 for x5 in line_5_list if x5 > 0]
    line_6_list_len=[x6 for x6 in line_6_list if x6 > 0]
    line_7_list_len=[x7 for x7 in line_7_list if x7 > 0]
    line_8_list_len=[x8 for x8 in line_8_list if x8 > 0]
    line_9_list_len=[x9 for x9 in line_9_list if x9 > 0]
    line_10_list_len=[x10 for x10 in line_10_list if x10 > 0]
    line_11_list_len=[x11 for x11 in line_11_list if x11 > 0]
    line_12_list_len=[x12 for x12 in line_12_list if x12 > 0]
    



    line_1_list3=len(line_1_list_len)
    if line_1_list3 == 0:
        line_1_list3=1

    line_2_list3=len(line_2_list_len)
    if line_2_list3 == 0:
        line_2_list3=1
    
    line_3_list3=len(line_3_list_len)
    if line_3_list3 == 0:
        line_3_list3=1
    
    line_4_list3=len(line_4_list_len)
    if line_4_list3 == 0:
        line_4_list3=1
    
    line_5_list3=len(line_5_list_len)
    if line_5_list3 == 0:
        line_5_list3=1

    line_6_list3=len(line_6_list_len)
    if line_6_list3 == 0:
        line_6_list3=1

    line_7_list3=len(line_7_list_len)
    if line_7_list3 == 0:
        line_7_list3=1
    
    line_8_list3=len(line_8_list_len)
    if line_8_list3 == 0:
        line_8_list3=1
    
    line_9_list3=len(line_9_list_len)
    if line_9_list3 == 0:
        line_9_list3=1
    
    line_10_list3=len(line_10_list_len)
    if line_10_list3 == 0:
        line_10_list3=1

    line_11_list3=len(line_11_list_len)
    if line_11_list3 == 0:
        line_11_list3=1

    line_12_list3=len(line_12_list_len)
    if line_12_list3 == 0:
        line_12_list3=1
    
    line_1_kakuritu=line_1_list2_len / line_1_list3
    line_2_kakuritu=line_2_list2_len / line_2_list3
    line_3_kakuritu=line_3_list2_len / line_3_list3
    line_4_kakuritu=line_4_list2_len / line_4_list3
    line_5_kakuritu=line_5_list2_len / line_5_list3
    line_6_kakuritu=line_6_list2_len / line_6_list3
    line_7_kakuritu=line_7_list2_len / line_7_list3
    line_8_kakuritu=line_8_list2_len / line_8_list3
    line_9_kakuritu=line_9_list2_len / line_9_list3
    line_10_kakuritu=line_10_list2_len / line_10_list3
    line_11_kakuritu=line_11_list2_len / line_11_list3
    line_12_kakuritu=line_12_list2_len / line_12_list3
    a_a='全チーム合格率'

    aa='4月'
    bb='5月'
    cc='6月'
    dd='7月'
    ee='8月'
    ff='9月'
    gg='10月'
    hh='11月'
    ii='12月'
    jj='1月'
    kk='2月'
    ll='3月'

    columns=[a_a]
    index=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll]
    df_a=pd.DataFrame([line_1_kakuritu,line_2_kakuritu,line_3_kakuritu,line_4_kakuritu,line_5_kakuritu,line_6_kakuritu,
    line_7_kakuritu,line_8_kakuritu,line_9_kakuritu,line_10_kakuritu,line_11_kakuritu,line_12_kakuritu],index=index,columns=columns)
    figure(num=None, figsize=(16, 9))
    plt.title('５sパトロール合格率[全チーム]',fontsize=30)
    plt.xlabel(f'{nen}年{now.month}月{now.day}日現在【月】',fontsize=25)
    plt.ylabel('合格率【％】',fontsize=25)
    plt.plot(list(df_a.index),df_a[a_a],marker='o',label=a_a)
    plt.legend()

def plt2svg_zz():
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    return s

@login_required
def get_svg_zz(request):
    setplt_zz()
    svg=plt2svg_zz()
    plt.cla()
    response=HttpResponse(svg,content_type='image/svg+xml')
    return response

