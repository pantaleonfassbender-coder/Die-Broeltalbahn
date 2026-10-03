"""Modul 3: Nach dem Erz, 1870–1890. Schreibt data/krise.json.

Alle Stellen am Seitenbild gelesen, in den Digitalisaten der Bayerischen Staatsbibliothek
(digitale-sammlungen.de; Bildnummer in Klammern):
- Zeitschrift für Kapital und Rente 6 (1870), S. 175–176 (bsb10620151, Bild 183–184).
- Der Berggeist 15 (1870), Nr. 92, S. 570 (bsb10705901, Bild 574); 18 (1873), S. 559
  (bsb11038191, Bild 567); 25 (1880), S. 105 (bsb11558115, Bild 109).
- Zeitung des Vereins Deutscher Eisenbahnverwaltungen 15 (1875), S. 754–755 (bsb11305412,
  Bild 756–757); 18 (1878), S. 371 (bsb11362291, Bild 391); 26 (1886), S. 414 (bsb11452830, Bild 448).
- Annalen des Deutschen Reiches 1878, S. 101 (bsb11369690, Bild 115).
- Correspondenzblatt des Niederrheinischen Vereins für öffentliche Gesundheitspflege 9 (1880),
  S. 145–146 (bsb11465070, Bild 163–164).
- Jahrbuch für Gesetzgebung, Verwaltung und Volkswirtschaft 4 (1880), S. 284 (bsb11635615, Bild 670).
- Verhandlungen des 30. Rheinischen Provinzial-Landtages (1884), S. 259 (bsb11480800, Bild 263).
- Deutsche Industrie-Zeitung 1882, S. 276; 1883, S. 259; 1884, S. 289; 1885, S. 269; 1887, S. 229
  (bsb11465375 Bild 304, bsb11465376 Bild 295, bsb11465377 Bild 323, bsb11465378 Bild 303,
  bsb11465380 Bild 245).
- Eisenbahn-Verordnungs-Blatt 12 (1889), S. 301 (bsb11467423, Bild 323).
Schreibung und Zeichensetzung der Drucke; ſ als s, ℳ als M, ₰ als Pf.; Silbentrennung aufgelöst;
Sperrungen nicht wiedergegeben; Auslassungen […].
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "krise.json"
SORGE = "ZVDEV 15 (1875), S. 754"
SORGE2 = "ZVDEV 15 (1875), S. 755"


def u(n, pg, titel, orig, note=""):
    d = {"n": n, "pg": pg, "titel": titel, "orig": orig.strip()}
    if note:
        d["note"] = note
    return d


WALDBROEL = [
    u(1, "Kapital und Rente 6 (1870), S. 175–176", "1869: Aktiengesellschaft und Staatsprämie",
      """Broelthaler Eisenbahn-Aktiengesellschaft. Die einschliesslich der Zweigbahn im Sauerbacher Thale 6420 Ruthen lange Broelthalbahn — welche Pferdebahn von der Station Hennef der Cöln-Giessener Eisenbahn abzweigt und deren Anlagekapital einschliesslich der Brücke über die Sieg bis Ende 1868 151,872 Thlr. betrug — war bis jetzt im Besitz der Broelthaler Eisenbahn-Kommanditgesellschaft in „Firma Friedlieb Gustorff & Comp.“ in Hennef. Mittelst Allerhöchster Concessions- und Bestätigungsurkunde vom 12. April 1869 ist die unter dem 3. Februar 1869 vollzogene Umwandlung der genannten Kommanditgesellschaft in eine Aktiengesellschaft unter der Firma „Broelthaler Eisenbahn-Aktiengesellschaft“ genehmigt worden. Gleichzeitig wurde auch der Weiterbau der bisher von der Kommanditgesellschaft betriebenen Transportbahn von Ruppichteroth nach Waldbrod bewilligt; die Aktiengesellschaft als Rechtsnachfolgerin der Kommanditgesellschaft wird denselben auf Grund eines von dieser mit dem Kgl. Eisenbahnkommissariat abgeschlossenen Vertrags vom 25/29. November 1868 zur Ausführung bringen.

Das Grundkapital der Gesellschaft besteht aus 230,000 Thalern, wovon 170,000 Thlr. auf das Aktienkapital und 60,000 Thlr. auf die vom Staate auf Grund des ebenerwähnten Vertrags zu gewährende Staatsprämie entfallen. (In Folge dieses Staatszuschusses geht bei einer etwaigen Auflösung der Gesellschaft das Eigenthum der neu zu erbauenden Strecke Ruppichteroth-Waldbrod nebst antheiligem Inventar ohne Weiteres an den Staat über). — Das Aktienkapital zerfällt in 1700 auf den Inhaber lautende und mit Dividendenscheinen nebst Talons versehene Aktien, jede zu 100 Thaler. […]""",
      "Aus der „Finanziellen Monats-Chronik des Jahres 1869“, einer Übersicht für Anleger. Neu gegenüber dem vorigen Modul (Aktien [1] und [2]) sind der Vertrag mit dem Staat vom November 1868 und die Bedingung, an der das Staatsgeld hing: Löst sich die Gesellschaft auf, fällt die neue Strecke an den Staat. Die Bahn heißt hier noch „Pferdebahn“, sechs Jahre nach der ersten Lokomotive; „Waldbrod“ ist ein Druckfehler für Waldbröl. 6 420 Ruten sind gut 24 Kilometer."),
    u(2, SORGE, "Die Bahn um 1875: auf der Chaussee bis Wörth, dann auf eigenem Grund",
      """Die Brölthalbahn.*

