from django.core.exceptions import ValidationError


def validate_content(value):
    if len(value) > 165:
        raise ValidationError('Tweet content must be less than or equal to 140 characters.')  # noqa: E501
    if not value.strip():
        raise ValidationError('Tweet content cannot be empty.')
    if value.startswith('@') or value.startswith('#'):
        raise ValidationError('Tweet content cannot start with @ or #.')
    if value.endswith('.') or value.endswith('!') or value.endswith('?'):
        raise ValidationError('Tweet content cannot end with a punctuation mark.')  # noqa: E501
    if value.count('http://') > 1 or value.count('https://') > 1:
        raise ValidationError('Tweet content cannot contain more than one URL.')  # noqa: E501
    return value
