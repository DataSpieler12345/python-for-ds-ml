#!/usr/bin/env python
# coding: utf-8

# ## L: Grenzwertanalyse durchführen 

# Für ein Zeiterfassungsprogramm soll eine Python-Funktion entwickelt werden, die aus eingegebener Stundenzahl und einem Stundensatz die entstandenen Kosten berechnet: berechne_lohn(wochenarbeitszeit, stundenlohnInEuro) 
# 
# Die angefallenen Zeiten werden wöchentlich erfasst. Die Regelarbeitzeit pro Tag beträgt 8 Stunden. In einer Woche darf die Regelarbeitzeit um maximal 10% überschritten werden. Jede angefangene Stunde wird dabei als volle Stunde gezählt. 
# 
# Führen Sie eine Grenzwertanalyse für den Parameter wochenarbeitszeit durch und notieren Sie mögliche Testwerte inkl. erwartetem Ergebnis. Gehen Sie davon aus, dass der Stundenlohn bei jedem Test 10,00 beträgt.   
# 
# • Ziel ist - wie immer - eine möglichst robuste Funktion zu verfassen. 
# 
# • Die Anzahl der Zeilen gibt keinen Aufschluss darüber, wie viele Testfälle mindestens nötig sind. 

# ### Grenzwertanalyse 
# 
# Die Grenzwertanalyse, auch als Grenzwertprüfung oder Grenzanalyse bekannt, ist eine Technik, die im Bereich der Softwaretechnik und Softwaretests eingesetzt wird. Ihr Ziel ist es, die Eingabe- und Ausgabegrenzen eines Systems oder Softwarekomponente zu identifizieren und zu testen.
# 
# Bei der Grenzwertanalyse werden spezifische Testfälle ausgewählt, die nahe an den Grenzen der gültigen Werte für die Systemeingaben liegen. Dies geschieht, da Fehler und unerwartetes Verhalten oft an diesen Grenzen auftreten.
# 
# Die Technik basiert auf der Annahme, dass Fehler häufiger an oder in der Nähe der Grenzen der gültigen Eingabebereiche auftreten. Durch das Testen dieser Grenzen können Fehler entdeckt werden, die in allgemeineren Tests möglicherweise übersehen worden wären.
# 
# Zum Beispiel nehmen wir an, dass eine Inventarverwaltungssoftware entwickelt wird, die Produktmengen zwischen 0 und 100 akzeptiert. Anstatt willkürliche Werte im gesamten Bereich zu testen, konzentriert sich die Grenzwertanalyse auf spezifische Grenzwerte wie 0, 1, 99 und 100. Dadurch können potenzielle Fehler oder unerwartetes Verhalten entdeckt werden, die auftreten könnten, wenn die Werte nahe an den festgelegten Grenzen liegen.
# 
# Durch die Anwendung der Grenzwertanalyse können Testfälle entworfen werden, die die unteren und oberen Grenzen, Toleranzgrenzen, Kapazitätsgrenzen, Geschwindigkeitsgrenzen oder andere relevante Grenzen des Systems oder der Softwarekomponente abdecken.
# 
# Zusammenfassend ist die Grenzwertanalyse eine Testtechnik, die sich auf die Grenzen oder Schwellenwerte gültiger Werte konzentriert, um Fehler und unerwartetes Verhalten zu identifizieren. Sie trägt dazu bei sicherzustellen, dass das System oder die Softwarekomponente unter extremen Bedingungen oder nahe an den festgelegten Grenzen korrekt funktioniert.

