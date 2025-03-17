import csv

import os

def secure():
    """
    sig:
    main function, uses other functions and operations to detect intruder and compile information about the attack
    """
    Master_code = '123456'
    correct_pass = 'YamaniMpofu'
    correctls = list(correct_pass)
    CODE_LEN = len(correct_pass)
    while True:
        #Prompting user for passcode 
        while True:
            code = input('Enter passcode: ')
            if len(code) != CODE_LEN:
                print(f'passcode should have {CODE_LEN} characters')
            else:
                break 
        
        #Adding NULL character to easily detect end of string
        code1 = code + '\0'
        #Converting the input to a list for convinience in iteration and indexing
        liscode = list(code1)
        #Number of correct characters and their related levels of threat
        lvl1 = round(0.25 * CODE_LEN)
        lvl2 = round(0.5 * CODE_LEN)
        lvl3 = round(0.75 * CODE_LEN)
        lvl4 = CODE_LEN - 2
        #Cater for correct password input 
        if code == correct_pass:
            return 0
        else:
            #Determinng level of threat
            lvl = matched(correctls,CODE_LEN,liscode)
        #Giving user N chances to enter correct passcode
        chances(correct_pass,level(lvl,lvl1,lvl2,lvl3,lvl4),Master_code)
        
        break
    #Creating class Intruder which records how much of personal data is mentioned in the password attempts
    class Intruder:
        def __init__(self,Birthdays,College_grad,):
            self.Birthdays = Birthdays
            self.College_grad = College_grad
        def __str__(self):
            return(f'Birthdays known are{self.Birthdays}, and College graduations known are{self.College_grad}')
        def __truediv__(self,input):
            return (self.Birthdays + self.College_grad) / (input.Birthdays + input.College_grad)
    #Loading "Perfect_Hack" variable of class Intruder,with all personal information about user
    with open('Personal_info.csv','r') as file:
        B_D = 0
        cllg = 0
        ready = csv.reader(file,delimiter=',')
        for line in ready:
            if line[2] == 'Birthday':
                B_D += 1
            if line[2] == 'College':
                cllg += 1 
        Perfect_Hack = Intruder(B_D, cllg)
        B_D = 0
        cllg = 0
        #Loading "Hacker variable" of class Intruder,with all personal information about user that showed up in password attempts
        with open('hack_attempts.csv','r') as file2:
            ready2 = csv.reader(file2,delimiter=',')
            #Catering for items to not be counted more than once
            seen = []
            dicti = {}
            for line2 in ready2:
                file = open('Personal_info.csv','r')
                ready = csv.reader(file,delimiter=',')
                for line in ready:
                    if (line[3] == line2[2]) and (line[3] in seen ) == False:
                        if line[2] == 'Birthday':
                            B_D += 1 
                            dicti[line[0]] = line[2]
                        if line[2] == 'College': 
                            cllg += 1 
                            dicti[line[0]] = line[2]
                        seen.append(line[2])
                        seen.append(line[3])
            Hacker = Intruder(B_D, cllg)
            index = round(Hacker / Perfect_Hack,2)
            #Report a summary that gives quantitative information about the risk hacker is to personal privacy
            with open(os.path.join('hack_attempts.txt'),'a') as file1:
                file1.write(f'Hello, I am concerned to report that there has been a security breach attempt. I have collected the following information about the breach attempt:\nThe Hacker knows the following information about the following people{dicti}\nI have calculated the hacker index,\nthis is a ratio of amount of personal data stored in your database to the amount of personal data I detected from the password attempts by the intruder,\nI have found this number to be {index}\n')
                if index < 0.07:
                    file1.write('Intruder is harmless acoording to my calculation, and there is no immediate cause for you to review your passwords, carefull with where you leave your devices next time\n')
                if index > 0.07 and (index < 0.6):
                    file1.write('Intruder knows a small amount of information about you, you may wish to review your passwords')
                if index > 0.6 and (index < 0.85):
                    file1.write('Intruder knows an alarmingly large amount of you personl data, you might want to look more into securing your information')
                if index > 0.85:
                    file1.write('Intruder is closely familiar with you, you should take great caution with your privacy')   
    
    return 1


def chances(a,b,c):
    """
    sig:
    str,int,str -> none
    Prompts user for password n chances, n depends on how much of threat intruder is i.e how much of the password they know.
    """
    file_dir = os.getcwd()
    csvf = os.path.join(file_dir,'hack_attempts.csv')
    if b != 4:
        for i in range((10 - (2 * b))):
            print(f'Incorrect passcode. You have {10 - (2 * b) - i} chances remaining')
            x = input('Enter passcode: ')
            if x == a:
                return 0 
        scanner(c)
    else: 
        scanner(c)
    return 1
 
     
def scanner(Key):
    """
    sig:
    str -> none
    prompts the user for input for as long as the input is not the master key
    """
    file_dir = os.getcwd()
    file_name = os.path.basename(file_dir)
    i = 1
    with open('hack_attempts.csv','a') as file:
        while True:
            code = input('Enter passcode: ')
            if code != Key:
                ready = csv.writer(file)
                ready.writerow([file_name,i,code])
                i += 1
                
            else:
                
                return 1
 
                     
def level(l,a,b,c,d):
    """
    sig:
    int -> int 
    
    Gives level of threat intruder is on a scale of 1 to 4
    """
    if l >= d:
        return 4
    if (l > 0) and l <= a:
        return 1
    if (l > a )and l <= b:
        return 2
    if (l > b )and l <= c:
        return 3
    return 0
  
  
def matched(correctls,attempt_len,attempt_list): 
    """
    sig:
    list,int,list -> int
    Counts number of charecters matched in each attempt
    """

  
    a = 0
    c = attempt_len - 2
    for j in range(attempt_len):
        if attempt_list[j] == correctls[j]:
            a += 1    
    return a

secure()
    
                    

            
                    
        
        
        
        
