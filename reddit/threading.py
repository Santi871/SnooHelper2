from threading import Thread


def threaded(func):
    """
    Decorator that starts a method or function on its own thread
    :param func: function
    :return: wrapped function
    """
    def wrapped_f(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        thread.start()

    return wrapped_f
