import re

v = 'aeiou'
c = 'qwrtypsdfghjklzxcvbnm'

m = re.findall('(?<=[%s])([%s]{2,})[%s]' % (c, v, c), input(), flags=re.I)
print('\n'.join(m or ['-1']))
