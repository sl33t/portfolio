from django import forms

from home.models import BlogPost, PortfolioItem


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                'required': 'true'}),
        required=True)
    sender = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'required': 'true'}),
        required=True)
    reason = forms.ChoiceField(
        label="Reason for Contact",
        widget=forms.Select,
        choices=[
            ("Job",
             "I have a job for you."),
            ("Blog Idea",
             "You should blog about...."),
            ("Message",
             "Other")],
        required=True)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Write your message here.',
                'required': 'required'}),
        required=True)


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['main_image_url', 'title', 'post']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = [
            'main_image_url',
            'title',
            'description',
            'examples1',
            'examples2',
            'examples3']
