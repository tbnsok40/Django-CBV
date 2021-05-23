from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']

# model 을 만든 것은 db 에 저장할 스키마와 필드를 지정하기 위함
# forms 를 정하는 것은 html 에 만들 input 칸을 수월하게 만들기 위함

