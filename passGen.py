#! Python 3
#! A program to create a random password

import random, logging, string
from sre_parse import SPECIAL_CHARS

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
# logging.disable(logging.CRITICAL)

# Determine min/max character length
minChar = input("Enter the minimum character requirment [1]: ") or 1
maxChar = input("Enter the maximum character limit [32]: ") or 32
logging.debug(f"The minimum character requirment is {minChar}")
logging.debug(f"The maximum character limit is {maxChar}")

# Determine special character allowance
specChar = input("Include special characters (Y/N)? [Y]") or "Y"
while specChar.upper() not in ("Y", "N"):
    print(f"{specChar} is not a valid input. Please enter Y or N.")
    specChar = input("Include special characters (Y/N)? [Y]") or "Y"
specChar = specChar.upper()
logging.debug(f"specChar is {specChar}")

# Create the password.
randPass = []
for char in range(random.randint(minChar, maxChar)):
    if specChar == "Y":
        passDict = {
            1: random.choice(string.ascii_lowercase),
            2: random.choice(string.ascii_uppercase),
            3: str(random.randint(0, 9)),
            4: random.choice(SPECIAL_CHARS),
        }
    else:
        passDict = {
            1: random.choice(string.ascii_lowercase),
            2: random.choice(string.ascii_uppercase),
            3: str(random.randint(0, 9)),
        }
    randPass.append(passDict[random.randint(1, len(passDict))])
print("".join(randPass))
logging.debug(f"The password length is {len(randPass)}")
