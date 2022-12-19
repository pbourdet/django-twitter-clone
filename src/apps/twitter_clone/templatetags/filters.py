import re

from django import template

register = template.Library()


@register.filter
def display_tweet(content: str) -> str:
    def replace_hashtag(match):
        hashtag = match.group()
        return (
            f'<a style="text-decoration: none" href="/hashtag/'
            f'{hashtag.lower()[1:]}">{hashtag}'
            f"</a>"
        )

    return re.sub(r"#\w+", replace_hashtag, content)
