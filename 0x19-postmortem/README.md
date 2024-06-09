# 0x19. Postmortem

!["meme image"](https://i.pinimg.com/564x/ac/46/d4/ac46d4eb2d4430e982e5797b7e1ac868.jpg)

- 0. My first postmortem:

# Puppet Manifest Error - WordPress Configuration Change
## Incident Summary:
On 05 June at 10:00 PM, a Puppet manifest error resulted in a configuration change affecting WordPress installations managed by the Puppet infrastructure. This caused errors in the wp-settings.php file potentially impacting website functionality.
## Timeline:
- 09:30 PM: Puppet manifest error triggers configuration change.
- 10:00 PM: Users report issues with WordPress installations.
- 08:45 AM: Identified the Puppet manifest error as the root cause.
- 10:00 AM: Reverted the faulty configuration change.
- 12:00 PM: System recovers and WordPress installations function normally.
## Root Cause:
A Puppet manifest containing an error was applied to the infrastructure. This error likely involved an incorrect path specification for the wp-settings.php file or a faulty modification attempt within the file itself.
## Resolution and Recovery:
I identified and reverted the erroneous manifest, restoring the original configuration for the WordPress installations. This process took approximately 5 hours to complete.
## Corrective and Preventative Measures:
- The Puppet manifest responsible for the error will be reviewed and corrected.
- I will implement additional testing procedures to ensure future Puppet manifests do not introduce similar errors.
- I will strengthen my code review process to identify potential issues before deployment.
