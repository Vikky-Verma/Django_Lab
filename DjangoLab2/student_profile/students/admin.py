from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    #  Columns shown in admin list
    list_display = (
        'id',
        'name',
        'email',
        'age',
        'course',
        'enrollment_date'
    )

    # 2️⃣ Search bar (top)
    search_fields = (
        'name',
        'email',
        'course'
    )

    # 3️⃣ Right sidebar filters
    list_filter = (
        'course',
        'enrollment_date'
    )

    # 4️⃣ Default ordering (latest first)
    ordering = (
        '-enrollment_date',
    )

    # 5️⃣ Read-only fields
    readonly_fields = (
        'enrollment_date',
    )

    # 6️⃣ Group fields nicely in admin form
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'email', 'age')
        }),
        ('Academic Information', {
            'fields': ('course',)
        }),
        ('Metadata', {
            'fields': ('enrollment_date',)
        }),
    )
