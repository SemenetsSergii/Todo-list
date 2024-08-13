from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        created_at = timezone.now()  # Use timezone-aware now
        deadline = cleaned_data.get("deadline")

        if deadline and deadline < created_at:
            raise ValidationError("Deadline can't be before the current time.")

        return cleaned_data

    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "tags",
        )
