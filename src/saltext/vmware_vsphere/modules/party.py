# hrm. Where the heck did I put those changes? lol. 
from pyVim import *
import functools


def needs_service_instance(func):
    @functools.wraps(func)
    def wrapper(service_instance=None, thing='neato'):
        return func(service_instance=(service_instance or thing)+' cheeto')
    return wrapper


# okay... so. The decorator approach was not quite right. At least, I don't think so.
# Yeah. I'm curious...

# ---___--- That's literally what we don't want, bruh.
# I guess I maybe get it... but... lol at us for breaking exactly the thing that I was trying to do

# We're literally unwrapping the function, rather than just reading the
# arguments from the function. And it doesn't look like there's a way to tell
# args to shove off, we know what we want.
#
# Thus? Decorator approach is right out. We *have* to require all of the arguments to the function which is disappointing.
# 
# Grumblecakes. Well, let's take this to chat, I think I've seen enough for now lol.
@needs_service_instance
def cool(service_instance):
    return service_instance
