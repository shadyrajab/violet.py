def changeprefix(language, prefix):
    if language == 'portuguese':
        return f'Prefixo alterado para `{prefix}` com sucesso'
    if language == 'spanish':
        pass
    return f'Prefix changed to `{prefix}` succesfully'

def prefix_limit(language):
    if language == 'portuguese':
        return 'O prefixo não pode ultrapassar `3` caractéres.'
    if language == 'spanish':
        pass
    return "The prefix can't exceed 3 characters"

def clear(ctx, language, messages):
    if language == 'portuguese':
        return f'> Chat limpo por {ctx.author.mention}. Foram deletadas `{messages}` mensagens.'
    if language == 'spanish':
        pass
    return f'> Chat cleared by {ctx.author.mention}. `{messages}` messages was deleted.'

def lock(ctx, language, channel):
    if language == 'portuguese':
        return f'Canal {channel.mention} trancado por {ctx.author.mention}. Use `unlock` para destrancar.'
    if language == 'spanish':
        pass
    return f'Channel {channel.mention} locked by {ctx.author.mention}. Use `unlock` to unlock.'

def unlock(ctx, language, channel):
    if language == 'portuguese':
        return f'Canal {channel.mention} destrancado por {ctx.author.mention}.'
    if language == 'spanish':
        pass
    return f'Channel {channel.mention} unlocked by {ctx.author.mention}.'

def higher(language):
    if language == 'portuguese':
        return 'Você não pode punir um membro superior à você!'
    if language == 'spanish':
        pass
    return "You can't punish a member higher than you!"

def user_not_found(language):
    if language == 'portuguese':
        return 'Não consegui encontrar este usuário.'
    if language == 'spanish':
        pass
    return "I couldn't find this user"

def guild_not_found(language):
    if language == 'portuguese':
        return 'Não consegui encontrar este servidor ou o ID do servidor não foi informado!'
    if language == 'spanish':
        pass
    return "I couldn't find this server or the server ID was not informed"

def user_or_role_not_found(language):
    if language == 'portuguese':
        return 'Não consegui encontrar o usuário ou cargo '
    if language == 'spanish':
        pass
    return "I couldn't find the user or role "

def how_long(language):
    if language == 'portuguese':
        return 'Daqui quanto tempo você quer receber o lembrete? Exemplo: `1d`, `8h`, `12d 5m`, `8h 20s`...'
    if language == 'spanish':
        pass
    return 'How long do you want to receive the reminder? Example: `1d`,` 8h`, `12d 5m`,` 8h 20s` ...'

def noted(language, time):
    if language == 'portuguese':
        return f'Anotado! Daqui `{time[0]}` eu irei te lembrar!'
    if language == 'spanish':
        pass
    return f'Noted! I will remind you in {time[0]}'

class Info():
    def __init__(self, language):
        self.language = language
    
    @property
    def owner(self):
        if self.language == 'portuguese':
            return '👑 Dono:'
        if self.language == 'spanish':
            pass
        return '👑 Owner:'
    
    @property
    def creation_date(self):
        if self.language == 'portuguese':
            return '📅 Criado em:'
        if self.language == 'spanish':
            pass
        return '📅 Created in:'
    
    @property
    def join_date(self):
        if self.language == 'portuguese':
            return '🔔 Entrei aqui em:'
        if self.language == 'spanish':
            pass
        return '🔔 Join here in:'

    @property
    def region(self):
        if self.language == 'portuguese':
            return '🌎 Região:'
        if self.language == 'spanish':
            pass
        return '🌎 Region:'

    @property
    def members(self):
        if self.language == 'portuguese':
            return '👥 Membros:'
        if self.language == 'spanish':
            pass
        return '👥 Members:'

    @property
    def main_role(self):
        if self.language == 'portuguese':
            return '💫 Cargo principal:'
        if self.language == 'spanish':
            pass
        return '💫 Main role:'
    
    @property
    def secondary_roles(self):
        if self.language == 'portuguese':
            return '📜 Cargos secundários:'
        if self.language == 'spanish':
            pass
        return '📜 Secondary roles:'

    @property
    def booster_since(self):
        if self.language == 'portuguese':
            return 'Booster desde:'
        if self.language == 'spanish':
            pass
        return 'Booster since:'

class BanMessages():
    def __init__(self, language, ctx, member, reason):
        self.language = language
        self.ctx = ctx 
        self.member = member
        self.reason = reason

    @property
    def banned_from(self):
        if self.language == 'portuguese':
            return f'Você foi banido(a) do servidor {self.ctx.guild.name}'
        if self.language == 'spanish':
            pass
        return f'You are banned from the server {self.ctx.guild.name}'
    
    @property
    def banned_by(self):
        if self.language == 'portuguese':
            return '📌 Banido por'
        if self.language == 'spanish':
            pass
        return f'📌 Banned by'

    @property
    def reason_(self):
        if self.language == 'portuguese':
            return '📄 Motivo'
        if self.language == 'spanish':
            pass
        return f'📄 Reason'

    @property
    def ban_herself(self):
        if self.language == 'portuguese':
            return 'Por que quer se banir do servidor? Está triste? Solitário? Desanimado? Eu te entendo... 😔 Não sou boa em dar conselhos, mas prometo te ouvir caso queira desabafar comigo no privado...'
        if self.language == 'spanish':
            pass
        return "Why do you want to ban yourself from the server? Are you sad? Lonely? Sad? I understand you... 😔 I'm not good at giving advice, but I promise to listen to you if you want to get something off your chest..."
    
    @property
    def please(self):
        if self.language == 'portuguese':
            return 'Não me bane por favor 😥😥'
        if self.language == 'spanish':
            pass
        return "Don't ban me please 😥😥"

    @property
    def higher_role(self):
        if self.language == 'portuguese':
            return 'Não posso banir este usuário pois seu cargo é mais alto que o meu. Suba-o na lista de cargos para que eu possa puní-lo.'
        if self.language == 'spanish':
            pass
        return "I can't ban this user because his role is higher than my. Up her in the role list to I can punish him."

    @property
    def ban_message(self):
        if self.language == 'portuguese':
            return f"""> Você está prestes a banir {self.member.mention}. Caso tenha certeza disso, clique em ✅.
            > Caso queira baní-lo temporariamente, clique em ⏰;
            > Quer punir sem enviar uma mensagem pro usuário? Clique em 📌 antes de confirmar a punição."""
        if self.language == 'spanish':
            pass
        return f'''> You are about to ban {self.member.mention}. If you are sure, click on ✅;
        > If you want to ban him temporarily, click on ⏰;
        > Want to punish without notifying the user? Click on 📌 before confirming the punishment.'''

    @property
    def temp_ban(self):
        if self.language == 'portuguese':
            return '> Por quanto tempo deseja baní-lo? Exemplo: `1d`, `8h`, `12d 5m`, `8h 20s`...'
        if self.language == 'spanish':
            pass
        return '> How long time do you want to ban him? Example: `1d`, `8h`, `12d 5m`, `8h 20s`...'

    @property
    def time(self):
        if self.language == 'portuguese':
            return '⏰ Duração', 'Permanente'
        if self.language == 'spanish':
            pass
        return '⏰ Time', 'Permanent'

    def tban_announce(self, time):
        if self.language == 'portuguese':
            return f'{self.member.mention} foi temporariamente banido do servidor por {self.ctx.author.mention}! Duração: `{time[0]}`'
        if self.language == 'spanish':
            pass
        return f'{self.member.mention} was temporarily banned from the server by {self.ctx.author.mention}! Time: `{time[0]}`'

    def tban_log(self, time):
        if self.language == 'portuguese':
            return f'Banido por {self.ctx.author} | Duração: {time[0]} | Motivo: {self.reason}'
        if self.language == 'spanish':
            pass
        return f'Banned by {self.ctx.author} | Time: {time[0]} | Reason: {self.reason}'
    
    @property 
    def ban_announce(self):
        if self.language == 'portuguese':
            return f'{self.member.mention} foi permanentemente banido do servidor por {self.ctx.author.mention}'
        if self.language == 'spanish':
            pass
        return f'{self.member.mention} was permanently banned from the server by {self.ctx.author.mention}'

    @property
    def ban_log(self):
        if self.language == 'portuguese':
            return f'Banido por {self.ctx.author} | Duração: Permanente | Motivo: {self.reason}'
        if self.language == 'spanish':
            pass
        return f'Banned by {self.ctx.author} | Time: Permanently | Reason: {self.reason}'

