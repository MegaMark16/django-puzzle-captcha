import random
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.conf import settings
from models import Puzzle

class PuzzleCaptchaInput(widgets.Widget):
    def render(self, name, value, attrs = None):
        puzzle = random.choice(Puzzle.objects.all())
        pieces = []
        
        for piece in puzzle.get_random_pieces():
            pieces.append(u'<li class="piece"><img src="%s%s" /><input type="hidden" name="%s" /></li>' % (settings.MEDIA_URL, piece.image.name, piece.key))
        args = { 
            'fields': '\n'.join(pieces), 
            'name': name,
            'puzzle_key': puzzle.key,
        }
        
        raw_html = u"""
<script type="text/javascript">
function updatePuzzleOutput() {
    output = '"puzzle_key": "' + $('#puzzle_key').val() + '"';
    $(".piece input").each(function() {
        output += ',"' + $(this).attr('name') + '": "' + $(this).val() + '"';
    });
    $('#puzzle_captcha_output').val('{' + output + '}');
}

$(document).ready(function() {
    updatePuzzleOutput();
    $(".puzzle").sortable({ 
		    update: function() {
		        var looper = 1;
		        $(".piece input").each(function() {
		            $(this).val(looper);
		            looper+=1;
		        });
		        updatePuzzleOutput();
		    },
		});
});
</script>
<style>
.puzzle {
    padding-left: 0px;
}

.piece {
    list-style: none;
    margin-bottom:-3px;
}
</style>
<input type="hidden" id="puzzle_key" name="puzzle_key" value="%(puzzle_key)s" />
<ul class="puzzle">
%(fields)s
</ul>

<input type="hidden" name="%(name)s" id="puzzle_captcha_output" />
        """ % args
        
        return mark_safe(raw_html)

