"""Modul 4: Der Ausbau, 1891–1903. Schreibt data/ausbau.json.

Alle Stellen am Seitenbild gelesen. Digitalisate der Bayerischen Staatsbibliothek
(digitale-sammlungen.de; Bildnummer in Klammern):
- Lauer, Die Brölthaler Eisenbahn, Zeitschrift für Kleinbahnen 1 (1894), S. 285–289 und 409
  (bsb11467140, Bild 299–303 und 429); der Text des Internet Archive (bub_gb_4HohAQAAMAAJ)
  diente als Lesehilfe und wurde am Bild berichtigt.
- Uhland's Verkehrszeitung 6 (1891/92), S. 366 (bsb11558744, Bild 380); 7 (1893), S. 173
  (bsb11558745, Bild 185); 9 (1895), S. 349 (bsb11558747, Bild 361).
- Verhandlungen des Landeseisenbahnrates 1893, S. 54 (bsb11467451, Bild 74).
- Kladderadatsch 45 (1892), Briefkasten (bsb11464406, Bild 514).
- Jahresbericht der Handelskammer zu Bonn für 1895, S. 130–131 (bsb11793900, Bild 150–151);
  für 1896, S. 157 (bsb11793901, Bild 179).
- Der Aktionär 43 (1896), S. 285 (bsb11787253, Bild 295).
- Jahrbuch der Berliner Börse 1897/98, S. 651 (bsb11868083, Bild 703).
- Bayerisches Börsen- und Handelsblatt 6 (1898), S. 155 (bsb11850555, Bild 159).
Internet Archive (archive.org, Google-Digitalisate der Zeitschrift für Kleinbahnen):
- Zeitschrift für Kleinbahnen 6 (1899), S. 340 (bub_gb_R_rNAAAAMAAJ, Blatt 353);
  8 (1901), S. 732 (bub_gb_IoAhAQAAMAAJ, Blatt 726).
Schreibung und Zeichensetzung der Drucke; ſ als s; Silbentrennung aufgelöst;
Sperrungen nicht wiedergegeben; Auslassungen […].
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "ausbau.json"
L = "Lauer 1894"


def u(n, pg, titel, orig, note=""):
    d = {"n": n, "pg": pg, "titel": titel, "orig": orig.strip()}
    if note:
        d["note"] = note
    return d


RUECKBLICK = [
    u(1, L + ", S. 285", "Wie es anfing: Schleppbahn, Siegbrücke, ein Polizeikommissar im Zug",
      """Die Brölthaler Eisenbahn. Von Lauer, Königl. Regierungsbaumeister in Elberfeld.

1. Entwicklungsgang.

Die älteste Schmalspurbahn Deutschlands, die Brölthalbahn, blickt gegenwärtig bereits auf ein zweiunddreissigjähriges Dasein zurück.

Als im Jahre 1860 das Brölthal, welches bei Hennef nach Nordosten hin vom Siegthale abzweigt, durch eine von den betheiligten Gemeinden mit Staatsunterstützung gebaute Strasse erschlossen war, kamen sogleich die in der Nähe von Schönenberg gelegenen Eisensteingruben und Kalksteinbrüche in lebhafteren Betrieb, doch stellte sich bald heraus, dass die Achsenfracht noch zu theuer war, um ihn lohnend werden zu lassen. Die Eigenthümer, welche nach den gemachten Aufschlüssen die Gruben für sehr ergiebig hielten, planten daher den Bau einer schmalspurigen Schleppbahn nach dem Bahnhofe Hennef der Köln-Giessener Eisenbahn, welche ganz auf dem Banket der Strasse liegen sollte. Es hielt schwer, die Gemeinden, denen die letztere gehörte, zur Gestattung der Mitbenutzung zu bewegen, was heute verwunderlich erscheinen mag. Nach langen Verhandlungen kam eine Vereinbarung zu Stande, in welcher die Gesellschaft — damals unter der Firma Aktien-Kommanditgesellschaft Friedlieb, Gustorff & Co. — sich zum Bau einer gemeinsamen Siegbrücke bei Allner unter Ablösung einer daselbst bestehenden Fährgerechtsame verpflichtete, aber ausser der Unterhaltung des von ihr benutzten Strassentheils keine dauernde Last übernahm. Nunmehr wurde das Gleis rasch vorgestreckt, und im März 1862 die Strecke von der 0,4 km von Bahnhof Hennef entfernten Ueberladestelle Warth bis Schönenberg mit Abzweigung ins Saurenbacher Thal für Pferdebetrieb eröffnet.

Wie vorausgesehen war, erwies sich dieser schon nach kurzer Zeit als gänzlich ungenügend, und es wurde bei der Aufsichtsbehörde, damals der königlichen Regierung zu Köln, beantragt, die Verwendung von Lokomotiven zu gestatten. Da es derzeit etwas ganz unerhörtes war, Lokomotiven auf einer Strasse laufen zu lassen, darf es nicht verwundern, dass die Betheiligten lebhaften Einspruch erhoben, und so wurde die beantragte Erlaubniss im Jahre 1863 zunächst nur versuchsweise ertheilt. Einige Monate lang fuhr mit jedem Zuge ein Kommissar der Polizeiverwaltung mit und notirte jedes Scheuwerden von Pferden. Glücklicherweise kamen keine grösseren Unglücksfälle vor, so dass der Lokomotivbetrieb gegen Ende des Jahres unter den nöthigen Sicherheitsvorschriften endgültig gestattet wurde. Zu der ersten wurde nun eine zweite Maschine beschafft, und zugleich 1864 das Gleis bis Ruppichteroth fortgeführt, um sämmtliche Gruben des Thales anschliessen zu können. Damit war das kleine Unternehmen zu einem vorläufigen Abschlusse gelangt, aber es sollte bald eine schwere Krisis durchmachen.""",
      "Die erste zusammenhängende Geschichte der Bahn, geschrieben 1894 von einem preußischen Regierungsbaumeister für die neue Fachzeitschrift der Kleinbahnen, wohl mit Unterlagen der Gesellschaft. Sie erzählt einiges, was die Quellen der 1860er Jahre nicht sagen: den Widerstand der Gemeinden gegen die Bahn auf ihrer Straße, die Fähre bei Allner, die der Brücke weichen musste, und den Polizeikommissar, der 1863 jedes scheuende Pferd notierte; im Einzelnen geregelt wurde der Dampfbetrieb dann im November 1864 (Verordnung [1]). Anderes weicht ab: Eröffnung im März 1862 (die Meldungen von 1862 erwarteten sie im Juni, Anleihe [3]), Ruppichteroth 1864 (der Hüttenbericht sagt 1. Juli 1863, Dampf [2]). „Betheiligte“, die Einspruch erhoben, sind die Anlieger und Fuhrleute. Lauers Lebensdaten sind nicht ermittelt."),
    u(2, L + ", S. 285–287", "Die Krise und die Wende: vom Erz zur Landwirtschaft",
      """Wenn auch der Güterverkehr von vornherein öffentlich war, so entwickelte sich doch der allgemeine Verkehr bei dem gänzlichen Mangel einer Industrie im Thale nur sehr langsam, und die Sendungen von den Gruben bei Schönenberg nach Hennef bildeten weitaus die Mehrzahl der beförderten Gütermengen. Diese Förderungen liessen aber schon nach wenigen Jahren erheblich nach, theils weil die Gruben nicht so ergiebig blieben, wie sie sich zuerst gezeigt hatten, theils weil die abnehmenden Hüttenwerke ihre Erze auf inzwischen entstandenen neuen Schienenwegen von anderen Bergwerken her vortheilhafter beziehen konnten. Die thalabwärts beförderte Gütermenge sank unter diesen Verhältnissen von rund 28 700 t im Jahre 1864 auf 13 200 t im Jahre 1869, und es war abzusehen, dass das Unternehmen zum Erliegen kommen musste, wenn nicht andere Verkehrsquellen erschlossen wurden.

