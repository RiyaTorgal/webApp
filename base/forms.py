from django import forms

class UserForm(forms.Form):
    fullName = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male','Male'),('female','Female'),('other','Other')])
    country = forms.ChoiceField(choices=[
        ('Europe', 'Europe'),
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('North America', 'North America'),
        ('South America', 'South America')
    ])
    phNo = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)