import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_git_installed(host):
    package = host.package("git")

    assert package.is_installed


def test_git_lfs_installed(host):
    package = host.package("git-lfs")

    print(package)
    assert package.is_installed
