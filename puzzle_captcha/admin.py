from django.contrib import admin
from puzzle_captcha.models import Puzzle, PuzzlePiece

class PuzzlePieceInline(admin.StackedInline):
    model = PuzzlePiece
    readonly_fields = ('key', 'image', 'order')
    can_delete = False
    extra = 0

class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('key', 'rows', 'cols')
    readonly_fields = ('key', 'rows', 'cols')
    class Meta:
        model = Puzzle
    inlines = [
        PuzzlePieceInline,
    ]
    
admin.site.register(Puzzle, PuzzleAdmin)

