from django import forms

class ItemTrackForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = 'Track Items'
        self.fields['q'].widget.attrs.update({
            'class': 'form-control form-control-lg'
        })

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': '7'}))