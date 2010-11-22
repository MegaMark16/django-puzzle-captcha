Check out a demo at `http://puzzlecaptcha.apprabbit.com <http://puzzlecaptcha.apprabbit.com>`_.

Django Puzzle Captcha is a Form Field for django forms that adds a special type of captcha to your form and validates it during form validation.  

The captcha is unique in that it is an image split up into different pieces like a puzzle, and it uses javascript to allow the user to drag and drop the pieces of the puzzle to put them in the correct order.

Using this field has three parts.  

1. Add "puzzle_captcha" to your installed apps and run the "syncdb" management command to setup the required database tables.

2. Load in images to be used as puzzles.  This can be done either through the admin interface or through the built in load_images management command:

::

    python manage.py load_images <path_to_folder_containing_images>    


3. Add a PuzzleCaptchaField to your form, like so:

::

    from django import forms
    from puzzle_captcha.fields import PuzzleCaptchaField

    class MyForm(forms.Form):
        captcha = PuzzleCaptchaField()  

That's pretty much it.
