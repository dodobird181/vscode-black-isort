import subprocess
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class Watcher:
    DIRECTORY_TO_WATCH = "./"  # Set this to your project directory

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == "modified":
            # If a Python file is modified, run Black on it
            if event.src_path.endswith(".py"):
                print(f"Running Black on: {event.src_path}")
                subprocess.run(["isort", "--profile", "black", event.src_path])
                subprocess.run(["black", "--preview", event.src_path])


if __name__ == "__main__":
    w = Watcher()
    w.run()
