from django.contrib.auth.forms import UserCreationForm
from .models import User

# account의 form 변경도 잘 확인하자
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User