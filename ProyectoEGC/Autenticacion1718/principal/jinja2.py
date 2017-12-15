from __future__ import absolute_import  # Solo si usas python 2

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from jinja2 import Environment 
from jinja2 import PackageLoader
from jinja2 import select_autoescape
from jinja2 import FileSystemLoader



from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('principal', 'plantillas'),
    autoescape=select_autoescape(['html', 'xml'])
)


def ini_jinja2(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env