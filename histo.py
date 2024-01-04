import asyncio
from save import load_data, save_data

class CommandHistory:
    def __init__(self):
        self.command_history, self.conversation_progress = load_data()
        self.access_lock = asyncio.Lock()

    async def add_command(self, user, command):
        async with self.access_lock:
            str_user = str(user)
            if str_user not in self.command_history:
                self.command_history[str_user] = []
            self.command_history[str_user].append(command)
            save_data(self.command_history, self.conversation_progress)

    async def get_last_command(self, user):
        async with self.access_lock:
            str_user = str(user)
            if self.command_history.get(str_user):
                user_commands = self.command_history[str_user]
                if user_commands:
                    return user_commands[-1]
        return None

    async def get_user_commands(self, user):
        async with self.access_lock:
            str_user = str(user)
            return self.command_history.get(str_user, [])

    async def clear_history(self, user):
        async with self.access_lock:
            str_user = str(user)
            if str_user in self.command_history:
                del self.command_history[str_user]
                del self.conversation_progress[str_user]

    async def get_conversation_progress(self, user):
        async with self.access_lock:
            str_user = str(user)
            return self.conversation_progress.get(str_user, None)

    async def set_conversation_progress(self, user, progress):
        async with self.access_lock:
            str_user = str(user)
            self.conversation_progress[str_user] = progress
            save_data(self.command_history, self.conversation_progress)
