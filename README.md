This is a very simple Discord bot written off of very basic fundamentals found in the discord.py project.


However, through trying to develop something else, I found something quite strange would occur if a user were to be kicked upon joining the server.


This works and hinges on the target server/guild that the bot is connected to has default join messages enabled, and is designed to work alone in a server with administrative privilages.

An invite link is to be generated and sent to someone who you're either in a call with, or who is in a call.

Upon the person clicking said invite link, they will be disconnected from the call following being disconnected from the server.


More specifically, you're disconnected from the voice server, for some strange reason.


To set up the bot:
* Head to the Discord Developer portal found at the [Discord Developer Portal](https://discord.com/developers/applications)
  * Go to Applications -> New Application
  * Provide a simple name
  After creating the application, go to:
    * Bot -> Add Bot (and of course get the token of the bot, which would be used in `--token <token>`)
    and proceed to provide the bot with Administrator privilages.
    
  Following this, head to the OAuth2 tab, and make your respective link with the parameter for permissions being set to 8 (within the Link).
  Then, you can invite the newly created bot via the OAuth link to an empty and newly created server of your own in where you have the ability to invite bots to, and of course, as well,
  create an invite link that will be used as the sort of "Goodbye button" for people in calls, that you would send to them.
  
  
 Next, you would of course have to initialize the bot via the syntax seen below:
 ```  
 -userid <USERID>  The Snowflake ID of the person who you would like to disconnect.
  -all            Do this to everyone, in where if anyone clicks the Invite link, they are disconnected from active call.
  -token <TOKEN>    Token of bot as found in the Discord Developer Portal```
