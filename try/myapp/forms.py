from django import forms
from .models import Newsletter

# choices = (
#     ('friends', 'Friends'),
#     ('search', 'Search Engine'),
#     ('add', 'Advertisement'),
#     ('others', 'Other'),
# )

class Newsletter_form(forms.ModelForm):
    # name = forms.CharField(label="", max_length=100)
    # email = forms.EmailField(label="")
    # news = forms.CheckboxInput()
    # select = forms.ChoiceField(widget=forms.Select, choices=choices)
    # message = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model=Newsletter
        fields = '__all__'







