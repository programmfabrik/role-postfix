import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


MAIN_CF = """#
# Ansible managed: Do NOT edit this file manually!
#

## Generic Settings
smtpd_banner = $myhostname ESMTP $mail_name (Ubuntu)
biff = no
readme_directory = no
append_dot_mydomain = no
maximal_queue_lifetime = 1d
bounce_queue_lifetime = 1d
smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination
## SMTP Settings
smtp_sender_dependent_authentication = yes
smtp_sasl_auth_enable = yes
smtp_sasl_mechanism_filter = digest-md5, plain, login
smtp_sasl_security_options = noanonymous
smtp_sasl_password_maps = hash:/etc/postfix/sasl-passwords
# Disable plaintext - always use TLS
smtp_use_tls = yes
smtp_tls_enforce_peername = no
smtp_tls_session_cache_database = btree:${{data_directory}}/smtp_scache
smtp_tls_wrappermode = yes
smtp_tls_security_level = encrypt
smtp_tls_mandatory_ciphers = medium
smtp_tls_mandatory_protocols = !SSLv2, !TLSv1

## Hostname settings
myhostname = {hostname}
myorigin = /etc/mailname
mydestination = {hostname}, {hostname}, localhost.localdomain, localhost
mynetworks = 127.0.0.0/8
inet_interfaces = 127.0.0.1

## Relayhost settings
sender_canonical_maps = hash:/etc/postfix/sender-canonical-maps, regexp:/etc/postfix/sender-canonical-maps-regex
sender_dependent_relayhost_maps = hash:/etc/postfix/relayhost-maps
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases"""


def test_etc_postfix_main_cf(host):
    f = host.file('/etc/postfix/main.cf')

    hostname = host.run('hostname -s').stdout
    assert f.exists
    assert f.content_string == MAIN_CF.format(hostname=hostname)
