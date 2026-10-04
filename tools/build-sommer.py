"""Modul 5: Kleinbahn und Sommerfrische, 1903–1914. Schreibt data/sommerfrische.json.

Alle Stellen am Seitenbild gelesen.
Internet Archive (archive.org; Blattnummer in Klammern):
- K. Baedeker, Die Rheinlande, 30. Aufl. (Leipzig 1905), S. 421 und 423
  (dierheinlandevo02firgoog, Blatt 619 und 623).
- K. Baedeker, The Rhine, including the Black Forest & the Vosges, 17. Aufl. (Leipzig 1911), S. 141
  (rhineincludingbl00ka, Blatt 240).
- Zeitschrift für Kleinbahnen 10 (1903), S. 323 (bub_gb_BYj-OWrauSMC, Blatt 340);
  15 (1908), S. 437 (bub_gb_0fvNAAAAMAAJ, Blatt 436).
Bayerische Staatsbibliothek (digitale-sammlungen.de; Bildnummer in Klammern):
- Zeitung des Vereins Deutscher Eisenbahnverwaltungen 40 (1900), S. 743 und 1080
  (bsb12041651, Bild 861; bsb12041652, Bild 334).
- Der Arbeiterfreund 39 (1901), S. 265 (bsb12069495, Bild 275).
- Allgemeine Zeitung, 14. Juni 1900 (bsb00085637, Bild 1081); 17. April 1903 (bsb00085669, Bild 773);
  30. März 1906 (bsb00085798, Bild 599).
- Münchner Neueste Nachrichten 1904 (bsb00130108, Bild 309); 4. April 1905 (bsb00130648, Bild 51);
  Oktober 1906 (bsb00130587, Bild 287); 1908 (bsb00130711, Bild 445).
Schreibung und Zeichensetzung der Drucke; ſ als s; Silbentrennung aufgelöst;
Sperrungen nicht wiedergegeben; Auslassungen […].
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "sommerfrische.json"


def u(n, pg, titel, orig, note=""):
    d = {"n": n, "pg": pg, "titel": titel, "orig": orig.strip()}
    if note:
        d["note"] = note
    return d


BAEDEKER = [
    u(1, "Baedeker, Rheinlande 1905, S. 421", "Beuel: Brücke, Gasthaus und Bahnhof der Bröltalbahn",
      """[…] Die Brücke bietet eine herrliche Aussicht auf die Stadt und das Siebengebirge (Brückengeld 5 Pf.).

Am rechten Rheinufer liegt das Dorf Beuel (Straßenbahn, s. S. 415; Gasth.: Schippers, mit großer Veranda, bei der Brücke), mit dem Bahnhof der S. 423 erwähnten Bröltalbahn (Pl. E 1) und dem Bahnhof der rechtsrheinischen Bahn (S. 409) 1km landeinwärts (vgl. Pl. F 1).""",
      "Der Baedeker, das maßgebliche Reisehandbuch der Zeit, im Abschnitt über Bonn. Seit 1898 verbindet die feste Rheinbrücke Bonn mit Beuel; wer aus der Stadt ins Bröltal oder in den Westerwald will, geht über die Brücke zum Bahnhof der Bröltalbahn, der am Ufer liegt und nicht wie der Staatsbahnhof einen Kilometer landeinwärts (Strecken [3]). Die Herausgabe des Baedeker verantwortete der Verlag; einzelne Verfasser nennt er nicht."),
    u(2, "Baedeker, Rheinlande 1905, S. 423", "Hennef: „Knotenpunkt für die Bröltalbahn“ und eine „beliebte Sommerfrische“",
      """Von Siegburg nach Beuel (S. 421), 11½km, Zweiglinie der Bröltalbahn (s. unten).

Die Bahn überschreitet bald jenseit Siegburg (r. das Siebengebirge) zum erstenmal die Sieg, deren Tale sie über 38 Brücken und durch 13 Tunnel bis Betzdorf und Siegen aufwärts folgt.

