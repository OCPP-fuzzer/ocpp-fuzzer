Downloaded
Intermediate state. New firmware has been downloaded by Charging Station.
DownloadFailed
Failure end state. Charging Station failed to download firmware.
Downloading
Intermediate state. Firmware is being downloaded.
DownloadScheduled
Intermediate state. Downloading of new firmware has been scheduled.
DownloadPaused
Intermediate state. Downloading has been paused.
Idle
Charging Station is not performing firmware update-related tasks. Status Idle SHALL only be used as in a FirmwareStatusNotificationRequest that was triggered by TriggerMessageRequest.
InstallationFailed
Failure end state. Installation of new firmware has failed.
Installing
Intermediate state. Firmware is being installed.
Installed
Successful end state. New firmware has successfully been installed in Charging Station.
InstallRebooting
Intermediate state. Charging Station is about to reboot to activate new firmware. If sent before installing the firmware, it indicates the Charging Station is about to reboot to start installing new firmware. If sent after installing the new firmware, it indicates the Charging Station has finished installing, but requires a reboot to activate the new firmware, which will be done automatically when idle. This status MAY be omitted if a reboot is an integral part of the installation and cannot be reported separately.
InstallScheduled
Intermediate state. Installation of the downloaded firmware is scheduled to take place on installDateTime given in UpdateFirmware request.
InstallVerificationFailed
Failure end state. Verification of the new firmware (e.g. using a checksum or some other means) has failed and installation will not proceed. (Final failure state)
InvalidSignature
Failure end state. The firmware signature is not valid.
SignatureVerified
Intermediate state. Provide signature successfully verified.