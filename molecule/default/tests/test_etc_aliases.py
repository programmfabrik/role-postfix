import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_etc_aliases(host):
    f = host.file('/etc/aliases')

    assert f.exists
    assert f.contains("root: monitoring-alerts@exampe.com")