32km Hennef (Gasth.: Laa, Nasshoven), Knotenpunkt für die „Bröltalbahn“ von Beuel (S. 421) nach Asbach (38km) und nach Waldbröl (46km, 31 von Hennef ab), die sich in Hennef gabelt.

Das Bröltal, in welchem die Waldbröler Linie aufwärts führt, bietet von der nächsten Station, Allner, mit Schloß des Hrn. Cockerill, an der Einmündung der Bröl in die Sieg, über Bröl, Ingersauelermühle, Herrnstein, Felderhoferbrücke (Gasth.: Linke, gut, beliebte Sommerfrische) bis Schönenberg eine Fülle landschaftlicher Schönheiten.""",
      "Die These dieses Apparats in einem Satz des Baedeker: Das Tal, durch das 1862 Erz und Kalk fuhren, bietet 1905 „eine Fülle landschaftlicher Schönheiten“, und an der Felderhoferbrücke steht ein Gasthaus, das als „beliebte Sommerfrische“ gilt. Erz, Gruben und Kalköfen nennt der Baedeker nicht mehr. Schloss Allner, an dem die Bahn seit 1862 vorbeifährt, gehört nach dem Baedeker einem „Hrn. Cockerill“. Die Schreibung „Bröltal“ ohne h setzt sich in diesen Jahren durch."),
    u(3, "Baedeker, The Rhine 1911, S. 141", "1911, für englische Reisende: „very picturesque“",
      """[…] 20 M. Hennef (Laa; Nasshoven) is the junction of the Bröltal Railway (p. 83) to (29 M.; 20 M. from Hennef) Waldbröl and to (24 M.) Asbach.

