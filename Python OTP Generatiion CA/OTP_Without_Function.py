import random
import smtplib

# Set your email credentials
EMAIL_ADDRESS = "mayurpawar9182736455@gmail.com"
EMAIL_PASSWORD = "wvya kagd bobm beuh"

# Set the recipient's email address
RECIPIENT_EMAIL = "mayurvpawar8@gmail.com"

# Generate a random 6-digit OTP
otp = random.randint(100000, 999999)

# Set the email subject and body
subject = "OTP"
body = f"Your OTP is: {otp}"

# Connect to the email server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Send the email
server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, f"Subject: {subject}\n\n{body}")

# Disconnect from the server
server.quit()

print("OTP sent successfully!")
