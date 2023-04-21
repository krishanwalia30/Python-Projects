
import mysql.connector

import random


mydb = mysql.connector.connect(host="localhost",user="root",passwd="abcd@1234")
mycur = mydb.cursor()


UPPERCASE_ALPHABETS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LOWERCASE_ALPHABETS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def CODE_GENERATOR_FOR_UPPERCASE():
     code = ""
     for i in range(no_encryption):
          code += UPPERCASE_ALPHABETS[random.randint(0,25)] 
     return code

def CODE_GENERATOR_FOR_LOWERCASE():
     code = ""
     for i in range(no_encryption):
          code += LOWERCASE_ALPHABETS[random.randint(0,25)]
     return code

def UPDATE_ENTRY_UPPERCASE():
     for i in range(len(UPPERCASE_ALPHABETS)):
          cmd = "UPDATE UPPERCASE SET CODE ='{}' WHERE ALPHABET = '{}'".format(CODE_GENERATOR_FOR_UPPERCASE(),UPPERCASE_ALPHABETS[i])
          mycur.execute(cmd)
          mydb.commit()
     cmd = "UPDATE UPPERCASE SET CODE = '{}' WHERE ALPHABET = ' '".format(CODE_GENERATOR_FOR_UPPERCASE())
     mycur.execute(cmd)
     mydb.commit()
     
def UPDATE_ENTRY_LOWERCASE():
     for i in range(len(LOWERCASE_ALPHABETS)):
          cmd = "UPDATE LOWERCASE SET CODE ='{}' WHERE ALPHABET = '{}'".format(CODE_GENERATOR_FOR_LOWERCASE(),LOWERCASE_ALPHABETS[i])
          mycur.execute(cmd)
          mydb.commit()
     cmd = "UPDATE LOWERCASE SET CODE = '{}'WHERE ALPHABET =' '".format(CODE_GENERATOR_FOR_LOWERCASE())
     mycur.execute(cmd)
     mydb.commit()


     
def DECRIPT_CHECKER_FOR_UPPER_OR_LOWER_CASE(message,cod=""):
     mycur.execute("SELECT CODE FROM UPPERCASE WHERE ALPHABET = 'A'")
     for i in mycur:
          for j in i:
               number = len(j)
     parts = [message[i:i+number] for i in range(0, len(message), number)]
     for i in parts:
          if i.isupper():
               cod += DENCRIPT_UPPERCASE_MESSAGE(i) 
          elif i.islower():
               cod += DENCRIPT_LOWERCASE_MESSAGE(i)
          else:
               cod += DENCRIPT_LOWERCASE_MESSAGE(i)
     return cod
               
def DENCRIPT_UPPERCASE_MESSAGE(message,cod=""):
     cmd = "SELECT ALPHABET FROM UPPERCASE WHERE CODE = '{}'".format(message)
     mycur.execute(cmd)
     for j in mycur:
          for k in j:
               cod += k
     return cod
     
def DENCRIPT_LOWERCASE_MESSAGE(message,cod=""):
     cmd = "SELECT ALPHABET FROM LOWERCASE WHERE CODE = '{}'".format(message)
     mycur.execute(cmd)
     for j in mycur:
          for k in j:
               cod += k
     return cod

def ENCRIPT_UPPERCASE_MESSAGE(message,cod=""):
     for i in message:
          cmd = "SELECT CODE FROM UPPERCASE WHERE ALPHABET ='{}'".format(i)
          mycur.execute(cmd)
          for j in mycur:
               for k in j:
                    cod += k
     return cod

def ENCRIPT_LOWERCASE_MESSAGE(message,cod=""):
     for i in message:
          cmd = "SELECT CODE FROM LOWERCASE WHERE ALPHABET ='{}'".format(i)
          mycur.execute(cmd)
          for j in mycur:
               for k in j:
                    cod += k
     return cod

def ENCRIPT_CHECKER_FOR_UPPER_OR_LOWER_CASE(message,cod=""):
     for i in message:
          if i.isupper():
               cod += ENCRIPT_UPPERCASE_MESSAGE(i)
          elif i.islower():
               cod += ENCRIPT_LOWERCASE_MESSAGE(i)
          else:
               cod += ENCRIPT_LOWERCASE_MESSAGE(i)
     return cod

#MAIN

login = input("ENTER THE PASSWORD :")
password = "QWERTY"
if login == password:
     print()
     print()
     print("                        WELCOME TO THE ENCRIPTION SOFTWARE    ")
     print("                                             ")
     print()
     print()
     program = input("TYPE 1 TO CONTINUE OR ANYTHING TO EXIT: ")
     if program == "1":
          program = True
          while program:
               print()
               print("TYPE 'A' TO ENCRIPT A MESSAGE")
               print()
               print("TYPE 'B' TO DECRIPT A MESSAGE")
               print()
               print("TYPE 'C' TO UPDATE THE CODES")
               print()
               print("TYPE 'D' TO EXIT THE SOFTWARE")
               choice = input("ENTER YOUR CHOICE: ")
               if choice =='A':
                    print()
                    message = input("ENTER THE MESSAGE TO BE ENCRIPTED: ")
                    code = ENCRIPT_CHECKER_FOR_UPPER_OR_LOWER_CASE(message)
                    print("THE ENCRIPTED MESSAGE IS: ",code)

               elif choice =='B':
                    print()
                    message = input("ENTER THE ENCRIPTED MESSAGE: ")
                    code = DECRIPT_CHECKER_FOR_UPPER_OR_LOWER_CASE(message)
                    print()
                    print("THE DECRIPTED MESSAGE IS: ",code)
                    
               elif choice =='C':
                    no_encryption = int(input("ENTER THE NO OF ENCRYPTION: "))
                    UPDATE_ENTRY_UPPERCASE()
                    UPDATE_ENTRY_LOWERCASE()
                    print("ALL THE CODES HAVE BEEN REVISED.")
               elif choice =='D':
                    quit()
               else:
                    print()
                    print("PLEASE CHOOSE FROM THE GIVEN OPTIONS")
                    print()
     else:
          quit()
else:
     print("ACCESS DENIED")
     quit()

