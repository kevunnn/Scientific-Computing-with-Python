class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.total = list()

    def __str__(self):
        star = "*" * int((30 - len(self.category)) / 2)
        ledger = ''
        for list in self.ledger:
            desc = list['description']
            amt = float(list['amount'])
            final_amt = str(f"{amt:.2f}")
            if len(desc+final_amt) > 30:
                desc = desc[0:(30-len(final_amt)-1)]
            elif len(desc+final_amt) < 30:
                desc = desc+' '*(30-len(desc+final_amt)-1)
            ledger += desc + ' ' + final_amt + '\n'
        if len(self.category) % 2 == 0:        
            return f"{star}{self.category}{star}\n{ledger}Total: {sum(self.total)}"
        else:
            return f"{star}*{self.category}{star}\n{ledger}Total: {sum(self.total)}"

    def deposit(self, amount: float, description=""):
        self.amount = amount
        self.total.append(amount)
        self.description = description
        self.dict = dict()
        self.dict["amount"] = self.amount
        self.dict["description"] = self.description
        self.ledger.append(self.dict)

    def withdraw(self, amount: float, description=""):
        self.amount = amount
        self.total.append(amount * -1)
        self.description = description
        self.dict = dict()
        self.dict["amount"] = self.amount * -1
        self.dict["description"] = self.description
        if self.amount > sum(self.total):
            return False
        else:
            self.ledger.append(self.dict)
            return True

    def transfer(self, amount: float, new_category: str):
        self.amount = amount
        self.new_category = new_category
        if self.amount > sum(self.total):
            return False
        else:
            self.withdraw(self.amount, f"Transfer to {self.new_category.category}")
            self.new_category.deposit(self.amount, f"Transfer from {self.category}")
            return True

    def get_balance(self):
        total = sum(self.total)
        return total
    
    def check_funds(self, amount):
        self.amount = amount
        if self.amount > sum(self.total):
            return False
        else:
            return True

def create_spend_chart(categories):
    withdrawn = []
    cat_amount = {}
    names = []
    lines = '-' * (len(categories) * 3 + 1)
    visualization = []
    final_lines = ''
    percentages = range(100, -10, -10)
    final_ = ''
    cat = []
    cline = '     '

    for category in categories:
        names.append(category.category)
        for list in category.ledger:
            if list['amount'] < 0:
                withdrawn.append(list['amount'])
        for amount in withdrawn:
            cat_amount[category.category] = amount * -1

    for percentage in percentages:
        line = f"{percentage}| "
        for category in categories:
            if (float(cat_amount[category.category]) / float(sum(withdrawn) * -1) * 100) >= percentage:
                line += "o  "
            else:
                line += "   "           
        visualization.append(line)  
    for line in visualization[0:-2]:
        final_lines += line + '\n '
    for line in visualization[-2:-1]:
        final_lines += line + '\n  '
    
    
    max_length = max(len(name) for name in names)
    for i in range(max_length):
        for name in names:
            if i < len(name):
                cline += name[i] + '  '
            else:
                cline += '   '
        cline += '\n     '
    cat.append(cline)
    for _str in cat:
        final_ += _str + '  \n     '
        final_ = final_.rstrip()
    final_lines += visualization[-1] + '\n    ' + lines + '\n' + final_ + '  '
    return(f"Percentage spent by category\n{final_lines}")