class Client:
    name="default"
    phone="(123)456-7890"
    email='foo@bar.com'
    purchases=0

def main():
    firstClient=Client()
    print(firstClient.name)
    print(firstClient.email)
    print(firstClient.phone)
    print(firstClient.purchases)
    firstClient.name="Prashanth"
    firstClient.purchases=10
    print(firstClient.name)
    print(firstClient.purchases)

main()