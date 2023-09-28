#!/usr/bin/env python
# coding: utf-8

# ## L: Deckungsgrade berechnen

#  Für ein Zeiterfassungsprogramm soll eine Python-Funktion entwickelt werden, die aus eingegebener Stundenzahl und einem Stundensatz die entstandenen Kosten berechnet: berechne_lohn(wochenarbeitszeit, stundenlohnInEuro) 
# 
# Die angefallenen Zeiten werden wöchentlich erfasst. Die Regelarbeitzeit pro Tag beträgt 8 Stunden. In einer Woche darf die Regelarbeitzeit um maximal 10% überschritten werden. Jede angefangene Stunde wird dabei als volle Stunde gezählt. 
# 
# Eine Ihrere Kolleginnen hat die folgende Python-Funktion auf Basis der Aufgabenbeschreibung implementiert: 

# ### Deckungsgrade 
# 
# Der Begriff "Deckungsgrad" wird im Finanz- und Managementbereich verwendet, um das Maß der Abdeckung oder des Beitrags einer Variablen oder Komponente zu einem Ziel oder zur Rentabilität eines Unternehmens zu beschreiben. Allerdings kann ich ohne weitere spezifische Informationen über ein konkretes Konzept namens "Deckungsgrad-Analyse" keine detaillierten Informationen liefern.
# 
# Im Allgemeinen beinhaltet die Analyse von "Deckungsgraden" die Bewertung und Messung, wie verschiedene Komponenten oder Faktoren zur Erreichung eines Ziels oder zur Gesamtrentabilität eines Unternehmens beitragen. Dies kann die Analyse von Einnahmen, Ausgaben, Gewinnmargen, Produktionskosten, Kostenstrukturen und anderen relevanten Aspekten umfassen, um die Abdeckung oder den Beitrag jeder Komponente zu bestimmen.
# 
# Es ist möglich, dass der Begriff "Deckungsgrad-Analyse" in einem spezifischen Kontext oder in Bezug auf einen bestimmten Geschäftsbereich oder eine bestimmte Branche verwendet wird. Wenn du weitere Details oder einen spezifischen Kontext hast, in dem dieser Begriff verwendet wird, kann ich eine präzisere Antwort geben.

# ### Business cases
# 
# Deckungsgrad im Vertrieb: In einem Vertriebsunternehmen kann der Deckungsgrad dazu verwendet werden, den Beitrag einzelner Produkte oder Produktkategorien zum Gesamtumsatz oder Gewinn zu analysieren. Indem man den Umsatz oder Gewinn eines bestimmten Produkts durch den Gesamtumsatz oder Gewinn des Unternehmens teilt und mit 100 multipliziert, erhält man den Deckungsgrad in Prozent. Dies ermöglicht es, Produkte zu identifizieren, die einen hohen Deckungsgrad haben und somit einen großen Beitrag zur Rentabilität des Unternehmens leisten.
# 
# 
# 
# Deckungsgrad in der Kostenrechnung: In der Kostenrechnung kann der Deckungsgrad dazu verwendet werden, die Beziehung zwischen den variablen Kosten und den Gesamtkosten eines Produkts oder einer Produktionslinie zu analysieren. Der Deckungsgrad wird berechnet, indem man die Differenz zwischen den Verkaufserlösen und den variablen Kosten durch die Verkaufserlöse dividiert und mit 100 multipliziert. Ein hoher Deckungsgrad zeigt an, dass die Verkaufserlöse die variablen Kosten gut abdecken und somit zur Deckung der Fixkosten und zur Erzielung eines Gewinns beitragen.
# 
# 
# 
# Diese Beispiele veranschaulichen, wie der Deckungsgrad dazu verwendet werden kann, die Abdeckung oder den Beitrag von Komponenten wie Produkten, Produktkategorien oder Kosten zu analysieren und zu bewerten. Die konkrete Anwendung kann je nach Branche, Unternehmen und Zielsetzung variieren.
# 

# In[18]:


