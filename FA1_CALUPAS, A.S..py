print('FA1_CALUPAS, A.S.\n')

# 1. How many seconds are there in 42 minutes 42 seconds?
minutes = 42
seconds = 42
total_seconds = (minutes * 60) + seconds
print('1.) There are %.0f seconds in %.0f minutes %.0f seconds.\n' %(total_seconds,minutes,seconds))

# 2. How many miles are there in 10 kilometers? (Hint: there are 1.61 kilometers in a mile.)
kilometers = 10
km_per_mile = 1.61
total_miles = kilometers / km_per_mile
print('2.) %.2f kilometers is equal to %.2f miles.\n' %(kilometers,total_miles))

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour? 
distance_ran_in_km = 10
km_per_mile = 1.61
miles = distance_ran_in_km / km_per_mile

minutes = 42
seconds = 42
time_in_seconds = (minutes * 60) + seconds

pace_per_mile_in_seconds = time_in_seconds / miles # Time per mile in seconds
pace_minutes = int(pace_per_mile_in_seconds // 60) # Divide in whole minutes
pace_seconds = int(pace_per_mile_in_seconds % 60) # Remainders as seconds
print('3.a.) The average pace per mile is %.0f minutes %.0f seconds.\n' %(pace_minutes,pace_seconds))

hours = time_in_seconds / 3600
mph = miles / hours
print('3.b.) The average speed is %f mph.' %(mph))