In welch' einfacher Weise eine Localbahn angelegt und wie dieselbe je nach ihrem Zwecke und eintretenden Bedürfnissen vervollkommnet werden kann, zeigt die schmalspurige Brölthalbahn, wohl das einfachste und bescheidenste Verkehrsinstitut der Neuzeit. Sie beweist, wie die Dampfkraft auch für einen geringen Güter- und Personenverkehr entsprechend, ohne grosse Opfer an Geld nutzbar gemacht werden kann, und ist ganz dazu bestimmt, die Aufmerksamkeit auf eine ausgedehntere Einführung von Secundärbahnen, behufs Aufschliessung von solchen Gegenden zu lenken, welche vermöge ihrer geographischen Lage von einer grösseren Bahnverbindung nicht berührt werden können, auch die Grundlagen zu einem solchen Verkehr nicht haben.

Die Brölthalbahn ist 30,3 Km lang, schmalspurig, zweigt von der Deutz-Giessener Bahn bei der Station Hennef a. d. S. ab und führt durch das Brölthal bis Waldbröl, während eine Seitenbahn von 3,3 Km, welche in der oben angegebenen Länge nicht mit enthalten ist, bei Schönenberg in das Sauerthal abzweigt.

Die Bahn liegt auf der längs des Thales sich hinziehenden Chaussee, welche eine Breite von 7,5 m hat und nimmt selbst eine Breite von 1,85 m ein, sodass für den übrigen Strassenverkehr 5,65 m frei bleiben.

Nur die letzte erst vor 2 Jahren beendete Strecke von Wörth bis Waldbröl zweigt von der Chaussee ab und liegt auf eigenem Grund und Boden.

Haltestellen giebt es elf.

Um an der Flusskante zu bleiben, wechselt die Bahn zweimal das Chausseebanquett.

Zwischen Fahrgleis und Bahn sind ähnlich, wie bei Pferdebahnen, weder Gräben noch besondere Absperrungen vorhanden, obgleich dieselben als wünschenswerth anerkannt werden müssen.

Barrièren sind nur 3—4 Mal und zwar an solchen Wegübergängen und innerhalb der Ortschaften an solchen Stellen angebracht, wo die Bahn ganz dicht an den Gebäuden vorüber geht und der Zug erst bei seinem Eintreffen gesehen werden kann.

* Aus C. Sorge, Oberbaurath a/D., ein weiteres Wort zu Gunsten der Secundärbahnen (Als Manuscript gedruckt). Dresden.""",
      "Die Eisenbahn-Fachzeitung druckt am 3. September 1875 einen Auszug aus einer Werbeschrift des sächsischen Oberbaurats a. D. C. Sorge für Nebenbahnen. Sorge war selbst auf der Bahn (Betrieb [3]). Die Hauptbahn liegt weiter auf der Straße; nur das neue Stück nach Waldbröl hat einen eigenen Bahnkörper. „Wörth“ ist wohl der alte Endpunkt bei Ruppichteroth. Dass dieses Stück „erst vor 2 Jahren“ fertig wurde, passt nicht zur Eröffnung 1870 nach der neueren Literatur; entweder schrieb Sorge um 1872, oder der letzte Abschnitt wurde später fertig. Elf Haltestellen gibt es 1875, sieben waren es 1865 (Dampf [4])."),
]

GRUBEN = [
    u(1, "Berggeist 15 (1870), Nr. 92, S. 570", "1870: „nur 254 Waggons Eisenstein“",
      """[…] Unsere Gruben hatten dagegen eine geringe Förderung, diesmal von nur 254 Waggons Eisenstein, und aus den früher entwickelten Gründen ist in dieser Abtheilung schwach und mit geringer Zubusse gearbeitet worden. […]

Das Unternehmen der Brölthaler Eisenbahn ist, unter thätiger Mitwirkung der durch reichen, ausgedehnten Gruben-Besitz betheiligten Actien-Gesellschaft Phönix, aus der Commandit-Gesellschaft F. Gustorff & Co. in eine selbstständige Actien-Gesellschaft umgebildet, und der Weiterbau der Bahn von Ruppichteroth nach Waldbröl unter Zuschuss des Staates von 60,000 Thlrn. nunmehr in der Hauptsache beendet; es werden dadurch günstigere Verhältnisse für das Brölthalbahn-Unternehmen in Aussicht genommen.""",
      "Aus dem Bericht des Sieg-Rheinischen Bergwerks- und Hütten-Actienvereins für 1869/70 (Berggeist vom 18. November 1870). Die Hüttengesellschaft, die die Bahn für ihr Erz angestoßen hatte, förderte im ganzen Jahr 254 Wagen Eisenstein; 1864 fuhr die Bahn täglich gut zwanzig Wagen Kalk und Erz (Chaussee [2]), die Jahresmenge der Hütte war also in zwei Wochen gefahren. Mit „Zubusse“ ist der Zuschuss gemeint, den eine Grube braucht, die sich nicht selbst trägt. Die Zukunft des Erzes im Bröltal liegt jetzt bei Phoenix."),
    u(2, "Berggeist 18 (1873), S. 559", "1873: Gruben und Bahn in einem Konto",
      """Köln, 21. Oct. [Siegrheinischer Bergwerks- und Hütten-Actien-Verein.] Aus dem Geschäftsberichte, welcher der gestern abgehaltenen Gen.-Vers. vorgelegt wurde, ist hervorzuheben, dass die Bilanz in Activen und Passiven die Summe von 2,733,632 Thlr. 29 Sgr. 5 Pfg. aufweist. Die Activen umfassen u. A. das Hohofen-Conto mit 550,000 Thlr., Gruben- und Brölthalbahn-Conto mit 275,000 Thlr., das Walzwerk-Conto mit 418,000 Thlr., das Maschinenfabrik-Conto mit 90,000 Thlr., das Giesserei-Conto mit 85,000 Thlr., die Debitoren mit 780,377 Thlr. 9 Sgr. 10 Pfg. und das Cassa-, Wechsel- und Effecten-Conto mit 66,855 Thlr. 2 Sgr. 6 Pfg. […]""",
      "Die Hüttengesellschaft führt ihre Gruben im Bröltal und ihre Aktien der Bahn in einem gemeinsamen Konto; 1871 waren es 71 100 Taler an Aktien der Bahn. Die Zahl ist ein Buchwert, kein Ertrag. Im „Aktionär“ steht dasselbe Konto 1875 mit über 481 000 Talern; ob darin Abschreibungen oder Zukäufe stecken, sagen die Notizen nicht."),
    u(3, SORGE + "–755", "„Täuschungen in der Ergiebigkeit der Erze“",
      """Von Haus aus waren es montane Interessen, welche die Bahn in's Leben riefen. Allein in Folge von Geschäftsstockungen, Täuschungen in der Ergiebigkeit der Erze etc. hat sich dieser Transportzweig nicht entwickelt und sich in der Hauptsache auf Kalksteine, gebrannten Kalk, Mauersteine, Kohlen, namentlich aber auf landwirthschaftliche Producte und Erzeugnisse beschränkt und ist demnach die Transportmasse eine viel geringere geworden, als ursprünglich angenommen wurde.

