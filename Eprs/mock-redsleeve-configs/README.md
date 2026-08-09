Notes: 

# Using local repo mirrors offline:

Since no container image exists  you need to force mock to fallback to chroot when working with offline repos.
Podman/containers may get in the way if your trying to use a local repo mirror.
    Dns resolution and the latest mock will likely fail with an error such as:
<code>
INFO: Pulling image: false
ERROR: b''
b'Error: short-name resolution enforced but cannot prompt without a TTY\n'
INFO: Pulling image: false
</code>

   _#*For now removing 'podman' will work around this.*#_
