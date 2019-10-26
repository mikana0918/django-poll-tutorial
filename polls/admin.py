from django.contrib import admin
from .models import Question
# Register your models here.
#Question オブジェクトがadmin インタフェースを持つということを、adminに伝える
admin.site.register(Question)