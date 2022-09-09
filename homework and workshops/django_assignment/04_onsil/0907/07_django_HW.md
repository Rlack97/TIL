1. 장고 user모델

class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"



2. Create user by ModelForm
from django.contrib.auth.forms import createuser

3. Django Session
a = django_session
b = login_session