On the Bennauer Kopf at Asbach are important quarries of columnar basalt. — The Bröl-Tal, which the Waldbröl line ascends, is very picturesque. At Allner, where the Bröl joins the Sieg, is a château of the 16-18th cent., remodelled in 1875-6. Other stations are Bröl, Ingersauelermühle, Herrnstein, Feldhoferbrücke (Linke, very fair, a favourite summer-resort), and Schönenberg. — From Waldbröl a branch-line runs to Wissen (see p. 143).""",
      "Die englische Ausgabe sechs Jahre später, übersetzt und gekürzt. Neu sind die Basaltbrüche am Bennauer Kopf, die der englische Leser sich ansehen soll (Basalt [1]), und die Staatsbahn von Waldbröl nach Wissen: Das Tal hat jetzt auch am oberen Ende Anschluss an das große Netz, und die Bröltalbahn ist nicht mehr der einzige Weg nach Waldbröl. Die Meilen sind englische Meilen (1,6 km); „Feldhoferbrücke“ steht so im Druck."),
]

SIEBENGEBIRGE = [
    u(1, "ZVDEV 40 (1900), S. 743", "1900: „im Interesse der Erhaltung des Siebengebirges“",
      """— Brölthaler Eisenbahn. Der Geschäftsbericht der Gesellschaft theilt bezüglich der Genehmigung für den Ankauf der Heisterbacher Thalbahn mit, dass der Ankauf der Bahn und deren Betrieb als Kleinbahn sowie die Erweiterung der Linie Niederpleis-Oberpleis bis Rostingen gestattet werden soll, wenn im Interesse der Erhaltung des Siebengebirges die Verbindung der Heisterbacher Thalbahn mit der Brölthalbahn fortfällt und der Betrieb der ersteren Bahn gewissen Einschränkungen unterworfen wird. Der Wegfall der früher von der Staatsregierung verlangten Verbindung der Heisterbacher Thalbahn mit der Brölthalbahn sei nicht nur unbedenklich, sondern sogar nutzbringend, da der Betrieb über die erstere wegen der grossen Steigungen sehr schwierig sein würde, auch die Verbindung nach dem Wasserumschlagplatze Beuel vor derjenigen nach Niederdollendorf den Vorzug verdiene. Eine weitere Bedingung sei, dass neue Anschlüsse von Steinbrüchen unzulässig sein und die vorhandenen nur insoweit weiter betrieben werden sollen, als der Besitzstand der Bruchbesitzer vom 1. April 1899 das zu verfrachtende Steinmaterial liefert. Eingehende Untersuchungen durch Sachverständige hätten ergeben, dass diese Beschränkungen der Ertragsfähigkeit der Bahn nicht schädlich seien, da der fragliche Besitzstand für eine reichliche Ausbeutung auf nicht absehbare Zeit Gewähr biete. Für die Weiterentwickelung des Unternehmens komme in Betracht die Eröffnung des uneingeschränkten Güterverkehrs auf der Strecke Niederpleis-Siegburg, die am 1. Mai d. J. erfolgt ist. Von dieser Strecke sei eine Steigerung des Verkehrs in Basalten und Quarziten von der Oberpleiser Strecke her zu erwarten. Der Anschluss des Thonwerkes Niederpleis mittelst Rollbockbetrieb wird voraussichtlich zum 1. August eröffnet werden und der Bahn einen erheblichen neuen Verkehr zuführen. […]""",
      "Eine der frühesten Stellen, an denen Naturschutz einer Bahn Grenzen setzt. Um 1900 wurde heftig über den Schutz des Siebengebirges vor den Steinbrüchen gestritten, die die Berge abtrugen; der Staat genehmigt den Kauf der Heisterbacher Talbahn deshalb nur, wenn sie keine neuen Brüche anschließt und nicht mit dem Bröltaler Netz verbunden wird. Die Gesellschaft macht aus der Not eine Tugend: Beuel sei als Umschlagplatz ohnehin besser. Damit endet der Plan von 1896 (Heisterbach [3]). Die Strecke nach Siegburg führt seit dem 1. Mai 1900 auch Güter; der Personenverkehr war ein Jahr früher eröffnet worden (Strecken [5]). Ein „Rollbock“ trägt einen normalspurigen Wagen auf der schmalen Spur."),
    u(2, "ZVDEV 40 (1900), S. 1080", "Oktober 1900: Haltepunkt Siegburg-Siegbrücke",
      """1. Eröffnung von Stationen.

Brölthaler Eisenbahn. (2168) Am 1. Oktober d. J. wird auf der Strecke Niederpleis-Siegburg der Haltepunkt Siegburg-Siegbrücke für den Personenverkehr eröffnet.""",
      "Eine Zeile in der Liste neuer Stationen. Das Netz wächst jetzt nicht mehr durch neue Strecken, sondern durch neue Haltepunkte, dichter an den Orten. Die Tafel „Siegburg um 1912“ zeigt die Bröltalbahn an dieser Strecke vor der Stadt."),
]

STATISTIK = [
    u(1, "Zeitschrift für Kleinbahnen 10 (1903), S. 323", "1901 im Vergleich: 4,54 Prozent",
      """Von den Privat-Schmalspurbahnen brachten:
die Ravensburg—Weingartener Eisenbahn 9,33 % (gegen 9,85 % im Vorjahre),
die Kaysersberger Talbahn 7,40 % (gegen 5,76 % im Vorjahre),
die Mülhausen—Wittenheimer Straßenbahnen 4,99 % (gegen 6,00 % im Vorjahre),
die Bröltaler Eisenbahn 4,54 % (gegen 5,68 % im Vorjahre),
die Zell—Todtnauer Eisenbahn 5,05 % (gegen 4,97 % im Vorjahre),
die Kreis Altenaer Schmalspurbahnen 2,45 % (gegen 2,43 % im Vorjahre),
die Mannheim—Weinheim—Heidelberger Bahn 4,18 % (gegen 4,99 % im Vorjahre),
die Ocholt—Westersteder Eisenbahn 2,67 % (gegen 6,00 % im Vorjahre),
die Walhallabahn 4,78 % (gegen 6,28 % im Vorjahre). […]

