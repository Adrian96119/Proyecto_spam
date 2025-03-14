
#mensajes de prueba para testear
messages = [
    "Congratulations! You've just won a $1000 gift card. Visit www.bestdeal.com to claim it now! Don't miss out!",
    "Can you send me the report by tomorrow morning? I need it for the meeting. Thanks!",
    "Hi, you have a package waiting for pickup! To reschedule, click on this link: www.pickupyourpackage.com",
    "Reminder: Your dentist appointment is scheduled for Monday at 10 AM. Please call to reschedule if needed.",
    "Free iPhone 15 Giveaway! Text 'WIN' to 12345 now for a chance to win. Only a few left, act fast!",
    "Hey, do you want to grab coffee tomorrow at 3pm? Let me know if that works for you.",
    "Limited time offer: Buy 1 get 1 free on all items! Text 'YES' to claim your free gift now. Hurry, this offer ends soon!",
    "I hope you're having a good day! I was thinking about our conversation last week—let’s catch up soon.",
    "URGENT! Your bank account has been compromised. Click here to secure your account: http://secure-your-account-now.com",
    "Just checking in to see if you received my email about the project. Let me know your thoughts when you can."
]


 # Lista de palabras comunes en mensajes de spam
spam_words = ["win", "free","free!" "urgent","urgent!","urgent.","attention","attention!","oportunity!","oportunity.","oportunity",
"exclusive","exclusive!", "reward","reward!", "bonus","bonus." "offer","offer!","congratulations!","clik!","clik","click here","click now","click now!",
              "click on","click on!","click here!","click in",
    "congratulations","alert","alert!","credit","credit!","selected","private!","action required","selected!","stop","stop!","now","now!","call now","call now!","mobile","mobile!","vip","vip!","vip.","importan","important.","important!"]



#columnas numéricas para normalizar
numeric_features = ['special_char_count', 'exclamation_count', 'number_count',
                   'emoticon_count', 'message_length', 'spam_word_count',
                   'stop_word_ratio', 'uppercase_word_count', 'url_count']

#columnas con las que necesito para mis test
columnas_importantes = [
    'special_char_count', 'exclamation_count', 'number_count', 'emoticon_count',
    'message_length', 'spam_word_count', 'stop_word_ratio',
    'uppercase_word_count', 'url_count', 'mensaje_limpio']