class MuteMessages():
    def __init__(self, language, ctx, member, reason=None):
        self.language = language
        self.ctx = ctx
        self.member = member
        self.reason = reason

    @property
    def muted_from(self):
        if self.language == 'portuguese':
            return f'Você foi mutado(a) do servidor {self.ctx.guild.name}'
        if self.language == 'spanish':
            pass
        return f'You are muted from the server {self.ctx.guild.name}'

    @property
    def muted_by(self):
        if self.language == 'portuguese':
            return '📌 Mutado por'
        if self.language == 'spanish':
            pass
        return f'📌 Muted by'

    @property
    def reason_(self):
        if self.language == 'portuguese':
            return '📄 Motivo'
        if self.language == 'spanish':
            pass
        return f'📄 Reason'

    @property
    def mute_herself(self):
        if self.language == 'portuguese':
            return 'Não é mais fácil apenas ficar calado?'
        if self.language == 'spanish':
            pass
        return "Isn't it easier to be silent?"
    
    @property
    def please(self):
        if self.language == 'portuguese':
            return 'Como que eu vou responder seus pedidos estando mutada?'
        if self.language == 'spanish':
            pass
        return 'How am I going to respond to your requests while muted?'
    
    @property
    def muted(self):
        if self.language == 'portuguese':
            return 'Este usuário já está mutado!'
        if self.language == 'spanish':
            pass
        return 'This user is already muted!'

    @property
    def higher_role(self):
        if self.language == 'portuguese':
            return 'Não posso mutar este usuário pois seu cargo é mais alto que o meu. Suba-o na lista de cargos para que eu possa puní-lo.'
        if self.language == 'spanish':
            pass
        return "I can't mute this user because his role is higher than my. Up it in the role list to I can punish him."

    @property
    def mute_message(self):
        if self.language == 'portuguese':
            return f'''> Você está prestes a mutar {self.member.mention}, se tiver certeza disso clique em ✅;
            > Caso queira mutá-lo temporariamente clique em ⏰;
            > Quer punir sem que o bot envie uma mensagem na dm do usuário? Reaja com 📌 antes de confirmar a punição.'''
        if self.language == 'spanish':
            pass
        return f'''> You are about to mute {self.member.mention}, if you are sure, click on ✅;
        > If you want to mute him temporarily, click on ⏰;
        > Want to punish without notifying the user? Click on 📌 before confirming the punishment.'''

    @property
    def temp_mute(self):
        if self.language == 'portuguese':
            return '> Por quanto tempo deseja mutá-lo? Exemplo: `1d`, `8h`, `12d 5m`, `8h 20s`...'
        if self.language == 'spanish':
            pass
        return '> How long time do you want to mute him? Example: `1d`, `8h`, `12d 5m`, `8h 20s`...'
    
    @property
    def time(self):
        if self.language == 'portuguese':
            return '⏰ Duração', 'Permanente'
        if self.language == 'spanish':
            pass
        return '⏰ Time', 'Permanent'

    def tmute_announce(self, time):
        if self.language == 'portuguese':
            return f'{self.member.mention} foi temporariamente mutado do servidor por {self.ctx.author.mention}! Duração: `{time[0]}`'
        if self.language == 'spanish':
            pass
        return f'{self.member.mention} was temporarily muted from the server by {self.ctx.author.mention}! Time `{time[0]}`'
    
    def tmute_log(self, time):
        if self.language == 'portuguese':
            return f'Mutado por {self.ctx.author} | Duração: {time[0]} | Motivo: {self.reason}'
        if self.language == 'spanish':
            pass
        return f'Muted by {self.ctx.author} | Time: {time[0]} | Reason: {self.reason}'
    
    @property
    def mute_annouce(self):
        if self.language == 'portuguese':
            return f'{self.member.mention} foi permanentemente mutado do servidor por {self.ctx.author.mention}'
        if self.language == 'spanish':
            pass
        return f'{self.member.mention} was permanently muted from the server by {self.ctx.author.mention}'

    @property
    def mute_log(self):
        if self.language == 'portuguese':
            return f'Mutado por {self.ctx.author} | Duração: Permanente | Motivo: {self.reason}'
        if self.language == 'spanish':
            pass
        return f'Muted by {self.ctx.author} | Time: Permanently | Reason: {self.reason}'
    
    @property
    def unmuted(self):
        if self.language == 'portuguese':
            return f'> {self.member.mention} foi desmutado por {self.ctx.author.mention}.'
        if self.language == 'spanish':
            pass
        return f'> {self.member.mention} was unmuted by {self.ctx.author.mention}.'

    @property
    def not_muted(self):
        if self.language == 'portuguese':
            return 'Esse usuário não está mutado!'
        if self.language == 'spanish':
            pass
        return 'This user is not muted!'

