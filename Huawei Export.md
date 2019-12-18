## Export message database on Huawei phones
This is a short guide on how to get the Whatsapp message database file from your Huawei phone.
##### 1. Create a backup with the (probably preinstalled) [KoBackup app](https://play.google.com/store/apps/details?id=com.huawei.KoBackup)
The KoBackup application is maybe only accessible via the phone settings. Just use the search function.  
You need to set up a password for the backup.  
Choose a local backup on your external phone storage.
##### 2. Copy the backup to your computer
The backup can be found in a subdirectory of ```/sdcard/Huawei/Backup/``` (probably the most recent one).  
From the backup directory copy the files ```info.xml``` and ```com.whatsapp.tar``` to your computer.
##### 3. Decrypt the backup
Download the python script from [https://github.com/RealityNet/kobackupdec](https://github.com/RealityNet/kobackupdec) and run it with
```console
foo@bar:~$ python kobackupdec.py -vvv password "C:\PathToPreviouslyCopiedFiles" "C:\PathToOutputDir"
```
Use your previously specified password.  
In the output directory go to ```data/data/com.whatsapp/databases```. There you can find your message database ```msgstore.db```.
