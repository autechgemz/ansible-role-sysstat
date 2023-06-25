
def test_system_type(host):
    assert host.system_info.type == "linux"

def test_system_dist(host):
    assert host.system_info.distribution in ["ubuntu", "debian", "redhat", "centos", "rocky", "almalinux"]
    assert host.system_info.arch == 'x86_64' 

def test_ssh_config(host):
    ssh_config = host.file("/etc/default/sysstat")
    assert ssh_config.user == "root"
    assert ssh_config.group == "root" 
    assert ssh_config.mode == 0o644

def test_sshd_config(host):
    sshd_config = host.file("/etc/sysstat/sysstat")
    assert sshd_config.user == "root"
    assert sshd_config.group == "root" 
    assert sshd_config.mode == 0o644

def test_sshd_installed(host):
    sshd = host.package("sysstat")
    assert sshd.is_installed

def test_sshd_running_and_enabled(host):
    sshd = host.service("sysstat")
    assert sshd.is_running
    assert sshd.is_enabled
