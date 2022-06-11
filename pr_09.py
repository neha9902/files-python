with open("poems.txt") as f:
    content=f.read()

print(content)
content = content.replace("Donkey","@%^$^&^%^&$")    
print(content)
with open("poems.txt","w") as f:
    f.write(content)

