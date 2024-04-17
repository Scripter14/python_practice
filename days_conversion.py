'''
Given a number of days (N) as input,
 write a program to convert N to years (Y), weeks (W), and days (D).
'''
given_number_of_days=int(input())
to_convert_days_to_years=given_number_of_days//365
to_convert_days_to_weeks =(given_number_of_days-(365*to_convert_days_to_years))//7
to_convert_days_to_days=(given_number_of_days-(365*to_convert_days_to_years))-to_convert_days_to_weeks*7
print(to_convert_days_to_years,"years",to_convert_days_to_weeks,"weeks",to_convert_days_to_days,"days")
'''
input- 1329
output-
3 years 33 weeks 3 days'''