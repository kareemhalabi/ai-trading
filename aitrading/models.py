from django.db import models


class AuthorizedUser(models.Model):
    email = models.EmailField(primary_key=True)
    account = models.CharField(max_length=12)

    def __str__(self):
        return '<User: %s, Account: %s>' % (self.email, self.account)