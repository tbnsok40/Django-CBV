from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from account.views import AccountCreateView, hello_world, AccountDetailView, AccountUpdateView, AccountDeleteView

# account app 내부의 hello_world라는 함수에 라우팅할 수 있도록
# account:hello_world
app_name = "account"

urlpatterns = [
    path('hello_world', hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),  # class엔 as_view()를 붙여주어야 한다.
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]