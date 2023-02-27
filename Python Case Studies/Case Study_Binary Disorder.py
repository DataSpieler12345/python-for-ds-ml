y_true = [int(x) for x in input().split()]
y_pred = [int(x) for x in input().split()]

from sklearn.metrics import confusion_matrix
import numpy as np

cm = confusion_matrix(y_pred, y_true, labels = [1,0])

print(np.array(cm, dtype ='f'))