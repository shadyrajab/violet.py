import discord
from discord.ext import commands
import traceback
from utils import Config
from translates import ErrorMessages, user_not_found

class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        messages = ErrorMessages(language=Config(ctx.guild).language)
        if isinstance(error, commands.NoPrivateMessage):
            help = self.client.get_command('help')
            return await ctx.invoke(help, (str(ctx.command))) 
        if isinstance(error, commands.MissingRequiredArgument):
            help = self.client.get_command('help')
            return await ctx.invoke(help, (str(ctx.command)))
        if isinstance(error, commands.MissingPermissions):
            return await ctx.message.reply(messages.not_permissions(error.missing_perms[0]))
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.BadUnionArgument):
            if str(error) == 'Could not convert "member" into Member or int.':
                return await ctx.message.reply(user_not_found(Config(ctx.guild).language))
        if isinstance(error, commands.CommandInvokeError):
            if str(ctx.command) == 'clear':
                if isinstance(error.original, ValueError):
                    return await ctx.message.reply(messages.invalid_argument) 
            if str(ctx.command) == 'trename':
                if isinstance(error.original, discord.HTTPException):
                    return await ctx.message.reply(messages.rate_limit)
            if str(error) == 'Command raised an exception: TimeoutError: ':
                return
            if str(error.original) == '404 Not Found (error code: 10013): Unknown User':
                return await ctx.message.reply(user_not_found(Config(ctx.guild).language))
        if isinstance(error, commands.BotMissingPermissions):
            return await ctx.message.reply(messages.bot_not_permissions(error.missing_perms[0]))
        tb = traceback.format_tb(error.original.__traceback__)
        cloud = self.client.get_guild(836748124139552788)
        channel = cloud.get_channel(836915657865691186)
        await channel.send(''.join(tb))
        await channel.send(f'**Error in command: {ctx.command}**;\n**type:** ``{type(error)}`` **/** ``{type(error.original)}``\n**error:** {error}\n**error.original: **{error.original}')
        await channel.send('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


def setup(client):
    client.add_cog(Errors(client))