class KickMessages():
    def __init__(self, language, ctx, member, reason):
        self.language = language
        self.ctx = ctx
        self.member = member
        self.reason = reason

    @property
    def kicked_from(self):
        if self.language == 'portuguese':
            return f'Você foi expulso(a) do servidor {self.ctx.guild.name}'
        if self.language == 'spanish':
            pass
        return f'You are kicked from the server {self.ctx.guild.name}'
    
    @property
    def kicked_by(self):
        if self.language == 'portuguese':
            return '📌 Expulso por'
        if self.language == 'spanish':
            pass
        return '📌 Kicked by'

    @property
    def reason_(self):
        if self.language == 'portuguese':
            return '📄 Motivo'
        if self.language == 'spanish':
            pass
        return '📄 Reason'

    @property
    def kick_herself(self):
        if self.language == 'portuguese':
            return 'Nunca que eu chuto essa sua bundinha pra fora daqui!'
        if self.language == 'spanish':
            pass
        return 'I will never kick your ass out of here!'

    @property
    def please(self):
        if self.language == 'portuguese':
            return 'Eu dou meu melhor e mesmo assim me rejeitam...Cansei desta vida.'
        if self.language == 'spanish':
            pass
        return "I do my best and yet they reject me... I'm tired of this life."

    @property
    def higher_role(self):
        if self.language == 'portuguese':
            return 'Não posso expulsar este usuário pois seu cargo é mais alto que o meu. Suba-o na lista de cargos para que eu possa puní-lo.'
        if self.language == 'spanish':
            pass
        return "I can't kick this user because his role is higher than my. Up it in the role list to I can punish him."

    @property
    def kick_message(self):
        if self.language == 'portuguese':
            return f"""> Você está prestes a expulsar {self.member.mention}. Caso tenha certeza disso, clique em ✅;
            > Quer punir sem enviar uma mensagem pro usuário? Clique em 📌 antes de confirmar a punição."""
        if self.language == 'spanish':
            pass
        return f'''> You are about to kick {self.member.mention}. If you are sure, click on ✅;
        > Want to punish without notifying the user? Click on 📌 before confirming the punishment.'''

    @property
    def kick_annouce(self):
        if self.language == 'portuguese':
            return f"{self.member.mention} foi expulso do servidor por {self.ctx.author.mention}!"
        if self.language == 'spanish':
            pass
        return f"{self.member.mention} was kicked from the server by {self.ctx.author.mention}!"

    @property
    def kick_log(self):
        if self.language == 'portuguese':
            return f'Expulso por {self.ctx.author} | Motivo: {self.reason}'
        if self.language == 'spanish':
            pass
        return f'Kicked by {self.ctx.author} | Reason: {self.reason}'

class TemporaryRoomsMessages():
    def __init__(self, language, member=None):
        self.language = language
        self.member = member

    @property
    def not_connected(self):
        if self.language == 'portuguese':
            return 'Você não está conectado à uma sala temporária.'
        if self.language == 'spanish':
            pass
        return "You aren't connected in a temporary room."
    
    @property
    def not_owner(self):
        if self.language == 'portuguese':
            return 'Você precisa ser dono desta sala para usar este comando.'
        if self.language == 'spanish':
            pass
        return 'You need to be the owner of this room to use this command.'
    
    @property
    def not_admin(self):
        if self.language == 'portuguese':
            return 'Você precisa ser administrador desta sala para usar este comando.'
        if self.language == 'spanish':
            pass
        return 'You need to be an administrator of this room to use this command.'

    @property
    def channel_limit(self):
        if self.language == 'portuguese':
            return f'{self.member.mention}, você só pode criar até `3` canais simultâneos."'
        if self.language == 'spanish':
            pass
        return f'{self.member.mention}, you can only create up to 3 simultaneous channels.'

    @property
    def temporary_rooms(self):
        if self.language == 'portuguese':
            return 'Salas temporárias'
        if self.language == 'spanish':
            pass
        return 'Temporary rooms'
    
    @property
    def join_here(self):
        if self.language == 'portuguese':
            return 'Entre aqui'
        if self.language == 'spanish':
            pass
        return 'Join here'

    @property
    def setup(self):
        if self.language == 'portuguese':
            return 'Sistema de salas temporárias ativado com sucesso!'
        if self.language == 'spanish':
            pass
        return 'Temporary room system activated successfully!'

    @property
    def already_activated(self):
        if self.language == 'portuguese':
            return 'O sistema de salas temporárias já está ativado.'
        if self.language == 'spanish':
            pass
        return 'The temporary room system is already activated.'
    
    @property
    def disable(self):
        if self.language == 'portuguese':
            return 'Sistema de salas temporárias desativado com sucesso!'
        if self.language == 'spanish':
            pass
        return 'Temporary room system disabled successfully!'
    
    @property
    def not_activated(self):
        if self.language == 'portuguese':
            return 'O sistema de salas temporárias não está ativado.'
        if self.language == 'spanish':
            pass
        return 'Temporary room system is not activated.'

    @property
    def room_name(self):
        if self.language == 'portuguese':
            return f'Sala de {self.member.name}'
        if self.language == 'spanish':
            pass
        return f"{self.member.name}'s room" 

    @property
    def rename(self):
        if self.language == 'portuguese':
            return f'Você renomeou sua sala para '
        if self.language == 'spanish':
            pass
        return 'You renamed your room to '
    
    @property
    def lock(self):
        if self.language == 'portuguese':
            return 'Você trancou sua sala com sucesso!\nPara destrancá-la, use **trunlock**.'
        if self.language == 'spanish':
            pass
        return 'You have locked your room succesfully!\nUse **trunlock** to unlock it.'

    @property
    def unlock(self):
        if self.language == 'portuguese':
            return 'Você destrancou sua sala com sucesso!\nPara trancá-la novamente, use **trlock**.'
        if self.language == 'spanish':
            pass
        return 'You have unlocked your room succesfully!\nUse **trlock** to lock it again.'

    @property
    def hide(self):
        if self.language == 'portuguese':
            return 'Você removeu a visibilidade da sua sala.\nPara adicioná-la novamente, use **trunhide**.'
        if self.language == 'spanish':
            pass
        return 'You have removed the visibility from your room\nUse **trunhide** to add it again.'
    
    @property
    def unhide(self):
        if self.language == 'portuguese':
            return 'Você adicionou novamente a visibilidade da sua sala.\nPara removê-la, use **trhide**.'
        if self.language == 'spanish':
            pass
        return 'You have added the visibility from your room again.\nUse **trhide** to remove it.'
    
    @property 
    def block_herself(self):
        if self.language == 'portuguese':
            return 'Vai bloquear você mesmo? 🤡 Bobinho!'
        if self.language == 'spanish':
            pass
        return 'Are you going to block yourself? 🤡 Silly!'

    @property
    def block_bot(self):
        if self.language == 'portuguese':
            return 'Vou entrar aí só de raiva!'
        if self.language == 'spanish':
            pass
        return 'I will enter there out of spite!'

    def block(self, users):
        users = ', '.join(users)
        if self.language == 'portuguese':
            return f'Você bloqueou {users} da sua sala.\nPara desbloqueâ-lo(s), use **trunblock <users>**.'
        if self.language == 'spanish':
            pass
        a = 'them' if len(users) > 1 else 'him'
        return f'You have blocked {users} from your room.\nUse **trunblock <users>** to unblock {a}.'
    
    def unblock(self, users):
        users = ', '.join(users)
        if self.language == 'portuguese':
            return f'Você desbloqueou {users} da sua sala.\nPara bloqueâ-lo(s) novamente, use **trblock <users>**.'
        if self.language == 'spanish':
            pass
        a = 'them' if len(users) > 1 else 'him'
        return f'You have unblocked {users} from your room.\nUse **trblock<users>** to block {a} again.'
    
    def add(self, users):
        users = ', '.join(users)
        if self.language == 'portuguese':
            return f'Você adicionou {users} em sua sala.\nPara removê-lo(s), use **tremove <users>**.'
        if self.language == 'spanish':
            pass
        a = 'them' if len(users) > 1 else 'him'
        return f'You have added {users} in your room.\nUse **tremove <users>** to remove {a}.'
    
    def remove(self, users):
        users = ', '.join(users)
        if self.language == 'portuguese':
            return f'Você removeu {users} da sua sala.\nPara adicioná-lo(s) novamente, use **tradd <users>**.'
        if self.language == 'spanish':
            pass
        a = 'them' if len(users) > 1 else 'him'
        return f'You have removed {users} from your room.\nUse **tradd <users>** to remove {a} again.'

    def set_admin(self, users):
        users = ', '.join(users)
        if self.language == 'portuguese':
            return f'Você adicionou {users} como administrador de sua sala.\nPara removê-lo(s), use **tremoveadmin <users>**.'
        if self.language == 'spanish':
            pass
        a = 'them' if len(users) > 1 else 'him'
        return f'You have added {users} as administrator in your room.\nUse **tremoveadmin <users>** to remove {a}.'

    def remove_admin(self, users):
        users = ', '.join(users)
        if self.language == 'portuguese':
            return f'Você removeu {users} de administrador de sua sala.\nPara adicioná-lo(s) novamente, use **trsetadmin <users>**.'
        if self.language == 'spanish':
            pass
        a = 'them' if len(users) > 1 else 'him'
        return f'You have removed {users} as administrator from your room.\nUse **trsetadmin <users> to add {a} again.'

    @property
    def set_owner(self):
        if self.language == 'portuguese':
            return f'Você setou {self.member.mention} como dono da sua sala.'
        if self.language == 'spanish':
            pass
        return f'You set {self.member.mention} as the owner of your room.'

