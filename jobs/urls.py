from django.urls import path

from .views import (
    job_list_view,
    create_job_view,
    job_detail_view,
    recruiter_dashboard_view,
    edit_job_view,
    delete_job_view,
    recruiter_jobs_view
)

urlpatterns = [

    path(
        '',
        job_list_view,
        name='jobs'
    ),

    path(
        'create/',
        create_job_view,
        name='create_job'
    ),

    path(
        '<int:id>/',
        job_detail_view,
        name='job_detail'
    ),

    path(
    'dashboard/',
    recruiter_dashboard_view,
    name='recruiter_dashboard'
),

    path(
    'edit/<int:id>/',
    edit_job_view,
    name='edit_job'
),

path(
    'delete/<int:id>/',
    delete_job_view,
    name='delete_job'
),

path(
    'recruiter/jobs/',
    recruiter_jobs_view,
    name='recruiter_jobs'
),

]