import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

RELAYHOST_MAP = """#
# Ansible managed: Do NOT edit this file manually!
#

server@example.com [smtp.gmail.com]:587"""


def test_relayhost_maps(host):
    f = host.file('/etc/postfix/relayhost-maps')
    db = host.file('/etc/postfix/relayhost-maps.db')

    assert f.exists
    assert db.exists

    assert f.content_string == RELAYHOST_MAP