# #### Notiz: 
# 
# Die Funktion berechne_lohn nimmt zwei Parameter entgegen: wochenarbeitszeit und stundenlohnInEuro.
# 
# Die *try-Anweisung* gibt an, dass Operationen ausgeführt werden, die Ausnahmen auslösen können, und es wird ein Codeblock bereitgestellt, um diese Ausnahmen abzufangen und zu behandeln.
# 
# Innerhalb des try-Blocks werden folgende Validierungen und Berechnungen durchgeführt:
# 
# Wenn wochenarbeitszeit oder stundenlohnInEuro kleiner als Null sind, wird eine ValueError-Ausnahme mit einer Nachricht ausgelöst, die darauf hinweist, dass das untere Grenzwert unterschritten wurde.
# 
# Wenn wochenarbeitszeit größer 44 ist, wird eine ValueError-Ausnahme mit einer Nachricht ausgelöst, die darauf hinweist, dass das obere Grenzwert überschritten wurde (40 Stunden plus 10 %).
# 
# Wenn wochenarbeitszeit kleiner als -1 ist, wird eine ValueError-Ausnahme mit einer Nachricht ausgelöst, die darauf hinweist, dass das untere Grenzwert unterschritten wurde.
# 
# Wenn wochenarbeitszeit vom Typ str ist, wird eine TypeError-Ausnahme mit einer Nachricht ausgelöst, die darauf hinweist, dass ein anderer Typ erwartet wird und eine zusätzliche Erklärung bereitgestellt wird.
# 
# Wenn alle Validierungen erfolgreich sind, wird der Lohn berechnet, indem wochenarbeitszeit mit stundenlohnInEuro multipliziert und in der Variablen result gespeichert wird.
# 
# Der Wert von result wird mit der Nachricht "Resultat:" ausgegeben.
# 
# Schließlich wird result zurückgegeben.
# 
# Wenn eine ValueError-Ausnahme auftritt, wird sie abgefangen und eine entsprechende Fehlermeldung mit dem spezifischen Ausnahmemessage (ValueError) ausgegeben.
# 
# Wenn eine TypeError-Ausnahme auftritt, wird sie abgefangen und eine entsprechende Fehlermeldung mit dem spezifischen Ausnahmemessage (TypeError) ausgegeben.
# 
# Zusammenfassend überprüft die Funktion berechne_lohn verschiedene Fehlerfälle und behandelt sie, um sicherzustellen, dass die Eingabewerte gültig sind. Anschließend wird der Lohn berechnet und zurückgegeben. Tritt eine Ausnahme auf, wird sie abgefangen und eine entsprechende Fehlermeldung ausgegeben.

# ### Try Statement 
# 
# Die try-Anweisung in Python wird verwendet, um Ausnahmen in einem Codeblock zu kontrollieren und zu behandeln. Sie bietet eine Möglichkeit, Fehler abzufangen und zu handhaben, die während der Ausführung des Codes auftreten können, und verhindert, dass das Programm abrupt abbricht.
# 
# Die Logik hinter der try-Anweisung basiert auf der Idee, dass bestimmte Teile eines Programms Ausnahmen, d.h. unerwartete Situationen oder Fehler, auslösen können. Durch Verwendung von try wird ein Codeblock in eine kontrollierte Umgebung eingebettet.
# 
# Wenn ein Codeblock innerhalb eines try-Blocks ausgeführt wird, überwacht der Python-Interpreter, ob eine Ausnahme auftritt. Wenn eine Ausnahme auftritt, wird der Programmfluss sofort zu einem entsprechenden except-Block umgeleitet, der diese spezielle Ausnahme behandelt. Dies ermöglicht es dem Programm, spezifische Maßnahmen als Reaktion auf die Ausnahme zu ergreifen, wie z.B. das Anzeigen einer Fehlermeldung, das Durchführen von Wiederherstellungsvorgängen oder das Treffen alternativer Entscheidungen.
# 
# Die grundlegende Struktur der try-Anweisung ist wie folgt:
# 
# 
# try:
# 
#     # Code, der Ausnahmen auslösen kann
#     
# except AusnahmeTyp1:
# 
#     # Behandlung der Ausnahme vom Typ 1
#     
# except AusnahmeTyp2:
# 
#     # Behandlung der Ausnahme vom Typ 2
#     
# ...
# 
# except:
# 
#     # Behandlung einer beliebigen anderen Ausnahme
#     
# 

# Der try-Block enthält den Code, der ausgeführt und auf Ausnahmen überwacht werden soll. Die except-Blöcke geben an, wie jede Art von Ausnahme behandelt werden soll, die auftreten kann. Optional kann ein finally-Block verwendet werden, um Code für Aufräumarbeiten auszuführen, der sicherstellt, dass bestimmte Aktionen unabhängig davon, ob eine Ausnahme auftritt oder nicht, durchgeführt werden.
# 
# Die Logik hinter der try-Anweisung besteht darin, außergewöhnliche Situationen vorherzusehen und zu behandeln, um das Programm robuster und fehlertoleranter zu machen. Durch das Erfassen und angemessene Behandlung von Ausnahmen können spezifische Maßnahmen ergriffen werden, um Fehler zu behandeln, das Programm nicht abzubrechen und dem Benutzer eine kontrolliertere Erfahrung zu bieten.
# 
# Zusammenfassend bietet die try-Anweisung in Python einen Mechanismus zum Kontrollieren und Behandeln von Ausnahmen, der es dem Programm ermöglicht, spezifische Maßnahmen als Reaktion auf außergewöhnliche Situationen zu ergreifen. Ihre Logik beruht auf der Vorwegnahme und kontrollierten Behandlung von Fehlern, um die Robustheit und Benutzererfahrung zu verbessern.

