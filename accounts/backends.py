from django.contrib.auth.backends import BaseBackend

from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAuthenticationBackend(BaseBackend):
    # https://stackoverflow.com/questions/25316765/log-in-user-using-either-email-address-or-username-in-django
    
    def authenticate(self, request, **kwargs):
        # If you made email case insensitive add kwargs['username'].lower()
        email = kwargs['username']
        password = kwargs['password']
        try:
            my_user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if my_user.is_active and my_user.check_password(password):
                return my_user
        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
