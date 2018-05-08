from importlib import import_module
import inspect


def get_provider(app):
    views = import_module('allauth.socialaccount.providers.' + app + '.views')
    for name, obj in inspect.getmembers(views):
        if inspect.isclass(obj) \
                and 'Adapter' in name \
                and app.upper() in name.upper():
            return obj

