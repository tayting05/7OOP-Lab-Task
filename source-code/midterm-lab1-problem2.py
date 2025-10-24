message = "Dear John,I hope this email finds you well.\nI wanted to reach out and say hello.\nI hope you are doing well and enjoying your day.\nIt's been a while since we last we spoke, and I wanted to catch up with you.\nLet's plan to meet up soon and have a great time together!"
subj_name = "Jane"
sender_name = "Jane"
ver_num = 1.2
discount = 10.50
status = 'A'
code = "ABCD123"
loc_name = "City XYZ"
_age = 30
company_name = "ABC Corporation"
web_name = "www.example.com"
phone_num = "+1 123-456-7890"
job_title = "Software Engineer"
depart_name = "Engineering"

print("%s \nSubject: %s\nVersion: %.1f" % (message,sender_name,ver_num,))
print("Discount: %.2f" %(discount), end='%\n')
print("Status: %c\nCode: %s\nLocation: %s\nAge: %d\nCompany: %s\nWebsite:%s\nPhone: %s\nJob Tittle: %s\nDepartment: %s"%(status,code,loc_name,_age,company_name,web_name,phone_num,job_title,depart_name))
