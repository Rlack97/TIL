from django import forms

from chattings.models import Chat

class ChatForm(forms.ModelForm):
    user = forms.CharField(
        label = '작성자:',
        widget=forms.TextInput(
            attrs={
                'class':'my-user',
                'placeholder':'Nickname',
                'maxlength':'10',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={'class':'my-content',
                'placeholder':'Chat!',
                'rows':5,
                'col':50,
            }     
        )
    )

    class Meta:
        model=Chat
        fields='__all__'
