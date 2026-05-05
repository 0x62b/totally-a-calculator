from machine import Pin
import time

ROW_PINS = [0, 1, 2, 3, 4, 5, 6]
COL_PINS = [7, 8, 9, 10, 11]
SDA_PIN = 12
SCL_PIN = 13

rows = [Pin(p, Pin.OUT) for p in ROW_PINS]
cols = [Pin(p, Pin.IN, Pin.PULL_UP) for p in COL_PINS]

for r in rows:
  r.value(1)

keymap = [
  ["",     "Up",   "",      "",    ""],
  ["Left", "Sel",  "Right", "",    ""],
  ["",     "Down", "",      "",    ""],
  ["7",    "8",    "9",     "DEL", "AC"],
  ["4",    "5",    "6",     "*",   "/"],
  ["3",    "2",    "1",     "+",   "-"],
  ["0",    ".",    "~",     "SQT", "="]
]

def scan():
  for r in rows:
    r.value(0)
    
    for c in cols:
      if c.value() == 0:
        r.value(1)
        return keymap[rows.index(r)][cols.index(c)]
        
    r.value(1)

while True:
  key = scan()
  if key:
    print(key)
  
  time.sleep(0.05)