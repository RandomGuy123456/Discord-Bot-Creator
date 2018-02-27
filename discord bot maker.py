T = True

print("""
Welcome to My discord Bot Creator By Richard!
To Use, go to "https://discordapp.com/developers/applications/me" and
create a new app. Give it a name and description, then click create app.
Then, scroll down to where it says create a bot user, and click it.
Copy the client ID and token to somewhere as we will be using it later.
Next, Install node.js here: https://nodejs.org/en/     After that,
create a folder for you bot, then shift + right click inside
the folder, and click open command window here. In the command window,
type "npm install --save discord.js" and hit enter, then close the window.
Now you're ready!
""")
print()
print()
print("Add the message and reply, type 0 when done")
f = open("discordbot.js", 'w')
f.write("""
const Discord = require("discord.js");
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.username}!`);
});


""")

while T:
    message = input("What should the bot respond to: ")
    if message == "0":
        T = False
        break
    reply = input("what should the bot reply with: ")
    f.write("""
client.on('message', msg => {
    if (msg.content === '""" + message + """') {
    msg.reply('""" + reply + """');
    }
});

    
    """)
    print()

print()
Id = input("What is the client ID: ")
token = input("What is the token: ")
f.write("client.login('" + token + "');")
f.close()
print("""

Now there should be a file named discordbot.js in the folder this file is located.
Next, Go to this link:""")
print("https://discordapp.com/api/oauth2/authorize?client_id=" + Id + "&scope=bot&permissions=0")
print("""
Put the bot in a chat. Then, Shift + right click the the folder discordbot.js is located and click
"open command window here". Then type in "node discordbot.js" and hit enter.
It should say logged in. Keep the window open and try the bot out for yourself!""")
print()
print()
input("Press enter to close")



