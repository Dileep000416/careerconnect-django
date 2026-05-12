from django.shortcuts import (
    redirect,
    get_object_or_404,
    render
)

from django.contrib.auth.decorators import login_required

from jobs.models import Job

from .models import (
    Application,
    SavedJob,
    Notification
)

from django.http import JsonResponse

from django.views.decorators.http import require_POST

from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def apply_job_view(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    if request.user.userprofile.role != 'candidate':

        return redirect(
            'job_detail',
            id=job.id
        )

    already_applied = Application.objects.filter(
        job=job,
        applicant=request.user
    ).exists()

    if not already_applied:

        application = Application.objects.create(
            job=job,
            applicant=request.user
        )

        Notification.objects.create(

            user=job.recruiter,

            application=application,

            message=f"{request.user.username} applied for {job.title}"

        )

        messages.success(
    request,
    "Application submitted successfully!"
)

    return redirect(
        'job_detail',
        id=job.id
    )


@login_required
def view_applicants(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    search_query = request.GET.get(
    'search',
    ''
)

    applications = Application.objects.filter(
        job=job
)

    if search_query:

        applications = applications.filter(
        applicant__username__icontains=search_query
)

    applications = applications.order_by(
    '-applied_at'
)

    context = {
    'job': job,
    'applications': applications,
    'search_query': search_query
}

    return render(
        request,
        'applications/view_applicants.html',
        context
    )


@login_required
@require_POST
def update_application_status_view(
    request,
    application_id
):

    application = get_object_or_404(
        Application,
        id=application_id
    )

    status = request.POST.get(
        'status'
    )

    valid_statuses = [
        'reviewed',
        'shortlisted',
        'accepted',
        'rejected'
    ]

    if status in valid_statuses:

        application.status = status

        application.save()

        Notification.objects.create(

            user=application.applicant,

            application=application,

            message=f"Your application for {application.job.title} was {status}"

        )

    return redirect(
        'view_applicants',
        job_id=application.job.id
    )


@login_required
def save_job_view(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    already_saved = SavedJob.objects.filter(
        user=request.user,
        job=job
    ).exists()

    if not already_saved:

        SavedJob.objects.create(
            user=request.user,
            job=job
        )

        return JsonResponse({
            'status': 'saved'
        })

    return JsonResponse({
        'status': 'already_saved'
    })


@login_required
def saved_jobs_view(request):

    saved_jobs = SavedJob.objects.filter(
        user=request.user
    ).order_by('-saved_at')

    context = {
        'saved_jobs': saved_jobs
    }

    return render(
        request,
        'applications/saved_jobs.html',
        context
    )


@login_required
def remove_saved_job_view(request, id):

    saved_job = get_object_or_404(
        SavedJob,
        id=id,
        user=request.user
    )

    saved_job.delete()

    return JsonResponse({
        'status': 'removed'
    })


@login_required
def candidate_dashboard_view(request):

    if request.user.userprofile.role != 'candidate':

        return redirect('home')

    applied_jobs = Application.objects.filter(
        applicant=request.user
    ).order_by('-applied_at')

    saved_jobs = SavedJob.objects.filter(
        user=request.user
    ).order_by('-saved_at')

    context = {
        'applied_jobs': applied_jobs,
        'saved_jobs': saved_jobs,
        'total_applied': applied_jobs.count(),

        'reviewed_count': applied_jobs.filter(
            status='reviewed'
        ).count(),

        'shortlisted_count': applied_jobs.filter(
            status='shortlisted'
        ).count(),

        'accepted_count': applied_jobs.filter(
            status='accepted'
        ).count(),
    }

    return render(
        request,
        'applications/candidate_dashboard.html',
        context
    )


@login_required
def notifications_view(request):

    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    notifications.update(
        is_read=True
    )

    context = {
        'notifications': notifications
    }

    return render(
        request,
        'applications/notifications.html',
        context
    )


@login_required
def recruiter_applications_view(request):

    applications = Application.objects.filter(
        job__recruiter=request.user
    ).order_by('-applied_at')

    context = {
        'applications': applications
    }

    return render(
        request,
        'applications/recruiter_applications.html',
        context
    )


@login_required
def candidate_profile_view(request, user_id):

    candidate = get_object_or_404(
        User,
        id=user_id
    )

    profile = candidate.userprofile

    context = {
        'candidate': candidate,
        'profile': profile
    }

    return render(
        request,
        'applications/candidate_profile.html',
        context
    )


@login_required
def shortlisted_candidates_view(request):

    applications = Application.objects.filter(
        job__recruiter=request.user,
        status='shortlisted'
    ).order_by('-applied_at')

    context = {
        'applications': applications
    }

    return render(
        request,
        'applications/shortlisted_candidates.html',
        context
    )