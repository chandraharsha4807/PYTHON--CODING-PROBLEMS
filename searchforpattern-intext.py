import re

text = "A random string. My name is Harsha_9-9-8@gmail.com. some chandu998@gmail.com"
#("\" is used to seperation or escape)

pattern = re.compile("[a-zA-Z0-9\.\_\-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")

result = pattern.findall(text)

print(result)