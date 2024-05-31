from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist


from .serializers import SubjectSerializer, ChapterSerializer, ChapterSerializer_Nested, TopicSerializer, QuestionSerializer, SmcqSerializer, MmcqSerializer, IntegerTypeSerializer
from .models import Subject, Chapter, Topic, Smcq, Mmcq, IntegerType

from django.core import serializers

# Create your views here.
  
class GetSmcqAll(APIView):
  def get(self, request, format=None):
    queryset = Smcq.objects.all()
    serializer = SmcqSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class GetMmcqAll(APIView):
  def get(self, request, format=None):
    queryset = Mmcq.objects.all()
    serializer = MmcqSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class GetIntegerTypeAll(APIView):
  def get(self, request, format=None):
    queryset = IntegerType.objects.all()
    serializer = IntegerTypeSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def GetSmcq(request, question_id):
  if request.method == 'GET':
    queryset = get_object_or_404(Smcq, pk=question_id)
    data = {
      'question': queryset.question.url,
      'creator': queryset.creator.username,
      'created_at': queryset.created_at,
      'topic_id': queryset.topic_id.id,
      'correct_option': queryset.correct_option,
    }
    return JsonResponse(data)

def GetMmcq(request, question_id):
  if request.method == 'GET':
    queryset = get_object_or_404(Mmcq, pk=question_id)
    data = {
      'question': queryset.question.url,
      'creator': queryset.creator.username,
      'created_at': queryset.created_at,
      'topic_id': queryset.topic_id.id,
      'is_O1_correct': queryset.is_O1_correct,
      'is_O2_correct': queryset.is_O2_correct,
      'is_O3_correct': queryset.is_O3_correct,
      'is_O4_correct': queryset.is_O4_correct,
    }
    return JsonResponse(data)
  
def GetIntegerType(request, question_id):
  if request.method == 'GET':
    queryset = get_object_or_404(IntegerType, pk=question_id)
    # print(queryset)
    data = {
      'question': queryset.question.url,
      'creator': queryset.creator.username,
      'created_at': queryset.created_at,
      'topic_id': queryset.topic_id.id,
      'correct_answer': queryset.correct_answer
    }
    return JsonResponse(data)
  
# class FetchSubjects(APIView):
#   def get(self, request, format=None):
#     subjects = Subject.objects.all()
#     serializer = SubjectSerializer(subjects, many=True)
#     return HttpResponse(serializer.data, status=status.HTTP_200_OK)

# class FetchChapters(APIView):
#   def get(self, request, format=None):
#     chapters = Chapter.objects.all()
#     serializer = ChapterSerializer(chapters, many=True)
#     return HttpResponse(serializer.data, status=status.HTTP_200_OK)

# class ListTopics(APIView):
#   def get(self, request, format=None):
#     queryset = Topic.objects.all()
#     serializer = TopicSerializer(queryset, many=True)
#     return HttpResponse(serializer.data, status=status.HTTP_200_OK)
  

######################

# def ListTopics(request, ch_name):
#   if request.method == 'GET':
#     ch_id = Chapter.objects.filter(chapter=ch_name)
#     chapters_queryset = get_object_or_404(Mmcq, pk=ch_id)


class TopicList_Subject(APIView):
  def get(self, request, format=None):
    subject_name = request.GET.get('subject_name')
    subject_id = get_object_or_404(Subject, subject_name__iexact=subject_name).id
    chapters = Chapter.objects.filter(subject_id=subject_id)    ## only chapters with taht subject id
    # chapters = Chapter.objects.all()
    serializer = ChapterSerializer_Nested(chapters, many=True, context={'request': request})  # Pass request to serializer
    return Response(serializer.data)
      
class TopicList_Chapter(APIView):
  def get(self, request, format=None):
    chapter_name = request.GET.get('chapter_name')
    chapter_id = get_object_or_404(Chapter, chapter_name__iexact=chapter_name).id
    # print(chapter_id)
    
    topics = Topic.objects.filter(id=chapter_id)
    serializer = TopicSerializer(topics, many=True)
    for topic in topics:
      print(topic)
      print(Topic.get_total_question(topic))
    return Response(serializer.data, status=status.HTTP_200_OK)
  
{
# class ListTopics(APIView):
#   def get(self, request, format=None):
#     for chapter in chapters:
#       data={}
#       # querying to get topic list for this chapter
#       chapters_qs = get_object_or_404(Chapter, chapter_name__iexact=chapter)
#       chapter_id = chapters_qs.id
#       topics = Topic.objects.filter(chapter_id=chapter_id)
      
#       # chapter_serializer = ChapterSerializer(chapter)
#       data[chapters_qs.chapter_name]={}
#       # adding each topic now
#       for topic in topics:
#         # topic serializer
#         serializer = TopicSerializer(topic)
#         extracted_data = serializer.data
#         data[chapters_qs.chapter_name][topic.topic_name] = {serializer}
#       print(data)
      
#     queryset = Topic.objects.all()
#     serializer = TopicSerializer(queryset, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
    #####################################################################
    
    # chapters = get_object_or_404(Chapter, pk=id)
    # queryset = Topic.objects.all()
    # serializer = TopicSerializer(queryset, many=True)     # many true means array of json format
    
    # # trying to get chapter name from chapter_id
    # id = serializer.data[0]['chapter_id']
    # queryset = get_object_or_404(Chapter, pk=id)
    # chapter_name = ChapterSerializer(queryset).data['chapter_name']       # json format

    # # reforming data
    # data = serializer.data
    # data[0]['chapter_name'] = chapter_name
    
    # return Response(data, status=status.HTTP_200_OK)
    
###############

}