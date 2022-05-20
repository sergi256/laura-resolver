import PySimpleGUI as sg
import sys

if len(sys.argv) == 1:
    event, values = sg.Window('My Script',
                    [[sg.Text('Document a obrir')],
                    [sg.In(), sg.FileBrowse()],
                    [sg.Open(), sg.Cancel()]]).read(close=True)
    fname = values[0]
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
#else:
#    sg.popup('The filename you chose was', fname)
### FI GUI


# Algorithm to find which number in a list sum up to a certain number

def f(v, i, S, memo):
  if i >= len(v): return 1 if S == 0 else 0
  if (i, S) not in memo:  # <-- Check if value has not been calculated.
    count = f(v, i + 1, S, memo)
    count += f(v, i + 1, S - v[i], memo)
    memo[(i, S)] = count  # <-- Memoize calculated result.
  return memo[(i, S)]     # <-- Return memoized value.

def g(v, S, memo):
  subset = []
  for i, x in enumerate(v):
    # Check if there is still a solution if we include v[i]
    if f(v, i + 1, S - x, memo) > 0:
      subset.append(x)
      S -= x
  return subset
### FI FUNCIONS 


v = []
#with open(r"C:\Users\Laura\Documents\sergi code\llista.txt") as file:
with open(fname) as file:
    for line in file:
        #print(line.rstrip())
        v.append(int(line.rstrip())) 

# now v contains integers like that: [1, 2, 3, 10]


sum = 12
memo = dict()
if f(v, 0, sum, memo) == 0: print("There are no valid subsets.")
else: 
    #sg.popup(g(v, sum, memo))
    print(v)
    print(g(v, sum, memo))