class PresetsMessages():
    def __init__(self, language, ctx):
        self.language = language
        self.ctx = ctx

    @property
    def default(self):
        if self.language == 'portuguese':
            return 'Configuração padrão de salas temporárias:'
        if self.language == 'spanish':
            pass
        return 'Temporary rooms default settings:'
    
    @property
    def room_name(self):
        if self.language == 'portuguese':
            return '📄 Nome das salas:'
        if self.language == 'spanish':
            pass
        return "📄 Room's name:"

    @property
    def locked(self):
        if self.language == 'portuguese':
            return '🔒 Sala trancada:'
        if self.language == 'spanish':
            pass
        return '🔒 Locked room:'
    
    @property
    def invisible(self):
        if self.language == 'portuguese':
            return '🔗 Sala invisível:'
        if self.language == 'spanish':
            pass
        return '🔗 Invisible room:'

    @property
    def members(self):
        if self.language == 'portuguese':
            return '👥 Membros adicionados:'
        if self.language == 'spanish':
            pass
        return '👥 Added members:'

    @property
    def admins(self):
        if self.language == 'portuguese':
            return '👑 Administradores:'
        if self.language == 'spanish':
            pass
        return '👑 Administrators:'

    @property
    def blockeds(self):
        if self.language == 'portuguese':
            return '❌ Membros bloqueados:'
        if self.language == 'spanish':
            pass
        return '❌ Blocked members:'

    @property
    def category(self):
        if self.language == 'portuguese':
            return 'Clique na reação correspondente à categoria que deseja\npara configurá-la. Para deletar seu perfil de configurações,\n clique em  🚫'
        if self.language == 'spanish':
            pass
        return 'Click on the reaction that corresponds the category you want\n to configure. React on 🚫 to delete your configuration profile.'

    @property
    def obs(self):
        if self.language == 'portuguese':
            return 'Essas configurações serão setadas automaticamente sempre que\nvocê criar uma nova sala temporária neste servidor.'
        if self.language == 'spanish':
            pass
        return 'These settings will be setted automaticaly whenever you create\na new temporary room in this server.'
    
    @property
    def what_name(self):
        if self.language == 'portuguese':
            return f"{self.ctx.author.mention}, qual será o nome das suas salas temporárias?"
        if self.language == 'spanish':
            pass
        return f'{self.ctx.author.mention}, what will be the name of your temporary rooms?"'

    @property
    def name_changed(self):
        if self.language == 'portuguese':
            return 'Você alterou o nome padrão das suas salas para'
        if self.language == 'spanish':
            pass
        return 'You changed the default name of your rooms to'
    
    @property
    def set_lock(self):
        if self.language == 'portuguese':
            return 'Você setou a tranca das suas salas como'
        if self.language == 'spanish':
            pass
        return 'You set the lock of your rooms as'
    
    @property
    def set_hide(self):
        if self.language == 'portuguese':
            return 'Você setou a invisibilidade das suas salas como'
        if self.language == 'spanish':
            pass
        return 'You set the invisibility of your rooms as'

    @property
    def add_members(self):
        if self.language == 'portuguese':
            return f'{self.ctx.author.mention}, clique em 🟢 para adicionar membros ou 🔴 para remover.'
        if self.language == 'spanish':
            pass
        return f'{self.ctx.author.mention}, click in 🟢 to add members or 🔴 to remove.'

    @property
    def add_who(self):
        if self.language == 'portuguese':
            return f'{self.ctx.author.mention}, quem você deseja adicionar? Você pode adicionar cargos ou membros, informe o ID ou nome para evitar marcações.'
        if self.language == 'spanish':
            pass
        return f'{self.ctx.author.mention}, who do you want to add? You can add roles or members, inform the ID or name to avoid mentions.'

    @property
    def members_added(self):
        if self.language == 'portuguese':
            return ' adicionados às suas salas temporárias com sucesso!'
        if self.language == 'spanish':
            pass
        return ' added to your temporary rooms succesfully!'
    
    @property
    def remove_who(self):
        if self.language == 'portuguese':
            return f'{self.ctx.author.mention}, quem você deseja remover? Informe o seu ID ou nome para evitar marcações.'
        if self.language == 'spanish':
            pass
        return f'{self.ctx.author.mention}, who do you want to remove? Inform the ID or name to avoid mentions.'
    
    @property
    def members_removed(self):
        if self.language == 'portuguese':
            return ' removidos das suas salas temporárias com sucesso!'
        if self.language == 'spanish':
            pass
        return ' removed from your temporary rooms succesfully!'
    
    @property 
    def add_admins(self):
        if self.language == 'portuguese':
            return f'{self.ctx.author.mention}, clique em 🟢 para adicionar administradores ou 🔴 para remover.'
        if self.language == 'spanish':
            pass
        return f'{self.ctx.author.mention}, click in 🟢 to add administrators or 🔴 to remove.'

    @property
    def admins_added(self):
        if self.language == 'portuguese':
            return ' adicionado(s) como administrador às suas salas temporárias com sucesso!'
        if self.language == 'spanish':
            pass
        return ' added as administrator to your temporary rooms succesfully!'
    
    @property
    def admins_removed(self):
        if self.language == 'portuguese':
            return ' removido(s) da administração das suas salas com sucesso!'
        if self.language == 'spanish':
            pass
        return ' removed from administration of your temporary rooms succesfully!'
    
    @property
    def block_members(self):
        if self.language == 'portuguese':
            return f'{self.ctx.author.mention}, clique em 🔴 para bloquear usuários ou 🟢 para desbloquear.'
        if self.language == 'spanish':
            pass
        return f'{self.ctx.author.mention}, click in 🔴 to block users or 🟢 to unblock.'
    
    @property
    def block_who(self):
        if self.language == 'portuguese':
            return f'{self.ctx.author.mention}, quem você deseja bloquear das suas salas temporárias? Você pode bloquear cargos ou membros, informe o seu ID ou tag para evitar marcações.'
        if self.language == 'spanish':
            pass
        return f'{self.ctx.author.mention}, who do youn want to block from your temporary rooms? You can block roles or members, inform the ID or name to avoid mentions.'
    
    @property
    def blocked(self):
        if self.language == 'portuguese':
            return ' bloqueado(s) das suas salas temporárias com sucesso!'
        if self.language == 'spanish':
            pass
        return ' blocked from you temporary rooms succesfully!'
    
    @property
    def unblock_who(self):
        if self.language == 'portuguese':
            return f'{self.ctx.author.mention}, quem você deseja desbloquear das suas salas temporárias? Informe o seu ID ou tag para evitar marcações.'
        if self.language == 'spanish':
            pass
        return f'{self.ctx.author.mention}, who do youn want to unblock from your temporary rooms? Inform the ID or name to avoid mentions.'
    
    @property
    def unblocked(self):
        if self.language == 'portuguese':
            return ' desbloqueado(s) das suas salas temporárias com sucesso!'
        if self.language == 'spanish':
            pass
        return ' unblocked from you temporary rooms succesfully!'
    
    @property
    def delete(self):
        if self.language == 'portuguese':
            return 'Tem certeza que deseja deletar suas configurações padrões neste servidor? Se sim, clique em ✅'
        if self.language == 'spanish':
            pass
        return 'Are you sure you want to delete your default configurations in this server? Click in ✅ if yes.'
    
    @property
    def deleted(self):
        if self.language == 'portuguese':
            return 'Suas configurações de salas foram deletadas deste servidor!'
        if self.language == 'spanish':
            pass
        return 'Your temporary rooms configurations were deleted from this server!'
    
    @property
    def inform(self):
        if self.language == 'portuguese':
            return 'Informe o ID do servidor que deseja ver suas configurações de salas.'
        if self.language == 'spanish':
            pass
        return "Inform the ID of the server you want to see your room's configurations."
    
    @property
    def not_presets(self):
        if self.language == 'portuguese':
            return 'Você ainda não configurou suas configurações padrões de salas temporárias nesse servidor, caso queira configurar, clique na reação abaixo:'
        if self.language == 'spanish':
            pass
        return 'You have not yet configured your default temporary room settings on this server, if you want to configure it, click on the reaction below:'
    
    @property
    def rate_limit(self):
        if self.language == 'portuguese':
            return 'Você não pode criar mais de 2 perfis de configuração de salas, delete o perfil de um servidor para que você possa criar um nesse.'
        if self.language == 'spanish':
            pass
        return 'You cannot create more than 2 room configuration profiles, delete an server profile so that you can create one here.'
    
    @property
    def exceed(self):
        if self.language == 'portuguese':
            return 'O nome da sala não pode ultrapassar ``25`` caractéres!'
        if self.language == 'spanish':
            pass
        return "The room's name can't exceed ``25`` characters!"

