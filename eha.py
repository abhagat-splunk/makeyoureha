import os,imaplib,email,getpass

mail = imaplib.IMAP4_SSL('imap.gmail.com')
user = raw_input("Enter your username\n>")
passwd = ge=tpass.getpass("Enter your Password\n>")
mail.login(user, passwd)
mail.select("Inbox")

result,data = mail.search(None, "All")
ids = data[0]
id_split = ids.split()
x = int(raw_input("Enter the index of the emails till which you would want to find header for: "))

#y = int(raw_input("Enter the index till you want it done."))
#listing out the subjects.
for i in range(-x,0,1):
    check_id = id_split[i]
    res1,dat1 = mail.uid('fetch',check_id,'(RFC822)')
    raw_email=dat1[0][1]
    message = email.message_from_string(raw_email)
    print -i
    print "\tSubject:\t", message['Subject']

z = int(raw_input("Please enter the index of the email you want to analyze header of: \n>"))
check_id1 = id_split[-1]
res1,dat1 = mail.uid('fetch',check_id1,'(RFC822)')
raw_email=dat1[0][1]
message = email.message_from_string(raw_email)
print "1. To:\t", message['To']
print "2. From:\t",message['From']
print "3. Subject:\t", message['Subject']
print "4. Date:\t",message['Date']
print "5. Delivered To:\t",message['Delivered-To']
print "6. Message ID:\t",message['Message-ID']
print "7. MIME Version:\t",message['MIME-Version']
print "8. Content Type:\t",message['Content-Type']
print "9. DomainKey-Signature",message['DomainKey-Signature']
print "10. Recieved SPF:\t",message['Received-SPF']
print "11. Return-Path:\t",message['Return-Path']
print "12. Authentication-Results:\t",message['Authentication-Results']
print "13. DomainKey-Status:\t",message['DomainKey-Status']
# list1 = message.items()
# for k in range(0,13):
#     for z in range(0,2):
#         print list1[k][z]
#         print "\n"
   #  print dat1

mail.logout()
print "Logged out successfully."
