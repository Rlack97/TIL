from django import forms
from. models import Article

class Articleform(forms.ModelForm):
    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                # 'class' : 'my_title'
                'placeholder' : '제목을 입력하라고',
                'maxlength' : 10,
            }
        ),
        error_messages={'required': '여기 빼먹었다'}
    )

    content = forms.CharField(
    label="내용",
    widget=forms.Textarea(
        attrs={
            # 'class' : 'my_title'
            'placeholder' : '내용도 입력하라고',
            'rows' : 4,
            }
        ),
        error_messages={'required': '여기 빼먹었다'}
    )
    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)

    # CLASS_A = 's1'
    # CLASS_B = 's2'
    # CLASS_C = 's3'
    # CLASS_D = 's4'
    # CLASS_F = 's5'
    # CLASS_CHOICES = [
    #     (CLASS_A,'1반'),
    #     (CLASS_B,'2반'),
    #     (CLASS_C,'3반'),
    #     (CLASS_D,'4반'),
    #     (CLASS_F,'5반'),
    # ]

    # ssafy_class = forms.ChoiceField(choices=CLASS_CHOICES)


    class Meta:
        model = Article
        fields = '__all__'
