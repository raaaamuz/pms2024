from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Segment
from .serializers import SegmentSerializer
from collections import defaultdict
from rest_framework import status
from django.db.models import Max, Subquery, OuterRef


@api_view(['POST', 'PATCH'])
def create_or_update_segment(request):
    if request.method == 'POST':
        # Existing POST logic
        data = request.data
        print(data)

        project_info = {
            'unit': data[0].get('Unit', ''),
            'year': data[0].get('Year', ''),
            'month': data[0].get('Month', ''),
            'project_name': data[0].get('ProjectName', ''),
            'job_number': data[0].get('JobNumber', ''),
            'client': data[0].get('Client', '')
        }
        
        segments_dict = defaultdict(dict)

        for item in data[1:]:
            segment_number = item.get('segmentNumber')
            item_key = item.get('item')

            if item_key is not None:
                key = item_key.lower().replace(' ', '_').replace('-', '_')
                value = item.get('value')
                segments_dict[segment_number][key] = value
            else:
                continue
        
        segments = []
        for segment_number, segment_data in segments_dict.items():
            segment_data.update(project_info)
            segment_data['segment_number'] = segment_number

            # Check if the segment exists
            try:
                existing_segment = Segment.objects.get(segment_number=segment_number, project_name=project_info['project_name'])
                for attr, value in segment_data.items():
                    setattr(existing_segment, attr, value)
                existing_segment.save()
                segments.append(existing_segment)
            except Segment.DoesNotExist:
                # If it doesn't exist, create a new one
                segments.append(segment_data)

        serializer = SegmentSerializer(data=segments, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        data = request.data
        project_name = data.get('project_name', None)
        
        if not project_name:
            return Response({"error": "Project name is required for PATCH requests."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            segments = Segment.objects.filter(project_name=project_name)
            if not segments.exists():
                return Response({"error": "No segments found for this project name."}, status=status.HTTP_404_NOT_FOUND)

            for segment in segments:
                for key, value in data.items():
                    setattr(segment, key, value)
                segment.save()

            serializer = SegmentSerializer(segments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Segment.DoesNotExist:
            return Response({"error": "Segment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
@api_view(['GET'])
def get_project_names(request):
    last_segments = Segment.objects.filter(project_name=OuterRef('project_name')).order_by('-segment_number')
    project_info = Segment.objects.annotate(last_segment_number=Subquery(last_segments.values('segment_number')
    [:1])).values_list('project_name', 'job_number', 'unit', 'year', 'month', 'last_segment_number',
    'expected_date_of_output', 'segment_number', 'client',
    'completed_month',
    'data_correction_done',
    'status',
    'research_group_head',
    'contact_person_in_research',
    'analysis_group_head',
    'contact_person_in_analysis',
    'actual_final_output',
    'check_list_followed',
    'feedback_survey_done',
    'remarks',
    'archive_taken',
    'loi',
    'number_of_response',
    'oe_costing',
    'oe_coding',
    'top_lines',
    'fw_end_date',
    'fw_start_date',
    'ap_received_date',
    'questionnaire_received_date',
    'top_lines_date',
    'final_r_awn',
    'date_of_r_awn1',
    'date_of_awn',
    'final_processed_samples',
    'achieved_sample_size',
    'actual_sample_size',
    'advanced_analytics',
    'norms_done',
    'survey_platform',
    'dp_platform',
    'project_classification', 'segment_name').distinct()
    return Response(project_info)

@api_view(['GET'])
def get_input_values(request, project_name):
    try:
        segments = Segment.objects.filter(project_name=project_name)
        
        if not segments.exists():
            return Response([], status=200)  # No segments found for this project

        serializer = SegmentSerializer(segments, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(f"Error occurred: {e}")
        return Response({'error': str(e)}, status=500)
