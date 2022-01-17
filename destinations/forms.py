from django import forms
from .models import Region

class RegionSelector(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name

class AddDestinationForm(forms.Form):
    name = forms.CharField(max_length = 255, required = True)
    region = RegionSelector(queryset = Region.objects.all(), required = True)
    country = forms.CharField(max_length = 255, required = True)
    introduction = forms.CharField(widget=forms.Textarea, required = True)
    photo = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = "Nom"
        self.fields['region'].widget.attrs['placeholder'] = 'Continent'
        self.fields['country'].widget.attrs['placeholder'] = 'Pays'
        self.fields['introduction'].widget.attrs['placeholder'] = 'Introduction'
        self.fields['photo'].widget.attrs['placeholder'] = 'Photo'
        for fieldname in ['name', 'region', 'country', 'introduction', 'photo']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""

class AddCountryForm(forms.Form):
    name = forms.CharField(max_length = 255)
    region = RegionSelector(queryset = Region.objects.all())

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = "Nom"
        self.fields['region'].widget.attrs['placeholder'] = 'Continent'
        for fieldname in ['name', 'region']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""