#!/usr/bin/env python
# coding: utf-8

# ![](teil_2.JPG)

# In[ ]:


void Umrechnung(dezimalzahl: int)
BEGIN
    rest: int
    rest = dezimalzahl modulo 2
    AUSGABE(rest)
    dezimalzahl = dezimalzahl div 2  # // führt eine Ganzzahldivision durch
    WENN dezimalzahl > 0 DANN
        Umrechnung(dezimalzahl)
    ENDE
ENDE

# Schreibtischtest
# Testfall 1:
# Dezimalzahl: 7
# Erwartetes Ergebnis: 111
# Ergebnis Schreibtischtest: 111
Umrechnung(7)  # Ausgabe: 1 1 1

# Testfall 2:
# Dezimalzahl: 11
# Erwartetes Ergebnis: 1011
# Ergebnis Schreibtischtest: 1011
Umrechnung(11)  # Ausgabe: 1 0 1 1


# In[2]:


7//2


# In[3]:


15//2


# In[4]:


15%2


# In[5]:


11//2


# In[6]:


11%2


# In[7]:


7%2


# Dieser **Pseudocode** beschreibt eine Funktion namens "Umrechnung", die ein Argument "dezimalzahl" vom Typ Ganzzahl (int) akzeptiert. Die Funktion hat die Aufgabe, eine Dezimalzahl in ihre binäre Darstellung unter Verwendung der Rekursion umzuwandeln. Im Folgenden wird Schritt für Schritt erläutert, was dieser Code macht:
# 
# Die **Funktion** "Umrechnung" wird mit einem Argument "dezimalzahl" vom Typ Ganzzahl **definiert**.
# 
# Es wird eine **lokale Variable** namens "rest" vom Typ Ganzzahl **deklariert**.
# 
# Der Rest der Division von "dezimalzahl" durch 2 wird berechnet (dies erfolgt unter Verwendung des Modulo-Operators, der in vielen Programmiersprachen mit "%" dargestellt wird). Das Ergebnis wird in der **Variable** "rest" **gespeichert**.
# 
# Der Wert von "rest", der ein binärer Ziffer ist, wird in der Ausgabe angezeigt (wahrscheinlich bedeutet dies, dass er in der Konsole gedruckt wird).
# 
# Anschließend erfolgt eine Ganzzahldivision von "dezimalzahl" durch 2 (dies geschieht mit "dezimalzahl div 2"). Diese Operation verschiebt im Wesentlichen die Ziffern in der binären Darstellung der **Dezimalzahl nach rechts**.
# 
# Es wird überprüft, ob "dezimalzahl" größer als 0 ist. Wenn dies der Fall ist, wird die Funktion "Umrechnung" rekursiv mit dem neuen Wert von "dezimalzahl" aufgerufen. **Dies bedeutet, dass der Umwandlungsprozess fortgesetzt wird, bis "dezimalzahl" zu 0 wird**.
# 
# Die Funktion wird rekursiv wiederholt, **bis "dezimalzahl" 0 ist**. In jeder Iteration wird eine binäre Ziffer berechnet und angezeigt.
# 
# Zusammenfassend stellt dieser Pseudocode einen rekursiven Algorithmus zur Umwandlung einer Dezimalzahl in ihre binäre Darstellung dar, **wobei die binären Ziffern einzeln in absteigender Reihenfolge von den signifikantesten (links) zu den weniger signifikanten (rechts)** berechnet und angezeigt werden.

# #### Python Code  | Ergebnis des Schreibtischtests:

# In[1]:


def Umrechnung(dezimalzahl):
    rest = dezimalzahl % 2
    print(rest)
    dezimalzahl = dezimalzahl // 2  # // führt eine ganzzahlige Division durch
    if dezimalzahl > 0:
        Umrechnung(dezimalzahl)

# Schreibtischtest
# Testfall 1:
# Dezimalzahl: 7
# Erwartetes Ergebnis: 111
# Ergebnis Schreibtischtest: 111
Umrechnung(7)  # Ausgabe: 1 1 1

# Testfall 2:
# Dezimalzahl: 11
# Erwartetes Ergebnis: 1011
# Ergebnis Schreibtischtest: 1011
Umrechnung(11)  # Ausgabe: 1 0 1 1


# In[2]:


Umrechnung(7)


# In[3]:


Umrechnung(11)


# #### Korrekt Function Python

# In[4]:


