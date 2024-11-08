# Password Checker
username = input('what is your username?')
password = input('what is your password?')
password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, Your Password, {hidden_password}, is {password_length} letters long')


#Car Quality Check
Reliable_Cars = ('lexus', 'Toyota', 'Mazda', 'Honda')
Non_Reliable_Cars = ('Audi', 'Chrysler' 'Range_Rover', 'Alfa_Romeo')

car = input('what car do you drive? ')

if car in Reliable_Cars:
    print(f"{car} is considered a reliable car!")
elif car in Non_Reliable_Cars:
    print(f"{car} is considered a non-reliable car.")
else:
    print(f"{car} is not in our list.")
