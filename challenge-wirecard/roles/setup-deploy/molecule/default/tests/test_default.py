import os
import requests
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', ['nginx', 'java-1.8.0-openjdk'])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', ['nginx'])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled


def test_files_exists(host):
    conf_files = ['/etc/systemd/system/tomcat.service',
                  '/etc/ssl/certs/server.crt',
                  '/etc/ssl/private/server.key',
                  '/etc/nginx/conf.d/ssl.conf']
    for f in conf_files:
        fl = host.file(f)
        assert fl.exists


def test_http_sock(host):
    for p in ("tcp://0.0.0.0:80", "tcp://0.0.0.0:443"):
        sock = host.socket(p)
        assert sock.is_listening


def test_tomcat_sock(host):
    assert host.socket("tcp://:::8080").is_listening


# The verification of the SSL cert is turned off because
# the cert was created with the IP assigned to the VM
# However I haven't yet figured how to get the ansible_host_ipv4.address
# from the facts imported here. So using the localhost.
def verify_hello():
    url = 'https://127.0.0.1/hello'
    r = requests.get(url, verify=False)
    assert r.status_code == 200
    assert "Hello from Wirecard DevOps Challenge!!" in r.text
