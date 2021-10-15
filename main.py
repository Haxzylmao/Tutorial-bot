import discord
from discord.ext import commands
import os
import json



EXTENSIONS = [
    # Remember this extensions variable is a list so put your cogs like this
    'cogs.cog1',
    'cogs.cog2'
]

def load_config(): # Loads config
    with open('config.json') as f:
        return json.load(f)

config = load_config()
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = "." # Your bots prefix
        )

        self.token = config['token']
        self.owner = 'your id' # The id is an integer btw
        self.bot.id = 'bots id' # Same as the owner id
        self.remove_command('help')

        # Here we load cogs

        for extension in EXTENSIONS:
            try:
                self.load_extension(extension)
            except Exception as e: # Returns an error if the bot is unable to load an extension
                print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

        async def on_command_error(self, ctx, error): # Error messages 
            if isinstance(error, commands.NoPrivateMessage):
                await ctx.author.send(f"**{ctx.command.name}** cannot be used in direct messages!")
            elif isinstance(error, commands.CommandInvokeError):
                print(f'In {ctx.command.qualified_name}:', file=sys.stderr)
                traceback.print_tb(error.original.__traceback__)
                print(f'{error.original.__class__.__name__}: {error.original}', file=sys.stderr)

        async def on_ready(self): # On ready stuff
            print('Online! as:')
            print('Username | ' + self.user.name)
            print('ID | ' + self.user.id)


        async def run(self): # Run function
            super().run(self.token)


# Run the bot
if __name__ == '__main__':
    bot = MyBot()
    bot.run()
