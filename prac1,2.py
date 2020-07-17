names = ['navin', 'nahid', 'nadia']
plays=['football', 'cricket', 'ragbi' ]
loves=dict(zip(names,plays))
print(loves)
loves['monika']='hidenseek'
print(loves)
del loves['nahid']
print(loves)

prog= { 'C':' codeblocks ', 'Js': 'Atom', 'Python': ['pycharm', 'sublime'], 'java':{'JSE': 'Netbeans', 'JEE': 'eclilips'}}
print(prog['java']['JSE'])
print(type(prog))
