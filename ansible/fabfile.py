from fabric.api import local


def deploy():
    local("ansible-playbook provision.yml -i hosts")
