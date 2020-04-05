# Pir_Project
 
Projekt Czytnika Kart RFID
https://github.com/SadOnion/Pir_Project/


Konfiguracja:

Dodawanie pracowników:
Aby dodać pracownika należy dopisać na koniec pliku workers.txt pracownika według wzorca:
	[Imie] [Nazwisko] [NrKarty] [NrPracownika]
Usuwanie pracowników:
Aby usunąć pracownika należy usunąć wiersz w pliku workers.txt z danymi pracownika którego chcemy usunąć
Dodawanie terminalu RFID:
Aby dodać terminal należy dopisać na koniec pliku terminals.txt id terminalu RFID.


Usuwanie terminalu RFID:
Aby usunąć terminal należy usunąć jego id w pliku terminals.txt
Uruchomienie aplikacji:
1.	Uruchomić skrypt Main.py (Serwer)
2.	Uruchomić skrypt RFIDClient.py (Klient)
Generowanie raportu o pracowniku:
W konsoli serwerowej wprowadzamy ‘1’, następnie wpisujemy id pracownika którego raport chcemy utworzyć. 




Otrzymujemy komunikat, że raport został utworzony w pliku workerLogs.txt


