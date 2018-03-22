import re


def parse_bytes(string):
    byte_pattern = re.compile(r'\b[0-1]{8}\b')
    result = byte_pattern.findall(string)
    return result


assert(parse_bytes('10011010 011 867') == ['10011010'])
assert(parse_bytes('my bytes are: 10011010 01101110') == ['10011010', '01101110'])
assert(parse_bytes('pepsi') == [])
