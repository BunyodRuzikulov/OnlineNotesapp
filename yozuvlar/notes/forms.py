from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note, Folder, Tag

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NoteForm(forms.ModelForm):
    tags = forms.CharField(max_length=255, required=False, help_text='Taglarni vergul bilan ajrating (masalan: muhim, shoshilinch)')

    class Meta:
        model = Note
        fields = ['title', 'content', 'folder', 'tags', 'file', 'share_mode']

    def clean_tags(self):
        tags_str = self.cleaned_data.get('tags')
        if tags_str:
            tag_names = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
            tags = []
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=name)
                tags.append(tag)
            return tags
        return []

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']