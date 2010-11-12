import random

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404

from puzzle_captcha.models import Puzzle

def render_puzzle(request):
    message = ''
    success = False
    if request.POST:
        puzzle = Puzzle.objects.get(key=request.POST['puzzle_key'])
        looper = 1
        for piece in puzzle.puzzlepiece_set.all():
            print request.POST[piece.key], looper
            success = True
            if request.POST[piece.key] != str(looper):
                message = 'You did not solve the puzzle correctly, please try again.'
                success = False
                break
            looper += 1
    if success:
        message = 'You solved the puzzle, good job!'
    else:
        puzzle = random.choice(Puzzle.objects.all())
    return render_to_response('puzzle/render_captcha.html', { 'puzzle': puzzle, 'message': message,}, context_instance=RequestContext(request))

