import discord
import asyncio
import requests
import json
import random
client = discord.Client()

#with open('lastchannel') as f:
#    lastchannel = f.read()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #await client.send_message(lastchannel, 'Xenu is up and running! Commands begin with the prefix ! (but don\t be surprised if Xenu answers by himself)')

""" EXAMPLE CODE
counter = 0
tmp = await client.send_message(message.channel, 'Calculating messages...')
async for log in client.logs_from(message.channel, limit=100):
    if log.author == message.author:
        counter += 1

await client.edit_message(tmp, 'You have {} messages.'.format(counter))
"""
insultList = [
    ', your face reminds me of a nasty little Pumpkin.',
    ', your face causes me distress.',
    ', is your ass jealous of the amount of shit that just came out of your mouth?',
    ', I could eat a bowl of alphabet soup and shit out a smarter statement than that.',
    ', a guy with your IQ should have a low voice too!',
    ', after meeting you, I\'ve decided I am in favor of abortion in cases of incest.',
    ', learn from your parents\' mistakes - use birth control!',
    ', calling you stupid would be an insult to stupid people.',
    ', can I borrow your face for a few days while my ass is on vacation?',
    ', did your parents ever ask you to run away from home?',
    ', ever wondered what your life would be like if you\'d had enough oxygen at birth?',
    ', don\'t feel bad, a lot of people have no talent whatsoever!',
    ', don\'t let your mind wander. It\'s too little to go out alone.',
    ', have you ever felt a feeling of emptyness... In your skull?',
    ', everyone has the right to be ugly, but you have abused the privilege.',
    ', please grasp your ears firmly and remove your head from your ass.',
    ', If you\'re gonna be a smartass, first you have to be smart. Otherwise you\'re just an ass.',
    ', You\'re so ugly, when you popped out the doctor said \"Aww what a treasure\" and your mom said \"Yeah, lets bury it.\"',
    ', Somewhere out there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology.',
    ', You\'re so ugly you scare the shit back into people.',
    ', Why don\'t you slip into something more comfortable -- like a coma.',
    ', You\'re the reason the gene pool needs a lifeguard.',
    ', Why don\'t you check eBay and see if they have a life for sale.',
    ', You didn\'t fall out of the stupid tree. You were dragged through dumbass forest.',
    ', I\'d like to see things from your point of view but I can\'t seem to get my head that far up my ass.',
    ', If laughter is the best medicine, your face must be curing the world.',
    ', I wasn\'t programmed with enough middle fingers to let you know how I feel about you. \n凸 (｀0´)凸',
    ', You’re not the dumbest person on the planet, but you sure better hope he doesn’t die.',
    ', You have more dick in your personality than you do in your pants.',
    ', You look like your father would be disappointed in you if he stayed.',
    ', You’re not pretty enough to be that dumb.',
    ', I’m sorry your dad beat you instead of cancer.',
    ', You couldn’t organize a blowjob if you were in a Nevada brothel with a pocket full of hundred-dollar bills.',
    ', You\'re the reason God left us.',
    ', I’d love to stay and chat but I’d rather have diabetes.',
    ', You should put a condom on your head, because if you’re going to act like a dick you better dress like one, too.',
    ', May your balls turn square and fester at the corners.',
    ', I hope your wife brings a date to your funeral.',
    ', If you were a potato you’d be a stupid potato.',
    ', People like you just need a high-five. In the face. With a chair.',
    ', Ready to fail like your dad’s condom?',
    ', I’d call you a cunt, but you have neither the warmth or the depth.',
    ', There may have been a single intelligent thought in your head, but it would have died from loneliness long ago.',
    ', I don’t have the time or the crayons to explain this to you.',
    ', The only difference between you and Hitler is Hitler knew when to kill himself.',
    ', The smartest thing that ever came out of *your* mouth was a dick.',
    ', You don\'t suck at everything! I mean, you can\'t suck your own dick.',
    ', No matter how hard you try, you\'ll never be half the man your mother is.',
    ', If you were on fire and I had a cup of my own piss, I’d drink it.',
    ', You\'re more inbred than a sandwich.'
]
insultPrefix = [
    'Hey ',
    'Yo ',
    'Whattup '
]
messageIndex = {
    'rickroll': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    'xcq': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    'it\'s time to stop': 'https://www.youtube.com/watch?v=2k0SmqbBIpQ',
    'stop': 'https://www.youtube.com/watch?v=2k0SmqbBIpQ'
}