[…] Obgleich das Thal weder bevölkert, noch industrielle Ortschafften oder auch nur einzelne dergleichen Etablissements besitzt, ist der Verkehr daselbst doch immer so gross, dass das Unternehmen, auch ohne den ursprünglich beabsichtigten Zweck erreicht zu haben, doch Dank der Einfachheit des Baues und Betriebes nicht nur bestehen, sondern auch noch einen kleinen Gewinn abwerfen kann, der mit jedem Jahre wächst.""",
      "Die Kernstelle des Moduls und die These des ganzen Apparats in den Worten eines Zeitgenossen: Die Bahn wurde für das Erz gebaut, das Erz hielt nicht, was es versprach, und die Bahn lebte trotzdem weiter, von Kalk, Kohle und Landwirtschaft. „Montane Interessen“ heißt Bergbau. Die Frachtmenge, die Sorge aus dem letzten Jahresbericht nennt (Fahrgäste [1]), liegt allerdings sogar etwas über der von 1864 (Ertrag [1]); „viel geringer“ ist sie gemessen an den Hoffnungen von 1860, nicht an den ersten Jahren."),
    u(4, "Berggeist 25 (1880), S. 105", "1880: die Grube der Phoenix, vier Jahre still",
      """Phönix, Act.-Ges. für Bergbau und Hüttenbetrieb in Laar bei Ruhrort. Das der Ges. gehörige Eisenstein-Bergwerk im Bröhlthal, dessen Betrieb vor 4 Jahren eingestellt wurde, ist jetzt wieder in Betrieb gesetzt worden.""",
      "Eine Zeile unter den Firmennachrichten. Die Grube der Phoenix, die 1869 die Verlängerung nach Waldbröl mitbezahlt hatte (Aktien [2]), stand von etwa 1876 bis 1880 still. Das deckt sich mit dem Ende des Bergbaus „um 1875“ nach der neueren Literatur, zeigt aber auch, dass es kein glatter Schluss war: 1880 wird wieder gefördert. Wie lange, sagt diese Quelle nicht."),
]

BETRIEB = [
    u(1, SORGE, "Kurven, Steigungen, Umladen in Hennef",
      """Die Thalbiegungen und Chausseewindungen bedingen enge Curven, welche bis auf 30 m R. herabgehen.

Die Steigungen sind anfangs günstig, gestalten sich aber nach dem Ende der Bahn zu immer stärker. Sie beginnen mit dem Verhältniss 1 : 350, endigen bei Wörth mit 1 : 80 und nehmen auf dem neuen Tracte bei Waldbröl auf 1 : 57 zu.

Die Geleise der Bahn haben 0,785 m Spurweite. Die Schienen hatten früher ein Gewicht von 11,145 k pr. lfd. m. Jetzt ist dafür ein Gewicht von 17,595 k pr. lfd. m. angenommen.

An Gebäuden besitzt die Bahn nur in Hennef einen Güterschuppen, einen Wagenschuppen, ein Maschinen- mit Wasserhaus und eine Werkstatt, sowie in Waldbröl einen Gütterschuppen, sämmtlich nur von Fachwerk und in der allereinfachsten Weise errichtet. Auf der Strecke giebt es einige Wasserstationen der primitivsten Art, welche nur noch eine Stube für einen Tagelöhner enthalten.

Erst in neuerer Zeit ist in Hennef ein massives Gebäude für pp. 21 000 M errichtet, welches im Parterre die Betriebsexpedition und in der ersten Etage die Wohnung des Inspectors enthält.

Ferner ist zur raschen und bequemen, selbstthätigen Umladung der Brölthalbahnwagen auf diejenigen der Köln-Mindener Bahn und umgekehrt ein Zu- und Abfuhrstrang auf einer geneigten Ebene angelegt, welche auf ein hölzernes Gerüst ausläuft. Dieses ist mit Trichtern versehen, vermittelst deren die nach Oeffnung der Seitenklappen der Wagen ausstürzenden Eisensteine, Kalksteine etc. in die darunter gestellten Köln-Mindener Wagen gelangen. […]""",
      "Sorge rechnet schon in Metern und Mark; die Mark galt seit 1873/76. Die Schienen sind schwerer geworden als die sieben Pfund je Fuß von 1865 (Dampf [4]). In Hennef wird Erz und Kalk über ein Holzgerüst mit Trichtern unmittelbar in die Wagen der Staatsbahn geschüttet; die Deutz-Gießener Bahn wurde von der Köln-Mindener Gesellschaft betrieben. „Gütterschuppen“ steht so im Druck."),
    u(2, SORGE, "Pferd gegen Lokomotive",
      """In der ersten Zeit des Betriebes benutzte man Pferde als Zugkraft und es berechnete sich bei der dadurch bedingten geringen Geschwindigkeit und Transportfähigkeit der Centner mit 37,5 Pf. Nach Einführung von Locomotiven und in Folge der dadurch erreichten grösseren Geschwindigkeit und Transportfähigkeit stellen sich die Kosten bis auf 18,1 und 20 Pf.

