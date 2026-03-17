import textwrap

name = input("Enter your name: ").strip()
profession = input("Enter your job title: ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favorite emoji: ").strip()
handle = input("(Optional) Enter your website or handle: ").strip()

print("\nChoose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("Enter 1, 2, or 3: ").strip()

#style validation
print(style)
while not style.isnumeric() or not (int(style) > 0 and int(style) <= 3):
    style = input("Please enter 1, 2, or 3 only: ").strip()

print(f"{emoji} {name} | {profession} \n🔯 {passion}\n {handle}" if handle else f"{handle}")

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n {passion}\n{handle}"
    elif style == "2":
        return f"{emoji} {name}\n {profession}🗱\n {passion} \n {handle}🗱"
    elif style == "3":
        return f"{emoji*3}\n {name} - {profession}\n {passion} \n {handle}\n {emoji*3}"
    
bio = generate_bio(style)

print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Would you like to save this bio? (y/n:) ").lower()

if save == 'y':
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("file saved")
    