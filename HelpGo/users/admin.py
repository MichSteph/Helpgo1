from django.contrib import admin
from .models import User
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'username':
#             kwargs['queryset'] = get_user_model().objects.filter(username=request.user.username)
#         return super(UserAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#     def get_readonly_fields(self, request, obj=None):
#         if obj is not None:
#             return self.readonly_fields + ('username',)
#         return self.readonly_fields

#     def add_view(self, request, form_url="", extra_context=None):
#         data = request.GET.copy()
#         data['username'] = request.user
#         request.GET = data
#         return super(UserAdmin, self).add_view(request, form_url="", extra_context=extra_context)


admin.site.register(User)