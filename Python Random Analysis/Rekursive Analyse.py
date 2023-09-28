#!/usr/bin/env python
# coding: utf-8

# ## Ü: Rekursive Analyse  
#     
# Ihnen steht die nachfolgende Python-Funktion zur Verfügung: 

# In[2]:


def bunnyEars(bunnies:int): 
    if bunnies == 0:              
        return 0      
    return 2 + bunnyEars(bunnies-1) 


# In[ ]:


#seudo code? was es bedeutet?


# ### die Funktion
# 
# Die Funktion bunnyEars ist eine rekursive Funktion, die die Gesamtanzahl der Ohren in einer Gruppe von Hasen berechnet, basierend auf der Anzahl der Hasen in der Gruppe.
# 
# So funktioniert es:
# 
# Die Funktion bunnyEars hat einen Parameter bunnies, der die Anzahl der Hasen in der Gruppe repräsentiert.
# 
# Die erste Zeile der Funktion überprüft, ob bunnies gleich 0 ist. Wenn dies der Fall ist, bedeutet dies, dass es keine Hasen in der Gruppe gibt, und die Funktion gibt 0 zurück, da es keine Ohren gibt.
# 
# Wenn bunnies nicht gleich 0 ist, wird der nächste Schritt ausgeführt. Die Funktion ruft sich selbst rekursiv mit dem Argument bunnies-1 auf. Dies bedeutet, dass die Funktion bunnyEars erneut aufgerufen wird, diesmal jedoch mit einem Hasen weniger.
# 
# Bei jedem rekursiven Aufruf wird 2 zur Rückgabe von bunnyEars(bunnies-1) addiert. Dies liegt daran, dass jeder Hase zwei Ohren hat.
# 
# Die Rekursion geht weiter, bis bunnies gleich 0 ist. Bei jedem rekursiven Aufruf wird die Anzahl der Hasen um 1 reduziert, sodass schließlich der Basisfall erreicht wird, in dem bunnies 0 ist und die Funktion aufhört, sich selbst aufzurufen.
# 
# Schließlich, wenn bunnies gleich 0 ist, wird die kumulierte Summe von 2 in jedem rekursiven Aufruf zurückgegeben, was die Gesamtanzahl der Ohren in der Hasengruppe darstellt.
# 
# Zusammenfassend verwendet die Funktion bunnyEars Rekursion, um die Gesamtanzahl der Ohren in einer Gruppe von Hasen zu berechnen. Es werden 2 Ohren pro Hase gezählt, und die Funktion ruft sich selbst mit einem Hasen weniger auf, bis der Basisfall erreicht ist, in dem keine Hasen vorhanden sind.

# ### Rekursive Analyse
# 
# Die rekursive Analyse ist ein Ansatz in der Informatik und Mathematik, bei dem ein Problem oder eine Funktion durch wiederholtes Anwenden derselben Funktion auf kleinere Teilprobleme gelöst wird. Es basiert auf dem Konzept der Rekursion, bei dem eine Funktion sich selbst aufruft, um eine Aufgabe zu erledigen.
# 
# Bei der rekursiven Analyse wird das Problem in kleinere Teilprobleme zerlegt, die sich leichter lösen lassen. Die Funktion wird dann auf jedes Teilproblem angewendet, bis ein Basisfall erreicht ist, der direkt gelöst werden kann. Die Ergebnisse der Teilprobleme werden dann kombiniert, um das Gesamtproblem zu lösen.
# 
# Der Schlüssel zur rekursiven Analyse liegt in der Definition der rekursiven Funktion und der Identifizierung des Basisfalls. Die rekursive Funktion muss so definiert sein, dass sie sich selbst mit kleineren Eingaben aufruft, um schließlich den Basisfall zu erreichen. Der Basisfall ist der Punkt, an dem das Problem so klein ist, dass es direkt gelöst werden kann, ohne einen weiteren rekursiven Aufruf.
# 
# Die rekursive Analyse kann in vielen Bereichen der Informatik nützlich sein, insbesondere bei der Lösung von Problemen, die sich in kleinere Teilprobleme zerlegen lassen. Sie wird häufig zur Implementierung von Algorithmen verwendet, z.B. bei der Sortierung (z.B. Quicksort oder Mergesort), der Baumtraversierung (z.B. Tiefensuche oder Breitensuche) und der Berechnung von Fibonacci-Zahlen.
# 
# Es ist wichtig, bei der Verwendung der rekursiven Analyse darauf zu achten, dass die rekursive Funktion korrekt definiert ist und dass es eine geeignete Abbruchbedingung gibt, um unendliche Rekursionen zu vermeiden. Wenn dies nicht beachtet wird, kann es zu Fehlern wie Endlosschleifen oder Speicherüberlauf kommen.
# 
# Insgesamt ermöglicht die rekursive Analyse eine elegante und effektive Lösung komplexer Probleme, indem sie diese in kleinere und leichter zu lösende Teilprobleme zerlegt. Durch die Anwendung der Funktion auf diese Teilprobleme und die Kombination der Ergebnisse kann das Gesamtproblem gelöst werden.

# ### a) Rekursive Analyse 

# In[3]:


#4
bunnyEars(4)


# In[6]:


