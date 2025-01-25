from django import template

register = template.Library()


@register.filter
def is_following(profile, user):
    return profile.is_following(user)
