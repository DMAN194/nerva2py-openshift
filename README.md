Running Nervatura on OpenShift
==================

Nervatura OpenShift Python 2.7 Template

This git repository is a Nervatura template to help you get started with using Python 2.7 on Red Hat's OpenShift PaaS.

The template is base on the OpenShift Community Python 2.7 Cartridge (https://github.com/openshift/openshift-community-cartridge-python-2.7) and install the last Nervatura Framework version (https://github.com/nervatura/nerva2py).

Checks it at the time of a startup and installs the latest Nervatura version (optional, default setting).

Install on OpenShift
----------------------------

Create an account at http://openshift.redhat.com/ and install the client tools (run 'rhc setup' first)

Create a Nervatura (scaled) application (you can call your application whatever you want)

    rhc app create nervatura python-2.7 --scaling --from-code=https://github.com/nervatura/nerva2py-openshift

That's it, you can now checkout your application at:

    http://nervatura-$yournamespace.rhcloud.com

Learn more at http://www.nervatura.com.

Database support
----------------------------

Sqlite support: default, separated data directory. The databases in the data directory the auto upgrade does not delete it. More databases can be created.

Postgesql support:

    rhc cartridge add postgresql-9.2 -a nervatura

MySql support:

    rhc cartridge add mysql-5.1 -a nervatura

