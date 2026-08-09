# linux-firmware

* I had a couple problems with the upstream linux firmware pkg on the RPIs
  * HUGE to install on a minimal system, just to install RPI wireless firmware.
  * The compression and autoloading did not work for me and manual decompression was problematic for brcm/cypress.
 
* My solutions:
  * Broke out the brcm/cypress firmware in the spec to separate packages based on other inline examples.
  * Disabled compression in the spec, so that auto-loading will work auto-magically.

  
