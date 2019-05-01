def account(initial_balance):
    """A bank account that allows deposits, withdrawals, and
    retrieving the balance.

    >>> a = account(100)
    >>> a('get_balance')()
    100
    >>> a('withdraw')(10)
    90
    >>> a('deposit')(20)
    110
    >>> a('withdraw')(200)
    'Insufficient funds'
    >>> a('get_balance')()
    110
    """
    def deposit(amount):
        new_balance = dispatch['balance'] + amount
        dispatch['balance'] = new_balance
        return new_balance
    def withdraw(amount):
        balance = dispatch['balance']
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        dispatch['balance'] = balance
        return balance
    def get_balance():
        return dispatch['balance']
    dispatch = {}
    dispatch['balance'] = initial_balance
    dispatch['deposit'] = deposit
    dispatch['withdraw'] = withdraw
    dispatch['get_balance'] = get_balance
    def dispatch_message(message):
        return dispatch[message]
    return dispatch_message

def checking_account(initial_balance):
    """A checking account that charges a $1 fee for withdrawal.

    >>> a = checking_account(100)
    >>> a('get_balance')()
    100
    >>> a('withdraw')(10)
    89
    >>> a('deposit')(20)
    109
    >>> a('withdraw')(200)
    'Insufficient funds'
    >>> a('get_balance')()
    109
    >>> a('get_balance').__qualname__ # check for code reuse
    'account.<locals>.get_balance'
    """
    def withdraw(amount):
        pass # replace with your code
    dispatch = {}
    # add any code you need here
    dispatch['withdraw'] = withdraw
    def dispatch_message(message):
        pass # replace with your code
    return dispatch_message