Interessant ist es, aus dem Bericht der Bahn eine Vergleichung der Kosten des Locomotivenbetriebs mit denjenigen des Betriebs mit Pferden anzustellen. Es ergiebt sich hieraus beispielsweise, dass eines der besten Pferde in steigender Richtung durchschnittlich 2½—3 leere Wagen oder höchstens 1 bis 100 Ctr. beladenen Wagen zog und zu der Tour von Hennef nach Schönenberg, bei günstigen Steigungen (18,75 Km) 5 Stunden und auf der weiteren Strecke bis Wörth eine weitere Stunde brauchte. Wöchentlich machte jedes Pferd 5 Touren. Es bedurfte ausser dem Sonntag noch einen Ruhetag. Die starken Steigungen bis 1 : 80 nahmen die Kraft der Thiere am empfindlichsten in Anspruch, auch dann, wenn sie in dem der Ebene gegenüberstehenden Verhältniss schwächer belastet waren.

Auf den Steigungen 1 : 57 sind dieselben nie verwendet worden.

Eine Locomotive dagegen kann, wie weiter unten angegeben werden wird, noch mehr (2400 Ctr. Brutto) mit doppelter Geschwindigkeit auf der ganzen Linie fördern. Die Locomotiven arbeiten mit einem Dampfüberdruck von 6 Atmosphären, sind Tender-Maschinen, haben Cylinder mit 250 mm Durchmesser und 30 mm Hub und laufen auf 6 gekuppelten Rädern, deren vorderes und hinderes Paar mit solchen Vorrichtungen versehen sind, dass sie sich in Curven seitlich verschieben können. Sie haben einen Radstand von 2,5 m, wiegen mit ganzer Wasser- und Kohlenfüllung 252 Ctr. und kosten 18 000 M.

In steigender Richtung bewegt eine Locomotive 2000—2400 Ctr. Brutto mit einer durchschnittlichen Geschwindigkeit von 1 Stunde pro Meile. In umgekehrter Richtung beträgt die Leistung das Doppelte.

Die Bahn besitzt drei Locomotiven.

Die Güterwagen haben ein Eigengewicht von 42—54 Ctr., eine Tragfähigkeit von 100 Ctr., 1,88 m Radstand und kosten 1500 M. Es sind 50 Stück incl. 3 Personenwagen vorhanden.

Die Bahn ist 33,6 Km lang, hat im Ganzen 874 140 M, mithin pro Kilometer 26 016 M gekostet.

Sie ist mit möglichst geringen Geldmitteln einfach, aber zweckentsprechend gebaut;

Dem Bau ist auch der Betrieb angemessen, der in ebenso einfacher Weise gehandhabt wird. […]

Der Betrieb wird von einem Betriebs-Inspector, 3—4 Expedienten, 2 Locomotivführern, 2 Feuerleuten, 2 Schaffnern und 12—14 Tagelöhnern, die zugleich den Dienst der Bremser, Schlagwärter, Streckenarbeiter etc. mit versehen, gehandhabt.

Der Fahrplan ist so bemessen, dass das Fahren in der Nacht vermieden und auf die Meile ¾ bis 1 Stunde Fahrzeit verwendet wird.""",
      "Der einzige genaue Bericht über die Pferdezeit: Ein gutes Pferd brauchte bergauf fünf Stunden bis Schönenberg, schaffte fünf Fahrten in der Woche und kam die steilen Stücke bei Waldbröl nie hinauf. Die Lokomotive halbierte die Kosten je Zentner; dass sie bergauf „mit doppelter Geschwindigkeit“ fuhr, heißt eine Stunde je Meile, gut 7 km/h. Gegenüber 1865 gibt es drei Lokomotiven statt einer und 50 Wagen statt 27, darunter drei für Personen (Dampf [4]). „1 bis 100 Ctr.“ und „30 mm Hub“ stehen so im Druck und sind wohl Satzfehler. Etwa zwanzig Mann fuhren und unterhielten die ganze Bahn."),
    u(3, SORGE + "–755", "„ein grosser Segen“: was die Anwohner sagten",
      """Auf geraden Strecken, im freien Feld, wo das Geleis sich auf angemessene Entfernung übersehen lässt, wird schneller als in Ortschaften, in Curven und bei Annäherung von Vieh gefahren. Die Fahrt ist letzteren Falls oft eine so langsame, dass, wenn nöthig, rasch still gehalten werden kann. Bei Begegnungen mit Pferden wird der Dampf regelmässig abgesperrt, in der Nähe der Häuser wird die Esse mit Funkenfängern geschützt. Beim Scheuen von Pferden halten nöthigenfalls die Züge, was aber sehr selten, in der letzten Zeit gar nicht mehr vorgekommen ist. Es sind daher auch während des 12jährigen Betriebes mit Locomotiven Unfälle nicht vorgekommen.

Bei der Fahrt, welche ich kürzlich auf der Bahn unternahm, habe ich nicht bemerkt, dass auch nur ein passirendes Zugvieh besonders unruhig geworden wäre, oder auch nur markirt hätte.

