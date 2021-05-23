from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):  # 1) 호출할 함수를 매개로 받는다.
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)  # 3) func() 함수 실행
    return decorated  # 2) account_ownership_required 함수는 곧 바로 decorated 함수 리턴
