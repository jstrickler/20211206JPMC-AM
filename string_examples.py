s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # RAW STRING


print(len(s1), len(s2))
print("Guido's the BDFL of Python")
print('Guido is the "BDFL" of Python')
print('''Guido's the "BDFL" of Python''')
print(r""" I give up \\o//""")



query = """
select *
from animals
where country = "Australia"
order by name
"""

