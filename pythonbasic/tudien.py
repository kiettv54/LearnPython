database = {
	'Baby':'Em bé',
	'Home':'Nhà',
	'Day':'Ngày'
}
def Show():
	print('------------------------------------------------------------------')
	print('-                 Dictionary English-Vietnamese                  -')
	print('------------------------------------------------------------------')
	print('- 0.Exit                                                         -')
	print('- 1.View                                                         -')
	print('- 2.Add                                                          -')
	print('- 3.Delete                                                       -')
	print('- 4.Change                                                       -')
	print('- 5.Find                                                         -')
	print('------------------------------------------------------------------')
def View():
	for word,mean in database.items():
		print('%s : %s' % (word,mean))
def Add():
	word=str(input('New words:'))
	mean=str(input('Mean is:'))
	word.title()
	database[word] = mean
	print('New words have been added!')

def Delete():
	word = str(input('Enter the word to delete:'))
	word.title()	
	for word in database:
			del database[word]
def Change():
	word=str(input('Enter the word:'))
	word.title()
	if word in database:
		word2=str(input('Enter new means:'))
		database[word]=word2
		print('Changed!')
	else:
		print('No word:',word)
def Find():
	word = str(input('Enter the word to find:'))
	word.title()
	if word in database:
		print('%s : %s' % (word,database[word]))
	else:
		print('No word:',word)
Show()
choose=int(input('You choose:'))
while choose !=0:
	if choose == 0:
		break
	elif choose == 1:
		View()
	elif choose == 2:
		Add()
	elif choose == 3:
		Delete()
	elif choose == 4:
		Change()
	elif choose == 5:
		Find()
	else :
		print('No choice !')
	choose = int(input('You choice:'))
