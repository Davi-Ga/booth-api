from django.core.exceptions import ValidationError
import re

def validation_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValidationError('Invalid email address')

def validation_password(password):
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$", password):
        raise ValidationError('Invalid password')
    
def validation_username(username):
    if not re.match(r"^[a-zA-Z0-9_]*$", username):
        raise ValidationError('Invalid username')