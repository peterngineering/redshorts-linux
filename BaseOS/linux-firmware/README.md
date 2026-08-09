# linux-firmware

* I had a couple problems with linux firmware on the RPIs
  * HUGE to install on a minimal system.
  * The compression and autoloading did not work for me and manual decompression was problematic for brcm/cypress.
 
* My solutions:
  * Broke out the brcm/cypress firmware in the spec to seperate packages based on other inline examples.
  * Disabled compression in the spec

  
