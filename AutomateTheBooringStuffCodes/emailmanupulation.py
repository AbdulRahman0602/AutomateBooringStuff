import smtplib

# Establish a connection to the SMTP server
conn = smtplib.SMTP("smtp.gmail.com", 587)

# Print the type of the conn object
print(type(conn))

conn.ehlo()
conn.starttls()

conn.login('abdulrahman2020abdullah@gmail.com','passwordl2')
conn.sendmail("abdulrahman2020abdullah@gmail.com","abdulrahman2020abdullah@gmail.com",'Subject:So lomg....\n\nDear Me,\nThis is to check my code \nThankingYou\nAR')
