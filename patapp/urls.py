from django.urls import path
from .import views
urlpatterns = [
    path('',views.zentai,name='zentai'),
    path('saiten/',views.saiten,name="saiten"),
    path('index/',views.index,name="index"),
    path('edit/<int:num>',views.edit,name='edit'),
    path('plot/',views.get_svg,name='plot'),

    path('saiten_a/',views.saiten_a,name="saiten_a"),
    path('index_a/',views.index_a,name="index_a"),
    path('edit_a/<int:num>',views.edit_a,name='edit_a'),
    path('plot_a/',views.get_svg_a,name='plot_a'),

    path('saiten_b/',views.saiten_b,name="saiten_b"),
    path('index_b/',views.index_b,name="index_b"),
    path('edit_b/<int:num>',views.edit_b,name='edit_b'),
    path('plot_b/',views.get_svg_b,name='plot_b'),

    path('saiten_c/',views.saiten_c,name="saiten_c"),
    path('index_c/',views.index_c,name="index_c"),
    path('edit_c/<int:num>',views.edit_c,name='edit_c'),
    path('plot_c/',views.get_svg_c,name='plot_c'),

    path('saiten_d/',views.saiten_d,name="saiten_d"),
    path('index_d/',views.index_d,name="index_d"),
    path('edit_d/<int:num>',views.edit_d,name='edit_d'),
    path('plot_d/',views.get_svg_d,name='plot_d'),

    path('saiten_e/',views.saiten_e,name="saiten_e"),
    path('index_e/',views.index_e,name="index_e"),
    path('edit_e/<int:num>',views.edit_e,name='edit_e'),
    path('plot_e/',views.get_svg_e,name='plot_e'),

    path('edit_name/<int:num>',views.edit_name,name='edit_name'),
    path('team_name_change/',views.team_name_change,name='team_name_change'),
    
    path('plot_z/',views.get_svg_z,name='plot_z'),

    path('goukakuten_change/',views.goukakuten_change,name='goukakuten_change'),
    path('edit_goukakuten/<int:num>',views.edit_goukakuten,name='edit_goukakuten'),
    path('plot_zz/',views.get_svg_zz,name='plot_zz'),
]