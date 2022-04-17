from typing import Any

from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for name in ["username", "password1", "password2"]:
            field = self.fields[name]
            field.help_text = None
            field.widget.attrs.update({"class": "form-control"})