In Folge dessen sind die Vorurtheile unter der dortigen Bevölkerung, die im Anfang wohl bestanden haben mögen, mehr und mehr geschwunden und mir selbst ist von vielen Anwohnern, die zu befragen ich Gelegenheit genommen habe, versichert worden, dass sie mit der Bahn vollkommen einverstanden und zufrieden seien, da dieselbe trotz der Kleinheit ihrer Verhältnisse doch ein grosser Segen sei und noch grösseren bringen würde. Ihr Nutzen hätte sich besonders in den letzten Jahren recht deutlich gezeigt, seitdem die Bahn bis Waldbröl verlängert worden sei. Sie habe zur Hebung dieses nur Oekonomie treibenden Dorfes ganz allein beigetragen, und den Beweis geliefert, dass auch die Landwirthschaft, das älteste und vornehmste Gewerbe, durch bessere Verkehrswege nicht nur erhalten, sondern auch gehoben werden könne.

Nicht unerwähnt darf es gelassen werden, dass zu der Harmonie, welche zwischen Anwohnern und Bahnverwaltung besteht, das Verhalten der Letzeren ganz wesentlich beigetragen hat. Dieselbe handhabt nicht nur unter Beobachtung der grössten Rücksichtsnahme für das Publicum den Betrieb und die Bahnpolizei, sondern gleicht auch, was ihr allerdings nur bei dem geringen Geschäftskreis möglich ist, entstehende Differenzen sofort und möchlichst persönlich aus.""",
      "Zum ersten Mal kommen die Leute im Tal zu Wort, wenn auch nur in indirekter Rede und durch einen Fürsprecher der Nebenbahnen, der überzeugen will. Die „Vorurtheile“ der Anfangszeit, die 1864 und 1865 nur als Befürchtungen erwähnt wurden (Chaussee [1] und [3]), sind nach Sorge verschwunden. Mit „diesem nur Oekonomie treibenden Dorfe“ ist wohl Waldbröl gemeint; „Oekonomie“ heißt Landwirtschaft. Die zwölf Jahre Dampfbetrieb führen von 1863 auf 1875."),
]

FAHRGAESTE = [
    u(1, SORGE2, "4 253 Fahrgäste in einem Jahr",
      """Schon in nächster Zeit wird die Betriebsverwaltung sich genöthigt sehen, noch einen Zug einzuschieben, um dem jetzt sehr vernachlässigten jedoch sich hebenden Personenverkehr mehr als bisher Rechnung zu tragen. […]

Nachstehende, dem letzten Jahresberichte der genannten Bahn entnommene Zahlen documentiren gleichfalls, dass dieselbe, wenn schon auf der niedrigsten Stufe des Eisenbahnwesens stehend, und trotz des ausserordentlich geringen Transportes, dennoch lebensfähig ist.

Nach diesem Berichte sind 379 Reisen im ganzen Jahr gemacht und in selbigem 4253 Personen und 662 690 Ctr. Güter befördert worden.

Dafür sind eingenommen worden:
73 557 M 83 Pf. für Frachten und Nebengebühren,
335 M 40 Pf. für Lagermiethe
1 693 M 6 Pf. für Personenbeförderung
75 586 M 29 Pf.

Die Betriebsausgaben betrugen dagegen:
57 655 M 70 Pf. Es ergiebt diess einen Gewinn von
17 930 M 29 Pf., wobei sich für die Person eine durchschnittliche Einnahme von 39,8 Pf. und auf je 100 Ctr. Fracht eine solche von 11 M 10 Pf. berechnet.

Ebenso ist aus der Rechnung zu ersehen, dass der Betrieb nicht mehr als 13 200 M pro Meile erfordert.""",
      "379 Fahrten im Jahr, gut eine am Werktag, und gut 4 000 Fahrgäste, im Schnitt elf bis zwölf am Tag: Der Personenverkehr ist „sehr vernachlässigt“ und bringt gut zwei Prozent der Einnahmen. Fast alles verdient die Bahn mit Fracht. Welches Jahr der „letzte Jahresbericht“ meint, sagt Sorge nicht, wohl 1873 oder 1874. Die Rechnung ergibt 17 930,59 Mark Gewinn statt der gedruckten 17 930,29."),
    u(2, "ZVDEV 18 (1878), S. 371", "1878: die Post fährt mit",
      """[…] Auf diese Anträge sind bis jetzt folgende Entscheidungen erfolgt: […] 3. Der Betriebsunternehmer der Broelthalbahn empfängt für die auf der Theilstrecke Honnef-Ruppichterod cursirenden Postsendungen 1 900 M jährlich, etwa der Ausgabe gleich, welche der Postverwaltung für die Unterhaltung der bisher bestandenen Postverbindung erwuchs. […]""",
      "Aus einem Bericht über die Pflichten kleiner Bahnen gegenüber der Reichspost. Die Bahn übernimmt die Post bis Ruppichteroth und erhält dafür so viel, wie die Post bisher für ihre eigene Verbindung ausgegeben hatte. „Honnef“ ist ein Druckfehler für Hennef; dieselbe Verwechslung steht 1870 in der Zeitschrift des Vereines Deutscher Ingenieure."),
    u(3, "Annalen des Deutschen Reiches 1878, S. 101", "„auch einen regen Personenverkehr“",
      """[…] Die technische Möglichkeit, das Planum der Straßen hierzu zu benutzen, ist durch die seit 1864 auf dem Bankett der Broelthaler Bezirksstraße von Hennef nach Waldbroel angelegte schmalspurige Lokomotiveisenbahn von 33,12 Kilometer Länge und neuerdings durch die normalspurige, gleichfalls mit Dampf betriebene, 5,2 Kilometer lange Straßenbahn von Kassel nach Wilhelmshöhe bewiesen.

