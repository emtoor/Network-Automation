# Network-Automation Juniper

This Python script using Paramiko that automates the process of upgrading firmware on a range of Juniper devices. The script prompts the user for a range of IP addresses, the specific Juniper model and firmware version, the SSH username and password, and the firmware file.

The script then loops through the range of IP addresses and for each IP, it connects to the Juniper device using Paramiko and checks the device model and firmware version. If the device model and firmware version match the user-specified values, the script uploads the firmware file to the device using FTP and applies the firmware to the device.

The script outputs the result of each device connection and upgrade process, so the user can see if the upgrade was successful or not.

Also added the ability to reload the device after the upgrade is complete however this is commented out to prevent any loss of connection.
