from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Team

def dashboard(request):
    teams = Team.objects.all().order_by('call_sign')
    active_teams = teams.exclude(status='OFF')
    standby_teams = teams.filter(status='OFF')
    main_statuses = [
        ('GREEN', 'Πράσινο - Ελεύθερη'),
        ('YELLOW', 'Κίτρινο - Περιπολία'),
        ('RED', 'Κόκκινο - Περιστατικό'),
        ('PURPLE', 'Μωβ - Σταθερό Σημείο'),
    ]
    return render(request, 'operations/dashboard.html', {
        'active_teams': active_teams,
        'standby_teams': standby_teams,
        'main_statuses': main_statuses
    })

@require_POST
def add_team(request):
    call_sign = request.POST.get('call_sign')
    leader_name = request.POST.get('leader_name')
    leader_phone = request.POST.get('leader_phone')
    members = request.POST.getlist('members[]')
    members_text = ", ".join(filter(None, members))
    
    Team.objects.create(
        call_sign=call_sign,
        leader_full_name=leader_name,
        leader_phone=leader_phone,
        members_list=members_text,
        status='OFF'
    )
    return redirect('dashboard')

@require_POST
def update_status(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    new_status = request.POST.get('status')
    team.status = new_status
    
    if new_status in ['GREEN', 'OFF']:
        team.location = ""
        team.incident_report = ""
    else:
        team.location = request.POST.get('location', '')
        team.incident_report = request.POST.get('incident_report', '')
    
    team.save()
    return redirect('dashboard')

@require_POST
def edit_team_details(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team.call_sign = request.POST.get('call_sign')
    team.leader_full_name = request.POST.get('leader_name')
    team.leader_phone = request.POST.get('leader_phone')
    members = request.POST.getlist('members[]')
    team.members_list = ", ".join(filter(None, members))
    team.save()
    return redirect('dashboard')

@require_POST
def delete_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team.delete()
    return redirect('dashboard')