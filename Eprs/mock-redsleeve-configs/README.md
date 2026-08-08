*  working mock versions tested so far:
    *  mock-3.0-1
    *  mock-4.1-1
    *  

  I'm testing with the following option to see the highest version mock possible to use:
 <code>
 config_opts['bootstrap_image'] = 'false'
</code>

*  Once you install mock-red*-configs and its dependency mock-3.0-1*

*  Block other mock versions in /etc/yum.conf with:
    <code>
    Exclude=mock*
    </code>

** I know the lastest Mock releases will NOT work with these redsleeve and redshorts configs I created, so pin to 3.0-1 until 
the configs are reworked to be compatible with the latest.

