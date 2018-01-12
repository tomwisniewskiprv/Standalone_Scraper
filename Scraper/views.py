from django.shortcuts import render, get_object_or_404, HttpResponse
from .schedule_scraper2 import ScheduleScraper


def scraper(request):
    template = "scraper.html"
    content = {}

    if request.COOKIES.get("cookie_info"):
        content["cookie_info"] = request.COOKIES["cookie_info"]

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

                if not request.COOKIES.get("_group"):
                    content["saved_group"] = request.POST["group"]
                else:
                    content["saved_group"] = request.COOKIES.get("_group")

                content["gschedule"] = schedule_scraper.get_schedule_for_all_groups()
                content["selected_week"] = request.POST["week"]

            elif request.POST.get("is_current_week"):
                content["c"] = request.POST.get("is_current_week")
                content["w"] = request.POST.get("week")

                schedule_scraper = ScheduleScraper()
                content["weeks"] = schedule_scraper.load_numbered_weeks()

                if not request.COOKIES.get("_group"):
                    content["saved_group"] = request.POST["group"]
                else:
                    content["saved_group"] = request.COOKIES.get("_group")

                content["gschedule"] = schedule_scraper.get_schedule_for_all_groups()
                content["selected_week"] = schedule_scraper.get_current_week()

            else:
                schedule_scraper = ScheduleScraper()
                content["weeks"] = schedule_scraper.load_numbered_weeks()

        except Exception as error:
            content["result"] = "Error {}".format(error)

    response = render(request, template, content)
    return response


def about(request):
    template = "about.html"
    content = {}

    if request.COOKIES.get("cookie_info"):
        content["cookie_info"] = request.COOKIES["cookie_info"]

    response = render(request, template, content)
    return response


def options(request):
    template = "options.html"
    content = {}

    if request.COOKIES.get("cookie_info"):
        content["cookie_info"] = request.COOKIES["cookie_info"]

    if request.method == "POST":
        if request.POST.get("_group"):
            msg = request.POST["_group"]
            content["msg"] = msg

            response = render(request, template, content)
            response.set_cookie('_group', msg, 3600 * 24 * 365)

            return response
    else:
        response = render(request, template, content)
        return response
