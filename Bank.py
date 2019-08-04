"""
ייצר מחלקה בשם BankAccount המקבלת ב- init מספר חשבון, שם פרטי, שם משפחה ויתרה.
ייצר פונקציית str, repr למחלקה. ממש את המחלקה כך שכאשר משווים בין שני חשבונות ) == ( אז
אם היתרה זהה יוחזר אמת, אחרת יוחזר שקר. אם נשאל אם חשבון אחד גדול יותר מהשני יחזור
אמת אם היתרה בראשון גדול מהשני, אחרת שקר. כאשר נחבר שני חשבונות יוחזר סכום היתרות
שלהם
**אתגר: ממש פונקצית חיסור בין שני חשבונות, מכפלה בין שני חשבונות, פונקציית שונה )שים לב
שאין לממש לוגיקה חדשה בפונקציה זו, אלא להחזיר את הערך ההפוך של פונקציית ==(
**אתגר: שים את היתרה בשדה "סודי". יצר פונקציה בשם getBalance המקבלת כפרמטר שם
מדינה. אם המדינה היא ישראל החזר את הערך בשקלים )דיפולטי(, אם המדינה היא ארצות הברית
החזר בדולרים )חלק ב 7.3 )ואם היא צרפת החזר ביורו )חלק ב- 88.3)
***אתגר: שנה את פונקציית החיבור כך שראשית תיבדוק שהארגומנט השני הוא מסוג
BankAccount ,אם כן- תחזיר חשבון בנק חדש המכיל מספר חשבון חדש חדש )אקראי?(, איחוד של
שמות בעלי החשבון, ויתרה המורכבת מסכום היתרות
***אתגר: שנה את פונקציית החיבור כך שאם הארגומנט השני הוא מסוג int אז תגדל יתרת
החשבון בסכום שהתקבל
"""


class BankAccount:
    def __init__(self, accNumber, pName, lName, balance):
        self.accNumber = accNumber
        self.pName = pName
        self.lName = lName
        self.__balance = balance

    def getBalance(self, currency='nis'):  # I know this method is only good for printing and not for usage.
        if currency.lower() == 'usd':
            cents = int((self.__balance / 3.7) * 100)
            return f'{cents / 100} USD'
        if currency.lower() == 'eur':
            cents = int((self.__balance / 3.8) * 100)
            return f'{cents / 100} EUR'
        if currency.lower() == 'gbp':
            cents = int((self.__balance / 4.2) * 100)
            return f'{cents / 100} GBP'
        if currency.lower() == 'nis':
            return f'{self.__balance} NIS'

    def addToBalance(self, deposit):
        self.__balance += deposit

    def __add__(self, other):
        # if isinstance(other, BankAccount):    -> Old implementation, just adds balances of both accounts.
        #     self.addToBalance (other.__balance)
        if isinstance(other, BankAccount):
            return BankAccount((str(self.accNumber)+'_'+str(other.accNumber)),
                               self.pName+' and '+other.pName,
                               self.lName+'-'+other.lName,
                               self.__balance+other.__balance)
        if isinstance(other, int):
            temp = BankAccount(self.accNumber,self.pName,self.lName,self.__balance)
            temp.__balance+=other
            return temp

    def __iadd__(self, other):
        if isinstance(other, int):
            self.addToBalance(other)
            return self

    def __sub__(self, other):
        if isinstance(other, int):
            temp = BankAccount(self.accNumber, self.pName, self.lName, self.__balance)
            temp.__balance -= other
            return temp
        else:
            return None

    def __isub__(self, other):
        if isinstance(other, int):
            self.addToBalance(-other)
            return self
    def __eq__(self, other):
        return self.__balance == other.__balance

    def __ne__(self, other):
        return self.__balance != other.__balance  # שים לב שאין לממש לוגיקה חדשה  - לא הבנתי.

    def __ge__(self, other):
        return self.__balance >= other.__balance

    def __gt__(self, other):
        return self.__balance > other.__balance

    def __le__(self, other):
        return self.__balance <= other.__balance

    def __lt__(self, other):
        return self.__balance < other.__balance

    def __repr__(self):
        return f'\nBankAccount({self.accNumber}, {self.pName}, {self.lName}, {self.__balance})\n'

    def __str__(self):
        return f'\nBankAccount(class):\n' \
            f'Account Number: {self.accNumber}\n' \
            f'Full Name: {self.pName} {self.lName}\n'


keynan = BankAccount(21541032,
                     'Keynan',
                     'Tenenbom',
                     7000)
noam = BankAccount(330741444,
                  'Noam',
                  'Tobias',
                  7001)

print(keynan, noam)
print(keynan.__repr__())

keynan+=4000
print(keynan.getBalance())

keynan-=500
print(keynan.getBalance())

keynan+500
print(keynan.getBalance())

keynan = keynan+500
print(keynan.getBalance())

keynan = keynan-500
print(keynan.getBalance())
# combined = keynan + noam
# print(keynan.getBalance())
# print(noam.getBalance('GBP'))
# print(combined)
# print('Balance: '+combined.getBalance('Usd'))
