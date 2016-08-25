import json
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.forms import fields, ValidationError

from puzzle_captcha.models import Puzzle
from puzzle_captcha.widgets import PuzzleCaptchaInput

class PuzzleCaptchaField(fields.Field):
    widget = PuzzleCaptchaInput
    
    def clean(self, value):
        try:
            values = json.loads(value)
            print values
            puzzle = Puzzle.objects.get(key=values['puzzle_key'])
            looper = 1
            for piece in puzzle.puzzlepiece_set.all():
                print "%s: %s = %s" % (piece.key, looper, values[piece.key])
                if values[piece.key] != str(looper):
                    raise ValidationError(_('You did not get the puzzle right.'))
                    break
                looper += 1
            return True
            
        except Puzzle.DoesNotExist:
            raise ValidationError(_('You did not get the puzzle right.'))
