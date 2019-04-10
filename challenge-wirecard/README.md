# Wirecard Configuration Management Challenge

This role is created to deploy a Tomcat9 web server behind a Nginx reverse proxy. The infrastructure choosen is a Centos7 compute instance on Google Cloud Platform (GCP).

Clone the 'wirecard_challenge' repo from the ansible branch.

`root@ubuntu:~/home/abc# git clone -b ansible https://bitbucket.org/kottapar/wirecard_challenge`

Pre-requisites
--------------
Install Python3 and create a virtual environment to start working.

`python3 -m venv my_env`

Source the newly created environment

`source my_env/bin/activate`

Change the path to 'challenge-wirecard' and install the requirements. This installs Molecule which installs Ansible as a dependency. 

`pip install -r requirements.txt`

GCP pre-requisites
------------------
Register with GCP, create a project and then create a service account (ansible here) with the Compute Admin and Editor roles assigned. 
Generate and download the JSON key for this service account.

Edit the inventory/gce.ini and fill in the details from the JSON key.
Make sure you **DO NOT** store this JSON file in your project dir and commit it. Bitcoin miners are waiting for that :)

Export the below environment variables. They're required by Molecule to spin up an instance for testing the role.

`export GCE_SERVICE_ACCOUNT_EMAIL="ansible@abcproject.iam.gserviceaccount.com" GCE_CREDENTIALS_FILE="~/keys/ansible_gcp.json" GCE_PROJECT_ID="abcproject-236712" ANSIBLE_REMOTE_TMP=/tmp/`

First steps
-----------
We're using the Ansible dynamic inventory to specify the host against which we'll run this role. Go to GCP and provision a Centos7 VM. Make sure you scroll down and enable the 'Allow HTTP' and 'Allow HTTPS' rules. Now run `./inventory/gce.py --list --pretty`

You should see a listing of your GCP instance details.You can also try doing a ping test using Ansible.

`(my_env) root@ubuntu:/challenge-wirecard#  ansible -i inventory/ vm01 -m ping
wirevm01 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}`

Testing the role
----------------
Traverse to the directory `..challenge-wirecard/roles/setup-deploy`. From this path you can run the molecule commands to test the role. Run `molecule test`

Deploying the role
------------------
Once the tests are done we can proceed to deploy our role on the VM in GCP. Traverse to the directory challenge-wirecard and run `ansible-playbook -i inventory/ vm01 webapp-deploy.yml`

Once the deployment is successful, head over to your GCP console -> Compute engine -> VM instances and copy the external ip of the VM. Then in a browser tab navigate to `https://<ip>/hello`

Assumptions/Limitations
-----------------------
It was assumed that this will be a fresh installation. If a new version of the app is to be deployed then the previous one has to be first undeployed manually.

