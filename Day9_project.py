logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dictionary1={}
def adder ():
    name=input("Enter your name:")
    bidds=int(input("Enter your bidds:$"))
    dictionary1.update({name:bidds})
adder()
tr=input("Enter yes if you want to Enter another person data:")
while tr=="yes":
    adder()
    tr=input("Enter yes if you want to Enter another person data:")
win=0
winner="none"
for keys in dictionary1:
    if dictionary1[keys]>win:
        win=dictionary1[keys]
        winner=keys
print(f"{winner} won having bidds {win}$")