Zu diesem Zwecke fasste man eine Verlängerung der Linie bis zur Kreisstadt Waldbröl ins Auge, die vor dem Bau der Aggerthalbahn ein nicht unbedeutendes Hinterland hatte. Das hierzu erforderliche Kapital war bei der ungünstigen Geschäftslage nicht leicht zu beschaffen, und es bedurfte einer einmaligen unverzinslichen Staatsbeihülfe von 180 000 M, hergegeben unter der Bedingung, dass die Strecke Waldbröl—Ruppichteroth mit einem entsprechenden Theil der Betriebsmittel für den Fall des Erlöschens der Gesellschaft in Staatseigenthum übergehen sollte und dass sie ferner für Personenverkehr eingerichtet würde, der auf die ganze Bahn auszudehnen war, sobald gewisse Reinüberschüsse erzielt wurden. […]

Es war vorab wenig Aussicht auf starken Personenverkehr im Brölthal, da es in zu geringem Abstande der Sieg nahezu parallel läuft, und die Ortschaften weniger im Grunde, als auf den beiderseitigen Höhen liegen. Als daher 1870 die Strecke nach Waldbröl eröffnet worden war, liess die Verwaltung zunächst zwei Jahre lang einen kleinen, eigentlich zum Dienstgebrauche gebauten Personenwagen am Schlusse des täglichen Güterzuges zur unentgeltlichen Benutzung mitlaufen und gewöhnte so das Publikum an die neue Beförderungsweise. Ferner wurde in Hennef das Gleis vom Güterbahnhof Warth bis zum Staatsbahnhof verlängert, um die Züge bis unmittelbar vor das Empfangsgebäude daselbst durchzuführen. 1872 fuhren die ersten gemischten Züge, von 1875 ab täglich drei Personenzüge und ein Güterzug. Die Zahl der Maschinen wurde allmählich auf 5, die der Güterwagen auf 62 und die der Personenwagen auf 10 gebracht.

Es folgten nun fünfzehn Betriebsjahre, in denen das Unternehmen nicht weiter ausgedehnt wurde. Der Personenverkehr nahm allmählich zu, während zugleich im Güterverkehr eine eigenthümliche und sehr interessante Wandlung vor sich ging. Die Gruben förderten immer weniger und kamen zuletzt zum Erliegen, so dass die Zweigbahn ins Saurenbacher Thal ausser Betrieb gestellt werden musste; dafür hob sich der Ortsgüterverkehr von Jahr zu Jahr, und die beförderte Gesammtmenge, die bis 1870 stetig gesunken war, stieg langsam und erreichte nahezu wieder die Anfangshöhe. Ausgeführt wurden hauptsächlich landwirthschaftliche Erzeugnisse und dafür Bedarfsartikel: Kohlen, künstliche Düngemittel, Baumaterialien, Sämereien und Lebensmittel in steigender Menge eingeführt, so dass die Sendungen zu Berg bald die zu Thale gehenden überstiegen. Beispielsweise wurden im Jahre 1864 rd. 4200 t herauf und rd. 28 700 t herunter, im Jahre 1881 rd. 19 000 t herauf und rd. 13 000 t herunter gefahren. […]""",
      "Lauer bestätigt aus zwanzig Jahren Abstand, was die Quellen des vorigen Moduls zeigen (Gruben [3]), und gibt den Grund hinzu: Die Hütten bezogen ihr Erz über neue Bahnen von anderswo. Der Umschlag ist in zwei Zahlenpaaren gefasst: 1864 fuhr fast alles talab, 1881 fuhr mehr talauf, Kohle, Kunstdünger, Baustoffe, Saatgut. Die Bahn war von einer Erzbahn zu einer Versorgungsbahn der Bauern geworden. Neu ist, wie der Personenverkehr begann: zwei Jahre lang mit einem Dienstwagen, den man umsonst benutzen durfte. Die 28 700 Tonnen von 1864 sind die Zahl, die die neuere Literatur übernommen hat."),
]

STRECKEN = [
    u(1, "Uhland's Verkehrszeitung 6 (1891/92), S. 366", "1891: Werft am Rhein, Basalt bis Holland",
      """Die Strecke Hennef-Asbach der Brölthalbahn soll im August dem Personenverkehr übergeben werden. Hierdurch wird das sich durch reiche Naturschönheiten auszeichnende Brölthal den Bewohnern des linken Rheinufers und dem grossen Touristenverkehr zugänglicher gemacht. Um es den Schiffen zu ermöglichen, zur Aufnahme von Gütern bis dicht an die Bahn heranzukommen, sind am Rheinufer bei Beuel Werftanlagen in einer Ausdehnung von 650 m hergestellt worden. Hochliegende Geleise ermöglichen es, selbst bei hohem Wasserstande Verladungen zu bewirken. Hierdurch wird die Versendung von Basaltsteinen und anderem Baumaterial bis nach Holland ermöglicht. Man erhofft von diesem Unternehmen einen hohen wirthschaftlichen Nutzen, mithin Deckung der nicht unbeträchtlichen Kosten.""",
      "Eine Meldung aus dem Sommer 1891. Die beiden Zwecke des neuen Netzes stehen nebeneinander: Ausflügler aus Bonn und vom linken Rheinufer ins Bröltal, und Basalt aus dem Westerwald über eine eigene Werft in Beuel auf Rheinschiffe bis Holland. Der August-Termin für Asbach hielt nicht; eröffnet wurde nach Lauer im Januar und Juni 1892 (Strecken [2])."),
    u(2, L + ", S. 287", "1885: neue Besitzer, Basalt und 82 Kilometer",
      """Im Jahre 1885 ging das Eigenthum der Bahn in andere Hände über, und der bisherige Betriebsleiter Saling trat als Vorstand und Direktor an die Spitze des Unternehmens. Auf seine Anregung hin nahmen die neuen Besitzer binnen kurzem eine wesentliche Erweiterung des Unternehmens in Aussicht. Es handelte sich darum, die im unteren Westerwalde in ausgezeichneter Beschaffenheit und unerschöpflichen Mengen vorkommenden Basalte und Quarzite zunächst nach Hennef behufs Umladung in die Staatsbahnwagen, dann aber auch nach dem Rhein zur Weiterbeförderung in Schiffe zu bringen. Zu diesem Zwecke wurde die neue Linie Asbach—Hennef—Beuel geplant, auf deren unterer Hälfte zugleich ein lebhafter Personenverkehr erwartet werden konnte. Die letztere Theilstrecke, die zugleich die Stammlinie mit dem Rhein verbindet, wurde wegen der geringeren Geländeschwierigkeiten zuerst fertiggestellt und im Dezember 1890 eröffnet. Ihr folgte im Januar 1892 die Theilstrecke Hennef—Buchholz und im Juni desselben Jahres die Schlussstrecke Buchholz—Asbach.

