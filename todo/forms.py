from django import forms


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date"}
        )
    )
