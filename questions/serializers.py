from rest_framework import serializers
from questions.models import Question, Subject, Chapter, AnswerSmcq, AnswerMmcq, AnswerIntegerType
  
class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subject
    fields = ('id', 'subject_name')
    
    
class ChapterSerializer(serializers.ModelSerializer):
  subject_id = serializers.SlugRelatedField(
    read_only=True,
    slug_field='id'
  )
  class Meta:
    model = Chapter
    fields = ('id', 'chapter_name', 'subject_id')

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = ('__all__')
    
  def get_image_url(self, question):
    request = self.context.get('request')
    photo_url = question.question.url
    return request.build_absolute_uri(photo_url)

class AnswerSmcqSerializer(QuestionSerializer):
  class Meta:
    model=AnswerSmcq
    fields = ('__all__')
    
class AnswerMmcqSerializer(QuestionSerializer):
  class Meta:
    model=AnswerMmcq
    fields = ('__all__')
class AnswerIntegerTypeSerializer(QuestionSerializer):
  class Meta:
    model=AnswerIntegerType
    fields = ('__all__')

# nested attempt
# class ChapterSerializer_Nested(serializers.ModelSerializer):
#     topics = TopicSerializer(many=True, read_only=True)  # Nested serializer for topics
#     class Meta:
#         model = Chapter
#         fields = ['id', 'chapter_name', 'subject_id', 'topics']