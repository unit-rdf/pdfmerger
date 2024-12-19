from Commands.Command import Command

class Invoker:
    def __init__(self):
        self._invoker_command = None

    def set_command(self, command: Command):
            self._invoker_command = command

    def run(self):
        if isinstance(self._invoker_command, Command):
            self._invoker_command.execute()
 