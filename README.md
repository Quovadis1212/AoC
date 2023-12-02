# AoC 2023
Advent of Code - https://adventofcode.com/

Die Lösungen sind für richtige Entwickler wahrscheinlich hässlich wie die Nacht, aber es sind meine.

## Tag 1

Da ich schon mit dem re Modul vertraut war, dachte ich mir dass diese Aufgabe recht einfach wird. Der 1. Teil war es auch. 
Auch im 2. Teil machte ich gute Vortschritte, jedoch hatte ich Probleme mit den sich überschneidenden Regex-Matches (oneight, twone etc.). Schon darauf zu kommen, bei dieser Datenmenge hat mich einige Minuten gekostet. Zuerst habe ich es mir einfach gemacht und die überschneidenden Matches in ein zusätzliches Dictionary aufgenommen. Die Lösung funktioniert zwar, befriedigend ist aber anders.
[Tag 1 Lösung 1](solutions/2023/01/solve.py)

Nach ein bischen suchen bin ich auf folgendes gestossen: https://stackoverflow.com/questions/5616822/how-to-use-regex-to-find-all-overlapping-matches. 
Der Trick ist die Regex-Suche in ein capture group in einem lookahead zu verpacken: (?=(\d{1}|one|two|three|four|five|six|seven|eight|nine)). Damit werden die positiven Bedingungen für das Lookahead-Muster von verschiedenen Positionen im Text aus überprüft und dabei die tatsächlichen Zeichen für die Capture-Gruppe berücksichtigt. So, viel besser.
[Tag 1 Lösung 2](solutions/2023/01/solve2.py)

## Tag 2 

Wieder ein Einsatz für das re Modul. Die meiste Zeit verbrauchte ich, um die Daten richtig zu Ordnen. Danach waren die Aufgaben sehr einfach. Den 2. Teil konnte ich in unter 5 Minuten lösen.
[Tag 2 Lösung 1](solutions\2023\02\solve.py)