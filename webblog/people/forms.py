from django import forms

class FriendInviteForm(forms.Form):
	name = forms.CharField(label='Friend\'s name')
	email = forms.EmailField(label = 'Friend\'s email')

