from django.urls import path

from .views import (
    apply_job_view,
    view_applicants,
    save_job_view,
    saved_jobs_view,
    remove_saved_job_view,
    candidate_dashboard_view,
    update_application_status_view,
    notifications_view,
    recruiter_applications_view,
    candidate_profile_view,
    shortlisted_candidates_view
)

urlpatterns = [

    path(
        'apply/<int:job_id>/',
        apply_job_view,
        name='apply_job'
    ),

    path(
        'job/<int:job_id>/applicants/',
        view_applicants,
        name='view_applicants'
    ),

    path(
        'save/<int:job_id>/',
        save_job_view,
        name='save_job'
    ),

    path(
        'saved-jobs/',
        saved_jobs_view,
        name='saved_jobs'
    ),

    path(
        'remove-saved-job/<int:id>/',
        remove_saved_job_view,
        name='remove_saved_job'
    ),

    path(
        'candidate/dashboard/',
        candidate_dashboard_view,
        name='candidate_dashboard'
    ),

    path(
        'application/<int:application_id>/status/',
        update_application_status_view,
        name='update_application_status'
    ),

    path(
        'notifications/',
        notifications_view,
        name='notifications'
    ),

    path(
        'recruiter/applications/',
        recruiter_applications_view,
        name='recruiter_applications'
    ),

    path(
        'candidate/<int:user_id>/profile/',
        candidate_profile_view,
        name='candidate_profile'
    ),

    path(
        'shortlisted/candidates/',
        shortlisted_candidates_view,
        name='shortlisted_candidates'
    ),

]