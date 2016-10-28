# CSci 1133 HW 2
# Kayla Engelstad
# HW Problem 2A
#
# WORKOUT BURN PROGRAM
# Using the user's input for age, weight (lbs), average heart rate (bpm),
# and workout duration (min), WORKOUT BURN PROGRAM will calculate the amount
# of calories burned for both a male and a female using the same data.
#
#   Man: Calories burned = [(Age x 0.2017) — (Weight x 0.09036) + (Average
#   Heart Rate x 0.6309) — 55.0969] x Time of Workout / 4.184
#
#   Woman: Calories burned = [(Age x 0.074) — (Weight x 0.05741) + (Average
#   Heart Rate x 0.4472) — 20.4022] x Time of Workout / 4.184

# define male function
def male_burn(age, weight, av_hr, time):

# put data into male equation
    m_cal = ((age * 0.2017) - (weight * 0.09036) + (av_hr * 0.6309) - 55.0969) * time / 4.184

# return male calories burned
    return m_cal
    

# define female function
def female_burn(age, weight, av_hr, time):
    
# put data into female equation
    f_cal = ((age * 0.074) - (weight * 0.05741) + (av_hr * 0.4472) - 20.4022) * time / 4.184
    
# return female calories burned
    return f_cal

    

# obtain data from the user.
print("To find out how many Calories a woman and man would burn during a\nworkout, please fill out the information.\n\n")
u_age = float(input("Enter age in years: "))
u_weight = float(input("Enter weight in lbs: "))
u_av_hr = float(input("Enter average heart rate during workout: "))
u_time = float(input("Enter the duration of the workout in minutes: "))

#call m and f functions
mresults = male_burn(u_age, u_weight, u_av_hr, u_time)
fresults = female_burn(u_age, u_weight, u_av_hr, u_time)

#print results with message
print("\n\nA man burns", int(mresults), "caloreis.\nA woman burns", int(fresults), "calories.")

