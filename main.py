height = input('Please enter your height'+'\n')

weight = input('Please enter your weight'+'\n')

height = (float(height))

weight = (float(weight))

bmi = weight/(height**2)



if bmi < 18.5 :
  print('Your below normal')
elif bmi >= 18.5 and bmi <= 25 :
  print('Your are normal')
elif bmi >= 25 and bmi <= 30 :
  print('Your are overweight')
elif bmi >= 30 and bmi <= 40 :
  print('Your are badly overweight')
elif bmi >= 40 :
  print('Your are extremly overweight')
  
print(bmi)