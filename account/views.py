from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from account.decorators import account_ownership_required
from account.forms import AccountUpdateForm

has_ownership = [login_required, account_ownership_required]


# @login_required  # login이 됐을 때만 작동하도록 데코레이터를 붙여준다
def hello_world(request):
    if request.method == "POST":
        return HttpResponse(reverse("account:hello_world"))
    else:
        return render(request, "hello_world.html")


# cbv에선 단순하고 직관적으로 만들 수 있다.
class AccountCreateView(CreateView):
    model = User  # django에서 기본 제공 모델, Abstract 를 또 상속받고 있다.
    form_class = UserCreationForm
    # 계정 만들기 성공하면 어느 유알엘로 연결해주냐
    success_url = reverse_lazy('account:hello_world')
    # reverse_lazy와 reverse의 차이: 함수와 클래스를 불러오는 차이 때문에 cbv에선 reverse_lazy사용
    template_name = 'create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'  # target이 되는 user의 정보를 보일 수 있도록
    template_name = "detail.html"


# 일반 function에 사용하는 decorator를 메서드에 사용할 수 있도록 해주는 데코레이터
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    # form_class = UserCreationForm  # AccountUpdateForm 으로 갈아끼우기 전
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('account:hello_world')
    template_name = 'update.html'

    # decorator로 치환 가능
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('account:login')
    template_name = 'delete.html'

    # decorator로 치환 가능
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()




