# Ansible Role: sysstat

## Description

Manage System performance tools.

## Requirements

None

## Dependencies

None

## OS Platforms

- RHEL-7/CentOS-7 or higher
- Ubuntu-20.04 or higher

## Example Playbook

```
- hosts: all
  roles:
    - sysstat
```

## Role Variables

### sysstat_package_ensure: (string)

```
sysstat_package_ensure: 'present'
```

### sysstat_service_ensure: (string)

```
sysstat_service_ensure: 'started'
```

### sysstat_service_enable: (bool)

```
sysstat_service_enable: true
```

### sysstat_config_options: (dict)

```
sysstat_config_options: {}
```

### sysstat_daemon_config_options: {}

```
sysstat_daemon_config_options: {}
```

### sysstat_config_crondata: (list or Literal Style)

```
sysstat_config_crondata: [] or |
```

## Example vars

```
sysstat_daemon_config_options:
  ENABLED: "true"
sysstat_config_options:
  HISTORY: 31
  COMPRESSAFTER: 10
  SADC_OPTIONS: "-S DISK"
  SA_DIR: /var/log/sysstat
  ZIP: "xz"
  DELAY_RANGE: 0
  UMASK: "0022"
sysstat_config_crondata: |
  PATH=/usr/lib/sysstat:/usr/sbin:/usr/sbin:/usr/bin:/sbin:/bin
  */1 * * * * root /usr/lib/sysstat/sa1 1 60
```
