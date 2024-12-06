from django.db import models


class BuiltinPropertyManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset().filter(is_builtin=True)
        return super().get_queryset().filter(library__is_builtin=True)


class CustomPropertyManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset().filter(is_builtin=False)
        return super().get_queryset().filter(library__is_builtin=False)
