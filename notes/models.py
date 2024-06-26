from django.db import models
from django.core.validators import FileExtensionValidator
from questions.models import Chapter

# Create your models here.

pdf_ext_validator = FileExtensionValidator(['pdf'])

class Notes(models.Model):
  id = models.CharField(max_length=10, primary_key=True)  
  chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
  file = models.FileField(upload_to='notes/', validators=[pdf_ext_validator])
  
  def save(self, *args, **kwargs):
    self.id = f"{self.chapter.id}NOTES"
    super().save(*args, **kwargs)
  
  def __str__(self):
      return f"Notes - {self.chapter.id} - {self.chapter.chapter_name}"