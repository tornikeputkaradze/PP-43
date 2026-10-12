# def create_account(owner, balance=0, history=None):
#     if history is None:
#         history = []
#
#     account = {
#         "owner": owner,
#         "balance": balance,
#         "history": history
#     }
#
#     return account
#
#
# def deposit(account, amount):
#     if amount <= 0:
#         return (False, "თანხა დადებითი უნდა იყოს")
#
#     account["balance"] = account["balance"] + amount
#     account["history"].append(f"+{amount}")
#
#     return (True, f"შეტანილია {amount} ლარი")
#
#
# def withdraw(account, amount, fee=0.5):
#     if amount <= 0:
#         return (False, "თანხა დადებითი უნდა იყოს")
#
#     total = amount + fee
#
#     if total > account["balance"]:
#         return (False, f"არასაკმარისი ბალანსი (საჭიროა {total})")
#
#     account["balance"] = account["balance"] - total
#     account["history"].append(f"-{total}")
#
#     return (True, f"გატანილია {amount} ლარი (საკომისიო {fee})")
#
#
# def statement(account, last=3):
#     print(f'--- {account["owner"]} | ბალანსი: {account["balance"]} ---')
#
#     if last > 0:
#         operations = account["history"][-last:]
#     else:
#         operations = []
#
#     for operation in operations:
#         print(operation)
#
#
# nino = create_account("ნინო", balance=100)
# luka = create_account("ლუკა")
#
# print(deposit(nino, 50))
# print(deposit(nino, -10))
#
# print(withdraw(nino, 30))
# print(withdraw(nino, 500))
# print(withdraw(nino, 20, fee=0))
#
# print(deposit(luka, 15))
#
# statement(nino)
# statement(nino, last=1)
# statement(luka)