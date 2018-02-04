
#Creating a random unique 3-digit number
import random
gen = random.sample(range(10), 3)
gen =int((''.join([str(x) for x in gen])))
gen_nos = [int(d) for d in str(gen)]

#A function for the game!
def main():
  print ("Welcome to Code Breaker! \nA 3-digit code has been generated. Let's see if you can guess the number! \n Note:Enter 0 to give up!")
  
  #While loop for the code to run as many times till the user gives up or guesses right!
  while (1):
    try:    
      guess = int(input("Whats your guess?: "))
      if guess==0:
        print ("The Code generated is:",gen)
        break
      individual_nos = [int(d) for d in str(guess)]
      
      #Making sure the number is not less than 100 or greater than 999.
      if (guess<100 or guess>999):
        print ("Enter a valid 3-digit number!")
        
      else:
        if (guess == gen):
          print ("spot on! you won!")
          break
        elif (individual_nos[0]==gen_nos[0] or individual_nos[1]==gen_nos[1] or individual_nos[2]==gen_nos[2]):
          print ("MATCH")
        else:
          for i in individual_nos:
            if i in gen_nos:
              print ("CLOSE")
              break
            print ("NOPE")          
            break
            
    #Incase a non-integer is given as an input!      
    except ValueError:    
      print("That's not an integer! Please enter a valid 3-digit number!")

main()
