from django.contrib.auth import get_user_model
from rest_framework import exceptions

User = get_user_model()


class SerializerClassesMixin:
    """
    Mixin for getting custom serializer classes for actions
    """

    serializer_classes = None

    def get_serializer_class(self):
        if not self.serializer_classes.get("default", None):
            raise exceptions.APIException("default serializer class was not provided")
        return self.serializer_classes.get(
            self.action, self.serializer_classes["default"]
        )


class PermissionClassesMixin:
    """
    Mixin for getting custom permission classes for actions
    """

    permission_classes = None

    def get_permissions(self):
        if not self.permission_classes.get("default", None):
            raise exceptions.APIException("default permission classes was not provided")
        return [
            permission()
            for permission in self.permission_classes.get(
                self.action, self.permission_classes["default"]
            )
        ]
