from django.conf.urls import url
from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns=[
    path('',views.SchoolListView.as_view(),name='list'),
    # path('detail/',views.SchoolDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),
    # path('',views.IndexView.as_view()),

]