Die Anfangs nur für Güterverkehr eingerichtete Broelthalbahn hat in den letzten Jahren durch regelmäßigen Anschluß an die Züge der Deutz-Giessener Bahn und Einstellen von Personenwagen für zwei Klassen auch einen regen Personenverkehr erlangt. Die Züge fahren mit einer Geschwindigkeit im Maximum von 15 Kilometer in der Stunde und haben dabei vielfach Kurven von 34 und 38 Meter Radius, sowie Steigungen von 1 : 50 […]""",
      "Aus dem Aufsatz „Neues System der Sekundärbahnen besonders normal- und schmalspuriger Eisenbahnen mit Dampfbetrieb auf Straßen und Chausseen“. Drei Jahre nach Sorge ist aus dem „vernachlässigten“ ein „reger“ Personenverkehr geworden, weil die Züge jetzt auf die Staatsbahn in Hennef abgestimmt sind. Die Höchstgeschwindigkeit ist dieselbe wie 1864 im freien Feld (Verordnung [2]). „Seit 1864“ ist ungenau; die Bahn fuhr seit 1862, mit Dampf seit 1863."),
    u(4, "Correspondenzblatt Niederrhein 9 (1880), S. 145–146", "Herbst 1880: sechzig Kölner Kinder an der Sieg",
      """Bericht des Kölner Komités für den Ferien-Aufenthalt armer, kränklicher Schulkinder im Herbste 1880, erstattet im Auftrage des Komités vom städtischen Schulinspektor Dr. Brandenberg in Köln.

[…] Die Abfahrt erfolgte am 18. August, morgens 8 Uhr 15 Minuten, von Deutz ab mit der Deutz-Giessener Bahn, deren Verwaltung in dankenswerter Weise die Fahrpreise auf die Hälfte ermässigt hatte. Sehr weit ging die Reise nicht. Nach ungefähr einstündiger Fahrt stiegen die Mädchen an der Station Hennef aus; die Knaben fuhren noch 20 Minuten weiter bis Eitorf. An den Stationen standen die Wirte, welche die Kinder aufnehmen sollten, mit Karren bezw. Leiterwagen bereit, um das Gepäck und im Notfalle auch die Kinder selbst zu fahren. Die Mädchen zogen nach den jenseit der Sieg gelegenen Örtchen Weingartsgasse und Seligenthal; die Knaben kamen teils nach Merten, teils nach Nieder-Ottersbach.

Die genannten Dörfchen haben eine angenehme und gesunde Lage, sind dem Fremdenverkehr nicht sehr ausgesetzt und bieten zu bequemen und hübschen Ausflügen sehr schöne Gelegenheit. […]

[…] Ebenso hatten die gemeinsamen Ausflüge beider Abteilungen für die Kinder manches Angenehme. Ein solcher Ausflug durch das Brölthal nach dem reizend gelegenen Herrenstein, der wegen der Entfernung mit Genehmigung des Komités auf Leiterwagen unternommen wurde, wird sicher so leicht nicht vergessen werden. Auch Schloss Allner mit seinen schönen Gärten und Park-Anlagen wurde gemeinsam besucht und steht bei allen in gutem Andenken.""",
      "Sechzig arme, kränkliche Kinder aus Köln verbringen 25 Tage auf dem Land, die Mädchen bei Hennef. Ihr Ausflug „durch das Brölthal“ zum Herrenstein, einer Haltestelle der Bahn (Dampf [4]), geht auf Leiterwagen, nicht mit dem Zug; ob aus Geldgründen oder weil die Bahn für eine Gruppe nicht passte, sagt der Bericht nicht. Das Bröltal ist hier schon Ausflugsziel für Städter, eine frühe Spur dessen, was um 1900 Sommerfrische heißt. Der Kopf des Berichts sagt „im Herbste“, gemeint sind die Herbstferien; abgefahren wurde am 18. August 1880."),
    u(5, "Jahrbuch für Gesetzgebung 4 (1880), S. 284", "Um 1880: 20 000 Fahrgäste im Jahr",
      """[…] Die Anlagekosten der 33,1 Kilometer langen Brölthalbahn berechneten sich inkl. Betriebsmitteln mit ca. 25,000 Mark. Diese Bahn beförderte in den letzten Jahren ca. 650 000 Zoll-Ctr. und 20 000 Passagiere jährlich und erzielte damit ca. 100 000 Mark Bruttoeinnahmen, welchen 60 000 Mark Regieausgaben gegenüberstehen. Die Ausgaben betragen daher per Bahnmeile jährlich ca. 14 000 Mark. Die Centnermeile kostete der Unternehmung 2½ Pf. und brachte ca. 3½ Pf. ein. — […]""",
      "Aus einer Buchbesprechung im Jahrbuch für Gesetzgebung, Verwaltung und Volkswirtschaft. Die Fracht liegt weiter bei rund 650 000 Zentnern wie 1864 und um 1875 (Ertrag [1], Fahrgäste [1]); die Zahl der Fahrgäste hat sich gegenüber Sorges Jahresbericht fast verfünffacht. Die Bahn wächst nicht mehr durch das Erz, sondern durch die Menschen. „25,000 Mark“ meint die Kosten je Kilometer; das Wort fehlt im Druck."),
]

MUSTER = [
    u(1, "ZVDEV 26 (1886), S. 414", "1886: die billigste Schmalspurbahn Preußens",
      """[…] Während die Schmalspurbahnen im Bezirk der Königlichen Eisenbahndirektion Breslau zu Ende 1884/85 ein Anlagekapital von rund 95 000 M. pro 1 km aufweisen, zeigen nachstehende Hauptbahnen geringere Anlagekosten: nämlich:
die Holsteinische Marschbahn rund 94 000 M.
„ Kirchheimer E. 89 000 „
„ Ludwigs-E. (Nürnberg-Fürth) 62 000 „

Unter den Normalspurbahnen untergeordneter Bedeutung erscheint mit dem geringsten Satz (rund 26 500 M.) die Parchim-Ludwigsluster Eisenbahn.

