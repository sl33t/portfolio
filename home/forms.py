from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                'required': 'required'}),
        required=True)
    sender = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'required': 'required'}),
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
