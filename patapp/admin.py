from django.contrib import admin

# Register your models here.
from .models import kakutuki,kakutuki_a,kakutuki_b,kakutuki_c,kakutuki_d,kakutuki_e,team,goukaku

admin.site.register(kakutuki)
admin.site.register(kakutuki_a)
admin.site.register(kakutuki_b)
admin.site.register(kakutuki_c)
admin.site.register(kakutuki_d)
admin.site.register(kakutuki_e)
admin.site.register(team)
admin.site.register(goukaku)
