from imhotep.tools import Tool
from collections import defaultdict
import re

class Pep8Linter(Tool):
    regex = re.compile(r'(?P<filename>.*):(?P<line_num>\d+):\d+: (?P<message>.*)')
    def invoke(self, dirname, filenames=set(), linter_configs=set()):
        retval = defaultdict(lambda: defaultdict(list))

        cmd = 'find %s -name "*.py" | xargs pep8' % dirname
        output = self.executor(cmd)
        for line in output.split("\n"):
            match = self.regex.search(line)
            if match is not None:
                retval[match.group('filename')][match.group('line_num')].append(match.group('message'))
        return retval
