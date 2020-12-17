

from google_trans_new import google_translator  
  
translator = google_translator()  



print('This language will be converted to English ->')
x = str(input())
print('')
print('')
print('')
print('')
try:
    trans_text = translator.translate(x,lang_tgt='en')
    print('Translated Text ->')
    print(trans_text)
except Exception as e:
    print(str(e)+' or poor Internet Connection' )
while True:
    if input()=='':
        break
    elif input():
        break






