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

function updatePieceOrder() {
    var looper = 1;
    $(".piece input").each(function() {
        $(this).val(looper);
        looper+=1;
    });
}

function swapNodes(a, b) {
    var aparent = $(a).parent();
    var aPosition = parseInt($(a).next().val());
    var bPosition = parseInt($(b).next().val());
    if (aPosition != bPosition) {
        if (aPosition < bPosition) {
            $(b).parent().insertBefore(aparent);
        }
        else {
            $(b).parent().insertAfter(aparent);
        }
    }
}

$(document).ready(function() {
    updatePuzzleOutput();
    updatePieceOrder();
    
    $(".puzzle .piece img").click(function() { 
        var currentlySelectedPiece = $(".puzzle .piece img.selected");
        if ($(currentlySelectedPiece).length > 0) {
            swapNodes(this, currentlySelectedPiece);
            $(currentlySelectedPiece).removeClass("selected");
            updatePieceOrder();
            updatePuzzleOutput();
        }
        else {
            $(this).addClass("selected");
        }
    });
    
    if ($(".puzzle").sortable) {
    $(".puzzle").sortable({ 
            start: function() {
                $(".puzzle .piece img.selected").removeClass("selected");
            },
            stop: function() {
                setTimeout('$(".puzzle .piece img.selected").removeClass("selected")', 10);
            },            
		    update: function() {
		        updatePieceOrder();
		        updatePuzzleOutput();
		    },
		});
		}
    });
</script>
<style>
.puzzle {
    padding-left: 0px;
}

.piece {
    list-style: none;
    margin-bottom: -4px;
}
.puzzle .piece img {
    border: thin solid white;
}
.puzzle .piece img.selected {
    border: thin solid blue;
}
</style>
<input type="hidden" id="puzzle_key" name="puzzle_key" value="%(puzzle_key)s" />
<ul class="puzzle">
%(fields)s
</ul>

<input type="hidden" name="%(name)s" id="puzzle_captcha_output" />
        """ % args
        
        return mark_safe(raw_html)

