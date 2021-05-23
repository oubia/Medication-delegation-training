from django import forms

class LoginFormUser(forms.Form):
    _id = forms.CharField(max_length=100)
    code = forms.CharField(label='Code',max_length=6 )
    password = forms.CharField(label='Password',max_length=6 )
    def __str__(self):
        return self.code ,self.password