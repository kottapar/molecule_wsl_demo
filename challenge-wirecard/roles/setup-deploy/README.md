Role Name
=========

This role is created to deploy a Tomcat9 web server behind a Nginx reverse proxy. The infrastructure choosen is a Centos7 compute instance on Google Cloud Platform (GCP).
The three tasks of creating a web server, deploying the app and the setting up of reverse proxy are included as tasks in this role. This is to enable testing of the full stack.
If we have three separate roles, Molecule will spin up a different instance for each and we may not be test the setup as intended. Hence the single role.

Requirements
------------

Ensure the pre-requisites mentioned in the main page are met.

Role Variables
--------------

Tomcat9 is selected as the webserver. Here's a brief of the vars in defaults/main.yml

`java_package       - Pre-requisite package for Tomcat
 tomcat_package_url - The URL from which to download the package
 tomcat_symlink     - A generic directory path which will be linked to the Tomcat installation in /opt`
 
Webapp variables
 
 `war_src  - The location of the war file
  war_dest - The webapps dir of Tomcat to which the war is to be deployed`
  
Nginx and SSL variables

`nginx_confd                   - The default nginx conf.d dir. We'll use this to copy the ssl.conf file
 nginx_ssl_certificate_subject - The subject to use when generating SSL certs
 nginx_ssl_certificate         - The path openssl command will use to save the cert
 nginx_ssl_certificate_key     - The path openssl command will use to save the key`

Testing the role
----------------

We're using Molecule with Testinfra as the verifier to perform unit and integration tests. Run `molecule test` to run create an instance, run our tests on it and then destroy it.

Example Playbook
----------------

The role can be called as below from the main playbook. 

`---
- name: WEB APP DEPLOYMENT
  hosts: all
  roles:
    - role: setup-deploy`
    


License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