Eine weitere Vergrösserung des Netzes bildet die im Mai 1893 bis Oberpleis eröffnete, im Januar 1894 nur für Güterverkehr bis Herresbach fortgeführte Zweigbahn in das sich hinter dem Siebengebirge her erstreckende Pleisthal. Auch hier ist in erster Linie auf Beförderung von Mineralien: Quarziten, Basalten und Thonen, demnächst vielleicht auch Braunkohlen gerechnet, daneben auch auf landwirthschaftliche Erzeugnisse und Bedarfsartikel, sowie Personenverkehr.

Alle neuen Strecken sind ganz aus den Mitteln der Gesellschaft, ohne Unterstützung vom Staate oder sonstigen Verbänden, auch nicht durch freie Hergabe des Grund und Bodens, gebaut worden. Der Güterverkehr, namentlich die Basaltförderung aus dem Westerwalde, hat sich stark entwickelt, ihm ist es zu verdanken, dass schon jetzt eine fünfprozentige Verzinsung des Anlagekapitals erreicht ist. Der Personenverkehr, an Sonn- und Feiertagen recht lebhaft, ist in der Woche ziemlich schwach und bringt kaum die Selbstkosten auf.

Im ganzen sind gegenwärtig 82 km Bahnlänge im Betriebe, darunter 78,1 km für den allgemeinen Verkehr. Auf denselben bewegen sich 11 Lokomotiven, 25 Personen- und 341 Güterwagen. Die Spurweite beträgt 0,785 m (2½ Fuss Rheinisch).""",
      "Der Besitzwechsel von 1885, den die neuere Literatur mit dem Bankhaus Sal. Oppenheim und der Disconto-Gesellschaft verbindet, steht hier ohne Namen: „in andere Hände“. Saling, der nach Lauer den Betrieb seit der Aktiengesellschaft von 1869 leitete, wird Direktor. Der Plan ist der des Jahres 1860 mit anderem Gestein: Wie damals Erz und Kalk, soll jetzt Basalt aus den Brüchen zur Staatsbahn und zum Rhein. Anders als 1869 baut die Gesellschaft ohne Staatsgeld. Gegenüber 1875 hat sich das Netz mehr als verdoppelt, die Zahl der Wagen fast versiebenfacht (Betrieb [2]). Zu den Eröffnungstagen siehe Strecken [4]."),
    u(3, L + ", S. 288", "Beuel, Pützchen und ein aufblühendes Hennef",
      """b) Beuel—Asbach und Niederpleis—Herresbach.

Die neueren Strecken der Brölthalbahn liegen zum weitaus grössten Theile auf eigenem Bahnkörper und ähneln überhaupt, soweit es der Charakter der Schmalspur gestattet, mehr modernen Nebenbahnen.

Der Anfangsbahnhof Beuel liegt auf Ordinate 52,10 unmittelbar am Rheinufer bei dem Landungsplatze der Bonner Fähre, in günstigster Lage für den Verkehr dieser grossen Stadt mit dem rechtsufrigen Hinterlande. Aus dem Bahnhofe heraustretend wendet sich die Bahn sogleich in scharfer Biegung landeinwärts und geht bei km 1,4 schienenfrei unter der rechtsrheinischen Staatsbahn durch, deren Bahnhof Beuel fast 20 Minuten von der Fähre entfernt ist, ersteigt dann mit 1 : 80 ansteigend die erste Terrasse der den Strom begleitenden Hügelreihe, auf der sie sich von da ab fast horizontal weiter bewegt, ohne irgendwie nennenswerthen Geländeschwierigkeiten zu begegnen. In km 1,8 wird der Wallfahrtsort Pützchen berührt, dessen Jahrmärkte einmal im Herbste einen gewaltigen Personenverkehr hervorrufen. […]

