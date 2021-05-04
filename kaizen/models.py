from django.db import models

# Create your models here.
class team_kaizen1(models.Model):
    team_name=models.CharField(max_length=30)
    kaizen_teian_hituyou_maisuu=models.IntegerField(default=2)
    nenkan_mokuhyou_kingaku=models.IntegerField(default=0)
    team_member_ninzuu=models.IntegerField(default=0)

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.team_name) +'チーム)('+ str(self.kaizen_teian_hituyou_maisuu)+'枚の改善提案提出目標)(年間'+str(self.nenkan_mokuhyou_kingaku)+'円目標)(メンバーは'+str(self.team_member_ninzuu)+'人）>'

class team_kaizen2(models.Model):
    team_name=models.CharField(max_length=30)
    kaizen_teian_hituyou_maisuu=models.IntegerField(default=2)
    nenkan_mokuhyou_kingaku=models.IntegerField(default=0)
    team_member_ninzuu=models.IntegerField(default=0)
    
    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.team_name) +'チーム)('+ str(self.kaizen_teian_hituyou_maisuu)+'枚の改善提案提出目標)(年間'+str(self.nenkan_mokuhyou_kingaku)+'円目標)(メンバーは'+str(self.team_member_ninzuu)+'人）>'

class team_kaizen3(models.Model):
    team_name=models.CharField(max_length=30)
    kaizen_teian_hituyou_maisuu=models.IntegerField(default=2)
    nenkan_mokuhyou_kingaku=models.IntegerField(default=0)
    team_member_ninzuu=models.IntegerField(default=0)
    
    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.team_name) +'チーム)('+ str(self.kaizen_teian_hituyou_maisuu)+'枚の改善提案提出目標)(年間'+str(self.nenkan_mokuhyou_kingaku)+'円目標)(メンバーは'+str(self.team_member_ninzuu)+'人）>'

class team_kaizen4(models.Model):
    team_name=models.CharField(max_length=30)
    kaizen_teian_hituyou_maisuu=models.IntegerField(default=2)
    nenkan_mokuhyou_kingaku=models.IntegerField(default=0)
    team_member_ninzuu=models.IntegerField(default=0)
    
    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.team_name) +'チーム)('+ str(self.kaizen_teian_hituyou_maisuu)+'枚の改善提案提出目標)(年間'+str(self.nenkan_mokuhyou_kingaku)+'円目標)(メンバーは'+str(self.team_member_ninzuu)+'人）>'

class team_kaizen5(models.Model):
    team_name=models.CharField(max_length=30)
    kaizen_teian_hituyou_maisuu=models.IntegerField(default=2)
    nenkan_mokuhyou_kingaku=models.IntegerField(default=0)
    team_member_ninzuu=models.IntegerField(default=0)
    
    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.team_name) +'チーム)('+ str(self.kaizen_teian_hituyou_maisuu)+'枚の改善提案提出目標)(年間'+str(self.nenkan_mokuhyou_kingaku)+'円目標)(メンバーは'+str(self.team_member_ninzuu)+'人）>'

class team_kaizen6(models.Model):
    team_name=models.CharField(max_length=30)
    kaizen_teian_hituyou_maisuu=models.IntegerField(default=2)
    nenkan_mokuhyou_kingaku=models.IntegerField(default=0)
    team_member_ninzuu=models.IntegerField(default=0)
    
    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.team_name) +'チーム)('+ str(self.kaizen_teian_hituyou_maisuu)+'枚の改善提案提出目標)(年間'+str(self.nenkan_mokuhyou_kingaku)+'円目標)(メンバーは'+str(self.team_member_ninzuu)+'人）>'


class team_kaizen1_kiroku(models.Model):
    tuki=models.IntegerField(default=4)
    output_kaizenteian=models.IntegerField(default=0)
    output_kingaku=models.IntegerField(default=0)
    

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +'月は)('+ str(self.output_kaizenteian)+'枚提案提出しました)('+str(self.output_kingaku)+'円合理化しました)>'

class team_kaizen2_kiroku(models.Model):
    tuki=models.IntegerField(default=4)
    output_kaizenteian=models.IntegerField(default=0)
    output_kingaku=models.IntegerField(default=0)
    

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +'月は)('+ str(self.output_kaizenteian)+'枚提案提出しました)('+str(self.output_kingaku)+'円合理化しました)>'

class team_kaizen3_kiroku(models.Model):
    tuki=models.IntegerField(default=4)
    output_kaizenteian=models.IntegerField(default=0)
    output_kingaku=models.IntegerField(default=0)
    

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +'月は)('+ str(self.output_kaizenteian)+'枚提案提出しました)('+str(self.output_kingaku)+'円合理化しました)>'

class team_kaizen4_kiroku(models.Model):
    tuki=models.IntegerField(default=4)
    output_kaizenteian=models.IntegerField(default=0)
    output_kingaku=models.IntegerField(default=0)
    

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +'月は)('+ str(self.output_kaizenteian)+'枚提案提出しました)('+str(self.output_kingaku)+'円合理化しました)>'

class team_kaizen5_kiroku(models.Model):
    tuki=models.IntegerField(default=4)
    output_kaizenteian=models.IntegerField(default=0)
    output_kingaku=models.IntegerField(default=0)
    

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +'月は)('+ str(self.output_kaizenteian)+'枚提案提出しました)('+str(self.output_kingaku)+'円合理化しました)>'

class team_kaizen6_kiroku(models.Model):
    tuki=models.IntegerField(default=4)
    output_kaizenteian=models.IntegerField(default=0)
    output_kingaku=models.IntegerField(default=0)
    

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +'月は)('+ str(self.output_kaizenteian)+'枚提案提出しました)('+str(self.output_kingaku)+'円合理化しました)>'


