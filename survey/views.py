from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Survey
from .serializers import SurveySerializer
import logging
logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_all_surveys(request):
    surveys = Survey.objects.all()
    
    # Handle empty queryset
    if not surveys.exists():
        return Response({'message': 'No surveys available'}, status=status.HTTP_204_NO_CONTENT)

    serializer = SurveySerializer(surveys, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_survey(request):
    # Validate and save survey data
    serializer = SurveySerializer(data=request.data)
    if serializer.is_valid():
        survey = serializer.save()  # Save the form data
        return Response({'survey_id': survey.survey_id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_survey_by_id(request, survey_id):
    try:
        survey = Survey.objects.get(survey_id=survey_id)
        serializer = SurveySerializer(survey)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Survey.DoesNotExist:
        return Response({'error': 'Survey not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def submit_survey_responses(request, survey_id):
    try:
        # Fetch the survey by its unique survey_id
        survey = Survey.objects.get(survey_id=survey_id)
    except Survey.DoesNotExist:
        return Response({'error': 'Survey not found'}, status=status.HTTP_404_NOT_FOUND)

    # Get the responses from the request payload
    responses = request.data.get('responses', [])
    
    if not responses:
        return Response({'error': 'No responses provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Map the responses to the respective fields
    for response in responses:
        question = response.get('Question')
        answer = response.get('Response')
        
        if question == "Q1":
            survey.Q1 = answer
        elif question == "Q2":
            survey.Q2 = answer
        elif question == "Q3":
            survey.Q3 = answer
        elif question == "Q4":
            survey.Q4 = answer
        elif question == "Q5":
            survey.Q5 = answer
        elif question == "Q6":
            survey.Q6 = answer
        elif question == "Q7":
            survey.Q7 = answer
        elif question == "Q8":
            survey.Q8 = answer

    # Save the updated survey
    survey.save()

    return Response({'message': 'Responses saved successfully'}, status=status.HTTP_200_OK)