def Umrechnung(dezimalzahl):
    if dezimalzahl > 1:
        Umrechnung(dezimalzahl // 2)
    rest = dezimalzahl % 2
    print(rest, end='')

# Schreibtischtest
# Testfall 1:
# Dezimalzahl: 7
# Erwartetes Ergebnis: 111
Umrechnung(7)  # Ausgabe: 111

# Testfall 2:
# Dezimalzahl: 11
# Erwartetes Ergebnis: 1011
Umrechnung(11)  # Ausgabe: 1011


# ####   if dezimalzahl > 1:

# In[5]:


#7
Umrechnung(7)


# In[6]:


Umrechnung(11)


# Angenommen, wir rufen die Funktion **Umrechnung(7)** auf.
# 
# Im ersten Aufruf ist dezimalzahl gleich **7**.
# 
# Es berechnet den Rest von dezimalzahl geteilt durch **2 (7 % 2)**, was 1 ergibt, und speichert ihn in der Variablen rest.
# 
# rest, welches 1 ist, wird ausgegeben.
# 
# Dann führt es eine Ganzzahldivision von dezimalzahl durch **2 durch (7 // 2)**, was 3 ergibt. dezimalzahl ist jetzt 3.
# 
# Es überprüft, ob **dezimalzahl größer als 0 ist**. Da **3 größer als 0 ist**, erfolgt ein rekursiver Aufruf von Umrechnung(dezimalzahl) mit dezimalzahl gleich 3.
# 
# Jetzt befinden wir uns in einem neuen Aufruf mit dezimalzahl gleich 3.
# 
# In diesem neuen Aufruf werden **die Schritte 2 bis 5 wiederholt**. Der Rest von **3 % 2 wird berechnet**, was 1 ist, und dann wird **3 // 2 durchgeführt**, was 1 ergibt. Erneut ist dezimalzahl größer als 0, daher erfolgt ein weiterer rekursiver Aufruf mit dezimalzahl gleich 1.
# 
# Jetzt befinden wir uns in einem dritten Aufruf mit **dezimalzahl gleich 1**.
# 
# In diesem dritten Aufruf werden die Schritte **2 bis 5 wiederholt**. Der Rest von **1 % 2 wird berechnet**, was 1 ist, und dann wird 1 // 2 durchgeführt, was 0 ergibt. An diesem Punkt ist dezimalzahl gleich 0, daher erfolgt kein weiterer rekursiver Aufruf.
# 
# Der Prozess der rekursiven Aufrufe endet hier, und Sie erhalten die gedruckte Restfolge: **1 1 1**. Diese Sequenz stellt die binäre Darstellung von 7 dar.
# 
# Derselbe Prozess wird angewendet, wenn Sie **Umrechnung(11)** aufrufen, und Sie erhalten die korrekte binäre Darstellung von 11: **1011**.
# 
# Zusammengefasst funktioniert der Code durch rekursive Aufrufe, bei denen die ursprüngliche Dezimalzahl in jedem Schritt durch 2 geteilt wird, der Rest berechnet und gedruckt wird, bis die Dezimalzahl 0 wird. Das Ergebnis ist die binäre Darstellung der ursprünglichen Zahl.

# In[ ]:


Umrechnung(7) 


# In[ ]:


Umrechnung(11) 


# #### Das Ergebnis des Schreibtischtests:
# 
# das Ergebnis
# 
# für den **Testfall 1** (Dezimalzahl 7) ist **111**, 
# 
# und  
# 
# für den **Testfall 2** (Dezimalzahl 11) ist **1011**. 
# 
# Der **Algorithmus** gibt die entsprechenden Binärzahlen korrekt aus.

# ### Resume

# Dieser Code implementiert eine Funktion namens Umrechnung, die eine Dezimalzahl in ihre binäre Darstellung umwandelt. Hier ist, wie es funktioniert:
# 
# **Die Funktion Umrechnung** erhält einen Parameter dezimalzahl, der die zu konvertierende Dezimalzahl ist.
# 
# **Zuerst wird der Rest der Division von dezimalzahl durch 2 mit dem Modulo-Operator % berechnet**. Das Ergebnis wird in der Variablen rest gespeichert.
# 
# **Dann** wird der Wert von rest ausgegeben, der das am wenigsten signifikante Bit in der binären Darstellung repräsentiert.
# 
# Als nächstes **wird der Wert von dezimalzahl durch 2 mit dem Floor-Divisionsoperator // geteilt**, um die nächste Umrechnungsstufe vorzubereiten. Dies wird gemacht, um den nächsten Schritt der Umwandlung vorzubereiten.
# 
# Danach **wird überprüft, ob dezimalzahl größer als 0 ist**. Wenn dies der Fall ist, wird die Funktion Umrechnung rekursiv mit dezimalzahl als Argument aufgerufen. Dadurch wird der Umwandlungsprozess für die restlichen Bits fortgesetzt.
# 
# **Die Funktion wird rekursiv aufgerufen, bis dezimalzahl 0 ist**. Zu diesem Zeitpunkt wird die Rekursion beendet und die Funktion beendet sich.
# 
# **Der Code enthält auch einen Schreibtischtest, der verwendet wird, um die Funktionsweise des Algorithmus durch manuelle Überprüfung zu überprüfen**.
# 
# Im Schreibtischtest werden zwei Testfälle durchgeführt:
# 
# **Testfall 1**: Die Funktion Umrechnung wird mit dezimalzahl gleich 7 aufgerufen. Das erwartete Ergebnis ist die binäre Darstellung von 7, also 111. Das Ergebnis des Schreibtischtests zeigt, dass die Funktion die Bits 1, 1 und 1 korrekt ausgibt.
# 
# **Testfall 2**: Die Funktion Umrechnung wird mit dezimalzahl gleich 11 aufgerufen. Das erwartete Ergebnis ist die binäre Darstellung von 11, also 1011. Das Ergebnis des Schreibtischtests zeigt, dass die Funktion die Bits 1, 0, 1 und 1 korrekt ausgibt.
# 
# Zusammenfassend implementiert der Code eine rekursive Funktion, die eine Dezimalzahl in ihre binäre Darstellung umwandelt, indem sie die Bits nacheinander ausgibt.

# ### b)  Beschreiben Sie den Fehler und eine Korrekturmöglichkeit. 

# ![](teil_3.JPG)

# Der Fehler im **Pseudocode** liegt darin, dass die Bedingung für den rekursiven Aufruf des Algorithmus **"WENN dezimalzahl > 0 DANN" lautet**. Dadurch wird die Rekursion auch dann weitergeführt, **wenn** dezimalzahl den Wert 0 erreicht hat. Dies führt zu einer Endlosschleife, da die Bedingung für den rekursiven Aufruf immer wahr bleibt.
# 
# Um den Fehler zu **korrigieren**, sollte die Bedingung für den rekursiven Aufruf geändert werden, um sicherzustellen, dass der Algorithmus nur aufgerufen wird, wenn dezimalzahl größer als 0 ist. Hier ist der korrigierte Pseudocode:

# In[10]:


def Umrechnung(dezimalzahl):
    rest = dezimalzahl % 2
    print(rest)
    dezimalzahl = dezimalzahl // 2
    if dezimalzahl > 0:
        Umrechnung(dezimalzahl)

# Schreibtischtest
Umrechnung(7)  # Ausgabe: 1 1 1
Umrechnung(11)  # Ausgabe: 1 0 1 1


# In[11]:


#den Fehler
Umrechnung(11) # Ausgabe: 1 0 1 1


# In[12]:


Umrechnung(7)  # Ausgabe: 1 1 1


# ### Korrekt Alternative

# In[7]:


def Umrechnung(dezimalzahl):
    if dezimalzahl > 1:
        Umrechnung(dezimalzahl // 2)
    rest = dezimalzahl % 2
    print(rest, end='')

# Schreibtischtest
# Testfall 1:
# Dezimalzahl: 7
# Erwartetes Ergebnis: 111
Umrechnung(7)  # Ausgabe: 111

# Testfall 2:
# Dezimalzahl: 11
# Erwartetes Ergebnis: 1011
Umrechnung(11)  # Ausgabe: 1011


# In[9]:


Umrechnung(11)


# In[8]:


Umrechnung(7)


# ![](teil_4.JPG)

# **Die Anzahl der Stackframes**, die durch den Aufruf des Algorithmus erzeugt werden, entspricht der Anzahl der rekursiven Aufrufe plus dem initialen Aufruf. Jeder rekursive Aufruf erzeugt einen neuen Stackframe.
# 
# Für die gegebenen Testfälle ergibt sich folgendes:
# 
# **Testfall 1**: 
# 
# Dezimalzahl = 7
# 
# Erwartetes Ergebnis: 111
# 
# Anzahl der Stackframes: **4** (1 initialer Aufruf + 3 rekursive Aufrufe)
# 
# **Testfall 2**: 
# 
# Dezimalzahl = 11
# 
# Erwartetes Ergebnis: 1011
# 
# Anzahl der Stackframes: **5** (1 initialer Aufruf + 4 rekursive Aufrufe)
# 
# In **beiden Fällen** werden rekursive Aufrufe basierend auf dem Wert von dezimalzahl durchgeführt. Jeder rekursive Aufruf erzeugt einen zusätzlichen Stackframe, da die Funktion nicht beendet wird, sondern sich selbst aufruft, um den Rest der Umwandlung zu bearbeiten.

# **Testfall 1**: 
# 
# Dezimalzahl = 7
# 
# Erwartetes Ergebnis: 111
# 
# Anzahl der Stackframes: **4** (1 initialer Aufruf + 3 rekursive Aufrufe)
# 
# #### Notiz:
# 
# Wenn die Funktion Umrechnung mit dem Wert dezimalzahl gleich **7 aufgerufen wird**, werden aufgrund der rekursiven Aufrufe mehrere Stapelrahmen erzeugt. Schauen wir uns an, wie jeder Stapelrahmen erzeugt wird:
# 
# **Initialer Aufruf**: Zu Beginn wird der initiale Aufruf der Funktion **Umrechnung(7)** durchgeführt. Dadurch wird der **erste** Stapelrahmen erzeugt.
# 
# **Erster rekursiver Aufruf**: Innerhalb der Funktion wird ein rekursiver Aufruf von Umrechnung mit einem neuen Wert für dezimalzahl durchgeführt. In diesem Fall wird **Umrechnung(3)** aufgerufen. Dadurch wird der **zweite** Stapelrahmen erzeugt.
# 
# **Zweiter rekursiver Aufruf**: Innerhalb der Funktion wird erneut ein rekursiver Aufruf von Umrechnung mit einem neuen Wert für dezimalzahl durchgeführt. In diesem Fall wird **Umrechnung(1)** aufgerufen. Dadurch wird der **dritte** Stapelrahmen erzeugt.
# 
# **Dritter rekursiver Aufruf**: Nochmals wird ein rekursiver Aufruf von Umrechnung mit einem neuen Wert für dezimalzahl durchgeführt. In diesem Fall wird **Umrechnung(0**) aufgerufen. Dadurch wird der **vierte** Stapelrahmen erzeugt.
# 
# Zusammenfassend werden beim Ausführen des Testfalls mit dezimalzahl gleich 7 insgesamt **4 Stapelrahmen** erzeugt. Dies beinhaltet den initialen Aufruf und die drei rekursiven Aufrufe, die innerhalb der Funktion erfolgen.
# 
# **Es ist wichtig zu beachten**, dass jeder Stapelrahmen die erforderlichen Informationen zur Ausführung einer bestimmten Instanz der Funktion Umrechnung enthält. Wenn die rekursiven Aufrufe aufgelöst werden und der Basisfall erreicht wird, werden die Stapelrahmen in umgekehrter Reihenfolge freigegeben, wodurch die Ausführung zu den vorherigen Stapelrahmen zurückkehrt, bis der initiale Aufruf abgeschlossen ist.
# 

# **Testfall 2**: 
# 
# Dezimalzahl = 11
# 
# Erwartetes Ergebnis: 1011
# 
# Anzahl der Stackframes: **5** (1 initialer Aufruf + 4 rekursive Aufrufe)
# 
# 
# #### Notiz:
# 
# Wenn die Funktion Umrechnung mit dem Wert dezimalzahl gleich **11 aufgerufen wird**, werden aufgrund der rekursiven Aufrufe mehrere Stapelrahmen erzeugt. Schauen wir uns an, wie jeder Stapelrahmen erzeugt wird:
# 
# **Initialer Aufruf**: Zu Beginn wird der initiale Aufruf der Funktion **Umrechnung(11)** durchgeführt. Dadurch wird der **erste** Stapelrahmen erzeugt.
# 
# **Erster rekursiver Aufruf**: Innerhalb der Funktion wird ein rekursiver Aufruf von Umrechnung mit einem neuen Wert für dezimalzahl durchgeführt. In diesem Fall wird **Umrechnung(5)** aufgerufen. Dadurch wird der **zweite** Stapelrahmen erzeugt.
# 
# **Zweiter rekursiver Aufruf**: Innerhalb der Funktion wird erneut ein rekursiver Aufruf von Umrechnung mit einem neuen Wert für dezimalzahl durchgeführt. In diesem Fall wird **Umrechnung(2)** aufgerufen. Dadurch wird der **dritte** Stapelrahmen erzeugt.
# 
# **Dritter rekursiver Aufruf**: Nochmals wird ein rekursiver Aufruf von Umrechnung mit einem neuen Wert für dezimalzahl durchgeführt. In diesem Fall wird **Umrechnung(1)** aufgerufen. Dadurch wird der **vierte**  Stapelrahmen erzeugt.
# 
# **Vierter rekursiver Aufruf**: Schließlich wird ein weiterer rekursiver Aufruf von Umrechnung mit einem neuen Wert für dezimalzahl durchgeführt. In diesem Fall wird **Umrechnung(0)** aufgerufen. Dadurch wird der **fünfte** Stapelrahmen erzeugt.
# 
# Zusammenfassend werden beim Ausführen des Testfalls mit dezimalzahl gleich **11 insgesamt 5 Stapelrahmen erzeugt**. Dies beinhaltet den initialen Aufruf und die vier rekursiven Aufrufe, die innerhalb der Funktion erfolgen.
# 
# Jeder Stapelrahmen speichert die Informationen, die zur Ausführung einer bestimmten Instanz der Funktion Umrechnung erforderlich sind. Wenn die rekursiven Aufrufe aufgelöst werden und der Basisfall erreicht wird, werden die Stapelrahmen in umgekehrter Reihenfolge freigegeben, wodurch die Ausführung zu den vorherigen Stapelrahmen zurückkehrt, bis der initiale Aufruf abgeschlossen ist.

# ![](teil_5.JPG)

# **a) Vorteil der rekursiven Lösung**:
# 
# **Klarere und kompaktere Darstellung des Problems**: Rekursive Lösungen spiegeln oft die natürliche Struktur des Problems wider und können dadurch einfacher zu verstehen und zu implementieren sein. Sie ermöglichen eine elegante und intuitive Lösung, indem sie das Problem in kleinere Teilprobleme zerlegen.
# 
# 
# **b) Nachteil der rekursiven Lösung**:
# 
# **Potenzielle Gefahr von Stapelüberlauf (Stack Overflow)**: Bei tiefen Rekursionen oder großen Eingabedaten könnte es zu einem Stapelüberlauf kommen, wenn nicht genügend Speicherplatz im Stapel vorhanden ist. Dies kann zu einem Abbruch des Programms führen. Bei iterativen Lösungen tritt dieses Problem normalerweise nicht auf.
# 
# 
# **c) Vorteil der iterativen Lösung**:
# 
# **Bessere Kontrolle über den Speicherbedarf**: Iterative Lösungen verwenden in der Regel weniger Speicher, da sie keine zusätzlichen Stapelrahmen erzeugen. Dies kann besonders wichtig sein, wenn große Eingabedaten oder eine begrenzte Speicherressource vorliegen.
# 
# 
# **d) Nachteil der iterativen Lösung**:
# 
# **Möglicherweise komplexere Implementierung**: Im Vergleich zur rekursiven Lösung erfordert die iterative Lösung oft mehr Code und eine detailliertere Verwaltung von Schleifen, Indizes und Zwischenvariablen. Dies kann zu einem erhöhten Implementierungsaufwand führen und die Lesbarkeit des Codes beeinträchtigen.
# 
# Es ist wichtig zu beachten, dass die Wahl zwischen einer rekursiven und einer iterativen Lösung von mehreren Faktoren abhängt, einschließlich der Natur des Problems, der Eingabedaten, der Effizienzanforderungen und der verfügbaren Ressourcen. Es gibt keine eindeutige **"richtige" oder "falsche"** Lösungsmethode, und die Entscheidung sollte basierend auf den spezifischen Anforderungen und Einschränkungen getroffen werden.

# ![](teil_7.JPG)

# ![](teil_6.JPG)

# ##### option_pseudocode_1

# In[ ]:


void Umrechnung(dezimalzahl: int)
BEGIN
    rest: int
    rest = dezimalzahl modulo 2
    AUSGABE(rest)
    dezimalzahl = dezimalzahl div 2  # // führt eine Ganzzahldivision durch
    WENN dezimalzahl > 0 DANN
        Umrechnung(dezimalzahl)
    ENDE
ENDE

# Schreibtischtest
# Testfall 1:
# Dezimalzahl: 7
# Erwartetes Ergebnis: 111
# Ergebnis Schreibtischtest: 111
Umrechnung(7)  # Ausgabe: 1 1 1

# Testfall 2:
# Dezimalzahl: 11
# Erwartetes Ergebnis: 1011
# Ergebnis Schreibtischtest: 1011
Umrechnung(11)  # Ausgabe: 1 0 1 1


# ##### option_pseudocode_2

# In[ ]:


Klasse Liste:
    Prozedur Initialisieren():
        Elemente = LeereListe

    Prozedur Einfügen(Wert):
        Füge Wert zu Elemente hinzu

    Funktion Größe():
        Gib Länge von Elemente zurück

    Funktion Element(Pos):
        Gib Element an Position Pos in Elemente zurück

Prozedur Umrechnung(dezimalzahl):
    liste = Neue Instanz von Liste()

    Während dezimalzahl > 0 Mache:
        rest = dezimalzahl modulo 2
        liste.Einfügen(rest)
        dezimalzahl = dezimalzahl div 2

    # Gibt die binären Ziffern in umgekehrter Reihenfolge aus (von der letzten zur ersten)
    Für i von liste.Größe() - 1 bis 0 in Schritten von -1 Mache:
        Schreibe liste.Element(i)

# Beispiel für die Verwendung
dezimalzahl = 10
Umrechnung(dezimalzahl)


# ### My Py Code

# In[15]:


class List:
    def __init__(self):
        self.elements = []

    def insert(self, Wert):
        self.elements.append(Wert)

    def size(self):
        return len(self.elements)

    def element(self, Pos):
        return self.elements[Pos]

def Umrechnung(dezimalzahl):
    rest = 0
    i = 0
    lista = List()
    
    while dezimalzahl > 0:
        rest = dezimalzahl % 2
        lista.insert(rest)
        dezimalzahl = dezimalzahl // 2
    
    for i in range(lista.size() - 1, -1, -1):
        print(lista.element(i))

# Schreibtischtest
# Testfall 1:
# Dezimalzahl: 7
# Erwartetes Ergebnis: 111
Umrechnung(7)  # Ausgabe: 111

# Testfall 2:
# Dezimalzahl: 11
# Erwartetes Ergebnis: 1011
Umrechnung(11)  # Ausgabe: 1011


# #### f) Implementieren Sie beide Algorithmen in Python, um Ihre Lösungen zu überprüfen. * 

# In[ ]:


class List:
    def __init__(self):
        self.elements = []

    def Insert(self, Wert):
        self.elements.append(Wert)

    def size(self):
        return len(self.elements)

    def Element(self, Pos):
        return self.elements[Pos]

def Umrechnung(dezimalzahl):
    lista = List()

    while dezimalzahl > 0:
        rest = dezimalzahl % 2
        lista.Insert(rest)
        dezimalzahl = dezimalzahl // 2

    # Druckt die binären Ziffern in umgekehrter Reihenfolge (von der letzten zur ersten)
    for i in range(lista.size() - 1, -1, -1):
        print(lista.Element(i))

# Beispiel für die Verwendung
dezimalzahl = 10
Umrechnung(dezimalzahl)


# #### Notiz

# **7 % 2** ergibt 1 als Ergebnis, weil es sich um eine Modulo- oder Restoperation handelt. Bei dieser Operation wird die Zahl 7 durch 2 geteilt, und der Rest der Division wird berechnet.
# 
# Wenn man 7 durch 2 teilt, erhält man einen Quotienten von 3 und einen Rest von 1. Das bedeutet:
# 
# **7 geteilt durch 2 ergibt 3 mit einem Rest von 1**.
# 
# Der Rest ist das Ergebnis der Operation 7 % 2, und in diesem Fall beträgt dieser Rest 1. Zusammengefasst, **7 % 2 ergibt 1**, weil bei der Division von 7 durch 2 ein Rest von 1 bleibt.

# In[ ]:


7%2


# In[ ]:


7//2


# #### Resume: 
# 
# **Algorithmus** für die Klasse **"List"**: Dieser Algorithmus definiert eine Klasse namens "List" mit Methoden zur Initialisierung einer Liste, zum Einfügen von Elementen, zum Ermitteln der Größe der Liste und zum Abrufen eines Elements an einer bestimmten Position. Obwohl es sich um mehrere Methoden handelt, wird es als ein einziger Algorithmus betrachtet, da alle mit der Funktionalität der Klasse "List" zusammenhängen.
# 
# **Algorithmus** für die binäre Umrechnung **("Umrechnung")**: Dieser Algorithmus akzeptiert eine Dezimalzahl als Eingabe und wandelt diese Zahl in ihre binäre Darstellung um. Er verwendet Schleifen, darunter while und for, um diese Umwandlung durchzuführen, und gibt dann die binären Ziffern in umgekehrter Reihenfolge aus.
# 
# **Zusammengefasst gibt es zwei Algorithmen im Code**: einen im Zusammenhang mit der Definition der Klasse "List" und einen im Zusammenhang mit der Umwandlung von Dezimalzahlen in Binärzahlen.

# ### Pseudo-Beispiele

# **seudocode** (Pseudocode auf Deutsch oder Pseudocódigo en español) ist eine informelle, halbformale Darstellung eines Algorithmus oder Computerprogramms. Es ist eine Art menschenlesbare Beschreibung des Ablaufs von Aufgaben oder Prozessen, die einem Computer verständlich gemacht werden sollen, bevor sie in einer bestimmten Programmiersprache implementiert werden.
# 
# **Pseudocode** wird verwendet, um den Algorithmus in einer strukturierten und leicht verständlichen Form zu beschreiben, ohne sich auf die spezifische Syntax einer Programmiersprache festzulegen. Es ist eine Brücke zwischen der menschlichen Denkweise und der Programmierung. Es ermöglicht Programmierern, Probleme zu planen, zu analysieren und zu diskutieren, bevor sie mit der eigentlichen Codierung beginnen.
# 
# Typischerweise verwendet **Pseudocode** natürliche Sprache, mathematische Notation und einfache Konzepte aus der Programmierung, um den Algorithmus zu beschreiben. Es kann Schlüsselwörter wie "IF" (wenn), "FOR" (für), "WHILE" (solange), "BEGIN" (Anfang), "END" (Ende) und andere verwenden, um die Struktur des Algorithmus darzustellen.
# 
# **Pseudocode ist nicht für die Ausführung gedacht, sondern dient dazu, den Ablauf und die Logik eines Algorithmus zu planen und zu kommunizieren**. Es ist ein nützliches Werkzeug für die Entwicklerzusammenarbeit, die Dokumentation von Programmen und die Schulung von Programmieranfängern. Es ermöglicht Entwicklern, Ideen zu skizzieren und zu verfeinern, bevor sie den eigentlichen Code schreiben.

# ![](pseudo_1.PNG)

# ![](pseudo_2.PNG)

# ![](pseudo_3.PNG)

# ![](pseudo_4.PNG)

# ![](pseudo_py_linked.PNG)

# ![](pseudo_py_linked_1.PNG)

# #### Media support 

# https://www.youtube.com/watch?v=BwQNKiG86Gs

# #### Was ist pseudocode?

# **Pseudocode** ist eine informelle Beschreibung eines Algorithmus, die Elemente aus natürlicher Sprache und Programmiersprachen kombiniert. Es ist eine Möglichkeit, den Algorithmus in einer allgemein verständlichen Form zu skizzieren, ohne auf die spezifische Syntax einer bestimmten Programmiersprache eingehen zu müssen.
# 
# **Pseudocode** verwendet einfache Konstruktionen, um die Funktionalität des Algorithmus zu beschreiben, wie zum Beispiel Zuweisungen, Schleifen, Bedingungen und Unterprogramme. Es dient dazu, den grundlegenden Ablauf des Algorithmus zu vermitteln und die Logik und Schritte zu verdeutlichen, ohne sich um die Details der tatsächlichen Implementierung in einer bestimmten Programmiersprache zu kümmern.
# 
# **Pseudocode** ist flexibel und kann an die Bedürfnisse und Präferenzen des Schreibenden angepasst werden. Es ist ein nützliches Werkzeug, um zu planen, zu entwerfen und Algorithmen zu kommunizieren, bevor sie in einer bestimmten Programmiersprache implementiert werden. Pseudocode kann von Entwicklern, Programmierern oder anderen Personen verwendet werden, um einen Algorithmus zu verstehen, zu überprüfen oder zu dokumentieren, ohne auf spezifische Syntaxdetails eingehen zu müssen.

# #### Viel spass!!!
