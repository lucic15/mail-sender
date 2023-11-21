import re

input_text = """
email@email.com name
"""

lines = input_text.strip().split('\n')

output_list = []

for line in lines:
    match = re.match(r'(\S+@\S+)\s+(.+)', line)
    if match:
        email, name = match.groups()
        output_list.append((email, name))

print(output_list)