def berechne_lohn(wochenarbeitszeit, stundenlohnInEuro):
    if wochenarbeitszeit < 0 or stundenlohnInEuro < 0:        
        raise ValueError('Werte dürfen nicht negativ sein.')          
        
    if wochenarbeitszeit > 44:        
        raise ValueError('Wochenarbeitszeit darf Regelarbeitszeit nicht mehr als 10% übersteigen')  
        
    if(wochenarbeitszeit > 0 and wochenarbeitszeit < 44):         
        return wochenarbeitszeit * stundenlohnInEuro        
    
    return -1 


# ### raise Statement 

# In Python wird die Anweisung raise verwendet, um eine Ausnahme (exception) explizit zu erzeugen. Es ermöglicht dem Programmierer, anzugeben, dass eine außergewöhnliche Situation oder ein Fehler im Programm aufgetreten ist und eine entsprechende Ausnahme ausgelöst wird. Das raise wird normalerweise in Verbindung mit der Erstellung von Ausnahmeobjekten verwendet.
# 
# Die grundlegende Syntax der raise-Anweisung lautet wie folgt:
#     
#     raise [Ausnahme]
#     
#     

# Hier bezieht sich [Ausnahme] auf den Typ der zu erzeugenden Ausnahme. Es kann sich um ein Objekt handeln, das von der Klasse BaseException oder einer ihrer Unterklassen erbt. Zum Beispiel sind ValueError, TypeError und ZeroDivisionError Beispiele für in Python integrierte Ausnahmen.
# 
# Es kann auch eine optionale Nachricht bereitgestellt werden, um die spezifische Ausnahme zu beschreiben:
# 
# 	raise [Ausnahme](Nachricht)
# 
# 

# Hier ist Nachricht ein String, der zusätzliche Informationen über die Ausnahme bereitstellt.
# 
# Wenn die raise-Anweisung ausgeführt wird, wird eine Ausnahme ausgelöst und der normale Programmfluss wird unterbrochen. Abhängig davon, wie Ausnahmen im Code behandelt werden, wird nach einem entsprechenden try-except-Block gesucht, um die Ausnahme abzufangen und zu behandeln. Wenn kein geeigneter try-except-Block gefunden wird, wird das Programm gestoppt und ein Traceback angezeigt, der die Aufrufsequenz zeigt, die zur Ausnahme geführt hat.
# 
# Hier ist ein Beispiel für die Verwendung der raise-Anweisung:
#     
# def division(a, b):
# 
#     if b == 0:
#         raise ValueError("Der Divisor darf nicht Null sein.")
#     return a / b
# 
# try:
#     ergebnis = division(10, 0)
#     
#     print(ergebnis)
#     
# except ValueError as fehler:
# 
#     print("Fehler:", str(fehler))
#     
#     
# In diesem Beispiel wird, wenn der Divisor b Null ist, eine ValueError-Ausnahme mit der Nachricht "Der Divisor darf nicht Null sein." ausgelöst. Anschließend wird die Ausnahme im except-Block abgefangen und die entsprechende Fehlermeldung ausgegeben.
# 
# Die korrekte Verwendung der raise-Anweisung ermöglicht es dem Programmierer, Ausnahmen in seinem Code gezielt und individuell zu steuern und zu behandeln.   
#     
#     

# a) Bestimmen Sie die notwendigen Funktionsaufrufe, um eine Anweisungsüberdeckung (C0) von 100% zu erreichen!

# In[4]:


# if wochenarbeitszeit < 0 or stundenlohnInEuro < 0:        
# raise ValueError('Werte dürfen nicht negativ sein.')
berechne_lohn(-1,10.0)


# In[5]:


# if wochenarbeitszeit > 44:        
# raise ValueError('Wochenarbeitszeit darf Regelarbeitszeit nicht mehr als 10% übersteigen')  
berechne_lohn(45,10.0)


# In[6]:


berechne_lohn(10,10.0)


# In[7]:


#gibt sie -1 zurück, wenn die Bedingung wahr ist.
berechne_lohn(44,10.0)