class ErrorMessages():
    def __init__(self, language):
        self.language = language

    def not_permissions(self, perm):
        if self.language == 'portuguese':
            return f'Você precisa da permissão de ``{perm}`` para usar este comando.'
        if self.language =='spanish':
            pass
        return f'You need ``{perm}`` permission to use this command.'
    
    @property
    def invalid_argument(self):
        if self.language == 'portuguese':
            return 'Argumento inválido.'
        if self.language == 'spanish':
            pass
        return 'Invalid argument.'
    
    @property
    def rate_limit(self):
        if self.language == 'portuguese':
            return 'O nome da sala não pode ultrapassar ``25`` caractéres!'
        if self.language == 'spanish':
            pass
        return "The room's name can't exceed ``25`` characters!"
    
    def bot_not_permissions(self, perm):
        if self.language == 'portuguese':
            return f'Algum membro malvado tirou minha permissão de ``{perm}`` 😰!\nColoque-a de volta para que eu possa realizar essa e outras tarefas normalmente.'
        if self.language == 'spanish':
            pass
        return f'Some bad member has removed my ``{perm}`` permission 😰!\nPut it back so I can do this and other tasks normally.'
    
class HelpMessages():
    def __init__(self, language, prefix):
        self.language = language
        self.prefix = prefix
    
    @property
    def get_command(self):
        if self.language == 'portuguese':
            return 'Utilize `*help <comando>` para obter uma ajuda detalhada de um comando específico.'
        if self.language == 'spanish':
            pass
        return 'Use `*help <command>` to get a detailed help from a specific command.'

    @property
    def temporary_rooms(self):
        if self.language == 'portuguese':
            return '** 🔊 Salas temporárias**'
        if self.language == 'spanish':
            pass
        return '** 🔊 Temporary rooms**'
    
    @property
    def moderation(self):
        if self.language == 'portuguese':
            return '**🔨 Moderação**'
        if self.language == 'spanish':
            pass
        return '**🔨 Moderation**'
    
    @property
    def utility(self):
        if self.language == 'portuguese':
            return '** 📜 Utilidade**'
        if self.language == 'spanish':
            pass
        return '** 📜 Utility**'

    @property
    def games(self):
        if self.language == 'portuguese':
            return '** 🎮 Jogos**'
        if self.language == 'spanish':
            pass
        return '** 🎮 Games**'
    
    @property
    def configuration(self):
        if self.language == 'portuguese':
            return '** ⚙️ Configuração**'
        if self.language == 'spanish':
            pass
        return '** ⚙️ Configuration**'

    @property
    def invite(self):
        if self.language == 'portuguese':
            return '''Quer acesso às minhas utilidades? [Clique aqui](https://discord.com/api/oauth2/authorize?client_id=862740130385494027&permissions=286616662&scope=bot) e me adicione em seu servidor!
            💸 Me ajude a me manter online, faça uma doação [clicando aqui](https://www.paypal.com/donate?hosted_button_id=4KQY6N6GC23RS) !'''
        if self.language == 'spanish':
            pass
        return '''Do you want access to my utilities? [Click here](https://discord.com/api/oauth2/authorize?client_id=862740130385494027&permissions=286616662&scope=bot) and add me in your server!
        Help me get online, make a donation [clicking here](https://www.paypal.com/donate?hosted_button_id=4KQY6N6GC23RS) !'''
    
    @property
    def ban(self):
        if self.language == 'portuguese':
            return 'Bane um membro permanentemente ou temporariamente, além de notificá-lo no privado, caso deseje.'
        if self.language == 'spanish':
            pass
        return 'Ban a member permanently or temporarily, and notify him privately if you wish.'
    
    @property
    def ban_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}ban @hiury Flood`` - Bane ``@hiury`` pelo motivo ``Flood``;
            ``{self.prefix}ban 669975205325570048 Doxxing`` - Bane o usuário de ID ``669975205325570048`` pelo motivo ``Doxxing``. O usuário não precisa estar no servidor.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}ban @hiury Flood`` - Ban ``@hiury`` for the reason ``Flood``;
        ``{self.prefix}ban 669975205325570048 Doxxing`` - Ban user ID ``669975205325570048`` for the reason ``Doxxing``. The user don't need to be on the server.'''

    @property
    def mute(self):
        if self.language == 'portuguese':
            return f'Muta um usuário, impedindo-o de enviar mensagens em canais de texto. Utilize ``{self.prefix}unmute <member>`` para desmutar.'
        if self.language == 'spanish':
            pass
        return f'Mute a user, preventing him from sending messages in text channels. Use `` {self.prefix} unmute <member> `` to unmute.'

    @property
    def mute_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}mute @kayke chato pra karalho em`` - Muta ``@kayke`` pelo motivo ``chato pra karalho em``;
            ``{self.prefix}mute 669975205325570048 Flood`` - Muta o usuário de ID ``669975205325570048`` pelo motivo ``Flood``.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}mute @kayke fucking boring`` - Mute ``@kayke`` for the reason ``fucking boring``;
        ``{self.prefix}mute 669975205325570048 Flood`` - Mute the user ID ``669975205325570048`` for the reason ``Flood``.'''
    
    @property
    def kick(self):
        if self.language == 'portuguese':
            return 'Expulsa um membro e o notifica no privado, caso deseje.'
        if self.language == 'spanish':
            pass
        return 'Kicks a member and notify him privately if you wish.'

    @property
    def kick_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}kick @bieeu Flood`` - Expulsa ``@bieeu`` pelo motivo ``Flood``;
            ``{self.prefix}kick 669975205325570048 Doxxing`` - Expulsa o usuário de ID ``669975205325570048`` pelo motivo ``Doxxing``.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}kick @bieeu Flood`` - Kicks ``@bieeu`` for the reason ``Flood``;
        ``{self.prefix}kick 669975205325570048 Doxxing`` - Kicks user ID ``669975205325570048`` for the reason ``Doxxing``.'''
    
    @property
    def clear(self):
        if self.language == 'portuguese':
            return 'Limpa as últimas mensagens de um chat.'
        if self.language == 'spanish':
            pass
        return 'Clears the latest messages from a chat.'
    
    @property
    def lock(self):
        if self.language == 'portuguese':
            return f'Tranca um canal, tirando a permissão de enviar mensagens de todos os membros. Utilize ``{self.prefix}unlock [channel]`` para destrancar.'
        if self.language == 'spanish':
            pass
        return f'Locks a channel, removing the permission to send messages from all members. Use ``{self.prefix}unlock [channel]`` to unlock.'
    
    @property
    def lock_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}lock #exemplo`` - Tranca o canal ``#exemplo;``
            ``{self.prefix}lock`` - Tranca o canal em que o comando foi digitado.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}lock #example`` - Lock the channel ``#example;``
        ``{self.prefix}lock`` - Locks the channel where the command was sent.'''

    @property
    def avatar(self):
        if self.language == 'portuguese':
            return 'Mostra o avatar de um usuário em uma visibilidade melhor e maior.'
        if self.language == 'spanish':
            pass
        return "Displays a user avatar's with a better and bigger visibility."

    @property
    def avatar_examples(self):
        if self.language == 'portuguese':   
            return f'''``{self.prefix}avatar`` - Mostra seu próprio avatar.
            ``{self.prefix}avatar @flash`` - Mostra o avatar de ``@flash``;
            ``{self.prefix}avatar 390178236065251328`` - Mostra o avatar do usuário de ID ``390178236065251328``. O usuário não precisa estar no servidor.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}avatar`` - Shows your own avatar;
        ``{self.prefix}avatar @flash`` - Shows the ``@flash`` avatar's;
        ``{self.prefix}avatar 390178236065251328`` - Show the user ID ``390178236065251328`` avatar's. The user don't need to be on the server.'''

    @property
    def namemc(self):
        if self.language == 'portuguese':
            return '''Exibe o perfil de uma conta do Minecraft no site NameMC. O perfil contêm informações como o histórico de nick's da conta, o UUID da conta, sua skin, etc...'''
        if self.language == 'spanish':
            pass
        return '''Displays the minecraft profile on the NameMC website. The profile contains information such as the account's nickname history, the account's UUID, its skin, etc...'''
    
    @property
    def namemc_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}namemc _Hatsya`` - Exibe o perfil de nick _Hatsya;
            ``{self.prefix}namemc Liliawn`` - Exibe as contas que já usaram esse nick e a disponibilidade do mesmo.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}namemc _Hatsya`` - Displays the nick _Hatsya account;
        ``{self.prefix}namemc Liliawn`` - Displays the accounts that have already used this nick and the availability of it.'''
    
    @property
    def remindme(self):
        if self.language == 'portuguese':
            return 'Programa o envio de uma mensagem para você em forma de um lembrete. Use caso não queira esquecer de buscar a sua irmã na creche.'
        if self.language == 'spanish':
            pass
        return "Schedule to send a message to you in the form of a reminder. Use it if you don't want to forget to pick up your sister from the daycare."
    
    @property
    def remindme_examples(self):
        if self.language == 'portuguese':
            return f'``{self.prefix}remindme dar banho no peixe`` - Assim que o comando for utilizado, lhe perguntarei em quanto tempo você deseja receber o aviso.'
        if self.language == 'spanish':
            pass
        return f'``{self.prefix}remindme bathe the fish`` - As soon as the command is used, I will ask how long you want to receive the warning.'

    @property
    def servericon(self):
        if self.language == 'portuguese':
            return 'Exibe o ícone de um servidor em uma visibilidade melhor e maior.'
        if self.language == 'spanish':
            pass
        return f'Displays a server icon with a better and bigger visibility.'
    
    @property
    def servericon_examples(self):
        if self.language == 'portuguese':
            f'''``{self.prefix}servericon`` - Mostra o ícone do servidor em que o comando foi utilizado;
            ``{self.prefix}servericon 836748124139552788 - Mostra o ícone do servidor de ID ``836748124139552788``.''' 
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}servericon`` - Displays the icon of server where the command was sent;
        ``{self.prefix}servericon 836748124139552788 - Displays the server ID ``836748124139552788`` icon.''' 
    
    @property
    def serverinfo(self):
        if self.language == 'portuguese':
            return 'Exibe as informações de um servidor.'
        if self.language == 'spanish':
            pass
        return 'Display informations from a server.'

    @property
    def serverinfo_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}serverinfo`` - Mostra as informações do servidor em que o comando foi utilizado;
            ``{self.prefix}servericon 799731802096271370 - Mostra as informações do servidor de ID ``799731802096271370``.''' 
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}serverinfo`` - Displays the informations from the server where the command was sent.
        ``{self.prefix}servericon 799731802096271370 - Displays the informations from the server ID ``799731802096271370``.''' 

    @property
    def userinfo(self):
        if self.language == 'portuguese':
            return 'Exibe as informações de um membro do servidor.'
        if self.language == 'spanish':
            pass
        return 'Display informations from a server member.'
    
    @property
    def userinfo_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}userinfo`` - Mostra suas informações no servidor;
            ``{self.prefix}userinfo @karol`` - Mostra as informações de ``@karol``'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}userinfo`` - Displays your informations on the server
        ``{self.prefix}userinfo @karol`` - Displays the informations from ``@karol``'''
    
    @property
    def presets(self):
        if self.language == 'portuguese':
            return 'Exibe suas configurações padrões de salas temporárias em um servidor. O mesmo comando pode ser criado para criar as configurações, caso você não tenha'
        if self.language == 'spanish':
            pass
        return "Displays your temporary channel default settings. The same command can be used to create a profile settings, if you don't have."

    @property
    def presets_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}presets`` - Exibe suas configurações no servidor em que o comando foi o utilizado;
            ``{self.prefix}presets 836748124139552788`` - Exibe suas configurações no servidor de ID ``836748124139552788``.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}presets`` - Displays your settings from the server where command was sent;
        ``{self.prefix}presets 836748124139552788`` - Displays your settings from the server ID ``836748124139552788``.'''
    
    @property
    def trsetup(self):
        if self.language == 'portuguese':
            return f'Ativa o sistema de salas temporárias. Utilize ``{self.prefix}trdisable`` para desativar.'
        if self.language == 'spanish':
            pass
        return f'Enable the temporary channel system. Use ``{self.prefix}trdisable`` to disable.'
    
    @property
    def trename(self):
        if self.language == 'portuguese':
            return 'Renomeia sua sala temporária.'
        if self.language == 'spanish':
            pass
        return 'Renames your temporary channel.'
    
    @property
    def trlock(self):
        if self.language == 'portuguese':
            return f'Tranca sua sala temporária, impedindo todos os membros do servidor de visualizá-la e adentrá-la, exceto os com permissão. Utilize ``{self.prefix}trunlock`` para destrancar sua sala.'
        if self.language == 'spanish':
            pass
        return f'Locks your temporary channel, denying all server members to view and join it, except those with permission. Use ``{self.prefix}trunlock`` to unlock your channel.'

    @property
    def tradd(self):
        if self.language == 'portuguese':
            return f'Adiciona um usuário ou cargo à sua sala, permitindo-o visualizar e entrar na sala mesmo caso esteja trancada ou invisível. Utilize ``{self.prefix}tremove <user>`` para remover um usuário.'
        if self.language == 'spanish':
            pass
        return f"Add an user or role to your channel, allow her to join and view your channel even if it's locked or invisible. Use ``{self.prefix}tremove <user> to remove an user."

    @property
    def tradd_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}tradd @milena`` - Adiciona ``@milena`` à sua sala;
            ``{self.prefix}tradd 744391839678857276`` - Adiciona o usuário de ID ``744391839678857276`` à sua sala.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}tradd @milena`` - Adds ``@milena`` to your channel;
        ``{self.prefix}tradd 744391839678857276`` - Adds the user ID ``744391839678857276`` to your channel.''' 

    @property
    def trhide(self):
        if self.language == 'portuguese':
            return f'Deixa sua sala invisível para todos os usuários, exceto os adicionados. Utilize ``{self.prefix}trunhide`` para deixar sua sala visível novamente.'
        if self.language == 'spanish':
            pass
        return f'Turn your channel invisible to all uers, except the added. Use ``{self.prefix}trunhide`` to turn your channel visible again.'
    
    @property
    def trblock(self):
        if self.language == 'portuguese':
            return f'Bloqueia um usuário ou cargo da sua sala, impedindo-o de visualizar e adentrar a sala. Utilize ``{self.prefix}trunblock <member>`` para desbloquear um usuário.'
        if self.language == 'spanish':
            pass
        return f'Blocks an user or role from your channel, denying him to view and join your channel. Use ``{self.prefix}trunblock <member>`` to unblock an user.'

    @property
    def trblock_examples(self):
        if self.language == 'portuguese':
            return f'''``{self.prefix}trblock @biel`` - Bloqueia ``@biel`` da sua sala;
            ``{self.prefix}trblock 256577941079588864`` - Bloqueia o usuário de ID ``256577941079588864`` da sua sala.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}trblock @biel`` - Blocks ``@biel`` from your channel;
        ``{self.prefix}trblock 256577941079588864`` - Blocks the user ID ``256577941079588864`` from your channel.'''

    @property
    def trsetadmin(self):
        if self.language == 'portuguese':
            return f'Adiciona um usuário ou cargo como administrador da sua sala, o administrador poderá: renomear, trancar ou destrancar e deixar sua sala invisível e adicionar ou remover e bloquear ou desbloquear um usuário. Utilize ``{self.prefix}tremoveadmin <user>`` para remover um usuário de administrador.'
        if self.language == 'spanish':
            pass
        return f'Add an user or role as administrator from your chanel, the user can: rename, lock and unlock and hide and unhide your channel and add or remove and block or unblock an user. Use ``{self.prefix}tremoveadmin <user>`` to remove and user from administration.'

    @property
    def trsetadmin_examples(self):
        if self.language == 'portuguese':
            f'''``{self.prefix}trsetadmin @1luc4s``` - Seta ``@1luc4s`` como administrador da sua sala;
            ``{self.prefix}trsetadmin 312711013889736705`` - Seta o usuário de ID ``312711013889736705`` como administrador da sua sala.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}trsetadmin @1luc4s - Set ``@1luc4s as administrator from your channel;
        ``{self.prefix}trsetadmin 312711013889736705`` - Set the user ID ``312711013889736705`` as administrator from your channel.'''
    
    @property
    def trsetowner(self):
        if self.language == 'portuguese':
            return 'Tranfere a posse da sua sala para outro usuário.'
        if self.language == 'spanish':
            pass
        return 'Transfers your channel ownership to other user.'
    
    @property
    def trsetowner_examples(self):
        if self.language == 'portuguese':
            f'''``{self.prefix}trsetowner @noggin`` - Transfere a posse da sala para ``@noggin``;
            ``{self.prefix}trsetowner 411651287550001163`` - Tranfere a posse da sala para o usuário de ID ``411651287550001163``.'''
        if self.language == 'spanish':
            pass
        return f'''``{self.prefix}trsetowner @noggin`` - Transfers the channel ownership to ``@noggin``;
        ``{self.prefix}trsetowner 411651287550001163`` - Transfers the channel ownership to user ID ``411651287550001163``.'''
    
    @property
    def command_not_found(self):
        if self.language == 'portuguese':
            return 'Esse comando não existe!'
        if self.language == 'spanish':
            pass
        return "This command doens't exist!"

    @property
    def channel_admin_permission(self):
        if self.language == 'portuguese':
            return 'Você precisa ser ``Administrador`` da sala para utilizar este comando. E eu preciso da permissão de ``Gerenciar Canais``'
        if self.language == 'spanish':
            pass
        return "You need to be an ``Administrator`` from the channel to use this command. And I need ``Manage Channels`` permission"
    
    @property
    def channel_owner_permission(self):
        if self.language == 'portuguese':
            return 'Você precisa ser ``Dono`` da sala para utilizar este comando. E eu preciso da permissão de ``Gerenciar Canais``'
        if self.language == 'spanish':
            pass
        return 'You need to be the ``Owner`` from the room to use this command. And I need ``Manage Channels`` permission.'
    
    @property
    def without_permissions(self):
        if self.language == 'portuguese':
            return 'Este comando não precisa de permissões, só não vai floodar!'
        if self.language == 'spanish':
            pass
        return "This command doesn't need permissions, just don't flood it!"

    @property
    def setup_permission(self):
        if self.language == 'portuguese':
            return 'Você precisa da permissão de ``Administrador`` para utilizar este comando. E eu da permissão de ``Gerenciar Canais``.'
        if self.language == 'spanish':
            pass
        return 'You need ``Administrator`` permission to use this command. And I need ``Manage Channels`` permission.'
    
    @property
    def autorole_permission(self):
        if self.language == 'portuguese':
            return 'Você precisa da permissão de ``Administrador`` para utilizar este comando. E eu da permissão de ``Gerenciar Cargos``.'
        if self.language == 'spanish':
            pass
        return 'You need ``Administrator`` permission to use this command. And I need ``Manage Roles`` permission.'
    
    @property
    def manage_channel_permission(self):
        if self.language == 'portuguese':
            return 'Você e eu precisamos da permissão de ``Gerenciar Canais`` para o comando poder ser utilizado!'
        if self.language == 'spanish':
            pass
        return 'We need ``Manage Channels`` permission to use this command!'
    
    @property
    def manage_messages_permission(self):
        if self.language == 'portuguese':
            return 'Você e eu precisamos da permissão de ``Gerenciar Mensagens`` para o comando poder ser utilizado!'
        if self.language == 'spanish':
            pass
        return 'Wee need ``Manage Messages`` permission to use this command!'
    
    @property
    def ban_permission(self):
        if self.language == 'portuguese':
            return 'Você e eu precisamos da permissão ``Banir membros`` para o comando poder ser utilizado!'
        if self.language == 'spanish':
            pass
        return 'We need ``Ban Members`` permission to use this command!'
    
    @property
    def kick_permission(self):
        if self.language == 'portuguese':
            return 'Você e eu precisamos da permissão ``Expulsar membros`` para o comando poder ser utilizado!'
        if self.language == 'spanish':
            pass
        return 'We need ``Kick Members`` permission to use this command!'
    
    @property
    def use(self):
        if self.language == 'portuguese':
            return '🔧 Uso:'
        if self.language == 'spanish':
            pass
        return '🔧 Use:'
    
    @property
    def examples(self):
        if self.language == 'portuguese':
            return '🧾 Exemplos:'
        if self.language == 'spanish':
            pass
        return '🧾 Examples:'
    
    @property
    def permissions(self):
        if self.language == 'portuguese':
            return '⚙️ Permissões:'
        if self.language == 'spanish':
            pass
        return '⚙️ Permissions:'
    
    @property
    def alias(self):
        if self.language == 'portuguese':
            return '🧷 Sinônimos:'
        if self.language == 'spanish':
            pass
        return '🧷 Aliases:'

    @property
    def arguments(self):
        if self.language == 'portuguese':
            return '``<argumento>`` - Argumento obrigatório; `[argumento]`` - Argumento opcional.'
        if self.language == 'spanish':
            pass
        return '``<argument>`` - Required argument; ``[argument]`` - Optional argument.'