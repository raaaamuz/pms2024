from django.contrib import admin
from .models import Segment

class SegmentAdmin(admin.ModelAdmin):
    list_display = ('segment_name', 'segment_number', 'job_number', 'status', 'remarks')
    search_fields = ('segment_name','status')
    readonly_fields = (
        'segment_number',
        'segment_name',
        'research_group_head',
        'contact_person_in_research',
        'analysis_group_head',
        'contact_person_in_analysis',
        'expected_date_of_output',
        'actual_final_output',
        'data_correction_done',
        'status',
        'check_list_followed',
        'completed_month',
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
        'project_classification',
        'unit',
        'year',
        'month',
        'project_name',
        'job_number',
        'client'
    )

admin.site.register(Segment, SegmentAdmin)
