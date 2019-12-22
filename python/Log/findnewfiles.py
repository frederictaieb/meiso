import glob, os
import threading, time, signal
from datetime import timedelta

WAIT_TIME_SECONDS = 1
filenames = {'wav'}

class ProgramKilled(Exception):
    pass

def get_wavfiles():
    for filename in glob.glob("*.wav"):
        filenames.add(filename)
    print("{}".format(filenames))
    write_html()

def write_html():
    f = open("index.html", "w")
    f.write("<html>\n")
    f.write("\t<body>\n")
    f.write("\t\t<ul>\n")
    f.write("\t\t\t<li>")
    f.write("</li>\n")
    f.write("\t\t</ul>\n")
    f.write("\t</body>\n")
    f.write("</html>\n")
    f.close()
    
def signal_handler(signum, frame):
    raise ProgramKilled

#def write_file():   
#    f.write("<html><body>")
#    f.write("<h1>Super Test</h1>")
#    f.write("</body></html>")

class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs
        
    def stop(self):
                self.stopped.set()
                self.join()
    def run(self):
            while not self.stopped.wait(self.interval.total_seconds()):
                self.execute(*self.args, **self.kwargs)
            
if __name__ == "__main__":
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=get_wavfiles)
    job.start()

    while True:
          try:
              time.sleep(1)
          except ProgramKilled:
              print "Program killed: running cleanup code"
              job.stop()
              break