[…] Dieser Ort ist ein aufblühendes, aus drei Dörfern: Hennef, Geistingen und Warth zusammenwachsendes Landstädtchen; der Gemeindebezirk, der den Namen Geistingen trägt, hat 4922 Einwohner. Um den Bahnhof Hennef herum ist eine rege Industrie entstanden, besonders Fabriken für landwirthschaftliche Maschinen, von denen die Fabrik automatischer Waagen von Reuther & Reisert die bedeutendste ist. Dass auch die Bodenpreise in der Nähe von Hennef eine ansehnliche Höhe erreicht haben, zeigen mehrere Schleifen und Krümmungen, die die Bahn zu beiden Seiten der Station macht, ohne durch technische Rücksichten dazu genöthigt zu sein.""",
      "Die neue Linie beginnt am Fähranleger gegenüber Bonn, näher an der Stadt als der Bahnhof der Staatsbahn. Der Markt in Pützchen, bis heute als „Pützchens Markt“ bekannt, bringt einmal im Jahr die Fahrgäste. In Hennef zeigt Lauer, was die Bahn mit dem Ort gemacht hat: aus drei Dörfern ein Landstädtchen mit Fabriken rund um den Bahnhof, und Grundstücke, die so teuer geworden sind, dass die Bahn um sie herumfährt."),
    u(4, "Jahrbuch der Berliner Börse 1897/98, S. 651", "Die Daten aus der Sicht der Börse",
      """[Zweck]: Bau und Betrieb der auf Grund der Concessionen vom 12. April 1869, 27. October 1889, 13. November 1890 und der Concession der Königl. Regierung zu Köln vom 29. August 1893 erbauten Eisenbahnlinien: Beuel—Hennef—Waldbröl, Hennef—Asbach, Niederpleis—Oberpleis—Herresbach. Die Bahn ist als Schmalspurbahn mit einer Spurweite von 0,785 m angelegt und hat eine Gesammtlänge von 79,60 km. Die Strecke Hennef—Waldbröl (31,10 km) ist im Betrieb seit 1870, Hennef—Beuel (14,80 km) seit 20. December 1891, Hennef—Asbach (23,60 km) seit 20. Januar 1892, Niederpleis—Oberpleis (8,00 km) seit 5. Mai 1893 und Oberpleis—Herresbach (1,50 km), seit 1. März 1894. Die Bahn hat in Hennef Anschluss an die Staatsbahn und in Beuel gegenüber von Bonn durch ihre Rheinwerftanlagen Verbindung mit der Rheinschifffahrt. Die Gen.-Vers. vom 5. October 1895 genehmigte den Bau der Linie Niederpleis-Siegburg, die am 7. April 1897 concessionirt wurde, und die Anpachtung der Heisterbachthalbahn auf zwei Jahre zu 26 000 M. für 1896 und 30 000 M. für 1897 abzüglich Verwaltungskosten und Rücklagen. Falls keine Kündigung erfolgt, wird die Pachtsumme für die nächsten beiden Jahre auf 32 000 M. jährlich erhöht. Die Gen.-Vers. vom 19. Mai 1897 beschloss die weitere Ausgestaltung des Unternehmens durch Verbesserung und Vergrösserung der eigenen Anlagen, sowie den Bau von neuen Strecken und Zweiglinien und den Erwerb sowie die Umwandlung der Heisterbacher Thalbahn in eine Eisenbahn nach den Bestimmungen des Gesetzes von 1838.

[Verhältniss zum Staate]: Die Ges. wurde mit einer unverzinslichen Staatsprämie von 180 000 M. ausgestattet; […]""",
      "Ein Nachschlagewerk für Anleger, sachlich und mit genauen Tagen. Für die Strecke nach Beuel nennt es den 20. Dezember 1891, Lauer den Dezember 1890 (Strecken [2]), die neuere Literatur den 1. Dezember 1891. Der Widerspruch bleibt hier stehen. Die eckigen Klammern ersetzen die gesperrten Stichwörter „Zweck“ und „Verhältniss zum Staate“, deren Anfang am Seitenrand verloren ist."),
    u(5, "Zeitschrift für Kleinbahnen 6 (1899), S. 340", "1. Mai 1899: Siegburg",
      """4. Betriebseröffnungen. […] 4. Am 1. Mai 1899 die Strecke Niederpleis-Siegburg der schmalspurigen Brölthalbahn.""",
      "Eine Zeile in der Liste der Betriebseröffnungen. Mit den dreieinhalb Kilometern von Niederpleis erreicht die Bahn die Kreisstadt Siegburg, den Sitz des Landratsamts. Konzessioniert war die Strecke am 7. April 1897 (Strecken [4])."),
    u(6, "Uhland's Verkehrszeitung 9 (1895), S. 349", "Pläne am Rhein: eine elektrische Bahn über die neue Brücke",
      """Die Brölthalbahn. Unter den Nebenbahnunternehmungen, welche in der Gegend zwischen Sieg und Rhein in jüngster Zeit entstanden sind, ist wohl eine der wichtigsten das Project der Brölthalbahn. Im Zusammenhange mit der bevorstehenden Errichtung einer festen Rheinbrücke zwischen Bonn und Beuel plant man die Anlage einer elektrisch betriebenen Bahn von Bonn aus über die zu errichtende Brücke, das rechte Rheinufer aufwärts nach Königswinter und Honnef. Hieran anschliessend soll die Brölthalbahn gebaut werden, welche von Beuel aus unmittelbar am Rhein hin nach Honnef und von da ins Brölthal führen würde.""",
      "Die Meldung ist verworren: Die Bröltalbahn bestand längst, gemeint ist wohl eine neue Strecke der Gesellschaft am Rhein entlang. Sie zeigt, wie weit die Pläne der neunziger Jahre griffen: Bonn bekam 1898 seine feste Rheinbrücke, und die Gesellschaft plante eine elektrische Bahn rheinaufwärts (Heisterbach [3]). Gebaut hat sie diese Strecke nicht."),
]

BASALT = [
    u(1, L + ", S. 289", "Basaltsäulen am Bennauer Kopf",
      """[…] Von Eudenberg an beginnen zu beiden Seiten auf den Höhen die Basalte sichtbar zu werden, die das Schiefergebirge in schmalem Gange durchbrochen haben und, oben breit auseinandergeflossen, zu fünfseitigen Säulen erstarrt sind. In km 27,9 von Beuel aus gerechnet, erreicht die Bahn Krautscheid, wo sich ein der Firma Krupp gehöriges Blei-, Zink- und Eisenbergwerk befindet. Hier beginnt mit anhaltender Steigung 1 : 60 der Anstieg zur Wasserscheide zwischen Hanfbach und Griesebach in langer Entwicklungsschleife, zunächst bis Mendt noch thalaufwärts, dann am selben Hange wieder zurück, so dass ähnlich wie bei der bekannten Schleife der Landquart-Davoser Bahn über Klosters die zurückgelegte Strecke weithin übersehen werden kann. Auf der Scheitelhöhe liegt in 247 m Meereshöhe, also 180 m über Hennef, die Station Buchholz, kurz dahinter der grosse angeschlossene Basaltbruch Limberger Kopf. Die Bahn fällt nun etwa 18 m herunter bis zur Station Bennau (Thal), jenseits deren sich der Bennauer Kopf mit den beiden weitaus grössten Basaltbrüchen des Westerwaldes erhebt. Diese Brüche gewähren mit ihren an 20 m hohen senkrechten Wänden, die ganz aus prachtvoll gleichmässigen Basaltsäulen gebildet sind, einen sehr malerischen Anblick. Sie sind durch eine besondere 1 : 40 steigende Zweigbahn angeschlossen, in deren zu den einzelnen Ladebühnen führenden Zweiggleisen sogar die Steigung 1 : 25 vorkommt.

