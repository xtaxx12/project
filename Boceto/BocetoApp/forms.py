from django import forms


class ContactForm(forms.Form):
    """Formulario de contacto rápido de la página de inicio."""

    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Escribe tu correo electrónico',
            'autocomplete': 'email',
            'required': True,
        }),
        error_messages={
            'required': 'Por favor, ingresa tu correo electrónico.',
            'invalid': 'El correo electrónico ingresado no es válido.',
        },
    )
