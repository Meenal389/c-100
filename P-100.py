class Atm(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo

    def CashWithdrawal(self):
        print("Cash Withdrawal means any amount obtained by use of the Debit Card or the PIN or in any manner authorised by the Debit Cardholder from an ATM, the Bank or any other bank or financial institution for debit to the Account.")

    def BalanceEnquiry(self):
        print("The Balance Inquiry function allows you to see the current balance on various types of accounts that a customer may have.")


card = Atm(3547826484,756)
card.CashWithdrawal()
card.BalanceEnquiry()