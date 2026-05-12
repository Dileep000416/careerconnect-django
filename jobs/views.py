from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from .models import Job
from .forms import JobForm

from applications.models import Application


def job_list_view(request):

    jobs = Job.objects.all().order_by(
        '-created_at'
    )

    search_query = request.GET.get(
        'search',
        ''
    )

    job_type = request.GET.get(
        'job_type',
        ''
    )

    if search_query:

        jobs = jobs.filter(
            title__icontains=search_query
        ) | jobs.filter(
            company_name__icontains=search_query
        ) | jobs.filter(
            location__icontains=search_query
        ) | jobs.filter(
            job_type__icontains=search_query
        )

    if job_type:

        jobs = jobs.filter(
            job_type=job_type
        )

    paginator = Paginator(
        jobs,
        3
    )

    page_number = request.GET.get(
        'page'
    )

    page_obj = paginator.get_page(
        page_number
    )

    context = {
        'jobs': page_obj,
        'page_obj': page_obj,
        'search_query': search_query,
        'job_type': job_type
    }

    return render(
        request,
        'jobs/job_list.html',
        context
    )


def job_detail_view(request, id):

    job = get_object_or_404(
        Job,
        id=id
    )

    already_applied = False

    if request.user.is_authenticated:

        already_applied = Application.objects.filter(
            job=job,
            applicant=request.user
        ).exists()

    context = {
        'job': job,
        'already_applied': already_applied
    }

    return render(
        request,
        'jobs/job_detail.html',
        context
    )

@login_required
def create_job_view(request):

    if request.user.userprofile.role != 'recruiter':

        return redirect('home')

    if request.method == 'POST':

        form = JobForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            job = form.save(commit=False)

            job.recruiter = request.user

            job.save()

            return redirect('jobs')

    else:

        form = JobForm()

    context = {
        'form': form
    }

    return render(
        request,
        'jobs/create_job.html',
        context
    )


@login_required
def recruiter_dashboard_view(request):

    if request.user.userprofile.role != 'recruiter':

        return redirect('home')

    jobs = Job.objects.filter(
        recruiter=request.user
    ).order_by(
        '-created_at'
    )

    applications = Application.objects.filter(
        job__recruiter=request.user
    ).order_by(
        '-applied_at'
    )

    shortlisted_count = applications.filter(
        status='shortlisted'
    ).count()

    context = {

    'jobs': jobs,

    'total_jobs': jobs.count(),

    'total_applications': applications.count(),

    'shortlisted_count': applications.filter(
        status='shortlisted'
    ).count(),

    'accepted_count': applications.filter(
        status='accepted'
    ).count(),

    'rejected_count': applications.filter(
        status='rejected'
    ).count(),

    'reviewed_count': applications.filter(
        status='reviewed'
    ).count(),

    'recent_applications': applications.order_by(
        '-applied_at'
    )[:5]
}

    return render(
        request,
        'jobs/recruiter_dashboard.html',
        context
    )


@login_required
def edit_job_view(request, id):

    if request.user.userprofile.role != 'recruiter':

        return redirect('home')

    job = get_object_or_404(
        Job,
        id=id,
        recruiter=request.user
    )

    if request.method == 'POST':

        form = JobForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            form.save()

            return redirect(
                'job_detail',
                id=job.id
            )

    else:

        form = JobForm(
            instance=job
        )

    context = {
        'form': form,
        'job': job
    }

    return render(
        request,
        'jobs/edit_job.html',
        context
    )


@login_required
def delete_job_view(request, id):

    if request.user.userprofile.role != 'recruiter':

        return redirect('home')

    job = get_object_or_404(
        Job,
        id=id,
        recruiter=request.user
    )

    job.delete()

    return redirect(
        'recruiter_dashboard'
    )


@login_required
def recruiter_jobs_view(request):

    jobs = Job.objects.filter(
        recruiter=request.user
    ).order_by(
        '-created_at'
    )

    context = {
        'jobs': jobs
    }

    return render(
        request,
        'jobs/recruiter_jobs.html',
        context
    )