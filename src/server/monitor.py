import os
import sys
import time
import logging
import watchdog
from collections import defaultdict
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

class MonitorDirectory(watchdog.events.FileSystemEventHandler):
    def __init__(self, inv_index):
        self.__inv_index = inv_index

    def add_dir(self, dir):
        for arg, dirs, files in os.walk(dir):
            for item in dirs:
                if item not in self.__inv_index:
                    continue
                self.__inv_index[item].add(os.path.abspath(arg))

    def del_dir(self, dir):
        for arg, dirs, files in os.walk(dir):
            for item in dirs:
                if item not in self.__inv_index:
                    continue
                try:
                    self.__inv_index[item].remove(os.path.abspath(arg))
                except:
                    continue

    def add_single_dir(self, dir):
        self.__inv_index[os.path.basename(dir)].add(os.path.dirname(dir))

    def del_single_dir(self, dir):
        base_name = os.path.basename(dir)
        dir_name = os.path.dirname(dir)
        if base_name not in self.__inv_index:
            return
        self.__inv_index[base_name].add(dir_name)

    def on_moved(self, event):
        if not event.is_directory:
            return
        self.del_single_dir(event.src_path)
        print "Del %s" % event.src_path
        self.add_single_dir(event.dest_path)
        print "Add %s" % event.dest_path

    def on_created(self, event):
        if not event.is_directory:
            return
        self.add_single_dir(event.src_path)
        print "Add %s" % event.src_path

    def on_deleted(self, event):
        if not event.is_directory:
            return
        self.del_single_dir(event.src_path)
        print "Del %s" % event.src_path


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MonitorDirectory(defaultdict(set))
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()