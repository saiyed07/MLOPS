import smtplib

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
my_emailid="saiyedaliiqbal@gmail.com"
pswd=*******
mail.login(my_emailid,pswd)
mail.sendmail("saiyedaliiqbal@gmail.com", "saiyediqqbal@gmail.com","acuracy is good")
mail.close()
  