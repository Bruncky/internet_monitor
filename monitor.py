import speedtest, csv
import datetime
import time as t
from graph_maker import make_graph
from drive_uploader import upload_to_drive

s = speedtest.Speedtest()

def record():
  #create csv file with headers time and speed
  with open(f'{datetime.date.today()}_speed.csv', mode='w') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'downspeed', 'upspeed'])
    csv_writer.writeheader()
    start_day = datetime.date.today()
    while True:
      #writes into the CSV file until the date changes
      time = datetime.datetime.now().strftime("%H:%M")
      downspeed = round((round(s.download()) / 1048576), 2)
      upspeed = round((round(s.upload()) / 1048576), 2)
      csv_writer.writerow({'time': time, 'downspeed': downspeed, "upspeed": upspeed})
      print({'time': time, 'downspeed': downspeed, "upspeed": upspeed}, "Mb/s")
      t.sleep(60)
      if datetime.date.today() != start_day:
      #when day changes stop writing, generate a graph, upload that graph to google drive and start again
        speedcsv.close()
        make_graph(start_day)
        try:
          upload_to_drive(f"{start_day}" + "_graph.jpg")
          print("now uploaded to drive")
        except:
          print("API keys not correct - now saving to local device")
          pass
        finally:
          record()

record()
