from datetime import date
import time

timestamp = time.time()
print("Time stamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)
    