bunnyEars(1)


# In[4]:


#2
bunnyEars(2)


# In[5]:


#1
bunnyEars(1)


# Wie viele Stackframes werden durch den Aufruf erzeugt?

# In[ ]:


# unter Berücksichtigung der Tatsache, dass Null die Position Nummer 1 ist

# bunnyEars(9) = 10 times

# bunnyEars(4) = 5 times
# bunnyEars(2) = 3 times
# bunnyEars(1) = 2 times


# #### Beispiel

# In[7]:


# Create a list of 10 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[8]:


# Select from the first to the last element
selection = numbers[0:len(numbers)]


# In[9]:


# print out the selection
print(selection)


# In[1]:


tuple = (1,2,3,4,5,6)
# mutable oder unmutable zu sein


# In[2]:


tuple[1]


# In[20]:


#select the first elemento of the list
numbers[0]


# In[21]:


numbers[1]


# In[22]:


numbers[2]


# In[23]:


numbers[3]


# In[24]:


numbers[4]


# In[25]:


numbers[5]


# In[26]:


numbers[6]


# In[27]:


numbers[7]


# In[28]:


numbers[8]


# In[29]:


numbers[9]


# ### b) Übertragen Sie den Rekursiven Algorithmus in einen Iterativen Algorithmus: 

# ### Notiz: 
# 
# Die while-Schleifen werden verwendet, um einen Codeblock zu wiederholen, solange eine bestimmte Bedingung erfüllt ist. 

# In[31]:


def bunnyEars_iterativ(bunnies:int):
    ears = 0
    while(bunnies > 0):
        ears = ears + 2         
        bunnies = bunnies - 1              
        return ears 


# ### die Function 
# 
# Die Funktion bunnyEars_iterativ ist eine iterative Version der Funktion bunnyEars, die die Gesamtanzahl der Ohren in einer Gruppe von Hasen berechnet, basierend auf der Anzahl der Hasen in der Gruppe. Im Gegensatz zur rekursiven Funktion verwendet diese Funktion einen iterativen Ansatz mit einer while-Schleife.
# 
# Hier ist, wie es funktioniert:
# 
# Die Funktion bunnyEars_iterativ nimmt ein Argument bunnies entgegen, das die Anzahl der Hasen in der Gruppe darstellt.
# 
# Eine Variable ears wird mit 0 initialisiert, um die Gesamtanzahl der Ohren zu zählen.
# 
# Es wird eine while-Schleife gestartet, die solange ausgeführt wird, wie bunnies größer als 0 ist.
# 
# Bei jedem Durchlauf der Schleife wird ears um 2 erhöht, da jeder Hase zwei Ohren hat.
# 
# Anschließend wird bunnies um 1 verringert, da ein Hase gezählt wurde.
# 
# Nachdem ears und bunnies aktualisiert wurden, wird zur Anfang der while-Schleife zurückgekehrt, um zu überprüfen, ob bunnies immer noch größer als 0 ist. Wenn dies der Fall ist, wird der Vorgang wiederholt. Wenn bunnies gleich oder kleiner als 0 ist, wird die Schleife verlassen.
# 
# Schließlich wird der Wert von ears zurückgegeben, der die Gesamtanzahl der Ohren in der Hasengruppe repräsentiert.
# 
# Zusammenfassend berechnet die Funktion bunnyEars_iterativ die Gesamtanzahl der Ohren in einer Hasengruppe mithilfe eines iterativen Ansatzes. Sie durchläuft die Hasen, während sie den Ohrenzähler und die verbleibende Anzahl der Hasen in jeder Iteration aktualisiert. Am Ende wird die Gesamtzahl der Ohren zurückgegeben.

# In[32]:


# Test the function with different inputs
print(bunnyEars_iterativ(4))  # Output: 4
print(bunnyEars_iterativ(2))  # Output: 2
print(bunnyEars_iterativ(1))  # Output: 1


# ### Notiz: 
# 
# Das Ergebnis dieser while-Schleife wird immer 2 sein, unabhängig vom anfänglichen Wert von bunnies. Dies liegt daran, dass die return-Anweisung innerhalb der Schleife steht, was dazu führt, dass die Schleife nur einmal durchlaufen wird und dann endet.
# 
# Wenn die Schleife zum ersten Mal durchlaufen wird, wird ears um 2 erhöht und bunnies um 1 verringert. Anschließend wird die return-Anweisung erreicht, was bedeutet, dass der aktuelle Wert von ears zurückgegeben wird und die Funktion bunnyEars_iterativ() endet.
# 
# Da die return-Anweisung innerhalb der Schleife steht, wird die Schleife nur einmal durchlaufen und der aktualisierte Wert von ears zurückgegeben. Daher wird das Ergebnis immer 2 sein, unabhängig vom anfänglichen Wert von bunnies.

# In[ ]:


#individual


# In[33]:


bunnyEars_iterativ(4)


# In[34]:


bunnyEars_iterativ(3)


# In[35]:


bunnyEars_iterativ(2)


# In[36]:


bunnyEars_iterativ(1)


# In[37]:


#zero ist raus weil the condition is > 0 und nicht >=0
bunnyEars_iterativ(0)


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

# #### viel Erfolg!!!
