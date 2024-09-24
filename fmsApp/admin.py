from django.contrib import admin
from .models import Post

from django.contrib import admin

# Set your company name
admin.site.site_header = "Obagi HCDT"  
admin.site.site_title = "Obagi HCDT"     
admin.site.index_title = "Welcome to Your Obagi HCDT"
# Register your models here.
admin.site.register(Post)
