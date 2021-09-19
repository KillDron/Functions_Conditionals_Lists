from datetime import datetime, timedelta
  

test_date1, test_date2 = datetime(2020, 8, 4), datetime(2021, 9, 19)

print("The original range : " + str(test_date1) + " " + str(test_date2))
  

dates = (test_date1 + timedelta(idx + 1)
         for idx in range((test_date2 - test_date1).days))
  

res = sum(1 for day in dates if day.weekday() < 5)
  

print("Total business days in range : " + str(res))
