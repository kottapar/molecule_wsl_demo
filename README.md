# Ansible role testing with Molecule and Vagrant using WSL

This role is created to deploy a Tomcat9 web server behind a Nginx reverse proxy. The infrastructure choosen is a Centos7 instance on Vagrant.

[Molecule](https://molecule.readthedocs.io/en/stable/index.html) will be used to test the role against a Vagrant VM.

Getting started
---------------
Clone the repo to get started

`git clone https://github.com/kottapar/molecule_wsl_demo.git`

In order to run the tests on our role we'll install Molecule and Ansible in a Python virtualenv. Login to your VM and complete the below steps.

Install Python3, python3-dev and python3-venv using your package manager and create a virtual environment.

`python3 -m venv my_env`

Source the newly created environment

`source my_env/bin/activate`

Use pip to install the requirements. This installs Molecule which installs Ansible as a dependency.

`pip install -r requirements.txt`

---

PREREQUISITES
-------------
If you're on a Linux VM and would like to test the role locally, ensure that your hypervisor supports nested virtualization.

If you are using Virtualbox, note that nested virtualization is not supported for Intel chipsets yet.

If you're on Windows 10, then install the Windows subsystem for Linux (WSL) from the [Microsoft store](https://www.microsoft.com/store/productId/9N9TNGVNDL3Q).

Vagrant prerequisites
---------------------
1.  If your VM supports nested virtualization then:
    * Install [Virtualbox](https://www.virtualbox.org/wiki/Linux_Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html) 
    
2.  However if your VM can't spin up Vagrant VMs on Virtualbox, then WSL is the way forward:
    * Install the Windows subsystem for Linux (WSL) from the [Microsoft store](https://www.microsoft.com/store/productId/9N9TNGVNDL3Q).
    * Install [Vagrant](https://www.vagrantup.com/downloads.html) in WSL. 
    * Install [Virtualbox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/downloads.html) on your Windows 10 machine.
        *  **NOTE**: Make sure you install the same version of Vagrant in WSL and the Windows machine
    * Execute `pip3 install python-vagrant` to install the python module for Vagrant if it's not already installed.
    * Execute `export VAGRANT_WSL_ENABLE_WINDOWS_ACCESS="1"` to enable WSL to use the Virtualbox from the Windows system.
    * Execute `export PATH="$PATH:/mnt/c/Program Files/Oracle/VirtualBox:/mnt/c/Windows/System32:/mnt/c/Windows/system32/WindowsPowerShell/v1.0"` to provide the paths to the Virtualbox, cmd and powershell executables.
    * For more info refer to the Vagrant WSL documentation [here](https://www.vagrantup.com/docs/other/wsl.html)

---

Testing the role
----------------
Scenarios
---------
Molecule uses [Scenarios](https://molecule.readthedocs.io/en/stable/getting-started.html#molecule-scenarios) to test the role against the Infra we define. We currently have two scenarios defined.

1.  default 
    * This scenario can be used if you'd like to test the role locally by spinning up a Vagrant VM in Virtualbox.
    * If you'd like to use this, then complete the `Vagrant pre-requisites`.

Vagrant
-------
Traverse to the directory `/roles/setup-deploy`. From this path you can run the molecule commands to test the role.

Ensure that `VAGRANT_WSL_ENABLE_WINDOWS_ACCESS="1"` and PATH variables are exported. If not export them.

Run `molecule test --destroy never` to test the role. The `--destroy never` ensures that the Vagrant VM is not removed once the tests are completed.