Die Hauptlinie ist von Bennau (Thal) noch bis zu dem Weiler Asbach fortgesetzt, wo sie in 245 m Meereshöhe, 38,4 km von Beuel, 23,6 km von Hennef entfernt, ihren Endpunkt erreicht.

Von der beschriebenen Bahnstrecke zweigt bei Station Niederpleis die 10,7 km lange Linie ins Pleisthal ab. […] dann endet die Linie für öffentlichen Verkehr in km 8,6 bei dem Orte Oberpleis, dessen Gemeindebezirk 3693 Einwohner zählt, in einer Meereshöhe von 119,4 m. Darüber hinaus ist sie noch bis zu der Ladestelle Herresbach fortgesetzt, um die dortigen ausgedehnten Quarzitbrüche anzuschliessen. Dieses Material, welches sich gewöhnlich in Begleitung des Basalts findet, ist von schöner kristallinischer Beschaffenheit, besteht aus fast reiner Kieselsäure und wird hauptsächlich von Chamottefabriken benutzt.""",
      "Hier liegt die neue Fracht der Bahn: Basalt vom Limberger und vom Bennauer Kopf, Quarzit bei Herresbach. Basalt brauchte man als Pflaster- und Schotterstein für Straßen, Uferbauten und Bahndämme; Quarzit für feuerfeste Steine. Bei Krautscheid liegt noch ein Erzbergwerk, das der Firma Krupp gehört. Das Asbacher Museum der Rhein-Sieg-Eisenbahn steht heute am Ende dieser Linie."),
    u(2, "Landeseisenbahnrat 1893, S. 54", "Der Basalt und die Konkurrenz von der Lahn",
      """[…] Die Berufungen anderer Steinbruchbesitzer seien gegenstandslos, da nur die regelmäßige Fracht des Spezialtarifs III der Staatseisenbahnen (26 Mark für 10 t auf 66 km) berechnet werden solle.

Seitens der Vertreter des Herrn Ministers wird mitgetheilt, daß von der Brölthalbahn-Aktiengesellschaft ebenfalls Widerspruch gegen den Antrag erhoben sei, indem sie eine Schädigung der in ihrem Verkehrsbereich vorhandenen Steinbruchbetriebe und eine Schmälerung ihrer Verkehrseinnahmen befürchte.

In thatsächlicher Beziehung werde hierzu bemerkt, daß die Brölthalbahn Bruchsteine zu Ausnahmetarifen fahre, denen erheblich niedrigere Einheitssätze zu Grunde liegen. Beispielsweise betrage für Sendungen von 10 t der Streckensatz in der Verkehrsbeziehung Asbach (Westerwald) — Beuel (Rheinufer) = 39 km bei Ausscheidung von 9 Pf. Abfertigungsgebühr für 100 kg nur 1,8 Pf. für das Tonnenkilometer, während derselbe sich in dem für die Strecke Heckholzhausen — Oberlahnstein = 66 km beantragten Frachtsatze auf 2,6 Pf. stelle. […]""",
      "Aus den Verhandlungen des Landeseisenbahnrats, des Beirats der preußischen Staatsbahnen. Ein Steinbruch an der Lahn wollte wohl für seinen Basalt einen billigen Tarif der Staatsbahn zum Rhein; die Bröltalbahn widersprach, weil ihre Westerwälder Brüche dieselben Abnehmer am Rhein belieferten. Die Antwort des Ministeriums: Die Bröltalbahn fahre ihren eigenen Basalt ohnehin billiger. Basalt war 1893 ein Markt, auf dem um Pfennige je Tonnenkilometer gestritten wurde."),
]

FAHRPLAN = [
    u(1, L + ", S. 287–288", "Die Stammlinie 1894: „nur den Touristen anziehende Strecke“",
      """3. Beschreibung der einzelnen Bahnstrecken.

a) Hennef—Waldbröl.

[…] Vom Ausgange dieses Bahnhofs an legt sich das Gleis auf das Banket der Brölstrasse und überschreitet mit ihr in km 2,2 bei Allner die Sieg auf gemeinsamer Brücke mit hölzernem Unterbau, die acht Oeffnungen von 11,75 m Spannweite besitzt. Von da ab folgt die Bahn, mit der Strasse allmählich ansteigend, den Windungen des romantischen Brölthales, berührt bei km 4,3 das Dorf Bröl, dann die Ingersaueler Mühle und das in tiefster Waldeinsamkeit liegende Schloss Herrnstein. Diese nur den Touristen anziehende Strecke endigt in km 14,6 bei Felderhoferbrücke, wo sich das Thal der Homburger Bröl abzweigt, die Bahn überschreitet den Bach und tritt in offeneres Gelände ein, in welchem sie bei km 16,9 das Dorf Schönenberg erreicht. 3,4 km weiter liegt der erste grössere Ort Ruppichteroth mit 3016 Gemeindeeingesessenen, der auf Ordinate 168,0 fast genau 100 m über Hennef gelegen, sechs Jahre lang den Endpunkt der Bahn bildete. Immer noch auf dem Strassenbanket liegend, steigt diese weiter an, an den Weilern Benroth, Berkenroth und Rossenbach vorbei, bis sie die Strasse bei km 30,0 verlässt, um auf eigenem Planum den Endbahnhof Waldbröl zu erreichen. Dieser liegt 267,8 m hoch, also zufällig wieder fast genau 100 m über Ruppichteroth und 200 m über Hennef. Waldbröl selbst ist ein Kreisstädtchen von 5216 Einwohnern, die hauptsächlich Landwirthschaft betreiben, doch ist auch einige Industrie vorhanden.

