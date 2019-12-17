## Whatsapp chat statistics
Little python script to analyze and export your Whatsapp chats from Whatsapps chat database. It creates some beautiful plots and an HTML version of the chat history.  
With the built-in export functionality you can only export the last 10,000 (with images) or 40,000 (without images) messages. Using the database you can analyze your complete chat history.
### 1. Export of your message database:
1. Option: Your phone is rooted. Just copy the file `msgstore.db` from the directory `/data/data/app/com.whatsapp/databases` to your computer.
2. Option: You have a Huawei Phone. In this case follow [this instructions](https://github.com/daandtu/whatsapp-chat-stats/blob/master/Huawei%20Export.md).

There may be other possibilities to get your message database like decrypting the sd-card backup, but they will not be discussed here.
### 2. Creating chat statistics
Download or clone the script and run:
> python whatsapp-stats.py "C:\PathToFile\msgstore.db"

### License
The script is licensed under the GPLv3: [http://www.gnu.org/licenses/gpl-3.0.html](http://www.gnu.org/licenses/gpl-3.0.html).
### Legal
This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This script is an independent and unofficial. Use at your own risk.