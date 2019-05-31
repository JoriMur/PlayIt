from django.contrib import admin
from .models import Game, Author

class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Spel Details", {"fields": ["image","title", "authors","publisher","numberofplayersminimum","numberofplayersmaximum","age","duration","type","skill"]}),
        ("Review", {"fields": ["review", "date_reviewed"]}),
    ]

    readonly_fields = (["date_reviewed"])

    def game_authors(self, obj):
        return obj.list_authors()

    game_authors.short_description = "Auteur(s)"

    list_display = ("title", "game_authors", "publisher", "date_reviewed")
    search_fields = ( "title", "authors__name", "publisher")
	
# Register your models here.
admin.site.register(Game, GameAdmin)
admin.site.register(Author)