Bei Schönenberg zweigte die 2,4 km lange, auf eigenem Planum liegende Zweigstrecke ins Saurenbacher Thal ab, die nicht mehr betrieben wird. […]

Die Brölstrasse ist, soweit sie von der Bahn benutzt wird, 7,53 m zwischen den Gräben breit und lässt bei einer grössten Breite der Fahrzeuge von 1,88 m noch 5,65 m für den Strassenverkehr frei. Es besteht keinerlei Abgrenzung zwischen Bahn und Strasse. […]

Wegeschranken kommen an zwei Stellen vor: die Siegbrücke wird bei Annäherung eines Zuges für Fuhrwerke gesperrt, und ausserdem ein ganz unübersichtlicher Uebergang im Dorfe Bröl durch Schranken geschlossen. Man sieht also, dass die örtlichen Verhältnisse solche unter Umständen auch bei einer ganz geringen Fahrgeschwindigkeit (im Dorfe sind nur 12 km gestattet) bedingen können.

Die gesammten Anlagekosten der Stammstrecke haben rund 757 000 M oder 22 880 M für das km einschliesslich der Betriebsmittel betragen.""",
      "Eine Fahrt durch das Tal, wie sie 1894 ein Fachmann beschrieb. Das untere Bröltal zwischen Allner und Felderhoferbrücke ist für Lauer nur noch „den Touristen anziehend“: Erz und Kalk, für die die Bahn gebaut wurde, kommen dort nicht mehr vor. Ruppichteroth war nach ihm „sechs Jahre“ Endpunkt, also von 1864 bis 1870 (Rückblick [1]). Die Bahn liegt weiter ohne Abgrenzung auf der Straße, wie 1875 (Waldbröl [2]); im Dorf Bröl darf sie 12 km/h fahren, 1864 waren es 7,5 (Verordnung [2])."),
    u(2, L + ", S. 409", "Der Fahrplan von 1894: Sonntagszüge und ein Viehmarktzug",
      """9. Der Fahrdienst.

Die grösste von der Aufsichtsbehörde zugelassene Fahrgeschwindigkeit beträgt auf den Strassenstrecken 18 km, auf den Strecken mit eigenem Bahnkörper 25 km für die Stunde.

Auf den Strecken Hennef—Asbach und Oberpleis—Niederpleis verkehren nur gemischte Züge, daneben auf ersterer Strecke Bedarfsgüterzüge. Zwischen Waldbröl und Beuel fahren zwar reine Personenzüge, aber auch sie dürfen an Wochentagen Güterwagen mitnehmen, soweit dieses ohne Ueberschreitung der Fahrzeit angängig ist. […]

Auf diese Weise sind die ganzen Fahrzeiten der Züge mit Personenbeförderung ermittelt:
zwischen Beuel und Hennef für 14,8 km mit 7 Zwischenstationen zu 55 Min.;
zwischen Hennef und Waldbröl für 31,1 km mit 10 Zwischenstationen zu 140 Min.;
zwischen Oberpleis und Niederpleis für 8,6 km mit 4 Zwischenst. zu 39 Min.;
zwischen Hennef und Asbach für 14,8 km mit 8 Zwischenstationen zu 92 Min.

Es verkehren täglich in jeder Richtung:
zwischen Beuel und Hennef: 6 Personenzüge, 1 Bedarfsgüterzug;
zwischen Hennef und Waldbröl: 3 Personenzüge, 1 Bedarfsgüterzug;
zwischen Oberpleis und Niederpleis: 4 gemischte Züge;
zwischen Hennef und Asbach: 3 gemischte Züge, 1 Bedarfsgüterzug.

Sonntags fallen die Güterzüge und je ein Frühpersonenzug zwischen Hennef und Beuel, sowie umgekehrt aus, dafür verkehren Sonntags nachmittags zwei Sonderpersonenzüge auf der letztgenannten Strecke und einer im Brölthale. Der Güterzug im Brölthale wird in der Regel nur im Sommer gefahren, da bei dem schwächeren Winterverkehre die Güterwagen mit den Personenzügen Beförderung finden können. Ausser diesen Zügen verkehrt noch ein Sonderviehzug mit Personenbeförderung an den Waldbröler Viehmarkttagen.

Den regelmässigen Dienst an Wochentagen versehen sechs Lokomotiven mit sechs Wagenzügen, sechs Lokomotivpersonalen und sechs Zugpersonalen, von denen dem Fahrplane entsprechend je vier an den Endstationen und zwei in Hennef stationirt sind. […] Die Wagenzüge bestehen entweder aus einem getheilten Wagen II./III. und einem III. Klasse oder (zwischen Beuel und Waldbröl) aus einem Wagen II. und zwei solchen III. Klasse. Sonntags tritt entsprechende Verstärkung ein […].""",
      "Zwei Stunden und zwanzig Minuten von Hennef nach Waldbröl, gut 13 km/h im Schnitt. Der Fahrplan zeigt die zwei Gesichter der Bahn: werktags Fracht und wenige Fahrgäste, sonntags Sonderzüge für Ausflügler zwischen Bonn und dem Bröltal. Und einen Zug für die Bauern: an den Viehmarkttagen in Waldbröl fährt ein Viehzug, in dem auch Menschen mitfahren. Die Fahrzeiten sind am Seitenbild gelesen; der Volltext des Internet Archive hat hier Lesefehler."),
    u(3, "Uhland's Verkehrszeitung 7 (1893), S. 173", "Mai 1893: Entgleisung in Beuel",
      """Auf dem Bahnhof Beuel, Brölthalbahn, fand am Abend des 22. Mai eine Zugentgleisung statt, wobei zwei Personen verletzt und mehrere Wagen stark beschädigt wurden.""",
      "Eine Zeile in einer Liste von Eisenbahnunfällen in aller Welt, zwischen einem Güterzug bei Biedenkopf und einem Unglück in Irland. Mehr ist über den Unfall in den zugänglichen Quellen nicht zu finden. Der 22. Mai 1893 war Pfingstmontag; die Züge am Rhein werden voll gewesen sein."),
]

HEISTERBACH = [
    u(1, "Kladderadatsch 45 (1892), Briefkasten", "1892: ein Extrazug zum Wurstessen",
      """Bonn. C. Z.: Im „General-Anzeiger für Bonn und Umgegend“ vom 12. Dec. macht die „Heisterbacher Thalbahn“ bekannt: „Zu dem am Dienstag d. 6. d. Mts. stattfindenden Wurstessen bei Peter Lichtenberg in Heisterbacherrott verkehrt ab Niederdollendorf ein Extrazug um 6 Nachmittags. Ferner wird Abends ein Zug zur Rückfahrt gestellt.“ Mehr kann man wirklich nicht verlangen.""",
      "Aus dem Briefkasten des Berliner Witzblatts, wo Leser Fundstücke aus Provinzzeitungen einsandten. Die Heisterbacher Talbahn war eine kleine Schmalspurbahn vom Rhein bei Niederdollendorf am Kloster Heisterbach vorbei ins Siebengebirge, mit Steinbrüchen als Hauptkunden. Ein Extrazug zum Wurstessen in einem Dorfwirtshaus sagt viel über eine Bahn, die um jeden Fahrgast warb."),
    u(2, "Handelskammer Bonn, Jahresbericht für 1895, S. 130–131", "1895: Defizit und Übernahme des Betriebs",
      """7. Heisterbacher Thalbahn.

