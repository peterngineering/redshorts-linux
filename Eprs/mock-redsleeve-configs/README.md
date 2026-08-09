Notes: 

Since no container image exists  you need to force mock to fallback to chroot.

Podman/containers may get in the way if your trying to use a local repo mirror.
    Dns resolution will likely fail with an error such as:

<code>
INFO: Pulling image: false
ERROR: b''
b'Error: short-name resolution enforced but cannot prompt without a TTY\n'
INFO: Pulling image: false
</code>

    For now removing 'podman' will work around this.
