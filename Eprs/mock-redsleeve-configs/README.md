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


# Forcing redsleeve armv6hl platform to build for armv7hl:
--forcearch target does not seem to work in the latest mock releases unless you adjust your platform/dnf var

To fudge it for armv7hl adjust your triplet to armv7hl in :
      /etc/rpm/platform
 and adjust your dnf var to armv7hl at:
     /etc/dnf/vars/arch

*since gcc's built in triple will use it's default cflags, change it back when your done.
*Note leaving the adjustmetns in place  will allow you to install higher level target packages such as those built for armv7hl, which may or may not work properly in all cases. YMMV




