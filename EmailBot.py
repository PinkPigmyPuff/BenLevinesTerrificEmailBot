import csv
import random
import smtplib
import ssl
import time

# The message that the email bot will send
# "Subject" and "To" are both custom, and set the respective parts of the email
# Anything in curly braces acts as a variable which we can specify when we send the message
message = """Subject: Merch Question
To: {to_address}
Hello,

I hope whoever is receiving this is having a great day! My name is Ben Levine and I'm currently a junior in high school. While it might seem strange considering I live nowhere close, I have become a massive fan of {name} via the internet. I have no clue if this is a possibility but it would mean a lot. Could you possibly send me a pin, hat, t-shirt, hoodie, or any other piece of merch, so I can represent you here in Los Angeles?

Thank you so much for even the consideration!

Thanks,
Ben Levine

Address:
10344 Cheviot Dr
Los Angeles, California 90064"""

#from_address = "bennysmith.532@gmail.com"
#password = "ldyivwrybtxdlcww"

from_address = "benlevine005@gmail.com"
#password = "Barklamb5%!%!"
password = "crgtffilxsbiavvb"


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("test_content - Sheet1.csv") as file:
        reader = csv.reader(file)
        for email, name in reader:
            time.sleep(random.randrange(2, 5))
            print(f"Sending an email from: {from_address} to {email}, under the name {name}")
            server.sendmail(
                from_address,
                email,
                message.format(name=name, to_address=email),
            )

# SENT STATUS: Up to fj@FlintJ.com, under the name The Flint Journal
