# DarazBot
A simple but scalable script which takes the URLs and names of your favorite items from Daraz.pk and notifies you about price drops.
You have to input name, url and price threshold of the item in Input.csv file and the script takes it from there. The name of item is just for identification purposes, you can give nicknames or numbers if you want. If price drops below or equal to your threshold value, you will be notified via email.
The script also updates the current price in Input.csv file. 
You can enter as many items as you want, however the run time will increase as the script iterates for each item.
The idea is to schedule the script atleast once a day so price drops/sales are not missed.
For email, Gmail is used. You will have to turn on login for less secure apps (go to https://myaccount.google.com/lesssecureapps), as the script will attempt to login to gmail and will be blocked unless that option is turned on.
Happy shopping!
