import datetime

profile = {
    "name": str,
    "age": str,
    "city": str,
    "profession": str,
    "favorite hobby": str

}

for x in profile:
    profile[x] = input("What is your " + x + "? ").strip()

intro_message = (
    f"Hello! My name is {profile['name']}. I'm {profile['age']} years old and live in {profile['city']}.\n"
    f"I work as a {profile['profession']} and love {profile['favorite hobby'].lower()} in my free time.\n" 
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"Logged on: {current_date}"

border = "*" * 80

final_output = f"{border}\n{intro_message}\n{border}"

print(final_output)
