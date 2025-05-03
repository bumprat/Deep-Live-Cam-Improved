import threading

# Global flags for pause and stop
pause_flag = threading.Event()
pause_flag.set()  # Initially set to allow processing

stop_flag = threading.Event()
