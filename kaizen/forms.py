from django import forms
from .models import *




class team_kaizen1_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen1
        fields=['team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu']

class team_kaizen2_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen2
        fields=['team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu']

class team_kaizen3_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen3
        fields=['team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu']

class team_kaizen4_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen4
        fields=['team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu']

class team_kaizen5_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen5
        fields=['team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu']

class team_kaizen6_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen6
        fields=['team_name','kaizen_teian_hituyou_maisuu','nenkan_mokuhyou_kingaku','team_member_ninzuu']


class team_kaizen1_kiroku_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen1_kiroku
        fields=['output_kaizenteian','output_kingaku']

class team_kaizen2_kiroku_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen2_kiroku
        fields=['output_kaizenteian','output_kingaku']

class team_kaizen3_kiroku_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen3_kiroku
        fields=['output_kaizenteian','output_kingaku']

class team_kaizen4_kiroku_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen4_kiroku
        fields=['output_kaizenteian','output_kingaku']

class team_kaizen5_kiroku_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen5_kiroku
        fields=['output_kaizenteian','output_kingaku']

class team_kaizen6_kiroku_Form(forms.ModelForm):
    class Meta:
        model=team_kaizen6_kiroku
        fields=['output_kaizenteian','output_kingaku']