Dem Bericht über das Geschäftsjahr 1895 ist folgendes zu entnehmen.
Die Betriebseinnahmen betrugen:
aus dem Personenverkehre 7074,10 Mk.
„ „ Güterverkehr 56081,50 „
hierzu kommen diverse Einnahmen 432,53 „
zusammen 63588,13 Mk.
Die Betriebsausgaben stellten sich auf 49421,78 „
mithin verblieb ein Brutto-Ueberschuß von 14166,35 Mk.
Hiervon sind zu bestreiten gewesen:
10743,75 Mk. Obligationszinsen
3512,50 „ „ , die später fällig sind
9695,45 „ Hypothekenzinsen
23951,70 Mk. zusammen.
Es ergab sich somit 1895 ein Defizit von 9785,35 Mk.
und zuzüglich des Vortrages aus 1894 9693,81 „
ein Gesammt-Defizit von 19479,16 Mk.
Abgeschrieben sind für zweifelhafte Debitoren 33043,64 „
ferner für Unterstützungs-Konto 15,— „
sowie auf Bahnanlage etc. 12000,— „
Das Jahr 1895 schloß somit ab mit einem Gesammtverlust von 64537,80 Mk.

Dies ungünstige Ergebniß wird als Folge mangelhafter Führung des Unternehmens seitens der früheren Verwaltung bezeichnet.

