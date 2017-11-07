#Task 3

#FAHRENHEIT: when asked to enter the temperature in Celsius, it returns it in Fahrenheit
#Input: A prompt for the user to input the temperature in Celsius and the forumla to convert Celsius to Fahrenheit
#Output: The temperature in Fahrenheitt
def Fahrenheit():
    #This tells the function that we want to manually input the celsius when asked and uses a command statement to do so
    Celsius = float(raw_input("Enter the temperature in Celsius: "));
    #This also provides the function with the formula of how to convert Celsius to Fahrenheit
    Fahrenheit = (9.0/5.0)*Celsius + 32.0;
    #This is then the return statement once a temperature in Celsius is entered
    print 'The temperature in Fahrenheit:', Fahrenheit;

Fahrenheit()

print '---------'

#This is a list of temperatures in Celsius which we want to convert to Fahrenheit using Lambda
Temps_in_Celsius = [15,14,11,10,12,11,12,9,8]
#Here we use the feature of map to convert the temperatures given into Fahrenheit
mylist=map(lambda x:(float(9)/5)*x + 32, Temps_in_Celsius)
print 'Should return 59.0, 57.2, 51.8, 50.0, 53.6, 51.8, 53.6, 48.2, 46.4'
print 'Returns\t\t',mylist


