from django.db import models

# Create your models here.
class kakutuki(models.Model):
    
    tuki=models.IntegerField(default=1)
    seiri_in=models.IntegerField(default=0)
    seiton_in=models.IntegerField(default=0)
    seisou_in=models.IntegerField(default=0)
    seiketu_in=models.IntegerField(default=0)
    situke_in=models.IntegerField(default=0)
    total_in=models.IntegerField(default=0)

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +')月>'

class kakutuki_a(models.Model):
    
    tuki=models.IntegerField(default=1)
    seiri_in=models.IntegerField(default=0)
    seiton_in=models.IntegerField(default=0)
    seisou_in=models.IntegerField(default=0)
    seiketu_in=models.IntegerField(default=0)
    situke_in=models.IntegerField(default=0)
    total_in=models.IntegerField(default=0)

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +')月>'

class kakutuki_b(models.Model):
    
    tuki=models.IntegerField(default=1)
    seiri_in=models.IntegerField(default=0)
    seiton_in=models.IntegerField(default=0)
    seisou_in=models.IntegerField(default=0)
    seiketu_in=models.IntegerField(default=0)
    situke_in=models.IntegerField(default=0)
    total_in=models.IntegerField(default=0)

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +')月>'

class kakutuki_c(models.Model):
    
    tuki=models.IntegerField(default=1)
    seiri_in=models.IntegerField(default=0)
    seiton_in=models.IntegerField(default=0)
    seisou_in=models.IntegerField(default=0)
    seiketu_in=models.IntegerField(default=0)
    situke_in=models.IntegerField(default=0)
    total_in=models.IntegerField(default=0)

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +')月>'

class kakutuki_d(models.Model):
    
    tuki=models.IntegerField(default=1)
    seiri_in=models.IntegerField(default=0)
    seiton_in=models.IntegerField(default=0)
    seisou_in=models.IntegerField(default=0)
    seiketu_in=models.IntegerField(default=0)
    situke_in=models.IntegerField(default=0)
    total_in=models.IntegerField(default=0)


    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +')月>'

class kakutuki_e(models.Model):
    
    tuki=models.IntegerField(default=1)
    seiri_in=models.IntegerField(default=0)
    seiton_in=models.IntegerField(default=0)
    seisou_in=models.IntegerField(default=0)
    seiketu_in=models.IntegerField(default=0)
    situke_in=models.IntegerField(default=0)
    total_in=models.IntegerField(default=0)

    def __str__(self):
        return '<作成No=' +str(self.id) +',(' + str(self.tuki) +')月>'

class team(models.Model):
    team_name=models.CharField(max_length=30)

    def __str__(self):
        return '<チーム名:id=' + str(self.id) + ',' + self.team_name + '>'

class goukakuten(models.Model):
    kijunten=models.IntegerField(default=85)

    def __str__(self):
        return '<作成No=' +str(self.id) +',(合格基準点は' + str(self.tuki) +')点>'

class goukakuten_in(models.Model):
    tuki=models.IntegerField(default=1)
    kijunten_in=models.IntegerField(default=85)
    
    def __str__(self):
        return '<作成No=' +str(self.id) +',(合格基準点は' + str(self.kijunten_in) +')点'+str(self.tuki)+'月>'

class goukaku(models.Model):
    tuki=models.IntegerField(default=1)
    kijunten_in=models.IntegerField(default=85)
    
    def __str__(self):
        return '<作成No=' +str(self.id) +',(合格基準点は' + str(self.kijunten_in) +')点'+str(self.tuki)+'月>'