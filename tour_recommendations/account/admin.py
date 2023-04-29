from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .models import Profile
from .forms import ProfileEditForm


# class ProfileChangeList(ChangeList):
#
#     def __init__(self, request, model, list_display,
#                  list_display_links, list_filter, date_hierarchy,
#                  search_fields, list_select_related, list_per_page,
#                  list_max_show_all, list_editable, model_admin, sortable_by, search_help_text):
#         super(ProfileChangeList, self).__init__(request, model,
#                                                 list_display, list_display_links, list_filter,
#                                                 date_hierarchy, search_fields, list_select_related,
#                                                 list_per_page, list_max_show_all, list_editable,
#                                                 model_admin, sortable_by, search_help_text)
#
#         # these need to be defined here, and not in MovieAdmin
#         self.list_display = ['user', 'date_of_birth', 'photo', 'categories']
#         self.raw_id_fields = ['user']
#         self.list_editable = ['categories']

class MembershipInline(admin.TabularInline):
    model = Profile.categories.through


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
    inlines = [MembershipInline]
    # def show_categories(self, obj):
    #     return "\n".join([a.title for a in obj.categories.all()])
    #
    # def get_changelist(self, request, **kwargs):
    #     return ProfileChangeList
    #
    # def get_changelist_form(self, request, **kwargs):
    #     return ProfileChangeList