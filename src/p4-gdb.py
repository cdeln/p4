# Stolen from https://stackoverflow.com/questions/60680813/how-to-do-a-gdb-backtrace-showing-only-function-names-and-nothing-else
class P4Backtrace(gdb.Command):
    """Backtrace with function names only"""
    def __init__(self):
        super(self.__class__, self).__init__('p4-backtrace', gdb.COMMAND_FILES)
    def invoke(self, argument, from_tty):
        frame = gdb.selected_frame()
        level = 0
        while frame is not None:
            funcname = frame.name() or "?"
            gdb.write(f'#{level} {funcname}\n')
            frame = frame.older()
            level += 1
P4Backtrace()
