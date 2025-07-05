from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('',views.user_app, name='user_app'),
    path('user_app',views.user_app, name='user_app'),
    path('create_acc_request',views.create_acc_request),
    path('account_requests',views.account_requests),
    path('success/<int:id>/', views.success, name='success'),
    path('netbanking', views.netbanking, name='netbanking'),
    path('user_acount',views.user_acount, name='user_acount'),
    path('currency_exchange',views.currency_exchange, name='currency_exchange'),
    path('loan',views.loan, name='loan'),
    path('support',views.support, name='support'),
    path('health',views.health, name='health'),
    path('life',views.life, name='life'),
    
    
    path('user_account_request_list',views.user_account_request_list, name='user_account_request_list'),
    path('get-user', views.get_user, name='get_user'),

    path('vehicle_insuranceform', views.vehicle_insuranceform, name='vehicle_insuranceform'),
    path('vehicle_insurance_list', views.vehicle_insurance_list, name='vehicle_insurance_list'),


    path('health_insurance_form',views.health_insurance_form, name='health_insurance_form'),
    path('health_insurance_list',views.health_insurance_list, name='health_insurance_list'),

    path('life_insurance_form',views.life_insurance_form, name='life_insurance_form'),
    path('life_insurance_list', views.life_insurance_list, name='life_insurance_list'),
    
    path('transaction',views.transaction, name='transaction'),
    path('transaction_list',views.transaction_list, name='transaction_list'),

    path('user_profile',views.user_profile, name='user_profile'),

    path('card_apply',views.card_apply, name='card_apply'),
    path('card_application_list',views.card_application_list, name='card_application_list'),

    path('loan',views.loan, name='loan'),
    path('loan_application_list',views.loan_application_list, name='loan_application_list'),

    path('Admin_page',views.Admin_page, name='Admin_page'),
    

]