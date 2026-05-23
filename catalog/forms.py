import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import BookInstance


class RenewBookForm(forms.Form):
    """Plain Form variant: a single renewal_date field with explicit validation."""

    weeks_ahead = 4
    renewal_date = forms.DateField(
        help_text=f'Enter a date between now and {weeks_ahead} weeks (default 3).'
    )

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        if data > datetime.date.today() + datetime.timedelta(weeks=self.weeks_ahead):
            raise ValidationError(
                _(f'Invalid date - renewal more than {self.weeks_ahead} weeks ahead')
            )
        return data


class BookInstanceCommentsForm(ModelForm):
    def clean_comments(self):
        data = self.cleaned_data['comments']
        if len(data) >= 200:
            raise ValidationError(_('Comment must be less than 200 characters.'))
        return data

    class Meta:
        model = BookInstance
        fields = ['comments']
        labels = {'comments': _('Comments')}
        help_texts = {'comments': _('Comment must be under 200 characters.')}


class RenewBookModelForm(ModelForm):
    """ModelForm variant over BookInstance.due_back. Functionally equivalent to
    RenewBookForm; the view can be switched to use this instead by swapping the
    import and the cleaned_data key ('due_back' instead of 'renewal_date')."""

    def clean_due_back(self):
        data = self.cleaned_data['due_back']
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('Renewal date')}
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')}
