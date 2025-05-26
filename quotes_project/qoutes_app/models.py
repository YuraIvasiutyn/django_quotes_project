from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=25)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'full_name'], name='author of username')
        ]

    def __str__(self):
        return f"{self.full_name}"


class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}"


class Quote(models.Model):
    name = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='quote of username')
        ]

    def __str__(self):
        return self.name[:50]
