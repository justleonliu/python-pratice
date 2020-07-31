height = input('Please enter your height'+'\n')

weight = input('Please enter your weight'+'\n')

height = (float(height))

weight = (float(weight))

bmi = weight/(height**2)




if bmi >= 18.5 and bmi <= 25 :
  print('Your Bmi is normal')
elif bmi >= 25 and bmi <= 30 :
  print('Your Bmi is overweight')
elif bmi >= 30 and bmi <= 40 :
  print('Your Bmi is badly overweight')
elif bmi >= 40 :
  print('Your Bmi is extremly overweight')
  
print(bmi)