import sys
import os
import time
from fsevents import Observer
from fsevents import Stream
from selenium import webdriver
from urllib2 import URLError
from list_env_var import ListEnvVar

def setupDriver(setid):
    """
    Sets up ChromeDriver.
    If ChromeDriver path does not exist,
    quit application.
    """

    if not os.path.exists("EnvFile"):
        print "Please run 'python add_env_var.py' first."
        sys.exit(1)

#    f = open("EnvFile", "rb")
#    path = f.readline()
#    url_path = f.readline()
#    f.close()

    env_var_dict = ListEnvVar.getEnvVarDict("EnvFile", setid)
    path = env_var_dict['chromedriver_path']
    url_path = env_var_dict['url_to_watch']

    chromedriver_abspath = os.path.abspath(path.strip())
    if not os.path.exists(chromedriver_abspath):
        print "%s does not exist." % chromedriver_abspath
        sys.exit(1)

    driver = webdriver.Chrome(chromedriver_abspath)
    driver.get(url_path)

    return driver

def callback(event):
    """
    Callback method when file change is
    observed.
    """
    print "File Changed, refreshing page."
    driver.refresh()

# Main Procedure
def main():
    if len(sys.argv) != 3:
        print "Usage: %s FilePath SetID" % sys.argv[0]
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print "Path does not exist"
        sys.exit(1)

    global driver
    driver = setupDriver(sys.argv[2])

    observer = Observer()
    stream = Stream(callback, os.path.abspath(path), file_events=True)
    observer.schedule(stream)
    observer.start()
    print "Starting observation..."
    print "Ctrl-C to exit."

    try:
        # yields to allow Ctrl-C to be captured
        while True:
            # sleep saves CPU cycles
            time.sleep(1)
    except KeyboardInterrupt:
        print "\nQuitting program gracefully"
        observer.unschedule(stream)
        observer.stop()

        try:
            driver.quit()
        except URLError:
           # Some URLError
           pass

        sys.exit(1)


if __name__ == "__main__":
    main()