Die durchschnittliche Verzinsung stellte sich im Jahre 1901 (gegen 1900):
für die Staatsbahnen (ohne die oberschlesischen Schmalspurbahnen) auf 0,00 (0,10) %,
für die Privatbahnen auf 2,58 (2,76) %,
für das Gesamtnetz überhaupt auf 1,35 (1,38) %.""",
      "Aus der amtlichen Statistik der deutschen Schmalspurbahnen für 1901, wie die Zeitschrift für Kleinbahnen sie wiedergibt. Gemeint ist, wie viel Prozent des Anlagekapitals der Betriebsüberschuss deckte. Die Bröltalbahn liegt mit 4,54 Prozent deutlich über dem Durchschnitt der privaten Schmalspurbahnen und weit über den staatlichen, die nichts erwirtschafteten. Die 1865 als Vorbild gelobte Bahn (Vorbild [1]) ist vierzig Jahre später eine der besseren ihrer Art, aber keine glänzende."),
    u(2, "Zeitschrift für Kleinbahnen 15 (1908), S. 437", "1906 und 1907: eine halbe Million Fahrgäste",
      """Auszüge aus Geschäftsberichten.

1. Bröltaler Eisenbahn-Akt.-Ges.
Aktienkapital 3 199 200 M.
Staatsbeteiligung 180 000 M.
Obligationen 3 305 000 M.
Dividende 4 %.

A. Bröltaler Nebenbahn.
[1906 | 1907]
Betriebslänge km: 87,3 | 87,3
Lokomotiv-Nutzkm: 393 866 | 393 594
Personenwagen-Achskm: 1 990 382 | 2 088 706
Gepäck- und Güterwagen-Achskm: 6 207 329 | 5 812 445
Personen: 475 640 | 502 491
Personenkm: 5 255 738 | 5 328 384
Jede Person ist durchschnittlich gefahren km: 11,05 | 10,60
Jede Person hat durchschnittlich eingebracht Pf: 40,51 | 37,20
Güter t: 532 576 | 552 571
Tonnenkm im ganzen: 7 521 662 | 7 355 523
Jede Tonne hat durchschnittlich eingebracht M: 1,08 | 1,05

B. Heisterbacher Talbahn (Kleinbahn).
[1906 | 1907]
Betriebslänge km: 7,2 | 7,2
Lokomotiv-Nutzkm: 108 886 | 133 662
Personenwagen-Achskm: 144 144 | 3 708
Güterwagen-Achskm: 664 112 | 813 554
[…]""",
      "Die Tabelle ist hier zeilenweise wiedergegeben; die Jahre stehen in eckigen Klammern. Sie fasst fünfzig Jahre zusammen: 1864 fuhren 33 000 Tonnen und keine Fahrgäste, um 1875 gut 4 000, um 1880 rund 20 000 Fahrgäste (Fahrgäste [1] und [5]); 1907 sind es eine halbe Million Menschen und 550 000 Tonnen auf 87 Kilometern. Im Schnitt fährt jeder Fahrgast elf Kilometer, vom Dorf in die nächste Stadt oder zum Rhein. Bei der Heisterbacher Talbahn bricht der Personenverkehr 1907 fast ganz ab, die Güter wachsen: Sie ist eine reine Steinbahn geworden, wie es die Auflagen von 1900 nahelegten (Siebengebirge [1])."),
]

DIVIDENDE = [
    u(1, "Allgemeine Zeitung, 14. Juni 1900", "1900: „Vertheuerung des Betriebes“",
      """r. Berlin, 13. Juni. Tel. Die Broelthaler Bahn erklärt 2½ Proz. Dividende (gegen 4 Proz. im Vorjahr). Infolge Vertheuerung des Betriebes und anderer Störungen ist die Rentabilität zurückgegangen.""",
      "Eine Börsenmeldung aus der Münchner Allgemeinen Zeitung. Um 1900 stiegen Kohlenpreise und Löhne überall; für eine Bahn mit niedrigen Tarifen, die sie nicht beliebig erhöhen durfte, schlug das unmittelbar durch."),
    u(2, "Der Arbeiterfreund 39 (1901), S. 265", "1901: ein Unterstützungsfonds",
      """Hennef (Sieg). Brölthaler Eisenbahn A.-G.: 1308 M dem Beamten- u. Arbeiter-Unterstützungsfonds.""",
      "Eine Zeile in einer langen Liste von Firmen, die aus ihrem Gewinn etwas für ihre Belegschaft zurücklegten, in der Zeitschrift des Centralvereins für das Wohl der arbeitenden Klassen. Es ist die einzige Stelle in diesem Apparat, die die Angestellten der Bahn als Empfänger erwähnt; um 1875 waren es etwa zwanzig Mann (Betrieb [2]), 1894 fuhren sechs Lokomotiv- und sechs Zugpersonale täglich (Fahrplan [2])."),
    u(3, "Allgemeine Zeitung 1903; Münchner Neueste Nachrichten 1904 und 1905", "1902 bis 1904: Vorzugsaktien und leere Stammaktien",
      """1903: Die Dividende der Broeltalbahn beträgt für die Vorzugsaktien 4 Prozent, wie im Vorjahre, für die Aktien 0 (gegen 2½ Prozent im Vorjahre).

