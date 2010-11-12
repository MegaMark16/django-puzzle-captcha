import Image
import hashlib
import datetime
import random
from cStringIO import StringIO

from django.db import models
from django.db.models.fields.files import ImageFieldFile, FileField
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

class Puzzle(models.Model):
    key = models.CharField(max_length=255, default='', unique=True)
    rows = models.IntegerField(default=0)
    cols = models.IntegerField(default=0)
    image = models.ImageField(upload_to='originals', null=True)
    
    def save(self, *args, **kwargs):
        super(Puzzle, self).save(*args, **kwargs)
        self.puzzlepiece_set.all().delete()
        self.create_pieces()
        super(Puzzle, self).save(*args, **kwargs)
      
    def create_pieces(self):
        image = Image.open(self.image.path)
        image.thumbnail((400, 400), Image.ANTIALIAS)
        self.key = hashlib.sha1(image.tostring()).hexdigest()
        """
        if image.size[0] < image.size[1]:
            cols = 2
            rows = 3
        else:
            cols = 3
            rows = 2
        """
        cols = 1
        rows = 6
        self.cols = cols
        self.rows = rows
        horizontal_cell_size = image.size[0]/cols
        vertical_cell_size = image.size[1]/rows
        looper = 0
        for row in range(rows):
            for col in range(cols):
                region = (horizontal_cell_size * col, vertical_cell_size * row, horizontal_cell_size * (col+1), vertical_cell_size * (row+1))
                subimage = image.crop(region)
                subimage_io = StringIO()
                subimage.save(subimage_io, 'JPEG')
                subimage_io.seek(0)
                key = hashlib.sha1(subimage.tostring()).hexdigest()
                looper += 1
                piece = PuzzlePiece(key=key, order=looper, puzzle=self)
                filename = '%s.jpg' % key
                piece.image.save(filename, SimpleUploadedFile(filename, subimage_io.read(), content_type='image/jpg'), save=True)
                piece.save()
    
    def get_random_pieces(self):
        pieces = [piece for piece in self.puzzlepiece_set.all()]
        random.shuffle(pieces)        
        return pieces
        
class PuzzlePiece(models.Model):
    key = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pieces')
    puzzle = models.ForeignKey(Puzzle)
    order = models.IntegerField()
    
        
