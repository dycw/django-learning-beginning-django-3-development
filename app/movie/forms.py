from typing import Any
from typing import TYPE_CHECKING

from django.forms.models import ModelForm
from django.forms.widgets import Textarea
from movie.models import Review


class ReviewForm(ModelForm[Review] if TYPE_CHECKING else ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for name, cls in [
            ("text", "form-control"),
            ("watch_again", "form-check-input"),
        ]:
            self.fields[name].widget.attrs.update({"class": cls})

    class Meta:  # type: ignore
        model = Review
        fields = ["text", "watch_again"]
        labels = {"watch_again": "Watch Again"}
        widgets = {"text": Textarea(attrs={"rows": 4})}
