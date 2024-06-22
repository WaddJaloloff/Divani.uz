from django import template
from application.models import Post

register = template.Library()

@register.filter
def get_item_by_id(posts, post_id):
    post = Post.objects.get(id=post_id)
    return post.title
