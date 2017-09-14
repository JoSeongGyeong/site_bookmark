from django.contrib import admin
from .models import Bookmark  #.은 현재폴더..import
#from bookmark.modes import Bookmark
# Register your models here.

admin.site.register(Bookmark)