Seit dem 6. September 1895 ist für Aufsichtsrath und Direktion ein Wechsel eingetreten. Die faktische Führung des Betriebes geschieht seit dem 3. Oktober 1895 durch die Brölthalbahn unter verantwortlicher Aufsicht eines technischen Leiters der Gesellschaft.""",
      "Die Nachbarbahn ist 1895 überschuldet: Sie verdient ihre Betriebskosten, aber nicht die Zinsen. Die Bröltalbahn übernimmt den Betrieb, zunächst als Pächterin (Strecken [4]). Auffällig ist das Verhältnis der Einnahmen: Fast neun Zehntel kommen aus dem Güterverkehr, also aus den Steinbrüchen des Siebengebirges, wie bei der Bröltalbahn aus dem Westerwälder Basalt."),
    u(3, "Handelskammer Bonn, Jahresbericht für 1896, S. 157", "1896: Pläne nach Rostingen, Neuwied und über Heisterbach",
      """[…] Der Bericht erwähnt, daß, wie schon mitgetheilt, die Betriebsgenehmigung für die Verbindungsstrecke Niederpleis-Siegburg zugesagt ist. Der von der Gesellschaft ausgearbeitete Plan einer elektrischen Bahn von Beuel über Honnef bis Neuwied mußte neu bearbeitet werden, da für die Strecke von Beuel nach Honnef statt der Landstraße eigener Grund benutzt werden soll. Durch diese Arbeiten ist eine Verzögerung eingetreten, sodaß bis jetzt die Betriebsgenehmigung nicht zu erlangen war. Sodann wird eine Verbindung mit der Heisterbacher Thalbahn, und zwar von Scheid über Oberpleis nach Herresbach und die Verlängerung der Brölthalbahn bis nach Rostingen erstrebt, wofür die allgemeinen Vorarbeiten fertiggestellt sind. Der Heisterbacher Thalbahn sollen ferner für den Bahnhofsumbau in Dollendorf 125 000 Mk. vorgeschossen werden und ebenso weitere Geldmittel zum Umbau ihrer Spur auf die der Brölthalbahn. Um dafür die nöthige Sicherheit zu erlangen, hat die Gesellschaft die Actien, Schuldverschreibungen und Hypothekenschulden der Heisterbacher Thalbahn erworben. […]""",
      "Aus dem Bericht der Bröltaler Gesellschaft für 1896, wie ihn die Bonner Handelskammer wiedergibt. Die Gesellschaft kauft die Heisterbacher Talbahn faktisch auf, über ihre Aktien und Schulden, und will sie auf die eigene Spur umbauen und mit dem eigenen Netz bei Oberpleis verbinden. Die elektrische Bahn bis Neuwied blieb Plan. Herresbach–Rostingen wurde nach der neueren Literatur 1902 gebaut."),
    u(4, "Zeitschrift für Kleinbahnen 8 (1901), S. 732", "1901: Erwerb der Heisterbacher Talbahn genehmigt",
      """[Genehmigungen …] 9. Der Brölthaler Eisenbahngesellschaft zu Hennef (Sieg) zum Erwerbe und Betriebe der Heisterbacher Thalbahn (Niederdollendorf—Grengelsbitze).""",
      "Eine Zeile in der Liste der Genehmigungen für Kleinbahnen. Sechs Jahre nach der Übernahme des Betriebs darf die Gesellschaft die Nachbarbahn auch förmlich erwerben; die neuere Literatur nennt 1903 als Jahr, in dem die Heisterbacher Talbahn ganz in der Bröltalbahn aufging. Mit ihr reicht das Netz an zwei Stellen an den Rhein, in Beuel und in Niederdollendorf."),
]

RENDITE = [
    u(1, "Der Aktionär 43 (1896), S. 285", "1895: Überschuss, Anleihen, Erdöl",
      """(Brölthaler Eisenbahn.) In 1895 betrugen die Betriebseinnahmen M 380,352 (— M 6000), wärend die Ausgaben M 192,292 (+ 4000) erforderten. Aus dem Ueberschuss von M 188,896 gehen ab für Anleihezinsen M 87,300 (— 8000), für die Rücklage M 31,422. Aus dem Ueberschuss von M 70,174 wird die erste Jahrestilgung der Schuldverschreibungen, die am 1. April 1896 fällig wurde, mit M 7500 entnommen. Die Dividende kann deshalb nur auf 3% (4½%) festgesetzt werden, wärend die Staatseisenbahnsteuer M 1491 erfordert und M 3049 vorgetragen werden. Der Geschäftsbericht teilt mit, dass die im Vorjahre in Aussicht gestellten grösseren Erdölsendungen wegen Nichtgenehmigung der erforderlichen geringen Tarifermässigungen bisher nicht erlangt wurden. […]""",
      "Die Einnahmen sind gegenüber 1875 fünfmal so hoch (Fahrgäste [1]), aber das neue Netz ist mit Anleihen gebaut, und deren Zinsen fressen fast die Hälfte des Überschusses. Die Dividende fällt von viereinhalb auf drei Prozent. Woher und wohin die Erdölsendungen gehen sollten, sagt die Notiz nicht. Die Zahlen in Klammern sind die Veränderungen gegenüber dem Vorjahr."),
    u(2, "Bayerisches Börsen- und Handelsblatt 6 (1898), S. 155", "1898: vier Prozent",
      """Die Broelthaler Bahn zahlt bei 86,914 Mk. (82,166) Ueberschuß 4 Proz. (3½) Dividende.""",
      "Eine Börsenzeile. Die Dividenden der neunziger Jahre liegen zwischen drei und fünfeinhalb Prozent: 1890 meldet die Allgemeine Zeitung 5½, 1891 5, 1895 3, 1897 4 Prozent. Für eine Kleinbahn in einer dünn besiedelten Gegend ist das ordentlich, für Spekulanten wenig. Der Basalt trägt die Bahn, aber er macht niemanden reich."),
]

SECS = [
    ("rueckblick", "Rückblick von 1894", "Rückblick", RUECKBLICK,
     "Die erste Geschichte der Bahn, geschrieben zu ihrem 32. Jahr: der Widerstand der Gemeinden, ein Polizeikommissar im Zug, das Ende des Erzes und die Wende zur Bahn der Bauern."),
    ("strecken", "Das Netz, 1890–1899", "Strecken", STRECKEN,
     "Neue Besitzer ab 1885 und ein neuer Zweck: Basalt. Strecken nach Beuel am Rhein, nach Asbach im Westerwald, nach Oberpleis und Siegburg; aus 33 Kilometern werden über 80."),
    ("basalt", "Der Basalt", "Basalt", BASALT,
     "Säulenbasalt am Bennauer Kopf, Quarzit bei Herresbach, und ein Streit um Pfennige je Tonnenkilometer mit der Konkurrenz von der Lahn."),
    ("fahrplan", "Fahrt und Fahrplan 1894", "Fahrplan", FAHRPLAN,
     "Die Stammlinie durch das „romantische“ Bröltal, der Fahrplan mit Sonntagszügen und einem Viehmarktzug, und ein Unfall am Pfingstmontag 1893."),
    ("heisterbach", "Die Heisterbacher Talbahn", "Heisterbach", HEISTERBACH,
     "Eine kleine Nachbarbahn im Siebengebirge: ein Extrazug zum Wurstessen, ein Defizit, die Übernahme des Betriebs 1895 und der Erwerb 1901."),
    ("rendite", "Rendite", "Rendite", RENDITE,
     "Was das Netz einbrachte: Überschüsse, Anleihezinsen, Dividenden zwischen drei und fünfeinhalb Prozent."),
]

DATA = {
    "titel": "Der Ausbau, 1891–1903",
    "autor": "Lauer (Zeitschrift für Kleinbahnen 1894), Fach- und Börsenpresse, Handelskammer Bonn, Landeseisenbahnrat, Kladderadatsch",
    "jahr": "1891–1901",
    "sprache": "de",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "Lauer, Die Brölthaler Eisenbahn, in: Zeitschrift für Kleinbahnen 1 (1894); Zeitschrift für Kleinbahnen 6 (1899) und 8 (1901); Uhland's Verkehrszeitung 1891–1895; Verhandlungen des Landeseisenbahnrates 1893; Kladderadatsch 45 (1892); Jahresberichte der Handelskammer zu Bonn für 1895 und 1896; Der Aktionär 1896; Jahrbuch der Berliner Börse 1897/98; Bayerisches Börsen- und Handelsblatt 1898. Gelesen an den Digitalisaten der Bayerischen Staatsbibliothek (digitale-sammlungen.de) und des Internet Archive (archive.org).",
    "hinweis": "Die Jahre, in denen aus der Talbahn ein Netz wurde: neue Besitzer 1885, Basalt aus dem Westerwald als neue Fracht, Strecken nach Beuel, Asbach, Oberpleis und Siegburg, dazu die Heisterbacher Talbahn. Die Hauptquelle ist der Aufsatz des Regierungsbaumeisters Lauer von 1894, die erste Geschichte der Bahn; seine Lebensdaten sind nicht ermittelt. Wer die Bahn 1885 kaufte, sagt keine der hier gelesenen Quellen; die neuere Literatur nennt Banken. Für die Eröffnung der Strecke nach Beuel stehen 1890 und 1891 gegeneinander. Text nach den Drucken, an den Seitenbildern gelesen; Schreibung und Zeichensetzung wie gedruckt, ſ als s, Silbentrennung aufgelöst, Sperrungen nicht wiedergegeben, Auslassungen mit […] bezeichnet.",
    "sections": [{"id": i, "titel": t, "zk": zk, "blurb": b, "units": us} for i, t, zk, us, b in SECS],
}

if __name__ == "__main__":
    for s in DATA["sections"]:
        ns = [x["n"] for x in s["units"]]
        assert ns == list(range(1, len(ns) + 1)), (s["id"], ns)
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, sum(len(s["units"]) for s in DATA["sections"]), "units")
