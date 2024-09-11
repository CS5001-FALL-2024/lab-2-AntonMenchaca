'''
    CS 5001
    Lab 1
    Exercise 4
    Name:
'''

'''
Write a Python program to solve the general version of the problem below. Ask the user for the time now (in hours),
and ask for the number of hours to wait. Your program should output what the time will be on the clock when the
alarm goes off.

You look at the clock and it is exactly 11am. You set an alarm to go off in 51 hours.
At what time does the alarm go off?

You may assume military time, so 1pm is 13:00 hours. Here is some example output:

What time is it? 23
How long until your alarm expires? 4
Your alarm will expire at 3.
'''

def main():
    # YOUR CODE HERE
    print('What hour is it right now in military time? ')
    hour_now: int = int(input())
    print('How long in hours until your alarm expires? ')
    expire_time: int = int(input())
    alarm = (hour_now + expire_time) % 24
    if (hour_now + expire_time >= 24):
        days_passed = (hour_now + expire_time) // 24
        print(f'your alarm will will go off at {alarm}:00 military time, {days_passed} day(s) from now')    
        return
    print(f'your alarm will will go off at {alarm}')
if __name__ == '__main__':
    main()
