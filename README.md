Running Nervatura on OpenShift
==================

Nervatura OpenShift Python 2.7 Template

This git repository is a Nervatura template to help you get started with using Python 2.7 on Red Hat's OpenShift PaaS.

The template is based on the OpenShift Community Python 2.7 Cartridge (https://github.com/openshift/openshift-community-cartridge-python-2.7) and installs the last Nervatura Framework version (https://github.com/nervatura/nerva2py).

Then the program at each startup checks whether the installed Nervatura version is the latest one and upgrades it if needed. (optional but set as default).

Install on OpenShift
----------------------------

Create an account at http://openshift.redhat.com/ and install the client tools (run 'rhc setup' first)

Create a Nervatura (scaled) application (you can call your application whatever you want)

    rhc app create nervatura python-2.7 --scaling --from-code=https://github.com/nervatura/nerva2py-openshift

That's it, you can now checkout your application at:

    http://nervatura-$yournamespace.rhcloud.com

Database supports
----------------------------

Sqlite support:

Included by default. Database files are stored in a separate data directory, independently from the application. Upgrade of the application does not affect the content of the database files. Several database files can be created.

Postgesql support:

    rhc cartridge add postgresql-9.2 -a nervatura

MySql support:

    rhc cartridge add mysql-5.1 -a nervatura

Additional description can be found here: http://nervatura.com/nervapage/default/community_setup_openshift