containsMessageIndex = {
    # Returns the corresponding text if it contains the keyword unless it interferes with the pMI or mI
    'determination' : 'Knowing the mouse might one day leave its hole and get the cheese... It fills you with determination.',
    'china' : 'https://www.youtube.com/watch?v=RDrfE9I8_hs',
    'tunak' : 'https://www.youtube.com/watch?v=vTIIMJ9tUc8',
    'tokyo' : 'https://www.youtube.com/watch?v=XxK54P_4PiA',
    'ghoul' : 'https://www.youtube.com/watch?v=XxK54P_4PiA',
    'nye' : 'https://www.youtube.com/watch?v=26OE9Bq-lr8',
    'yas' : 'https://www.youtube.com/watch?v=26OE9Bq-lr8',
    'taco' : 'https://www.youtube.com/watch?v=vZkjRVjge0g',
    'taco bell' : 'https://www.youtube.com/watch?v=vZkjRVjge0g',
    'senpai' : 'NOTICE ME SENPAI!!!! \nhttp://vignette4.wikia.nocookie.net/yandere-simulator/images/e/ea/Senpai_Sep18.png/revision/latest?cb=20150920021049',
    'jurassic' : 'https://www.youtube.com/watch?v=-w-58hQ9dLk',
    'my point' : 'https://www.youtube.com/watch?v=WOOw2yWMSfk',
    'shrek' : 'https://www.youtube.com/watch?v=cevWfNbRVpo',
    'america' : 'America is dead. All hail Rumpland.',
    'rump' : 'FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK https://www.youtube.com/watch?v=AtbMnixO2nc FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK RUMP'
}

@client.event
async def on_message(message):
    msg = message.content
    author = message.author
    channel = message.channel
    server = message.server
    #print('Xenu received message: "' + msg + '", said by user ' + str(author) + ' on channel ' + str(channel) + ' of server ' + str(server))
    if msg.startswith('!xenu'):
        await client.send_message(channel, 'Yes?')
    elif msg.startswith('!xkcd'):
        # Store the number/other content after the '!xkcd '.
        comic = msg[5:]
        # If the user included a specific comic number in their message, get the JSON data for that comic. Otherwise, get the JSON data for the most recent comic.
        r = requests.get('http://xkcd.com/' + comic + '/info.0.json' if comic else 'http://xkcd.com/info.0.json')
        # Send the URL of the image from the JSON fetched above.
        # The title text is half of the comic
        await client.send_message(channel, r.json()['img']+ '\n' + (r.json()['alt']))
    elif msg.startswith('!help') or msg.startswith('!about'):
        await client.send_message(channel, 'Xenu was the dictator of the Galactic Confederacy, who 75 million years ago brought billions of his people to Earth (then known as "Teegeeack") in DC-8-like spacecraft, stacked them around volcanoes, and killed them with hydrogen bombs. Bot is currently running as ' + client.user.name + ' (ID ' + client.user.id + '). View on GitHub: https://github.com/aderhall/xenu')
        await client.send_message(channel, 'Discuss Xenu at the Galactic Confederacy: https://discord.gg/aBT8hRT')
    elif msg.startswith('!invite'):
        await client.send_message(channel, 'Invite Xenu to your server with this link: https://discordapp.com/oauth2/authorize?client_id=' + str(client.user.id) + '&scope=bot&permissions=0\nNote: you must have *manage server* permissions on the server to add bots.')
    elif msg.startswith('!abuse'):
        if len(message.mentions) > 0:
            # Try to get the mention string
            name = msg[7:]
            await client.send_message(channel, random.choice(insultPrefix) + name + random.choice(insultList))
        else:
            await client.send_message(channel, 'No user specified')
    else:
        if msg in messageIndex:
            await client.send_message(message.channel, messageIndex[msg])
        else:
            for key, value in containsMessageIndex.items():
                if key in msg:
                    await client.send_message(message.channel, value)


@client.event
# Respond on a new member joining
async def on_member_join(member):
    await client.send_message(member.server.default_channel, '**Welcome ' + member.mention + ' to the ' + member.server.name + ' server! All Hail XENU**')

# Respond on member leaving
@client.event
async def on_member_remove(member):
    await client.send_message(member.server.default_channel, '**' + member.name + '\'s soul was captured and sucked into a vacuum zone. :frowning: Fuck **' + member.name)


with open('token.txt', 'r') as token_file:
    # Parse into a string, and get rid of trailing newlines
    token = token_file.read().replace('\n', '')
# It is only fair that whoever is running the bot should know their own token
print('Starting with token ' + token + '...')

# Start bot!
client.run(token)
