# Santiment-Auto-Cleanup

### Overview
-------------
   As it is known, those running node (readonly) on Santiment were experiencing heavy disk usage and a rapid decrease in free disk space due to this usage.
Finally, the team shared a command line that deleted unnecessary data.
So I wrote a bash command that checks the disk every 6 hours and automatically runs this command when the disk space exceeds 90%. I tested it myself and wanted to share it.

### Features
-------------

- Regularly checks disk usage every 6 hours.
- Starts a Prune operation for the Santiment Node when it exceeds the specified disk usage limit.
- Writes log records to DtractusSanrLog.log file.



### Prerequisites
-------------

- Santiment Node must be installed and running.
- You need to know your disk name. When you use the `df -h` command on your console, you will get an output like the image below. Here our disk name is /dev/sda1. This should learn your disk name and enter it this way when bash asks you.

     ![image](https://github.com/Dtractus/Santiment-Auto-Cleanup/assets/55835876/86ea3c62-788c-4722-8560-ce9f68a6e55f)


### Installation Steps
-------------

1. **Run the installation script using the following command:**

     ```
     source <(curl -s https://raw.githubusercontent.com/Dtractus/Santiment-Auto-Cleanup/main/DtractusAutoPrune.sh)
     ```
   This command installs the necessary dependencies, downloads your Python script, and makes the necessary configurations.
  
2. **During installation, the script will ask you for the following information:**
  
     * **DISK_NAME:** Name of the disk partition (The disk name you got above. For example: /dev/sda1)
     * **MAX_DISK_USAGE_PERCENT:** The percentage at which the cleanup process should be triggered when disk usage exceeds this percentage (For example: 90)

3. **Once the installation is complete, the tool will be automatically configured to run every 6 hours.**


### Log Records

   When the script is run, output and possible error messages are written to the $HOME/DtractusAutoPrune/DtractusSanrLog.log file. This log file can be examined to obtain information about the vehicle's operation and possible problems. You can view your logs with the following command;

```
tail -f $HOME/DtractusAutoPrune/DtractusSanrLog.log
```
