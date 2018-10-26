# Ansible Role postfix

This role installs and configures a postfix that send but not receives e-mails.

Ofter times, applications or services will want to send out e-mails.
This role will configure any such server to queue mails locally and then
forwarding them to one mail-relay or directly send it to the next hop towards the sender.

This way, applications and services on such a configured instance don't
require any special send/relay/bounce logic and can simply use mail-drop
to reliably send out e-mails.

The variables used by this role should be self-explanatory for anyone
with a Postfix background.

# Example play

```yaml
- hosts: mx-relays
  vars:
    postfix_debconf_mailname: host123.example.com
    postfix_default_sender_email: "server@example.com"
    postfix_default_monitoring_recipient: "monitoring-alerts@exampe.com"
    
    # Set to False to disable or to 'mail@example.com' to receive bounce mails
    postfix_bounce_notice_recipient: False
    
    # Mail relay configuration (optional)
    postfix_relayhost: '[192.168.99.56]:587'

    # Authentication with user:password on mail relay (optional)
    postfix_sasl_auth: 'username:password'
    
    # Rewriting all sender addresses of given domains
    postfix_sender_domains:
      - "{{ inventory_hostname }}"
      - "{{ inventory_hostname_shorts }}"
      - example.com
    
    # Setting aliases
    postfix_aliases:
      # Relay mails to the root use to the default_monitoring_recipient
      - name: root
        target: "{{ postfix_default_monitoring_recipient }}"

  roles:
    - programmfabrik.role-postfix
```

# License

Apache-2.0

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
