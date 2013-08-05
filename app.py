#!/usr/bin/env python
import imp
import os
import sys

try:
   zvirtenv = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'],
                           'virtenv', 'bin', 'activate_this.py')
   execfile(zvirtenv, dict(__file__ = zvirtenv) )
except IOError:
   pass


def run_gevent_server(app, ip, port=8080):
   from gevent.pywsgi import WSGIServer
   WSGIServer((ip, port), app).serve_forever()


def run_simple_httpd_server(app, ip, port=8080):
   from wsgiref.simple_server import make_server
   make_server(ip, port, app).serve_forever()


#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
# 

version_check = True
version_update = True
release_version_url = 'https://raw.github.com/nervatura/nerva2py/master/applications/nerva2py/VERSION'
release_zip_url = 'https://github.com/nervatura/nerva2py/archive/master.zip'

def get_version(vtype):
   try:
      if vtype=='current':
         version_info = open(os.path.join('wsgi/nerva2py/applications/nerva2py','VERSION'), 'r')
      else:
         from urllib2 import urlopen
         version_info = urlopen(release_version_url)
      version_str = version_info.read().split()[-1].strip()
      version_info.close()
      return version_str
   except Exception, err:
      print str(err)
      return False

def upgrade_version():
   from urllib2 import urlopen
   from zipfile import ZipFile
   from StringIO import StringIO
   import shutil
   try:
      print 'Download last release...'
      url = urlopen(release_zip_url)
      zipfile = ZipFile(StringIO(url.read()))
      print 'Extract file...'
      zipfile.extractall('wsgi')
      if os.path.isdir('wsgi/nerva2py'):
         if os.path.isdir('wsgi/nerva2py_bck'):
            shutil.rmtree('wsgi/nerva2py_bck')
         os.rename('wsgi/nerva2py', 'wsgi/nerva2py_bck')
      os.rename('wsgi/nerva2py-master', 'wsgi/nerva2py')
      if os.path.isfile(os.path.join('wsgi/nerva2py/applications/nerva2py/databases','demo.db')):
         print 'Move DEMO database to the data directory...'
         if not os.path.isdir('data'):
            os.mkdir('data')
         shutil.move(os.path.join('wsgi/nerva2py/applications/nerva2py/databases','demo.db'), 
            os.path.join('data','demo.db'))
      print 'Successful upgrade!'
   except Exception, err:
      print str(err)

#
#  main():
#
if __name__ == '__main__':

   cur_version = get_version('current')
   if cur_version != False:
      print 'Nervatura version: '+cur_version
      if version_check:
         rel_version = get_version('release')
         if rel_version != False:
            if cur_version != rel_version:
               print 'New versions are available: '+rel_version
               if version_update:
                  upgrade_version()
   else:
      upgrade_version()

   ip   = os.environ['OPENSHIFT_PYTHON_IP']
   port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
   zapp = imp.load_source('application', 'wsgi/application')

   #  Use gevent if we have it, otherwise run a simple httpd server.
   print 'Starting WSGIServer on %s:%d ... ' % (ip, port)
   try:
      run_gevent_server(zapp.application, ip, port)
   except:
      print 'gevent probably not installed - using default simple server ...'
      run_simple_httpd_server(zapp.application, ip, port)

