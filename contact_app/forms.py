from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'status', 'message_field']
        labels = {
            'name': 'NAME',
            'phone': 'PHONE',
            'email': 'EMAIL',
            'status': 'STATUS',
            'message_field': 'MESSAGE',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control', 'required': 'required'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone', 'class': 'form-control', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control', 'required': 'required'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'message_field': forms.Textarea(attrs={'placeholder': 'Type your message', 'class': 'form-control', 'required': 'required', "cols": "40", "rows": "9"}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('phone', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            'status',
            'message',
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
