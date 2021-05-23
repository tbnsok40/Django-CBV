from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):  #상속
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True  # 이줄이 없었다면, 초기화 이후 달라질게 없다(상속받은 그래도라는 말)
