# override save method in django gfg and sluggify
# generate random string in python gfg
import random
import string
from django.utils.text import slugify


def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))
    return res


def generate_slug(text):
    new_slug = slugify(text)
    from .models import BlogModel
    # print()
    # print(new_slug)
    # print(BlogModel.objects.filter(slug=new_slug).first())
    # print()

    if BlogModel.objects.filter(slug=new_slug).first():
        return generate_slug(text + generate_random_string(5))
    return new_slug