1904: Die Brölthaler Eisenbahn schlägt für das abgelaufene Geschäftsjahr eine Dividende von 1½ pCt. für die Stammaktien und von 4 pCt. für die Vorzugsaktien vor gegen 0 im Vorjahre.

1905: Die Bröhlthal-Eisenbahngesellschaft schlägt 4 % Dividende an die Vorzugsaktien und 2 % an die Stammaktien vor. (Privattelegr.)""",
      "Drei Börsenzeilen, jeweils im Frühjahr nach dem Geschäftsjahr. Für das neue Netz hatte die Gesellschaft Vorzugsaktien ausgegeben, die zuerst bedient wurden; die alten Stammaktien gingen für 1902 leer aus. Die Bahn trug sich, aber das Kapital war größer als der Ertrag. „Vor gegen“ steht so im Druck von 1904."),
    u(4, "Allgemeine Zeitung, 30. März 1906; Münchner Neueste Nachrichten, Oktober 1906", "1906: der Kapitalschnitt",
      """März 1906: Die Broelthalbahn reduziert die 1,938,000 M alten Stammaktien im Verhältnis von 5 : 3 und erhöht das Kapital um 277,200 neue Stammaktien und stellt die Stammaktien den Vorzugsaktien gleich.

Oktober 1906: * Brölthaler Eisenbahn-A.-G. Auf der Tagesordnung der außerordentlichen Generalversammlung am 17. November steht außer der gemeldeten Herabsetzung des Grundkapitals auch die Erhöhung desselben um nominell 277,200 M neue, ab 1. Januar 1907 dividendenberechtigte Inhaberaktien von je 1200 M.""",
      "Ein Kapitalschnitt: Die alten Stammaktionäre verlieren zwei Fünftel ihres Nennwerts, dafür werden alle Aktien gleichgestellt. Die Gesellschaft gesteht damit ein, dass ein Teil des Geldes, das seit 1885 in das Netz geflossen war, nicht mehr verdient werden konnte. Das Ergebnis sind die 3 199 200 Mark Aktienkapital der Statistik von 1908 (Statistik [2])."),
    u(5, "Münchner Neueste Nachrichten 1908", "1908: vier Prozent auf alles",
      """* Brölthaler Eisenbahn A.-G. in Hennef. (Priv.) Der Aufsichtsrat schlägt eine Dividende von 4 % vor auf das nunmehr einheitliche Aktienkapital von 3,199,200 M. (i. V. 4 % auf die Vorzugsaktien, 0 auf die Stammaktien).""",
      "Nach dem Kapitalschnitt verdient die Bahn vier Prozent auf alle Aktien. Das ist ungefähr, was 1894 erreicht war (Strecken [2]) und was man für eine sichere Anlage erwartete. Hier enden die gemeinfreien Börsennachrichten dieses Apparats; den Weg zur Rhein-Sieg-Eisenbahn ab 1921 erzählt die Zeitleiste nach der neueren Literatur."),
]

SECS = [
    ("baedeker", "Im Reiseführer", "Baedeker", BAEDEKER,
     "Der Baedeker 1905 und 1911: Beuel mit Rheinbrücke und Gasthaus, Hennef als „Knotenpunkt für die Bröltalbahn“, das Bröltal mit einer „beliebten Sommerfrische“. Vom Erz ist keine Rede mehr."),
    ("siebengebirge", "Grenzen am Siebengebirge", "Siebengebirge", SIEBENGEBIRGE,
     "1900 verbietet der Staat neue Steinbruchanschlüsse an der Heisterbacher Talbahn, „im Interesse der Erhaltung des Siebengebirges“. Das Netz wächst danach nur noch um Haltepunkte."),
    ("statistik", "Was die Bahn leistete", "Statistik", STATISTIK,
     "Die Verzinsung im Vergleich mit anderen Schmalspurbahnen 1901, und 1906/07 eine halbe Million Fahrgäste im Jahr."),
    ("dividende", "Dividenden und Kapitalschnitt, 1900–1908", "Dividende", DIVIDENDE,
     "Börsennotizen aus München: steigende Kosten, Vorzugsaktien, ein Unterstützungsfonds für das Personal, der Kapitalschnitt von 1906 und vier Prozent auf alles."),
]

DATA = {
    "titel": "Kleinbahn und Sommerfrische, 1903–1914",
    "autor": "Baedeker, Fachpresse der Kleinbahnen, Börsennachrichten",
    "jahr": "1900–1911",
    "sprache": "de",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "K. Baedeker, Die Rheinlande (1905) und The Rhine (1911); Zeitschrift für Kleinbahnen 10 (1903) und 15 (1908); Zeitung des Vereins Deutscher Eisenbahnverwaltungen 40 (1900); Der Arbeiterfreund 39 (1901); Allgemeine Zeitung 1900–1906; Münchner Neueste Nachrichten 1904–1908. Gelesen an den Digitalisaten des Internet Archive (archive.org) und der Bayerischen Staatsbibliothek (digitale-sammlungen.de).",
    "hinweis": "Die Bahn im Alltag des Tals vor dem Ersten Weltkrieg: im Reiseführer als Weg in eine Sommerfrische, im Siebengebirge an Grenzen, die der Naturschutz setzte, in der Statistik mit einer halben Million Fahrgästen, an der Börse mit einem Kapitalschnitt und vier Prozent Dividende. Über die Jahre 1909 bis 1914 fanden sich in den zugänglichen Digitalisaten kaum Stellen; Fahrpläne und Zeitungsanzeigen dieser Jahre stehen in den Lokalzeitungen, die von hier nicht zugänglich sind. Der Ausblick auf die Rhein-Sieg-Eisenbahn und die Stilllegung steht in der Zeitleiste nach der neueren Literatur. Text nach den Drucken, an den Seitenbildern gelesen; Schreibung und Zeichensetzung wie gedruckt, ſ als s, Silbentrennung aufgelöst, Sperrungen nicht wiedergegeben, Auslassungen mit […] bezeichnet.",
    "sections": [{"id": i, "titel": t, "zk": zk, "blurb": b, "units": us} for i, t, zk, us, b in SECS],
}

if __name__ == "__main__":
    for s in DATA["sections"]:
        ns = [x["n"] for x in s["units"]]
        assert ns == list(range(1, len(ns) + 1)), (s["id"], ns)
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, sum(len(s["units"]) for s in DATA["sections"]), "units")
