from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'status', 'message_field']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name*', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone*', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email*', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'message_field': forms.Textarea(attrs={'placeholder': 'Message*', 'class': 'form-control'}),
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
            'message_field',
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
