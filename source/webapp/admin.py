from django.contrib import admin
from webapp.models import Photography, Comments, Like


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'caption', 'created_date', "rating", "photo_author")
    list_filter = ('rating', "created_date")


class CommentsAdmin(admin.ModelAdmin):
    fields = ("id", "text", "photography", "comments_author", "created_date")
    list_filter = ("created_date",)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'photography', 'like_author', 'like')
    list_filter = ('id',)


admin.site.register(Photography, PhotoAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Like, LikeAdmin)
