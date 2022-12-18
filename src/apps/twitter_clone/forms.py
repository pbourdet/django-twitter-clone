from django import forms


class TweetForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={
                "class": "md-textarea form-control",
                "rows": 3,
                "placeholder": "What's going on ?",
                "maxlength": 255,
            }
        ),
    )
