from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None,
                    is_active=True, is_staff=False, is_admin=False, subscribed=True):
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.subscribed = subscribed
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password=None, subscribed=True):
        user = self.create_user(
            email, username, password=password, is_staff=True, subscribed=subscribed)
        return user

    def create_superuser(self, email, username, password=None, subscribed=True):
        user = self.create_user(email, username, password=password,
                                is_staff=True, is_admin=True, subscribed=subscribed)
        return user