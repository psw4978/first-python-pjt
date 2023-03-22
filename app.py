파일 = open('b.txt', 'w')
파일.write('삼성전자')
파일.close()

파일 = open('b.txt', 'a')
파일.write ('\n카카오\n네이버\n신풍제약')
파일.close()

파일 = open('b.txt', 'r')
print (파일.read())
파일.close()


