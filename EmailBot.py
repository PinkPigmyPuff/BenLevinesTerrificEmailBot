import csv, smtplib, ssl

message = """Subject: You pee/pooness

Hi {name}, your pee/pooness is {pee}"""

from_address = "bennysmith.532@gmail.com"
# to_address = ["ben.l24@k12.Xrds.org", "iloveewoks@icloud.com"]
password = "ldyivwrybtxdlcww"


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("test_content - Sheet1.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, pee in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name, pee=pee),
            )
