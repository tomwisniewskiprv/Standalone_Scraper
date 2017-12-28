from django.shortcuts import render, get_object_or_404, HttpResponse
from .schedule_scraper2 import ScheduleScraper


def scraper(request):
    template = "scraper.html"
    content = {}

    if request.method == "GET":
        try:
            schedule_scraper = ScheduleScraper()
            content["weeks"] = schedule_scraper.load_numbered_weeks()

        except Exception as error:
            content["result"] = "Error {}".format(error)

    if request.method == "POST":
        try:
            if request.POST.get("week") != None and request.POST.get("week") != '0':
                schedule_scraper = ScheduleScraper(request.POST.get("week"))
                content["weeks"] = schedule_scraper.load_numbered_weeks()
                content["schedule"], content["lecturers"] = schedule_scraper.get_schedule_for_group(request.POST["group"])
                content["group"] = request.POST["group"]

                content["selected_week"] = request.POST["week"]

                # debug
                content["test"] = content.get("weeks")
                content["test2"] = request.POST["week"]

            else:
                schedule_scraper = ScheduleScraper()
                content["weeks"] = schedule_scraper.load_numbered_weeks()

        except Exception as error:
            content["result"] = "Error {}".format(error)

    response = render(request, template, content)
    return response


def about(request):
    template = "about.html"
    response = render(request, template)
    return response
