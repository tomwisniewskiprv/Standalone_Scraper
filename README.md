# Standalone_Scraper
Next version of schedule scraper as standalone app.

'If you don't execute your ideas, they die.'

requirements:
* Python 3.6
* Requests: HTTP for Humans
* Beautiful Soup 4.4.0
* Django 1.8.6

OPIS / DESCRIPTION
------------------

[POL]

Skrypt ma za zadanie zeskrobać plan zajęć dla danego tygodnia ze
strony Uniwersytetu Śląskiego dla mojego roku w bieżącym tygodniu. 
Jest to program czysto ćwiczeniowy. Chciałem spróbować skrobania stron i akurat wybrałem plan
zajęć. Nie ukrywam, że dla innych stron było by to znacznie prostsze ze względu na mniej skomplikowaną 
strukurę HTML. Na szczęście BeautifulSoup działa cuda. :)


29-03-2018
Zmiany w systemie grup zostały uwzględnione w programie. Poprawki wprowadzone. Teraz plan dla trzech grup powinien 
wyświetlać się poprawnie.

23-02-2018
Zmiany w systemie grup na uczelni powodują błędne działanie programu. Zmiany w toku.

Nie istnieje jeszcze lista przedmiotów oraz wykładowców co powoduje nie wyświetlnie się planu. Zmiany w toku.


12-01-2018
Program domyślnie sprawdza plan w bieżącym tygodniu i wyświetla wyniki zaraz po wczytaniu.

06-01-2018
Aplikacja rozszerzona o GUI oraz możliwość zapisania preferowanej grupy (w cookies). Dodano także stronę informacyjną.

21-12-2017
Wersja 2.0 jest uaktualniona jako samodzielny projekt Django z wsparciem urządzeń mobilnych.

29-12-2017
Aplikacja wyświetla poprawne wyniki dla dni bez zajęć.

28-12-2017
Dodano Bootstrap.
Aplikacja w wersji stabilnej wdrożona na http://planus.pythonanywhere.com/



[ENG] 

The script is designed to scrape the schedule for a given week from the University of Silesia web page for my year.
It is a purely exercise program. I wanted to try to scrape pages and I just chose the class schedule. 
I do not hide that for other websites it would be much simpler due to the less complicated HTML structure. 
Fortunately, BeautifulSoup works wonders. :)


29-03-2018
Changes in the group system have been included in the program. Amendments introduced. Now a plan for three groups should
display correctly.

06-01-2018
Extended application with GUI and the ability to save your preferred group (in cookies). An information page has also been added.

29-12-2017
Application displays the correct results for days without classes.

28-12-2017
Added Bootstrap.
The stable version application implemented on http://planus.pythonanywhere.com/


21-12-2017
Version 2.0 is updated as a standalone Django project with the support of mobile devices.



