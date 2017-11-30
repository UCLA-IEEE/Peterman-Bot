import threading

def create_repeating_timer(func, interval, args=None, kwargs=None):
    """Creates a repeating timer for a given function. Must be started manually.
    
    Args:
        func: A function to repeat.
        interval (float): Interval to repeat at.
        args, kwargs: Arguments to pass to func.
    
    Returns:
        threading.Timer: A timer that can be started to repeatedly call func.
    """
    timer_func = get_timered_function(func, interval)
    return threading.Timer(interval, timer_func, args=args, kwargs=kwargs)

def get_timered_function(func, interval):
    """Give back a function that creates a timer for itself after finishing its work."""
    def timered_function(*args, **kwargs):
        threading.Timer(interval, timered_function, args=args, kwargs=kwargs).start()
        func(*args, **kwargs)
    return timered_function