from django.conf.urls import url
from myapp import views
from django.urls import path

urlpatterns = [
    path('',views.EstateListView.as_view(),name='home'),
    path('new_profile/',views.TestCreateView.as_view(),name='new_user'), # new profile viz broker, user, seller
    path('new_user/',views.CreateUserView.as_view(),name='user_details'), # new user
    path('new_estate/',views.CreateEstateForm.as_view(),name='new_estate'), # new estate
    path('estate/<int:pk>',views.EstateDetailView.as_view(),name='estate_detail'),
    path('estate/update/<int:pk>',views.EstateUpdateView.as_view(),name='estate_update'),
    url('^broker/(?P<pk>[0-100]+)$',views.BrokerDetailView.as_view(),name='broker_detail'),
    path('broker/update/<int:pk>',views.BrokerUpdateView.as_view(),name='broker_update'),

]

