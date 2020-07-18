from django.shortcuts import render
from .models import BuildingPhoto, Building


# Create your views here.

def show(requests, number):
    building = Building.objects.get(number=number)
    photos = BuildingPhoto.objects.filter(building=building)

    number = building.number
    cv_store = building.cv_store
    cafe = building.cafe
    lounge = building.lounge
    portal = building.portal
    department = building.department
    one_line = building.one_line
    cafeteria = building.cafeteria

    photos_data = []

    for photo in photos:
        photos_data.append(photo.url)

    viz = {"photos_data": photos_data, "number": number, "cv_store": cv_store, "cafe": cafe, "lounge": lounge, \
           "portal": portal, "department": department, "one_line": one_line, "cafeteria": cafeteria}

    return render(requests, 'info/info.html', viz)


def video(requests, number):
    building = Building.objects.get(number=number)
    portal_video = building.portal_video
    return render(requests, 'info/video.html', {"portal_video": portal_video})