# In[2]:


def berechne_lohn(wochenarbeitszeit, stundenlohnInEuro):
    try:
        if wochenarbeitszeit < 0 or stundenlohnInEuro < 0:        
            raise ValueError('Untergrenze unterschritten.')          
        
        if wochenarbeitszeit > 44:        
            raise ValueError('Obergrenze überschritten (40 Stunden + 10%)')
        
        if wochenarbeitszeit < -1:        
            raise ValueError('Unterschreitung der Untergrenze') 
    
        if isinstance(wochenarbeitszeit, str):      
            raise TypeError('Einmaliger Test für Typ sollte ausreichen, denn wenn die Entwicklung auf Typenfehler hingewiesen wird, sollte Sie überprüfen ob der erwartete Typ vorliegt wodurch alle anderen Typen unmöglich würden')
        
        result = wochenarbeitszeit * stundenlohnInEuro
        print("Result:", result)
        return result
    except ValueError as ve:
        print("ValueError:", str(ve))
    except TypeError as te:
        print("TypeError:", str(te))


# In[3]:


berechne_lohn(0,10)


# In[4]:


berechne_lohn(44,10)


# In[24]:


berechne_lohn(-1,10)


# In[6]:


berechne_lohn(45,10)


# In[26]:


berechne_lohn(str('a'),10)


# ## TypeError
# ('Einmaliger Test für Typ sollte ausreichen, denn wenn die Entwicklung auf Typenfehler hingewiesen wird, sollte Sie überprüfen ob der erwartete Typ vorliegt wodurch alle anderen Typen unmöglich würden')

# #### testing the function 

# In[7]:


berechne_lohn(43,10)


# In[8]:


berechne_lohn(42,10)


# In[29]:


berechne_lohn(41,10)


# ### Python training 
# 
# Hier sind einige Websites, auf denen du mit Python-Funktionsübungen arbeiten und üben kannst:
# 
# Exercism (https://exercism.io/tracks/python): Exercism bietet eine Vielzahl von Programmierübungen in Python an, einschließlich spezifischer Übungen zu Funktionen. Du kannst die Probleme lösen und Feedback von der Community erhalten.
# 
# CodingBat (https://codingbat.com/python): CodingBat bietet Programmierübungen in Python an, darunter einen speziellen Abschnitt für Funktionen. Du kannst verschiedene Konzepte und Herausforderungen im Zusammenhang mit Funktionen üben.
# 
# HackerRank (https://www.hackerrank.com/domains/tutorials/10-days-of-statistics): HackerRank bietet eine Vielzahl von Programmieraufgaben in Python an, einschließlich Herausforderungen im Zusammenhang mit Funktionen. Du kannst Probleme lösen und deine Lösungen mit anderen Programmierern vergleichen.
# 
# Project Euler (https://projecteuler.net/archives): Project Euler ist ein Projekt, das mathematische und programmierbezogene Herausforderungen bietet. Obwohl es nicht speziell auf Funktionen ausgerichtet ist, erfordern viele der Probleme die Implementierung von Funktionen, um sie zu lösen.
# 
# LeetCode (https://leetcode.com/problemset/all/): LeetCode ist eine Plattform für Programmieraufgaben, die auch Probleme in Python enthält. Du kannst üben und deine Programmierfähigkeiten verbessern, einschließlich dem Einsatz von Funktionen.
# 
# Dies sind nur einige Optionen, aber es gibt viele weitere online verfügbare Ressourcen. Durchsuche diese Websites und wähle diejenige aus, die am besten zu deinen Bedürfnissen und deinem Kenntnisstand passt. Viel Spaß beim Lösen von Problemen und beim Verbessern deiner Programmierfähigkeiten mit Funktionen in Python!

# #### KI support 
# 
# https://poe.com/login
# 
# https://heypi.com/es/talk

# #### Education 
# 
# https://skillsforall.com/

# #### viel Erfolg!!!