Das mittlere Anlagekapital der Schmalspurbahnen betrug zu Ende der dargestellten Periode rund 53 000 M. pro 1 km, während diese Kosten sich bei der Brölthalbahn auf nur rund 18 000 M. belaufen. […]""",
      "Aus einer Besprechung der amtlichen Eisenbahnstatistik. Je Kilometer kostete die Bröltalbahn ein Drittel des Durchschnitts der deutschen Schmalspurbahnen und ein Fünftel der schlesischen, mit denen man ihr 1865 ein schlechtes Ende vorausgesagt hatte (Vorbild [1]). Die Zahl weicht von Sorges 26 016 Mark ab (Betrieb [2]); sie rechnet wohl ohne Fahrzeuge oder mit anderem Kapitalbegriff."),
    u(2, "Provinzial-Landtag 30 (1884), S. 259", "Ein Abgeordneter warnt: Bahnen auf Provinzialstraßen",
      """Abgeordneter Freiherr Eugen von Loë: Meine Herren! Als im II. Ausschuß diese Vorlage zur Berathung stand, habe ich den Standpunkt vertreten, daß es mir bedenklich erscheine, ein zu großes Entgegenkommen der Anlage von Sekundärbahnen auf Straßen der Provinz zu bezeigen. Ich bin zu dieser Ansicht durch das gelangt, was ich in der Praxis erlebt habe. In meinem Kreise bestehen auf zwei Provinzialstraßen Sekundärbahnen mit Sekundärbetrieb; die eine ist die schmalspurige Sekundärbahn im Bröhlthal, die andere ist die am 15. Oktober d. J. eröffnete breitspurige Bahn mit Sekundärbetrieb auf der Aggerthalstraße.

Die Erfahrungen, die bis jetzt bei dem Betriebe der Aggerthalbahn gemacht worden sind, lassen es rathsam erscheinen, ein zu großes Entgegenkommen der Neuanlage von Bahnen dieser Art nicht entgegen zu tragen. Ich halte es für bedenklich, wenn Seitens der Provinz die Anlage von solchen Bahnen gefördert wird. Wo eine Sekundärbahn sich voraussichtlich rentiren wird, wird sie angelegt werden, auch ohne daß die Provinz ein Entgegenkommen bezüglich der Benutzung der Straßen zeigt. (Abgeordneter Dietze: Oho!)

Ich glaube es ganz gewiß, Herr Dietze. Wenn aber die Rentabilität fraglich ist, so wird die Preisgebung eines Streifens auf der Straße auch nicht dahin führen, daß die Bahn angelegt wird; sie muß aus anderen Gründen rentabel sein. […] Die Kurven, welche die Eisenbahn in Folge des Einhaltens des Laufes der Straße zu machen hat, sind so groß, daß nur eine Sekundär geschwindigkeit, keine normale Geschwindigkeit — von Schnellzugsgeschwindigkeit keine Rede — erreicht werden kann. Bis jetzt entgleist schon, ich will einmal sagen, alle 10—14 Tage bei der langsamen Geschwindigkeit ein Zug. […]""",
      "Die Gegenstimme. Freiherr Eugen von Loë spricht von „meinem Kreise“, dem Siegkreis, in dem beide Bahnen lagen. Seine Warnung gilt vor allem der neuen normalspurigen Aggertalbahn auf der Straße, auf der nach seinen Worten alle zwei Wochen ein Zug entgleiste; die Bröltalbahn nennt er nur als die andere Bahn dieser Art, ohne Klage. Die Provinz stand vor der Frage, ob sie ihre Straßen für weitere Bahnen hergeben sollte; fünf Jahre später erhält die Bröltalbahn die Konzession für neue Strecken (Bilanz [2])."),
]

BILANZ = [
    u(1, "Deutsche Industrie-Zeitung 1882–1887", "Gewinn, Abschreibung, Dividende: fünf Börsennotizen",
      """1882: […] Die Brölthal-Bahn verwendet den Gewinn von 33330 M zu Abschreibungen. […]

1883: […] Die Brölthal-Bahn verwendet den Ueberschuß zur Verzinsung und zu Abschreibungen. […]

1884: […] Die Brölthaler Eisenbahn-Aktiengesellschaft verwendet den Reingewinn zu Erweiterungen und Abschreibungen. […]

1885: […] Die Brölthaler Eisenbahn-Gesellschaft erzielte 1884 31226 M Brutto-Gewinn, wovon 15394 M zu Abschreibungen, 10076 M zur Zinsenzahlung und 5176 M zu Erneuerungsbauten benutzt werden. […]

1887: Dividenden: […] die Bröhlthaler Eisenbahn 5 %, […]""",
      "Fünf Zeilen aus den Dividendenlisten eines Wirtschaftsblatts, je eine aus einem Jahrgang (S. 276, 259, 289, 269 und 229). Jahrelang gehen die Gewinne in Abschreibungen, Zinsen und Erneuerung; erst 1887 meldet das Blatt eine Dividende von fünf Prozent. Für 1884 ergeben die drei Posten 30 646 Mark, 580 weniger als der genannte Gewinn. Nach der neueren Literatur übernahmen um 1885 das Bankhaus Sal. Oppenheim und die Disconto-Gesellschaft die Gesellschaft; in diesen Notizen findet sich davon nichts, und auch sonst ließ es sich in den Digitalisaten bisher nicht belegen."),
    u(2, "Eisenbahn-Verordnungs-Blatt 12 (1889), S. 301", "Oktober 1889: nach Beuel und Asbach",
      """Allerhöchste Konzessions-Urkunde, betreffend den Bau und Betrieb schmalspuriger Eisenbahnen von Hennef nach Beuel und nach Asbach durch die Brölthaler Eisenbahn-Aktien-Gesellschaft. Vom 27. Oktober 1889.

Wir Wilhelm, von Gottes Gnaden König von Preussen etc.

