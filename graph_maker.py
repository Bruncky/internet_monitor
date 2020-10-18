import matplotlib.pyplot as plt
import csv

def make_graph(date):
  x = []
  y = []

  with open(f'{date}_speed.csv', 'r') as csvfile:
      plots = csv.reader(csvfile, delimiter=',')
      next(csvfile)
      for row in plots:
          x.append(str(row[0]))
          y.append(float(row[1]))

  plt.plot(x, y, label='Mb/s')
  plt.xlabel('time')
  plt.ylabel('download speed')
  plt.title(f"Download speed for {date}")
  plt.legend()
  plt.savefig(f'{date}_graph.png')
