# Standalone_Scraper
Next version of schedule scraper as standalone app.

'If you don't execute your ideas, they die.'

requirements:
* Python 3.6
* Requests: HTTP for Humans
* Beautiful Soup 4.4.0
* Django 1.8.6

OPIS / DESCRIPTION
--

[POL]

Skrypt ma za zadanie zeskrobać plan zajęć dla danego tygodnia ze
strony Uniwersytetu Śląskiego dla mojego roku w bieżącym tygodniu. 
Jest to program czysto ćwiczeniowy. Chciałem spróbować skrobania stron i akurat wybrałem plan
zajęć. Nie ukrywam, że dla innych stron było by to znacznie prostsze ze względu na mniej skomplikowaną 
strukurę HTML. Na szczęście BeautifulSoup działa cuda. :)


21-12-2017
Wersja 2.0 jest uaktualniona jako samodzielny projekt Django z wparciem urządzeń mobilnych.

28-12-2017
Dodano Bootstrap.

Aplikacja w wersji stabilej wdrożona na http://planus.pythonanywhere.com/

29-12-2017
Applikacja wyświetla poprawne wyniki dla dni bez zajęć.


[ENG]

The script is designed to scrape the schedule for a given week from the University of Silesia web page for my year.
It is a purely exercise program. I wanted to try to scrape pages and I just chose the class schedule. 
I do not hide that for other websites it would be much simpler due to the less complicated HTML structure. 
Fortunately, BeautifulSoup works wonders. :)


21-12-2017
Version 2.0 is updated as a standalone Django project with the support of mobile devices.

28-12-2017
Added Bootstrap.

The stable version application implemented on http://planus.pythonanywhere.com/

29-12-2017
Application displays the correct results for days without classes.