# Whatsapp chat statistics
Little python script to analyze and export your Whatsapp chats from the Whatsapps chat database. It creates some beautiful plots, an HTML and a LaTeX version of the chat history.  
Printing HTML files to PDFs can be a problem for large chat histories. With the LaTeX version, you can create a beautiful (printable) PDF version of all your messages (with all emojis). ([see below](#latex))  
With the built-in export functionality you can only export the last 10,000 (with images) or 40,000 (without images) messages. Using the database you can analyze your complete chat history.
### 1. Export of your message database:
1. Option: Your phone is rooted. Just copy the file `msgstore.db` from the directory `/data/data/app/com.whatsapp/databases` to your computer.
2. Option: You have a Huawei Phone. In this case, follow [these instructions](https://github.com/daandtu/whatsapp-chat-stats/blob/master/Huawei%20Export.md).

There may be other possibilities to get your message database like decrypting the sd-card backup, but they will not be discussed here.
### 2. Creating chat statistics
Download or clone the repository and run
```console
foo@bar:~$ python whatsapp-stats.py --phone_number '+49 170 00000000' 'C:\PathToFile\msgstore.db' --mode tex
```
Available `mode`s are `normal` (default, no html or LaTeX generation), `html` (generates html) and `tex` (generates tex). They can also be combined: `html|tex`.

See all available options with
```console
foo@bar:~$ python whatsapp-stats.py --help
```

### <a name="latex"></a>LaTeX version to PDF
With the generated `.tex` file you can create a beautiful PDF version of your chat history which includes all emojis. Printing HTML files to a PDF with a normal computer is only possible for a small number of pages. PDF generation by LaTeX is much more efficient. Follow these steps to create your PDF file:
  1. If not already done: [Download](https://www.latex-project.org/get/) and install a LaTeX distribution (which comes with the `lualatex` package, probably all common distributions do that)
  2. If you want to display your emojis correctly, copy the contents of my coloremoji repository to your tex-output folder (probably `output/tex`).  
  Pay attention, that the directory `coloremoji` and the file `coloremoji.tex` are in the same directory as your `chat.tex`.
  3. Outcomment `\input{coloremoji.tex}` in line 22 of your `chat.tex`.
  4. Navigate a terminal to the directory of your `chat.tex` and run
     ```console
     foo@bar:~$ lualatex chat.tex
     ```
     You probably can use other LaTeX compiler but for me `lualatex` worked the best for non-ASCII characters and very large chat histories.
  
### License
The script is licensed under the GPLv3: [http://www.gnu.org/licenses/gpl-3.0.html](http://www.gnu.org/licenses/gpl-3.0.html).
### Legal
This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This script is an independent and unofficial. Use at your own risk.
