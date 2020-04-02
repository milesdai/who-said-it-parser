# 3E Who-Said-It Parser

Parses a .mbox file that contains emails sent to 3E's who-said-it mailing list.

I'm making no guaranatees about the correctness or quality of this code.

## Usage
You'll need to get the .mbox file from Faraz since uploading everyone's emails to Github seems like a bad idea.

Run `python3 main.py > output.txt` to generate a text file with all the emails.

## Notes
* By default, the script filters out 3W's emails
* Replies are filtered out by default since there's no great way of formatting it yet.
* Subject lines require special attention since a fraction of them are encoded either in utf-8 or Windows 1252
* No email contents are included at the moment because it's hard.

## TODO
* Generate PDFs
  * This actually seems to be a bit more complicated than anticipated. The most promising route right now seems be generating HTML or LaTeX and then converting into PDF.
* Parse replies intelligently
* Parse email bodies