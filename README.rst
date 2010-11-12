Django Puzzle Captcha is a Form Field for django forms that adds a special type of captcha to your form and validates it during form validation.  

The captcha is unique in that it is an image split up into different pieces like a puzzle, and it uses javascript to allow the user to drag and drop the pieces of the puzzle to put them in the correct order.

Using this field has two parts.  

The first step is to load in images to be used as puzzles.  This can be done either through the admin interface or through "python manage.py load_images <path_to_folder_containing_images>".

The second step is to add a PuzzleCaptchaField to your form, like so:


::
from django import forms
from puzzle_captcha.fields import PuzzleCaptchaField

::
class MyForm(forms.Form):
    captcha = PuzzleCaptchaField()  

That's pretty much it.
