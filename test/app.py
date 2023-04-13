import smtplib
from email.mime.text import MIMEText
 
text = "메일 내용입니다"
msg = MIMEText(text) 
 
msg['Subject'] ="이것은 메일제목"
msg['From'] = 'psw4978@naver.com'
msg['To'] = 'psw4978@swpe.co.kr'
print(msg.as_string())
 
s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
s.starttls() #TLS 보안 처리
s.login( 'psw4978' , 'qwer8456123' ) #네이버로그인
s.sendmail( 'psw4978@naver.com', 'psw4978@swpe.co.kr', msg.as_string() )
s.close()