Nachdem die Brölthaler Eisenbahn-Aktien-Gesellschaft zu Hennef a. d. Sieg darauf angetragen hat, ihr die Ausdehnung ihres Unternehmens auf den Bau und Betrieb schmalspuriger Eisenbahnen von Hennef einerseits nach Beuel, andererseits nach Asbach nebst Abzweigung zu den Brüchen an der Bennau zu gestatten, wollen Wir der gedachten Gesellschaft zum Baue und Betriebe dieser Bahnen Unsere landesherrliche Genehmigung, sowie das Recht zur Entziehung und Beschränkung des Grundeigenthums nach Massgabe der gesetzlichen Bestimmungen unter den nachstehenden Bedingungen hierdurch ertheilen.

I.

Die Gesellschaft ist für ihr gesammtes Bahnunternehmen den bestehenden, wie den künftig ergehenden Reichs- und Landesgesetzen ohne Weiteres unterworfen. […]""",
      "Der Ausblick auf das nächste Modul. Zwanzig Jahre nach Waldbröl erhält die Gesellschaft das Recht, aus der Talbahn ein Netz zu machen: nach Beuel am Rhein gegenüber Bonn und nach Asbach im Westerwald, mit einem Abzweig zu den Brüchen an der Bennau. Nach der neueren Literatur wird Basalt aus diesen Brüchen die Fracht, die das Erz nie geworden ist. Das Museum der Rhein-Sieg-Eisenbahn steht heute in Asbach."),
]

SECS = [
    ("waldbroel", "Bis Waldbröl, 1869–1875", "Waldbröl", WALDBROEL,
     "Die Aktiengesellschaft von 1869 mit der Staatsprämie für die Verlängerung, und die Bahn, wie sie ein sächsischer Baurat um 1875 sah: 30 Kilometer, elf Haltestellen, fast alles auf der Straße."),
    ("gruben", "Das Erz bleibt aus", "Gruben", GRUBEN,
     "Für das Erz gebaut, vom Erz enttäuscht: 254 Wagen im ganzen Jahr 1870, „Täuschungen in der Ergiebigkeit der Erze“ 1875, eine Grube der Phoenix, die vier Jahre stillsteht."),
    ("betrieb", "Der Betrieb um 1875", "Betrieb", BETRIEB,
     "Was Pferde und was Lokomotiven leisteten, wie die Bahn gebaut war und wer sie fuhr, und was die Anwohner einem Besucher aus Sachsen sagten. Aus Sorges Bericht."),
    ("fahrgaeste", "Fahrgäste und Ausflügler", "Fahrgäste", FAHRGAESTE,
     "Von elf Fahrgästen am Tag zu 20 000 im Jahr: Personenwagen, Anschluss an die Staatsbahn, die Post, und sechzig Kölner Ferienkinder auf Leiterwagen im Bröltal."),
    ("muster", "Vorbild und Warnung", "Muster", MUSTER,
     "1886 die billigste Schmalspurbahn der Statistik, 1884 im Provinziallandtag ein Abgeordneter aus dem Siegkreis, der vor Bahnen auf Straßen warnt."),
    ("bilanz", "Bilanz und Ausblick, 1882–1889", "Bilanz", BILANZ,
     "Jahre der Abschreibung, 1887 eine erste Dividende in den Börsenblättern, und 1889 die Konzession für die Strecken nach Beuel und Asbach."),
]

DATA = {
    "titel": "Nach dem Erz, 1870–1890",
    "autor": "Börsen- und Fachpresse, ein sächsischer Baurat, ein Kölner Schulinspektor, der Provinziallandtag, amtliche Blätter",
    "jahr": "1870–1889",
    "sprache": "de",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "Zeitschrift für Kapital und Rente 6 (1870); Der Berggeist 15 (1870), 18 (1873) und 25 (1880); Zeitung des Vereins Deutscher Eisenbahnverwaltungen 15 (1875; Auszug aus C. Sorge, Ein weiteres Wort zu Gunsten der Secundärbahnen), 18 (1878) und 26 (1886); Annalen des Deutschen Reiches 1878; Correspondenzblatt des Niederrheinischen Vereins für öffentliche Gesundheitspflege 9 (1880); Jahrbuch für Gesetzgebung, Verwaltung und Volkswirtschaft 4 (1880); Verhandlungen des 30. Rheinischen Provinzial-Landtages (1884); Deutsche Industrie-Zeitung 1882–1887; Eisenbahn-Verordnungs-Blatt 12 (1889). Alle gelesen an den Digitalisaten der Bayerischen Staatsbibliothek (digitale-sammlungen.de).",
    "hinweis": "Die Jahre, in denen die Bahn ihren Zweck verlor und einen neuen fand: Das Erz blieb hinter den Erwartungen zurück, die Fracht stagnierte bei rund 650 000 Zentnern, und die Fahrgäste kamen, von gut 4 000 um 1875 auf 20 000 um 1880. Die Hauptquelle ist der Bericht des sächsischen Oberbaurats C. Sorge von 1875, ein Plädoyer für Nebenbahnen, das zugleich die genaueste Beschreibung der Bahn dieser Jahre ist. Die Übernahme durch Banken um 1885, die die neuere Literatur nennt, ließ sich in den Digitalisaten nicht belegen. Text nach den Drucken, an den Seitenbildern gelesen; Schreibung und Zeichensetzung wie gedruckt, ſ als s, ℳ als M, ₰ als Pf., Silbentrennung aufgelöst, Sperrungen nicht wiedergegeben, Auslassungen mit […] bezeichnet.",
    "sections": [{"id": i, "titel": t, "zk": zk, "blurb": b, "units": us} for i, t, zk, us, b in SECS],
}

if __name__ == "__main__":
    for s in DATA["sections"]:
        ns = [x["n"] for x in s["units"]]
        assert ns == list(range(1, len(ns) + 1)), (s["id"], ns)
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, sum(len(s["units"]) for s in DATA["sections"]), "units")