# #### Notiz: 
# 
# Die Funktion berechne_lohn hat einen Fehler in der Bedingung wochenarbeitszeit > 0 and wochenarbeitszeit < 44. Anstatt das Ergebnis der Berechnung wochenarbeitszeit * stundenlohnInEuro zurückzugeben, gibt sie -1 zurück, wenn die Bedingung wahr ist.
# 
# def berechne_lohn(wochenarbeitszeit, stundenlohnInEuro):
# 
#     if wochenarbeitszeit < 0 or stundenlohnInEuro < 0:
#         raise ValueError('Werte dürfen nicht negativ sein.')
# 
#     if wochenarbeitszeit > 44:
#         raise ValueError('Wochenarbeitszeit darf Regelarbeitszeit nicht mehr als 10% übersteigen')
# 
#     return wochenarbeitszeit * stundenlohnInEuro

# In[8]:


# Letzte Anweisung ist zwar sinnlos, aber im Sinne der Anweisungsüberdckung muss nur bewiesen werden, dass sie erreichbar ist. 
berechne_lohn(43,10.0)


# b) Um die Anweisungsüberduck automatisch zu testen, soll das Python-Packet "coverage" eigesetzt werden. Leider kann damit die Abdeckung von Fehlermeldungen nicht geprüft werden, weil das Programm - wie erwartet - mit einem Fehler abstürzt. Als Lösung sollen die Aufrufe in Unit-Tests verpackt werden und mit Hilfe von Pytest ausgeführt werden. Coverage könnte dadurhc die Testüberdeckung messen.

# #### Notiz

# The error message indicates that the XML-RPC search method is no longer supported by PyPI. Instead, it suggests using the website's search functionality at https://pypi.org/search. The XML-RPC API has been deprecated, and you should refer to the documentation at https://warehouse.pypa.io/api-reference/xml-rpc.html#deprecated-methods for more details on the deprecated methods and their alternatives.

# In[9]:


from lohnberechnung import berechne_lohn 


# In[10]:


import pytest 


# Formulieren Sie bespielhaft - einen Positiv- und  - einen Negativtest!  

# #### positiv

# In[11]:


def test_berechne_lohn__wird_korrekt_berechnet():
    # Arrange    
    wochenarbeitszeit = 10     
    stundenlohnInEuro = 10.0  
    
    # Act     
    ergebnis = berechne_lohn(wochenarbeitszeit, stundenlohnInEuro) 
    
    # Assert     
    assert ergebnis == 100.00 


# In[12]:


# test the function | no error than is correct! 
test_berechne_lohn__wird_korrekt_berechnet()
print("Positive test successful.")


# ### Test

# Wenn die Funktion "berechne_lohn" korrekt definiert ist und die Parameter "wochenarbeitszeit" und "stundenlohnInEuro" Standardwerte haben, ist es nicht erforderlich, die Parameter bei Aufruf der Funktion anzugeben.
# 
# Wenn die Parameter Standardwerte haben, verwendet die Funktion diese Werte, wenn keine Argumente beim Aufruf übergeben werden. In diesem Fall werden die Standardwerte stattdessen verwendet.

# In[13]:


test_berechne_lohn__wird_korrekt_berechnet(10,10)


# ### Notiz
# 
# Je nach Testfall kann es Sinn machen, das erwartete Ergebnis in den Arrange-Block zu schieben.  Hier habe ich mich dagegen entschieden, denn es hätte die Sache nur unnötig kompliziert. 

# #### negativ

# In[14]:


def test_berechne_lohn__negative_Eingabe_unmoeglich():     
    # Arrange     
    wochenarbeitszeit = -1     
    stundenlohnInEuro = 10.0          
    
    # Act     with pytest.raises(ValueError):         
    ergebnis = berechne_lohn(wochenarbeitszeit, stundenlohnInEuro)


# In[15]:


# test the function | no error than is correct! 
test_berechne_lohn__negative_Eingabe_unmoeglich()
print("Negative test successful.")


# ### Notiz: 
# Negativtests benötigen nicht zwingend einen Assert-Block.  Wir könnten einen Assert-Block nutzen, um z.B. die exakte Fehlermeldung vorzugeben.Bsp:  with pytest.raises(ValueError) as fehlerinfo: ...     raise ValueError("value must be 42")    assert fehlerinfo.type is ValueError   assert fehlerinfo.value.args[0] == "value must be 42" 

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

# ### Certification
# 
# https://info.credly.com/

# #### KI support 
# 
# https://poe.com/login
# 
# https://heypi.com/es/talk

# #### viel Erfolg!!!
