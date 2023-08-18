from django.contrib import admin
from project.models import Projects, Status, Priority, Tasks

# admin.site.register(Projects)
# admin.site.register(Status)
# admin.site.register(Priority)
# admin.site.register(Tasks)


def capitalize_title(modeladmin, request, queryset):
    for model in queryset:
        model.name = model.name.capitalize()
        model.save()

capitalize_title.short_description = 'Нормализовать заголовок'

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('name', )

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
    list_filter = ('is_active', 'name')
    search_fields = ('name',)
    actions = [capitalize_title]

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
    list_filter = ('is_active', 'name')
    search_fields = ('name',)
    actions = [capitalize_title]

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'status', 'priority')
    list_filter = ('project', 'name')
    search_fields = ('name', )

