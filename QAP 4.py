#Discriptiom: Create Invoice For One Stop Insurace. 
#Name: Morgan Browne
#Date: March 17th 2024

import datetime
import FormatValues as FV

def IsValidLetter(letter):
    ALLOWED_CHAR_SET = set("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-. '1234567890")
    return set(letter).issubset(ALLOWED_CHAR_SET)

def IsValidNum(name):
    ALLOWED_NUM_SET = set("1234567890-")
    return set(name).issubset(ALLOWED_NUM_SET)




# Bring over defaults for program
f = open( 'Defualt.dat', 'r')
POLICY_NUM = int(f.readline())
BASE_PREMIUM = float(f.readline())
DISS_CAR = float(f.readline())
LIABLE_COVER = float(f.readline())
GLASS_COVER = float(f.readline())
LOAN_COVER = float(f.readline())
HST_RATE = float(f.readline())
PRO_FEE_PAYMENT = float(f.readline())
f.close()



def PaymentOptions():
        PAY_OPTIONS = ["Full", "Monthly", "Down Payment"]
        while True:
            PayOption = input("How is the customer paying (Full, Monthly or Down Payment): ").title()
            if PayOption not in PAY_OPTIONS:
                print("Invalid option.")
            else:
                return PayOption
        
def MonthlyPay(TotalCost, DownPayment):
        if DownPayment > 0:
            TotalCost -= DownPayment
        MonthlyPayments = (TotalCost + PRO_FEE_PAYMENT) / 8
        return MonthlyPayments
     
def DownPayValidation(DownPay):
        DownPay = 0
        if not DownPay.strip():  
            return False, "Input cannot be empty."
    
        if not DownPay.replace('.', '', 2).isdigit():
            return False, "Invalid input. Please enter a valid number for the down payment."
    
        DownPay = float(DownPay)
        if DownPay >= 0:
            return True, DownPay
        else:
            return False, "Down payment must be a positive number."
     
     
PrevCusClaimLst = []    
def PrevCusClaimInfo(PrevCusClaimLst):
        
        while True:
            PrevCusClaim = input("Does the customer have any previous claims? (Y OR N): ").upper()
            if PrevCusClaim == "N":
                break
            elif PrevCusClaim != "Y":
                print("Data Entry Error - Must enter either Y OR N.")
                continue
            
            PrevClaimNum = input("Enter the previous claim number:")
            if not IsValidNum(PrevClaimNum):
                print("Data Entry Error - Must use a numerical value.")
                continue

            PrevClaimDate = input("Enter the previous claim date (YYYY-MM-DD): ")
            if not IsValidLetter(PrevClaimDate):
                print("Data Entry Error - must use correct date.")
                continue

            PrevClaimAmnt = input("Enter the previous claim amount: ")
            if not IsValidNum(PrevClaimAmnt):
                print("Data Entry Error - must use numerical value. ")
                continue

            PrevCusClaimLst.append(PrevClaimNum, PrevClaimDate, PrevClaimAmnt)
            return PrevCusClaimLst


while True: 
    #Gather user input
    while True: 
        FirstName = input("Enter the custommers first name: ").title()
        if FirstName == "":
            print("Data Entry Error - Customr First Name Cannot Be Blank.")
        else:
            break

    while True:
        LastName = input("Enter the customers last name: ").title()
        if LastName =="":
            print("Data Entry Error - Customr First Name Cannot Be Blank.")
        else:
            break

  
    ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
    while True:
        Prov = input("Enter the customer province (XX): ")
        if Prov == "":
            print("Error - cannot be blank.")
        elif len(Prov) != 2:
            print("Error - must be 2 characters only.")
        elif Prov not in ProvLst:
                print("Error - invalid province.")
        else:
            break

    while True:
      Address = input("Enter the customers Address: ").title()
      if Address == "":
            print("Data Entry Error - Address Cannot Be Blank.")
      else:
           break
    while True:
        City = input("Enter the customers City: ").title()
        if City == "":
            print("Data Entry Error - City Cannot Be Blank.")
        else:
             break
    while True:
         PostCode = input("Enter the custmers Postal Code (A1A A1A): ").title()
         if PostCode == "":
                print("Data Entry Error - Postal Code Cannot Be Blank.")
         else:
              break
    while True:
         PhoNum = input("Enter the customers phone number (9999999999): ")
         if PhoNum == "":
                print("Data Entry Error - Phone Number Cannot Be Blank.")
         else:
              break

    while True:
         NumCars = input("Enter the number of cars being insured: ")
         NumCars = int(NumCars)
         if NumCars == "":
                print("Data Entry Error - Number Of Cars Cannot Be Blank.")
         else:
              break
   
    while True:
         InsurOpt = input("Extra Coverage up to $1,000,000 (Y 0R N): ")
         if InsurOpt =="":
            print("Data Entry Error - Extra Coverage Cannot Be Blank.")
         else:
            break
    while True:
         GlassCover = input("Glass Coverage (Y OR N): ")
         if GlassCover =="":
            print("Data Entry Error - Glass Coverage Cannot Be Blank.")
         else:
              break
    while True:
         LoanCar = input("Loaner Car (Y OR N): ")
         if LoanCar == "":
            print("Data Entry Error - Loaner Car Cannot Be Blank.")
         else:
              break



# Calculations 
           
    TotalCost = BASE_PREMIUM + (NumCars - 1) * (BASE_PREMIUM * DISS_CAR)
    AddedCosts = 0
    if InsurOpt == "Y":
            TotalCost += NumCars * LIABLE_COVER
            AddedCosts += NumCars * LIABLE_COVER
    if GlassCover == "Y":
            TotalCost += NumCars * GLASS_COVER
            AddedCosts += NumCars * GLASS_COVER
    if LoanCar == "Y":
            TotalCost  += NumCars * LOAN_COVER
            AddedCosts  += NumCars * LOAN_COVER

    HST = TotalCost * HST_RATE
    PayOption = PaymentOptions()
    while True:
        if PayOption == "Down Payment":
            while True:
                    try:
                        DownPay = input("Enter the amount the customer will pay down: ")
                        ValidateDownPayment = DownPayValidation(DownPay)
                        if ValidateDownPayment:
                            DownPay = float(DownPay)
                            break
                    except ValueError:
                        print("Data Entry Error - must enter numeric value. ")
                    if DownPay > TotalCost:
                        print("Data Entry Error - Down Payment must be less than total cost. ")
                    else:
                        break
        else:
            DownPay = 0
            break
            
    InsurePrem = TotalCost - HST

    if PayOption == 'Full':
            PayAmnt = TotalCost
            MonthlyPayments = 0.0
    else:
            PaymentAmnt = TotalCost + PRO_FEE_PAYMENT
            MonthlyPayments = MonthlyPay(TotalCost, DownPay)
        
    CurrentDate = datetime.datetime.now()
    InvoiceDate = CurrentDate.strftime("%Y-%m-%d")
    NextMonth = (CurrentDate + datetime.timedelta(days=31)).strftime("%Y-%m-%d")
    Year = CurrentDate.year + (CurrentDate.month // 12)                                    
    Month = 1 if CurrentDate.month == 12 else CurrentDate.month + 1
    NextMonth = datetime.datetime(Year, Month, 1).strftime("%Y-%m-%d")
    FirstPaymentDate = NextMonth
    NumCarsDsp =str(NumCars)

    

        
    if PayOption == "Full":
            PayOptionDsp = "Paid In Full"
    elif PayOption == "Monthy":
            PayOptionDsp = "Monthly Payments"
    else:
            PayOptionDsp == "Down Payment"



        # Print results 
    print()
    print("         1         2         3         4         5")
    print("12345678901234567890123456789012345678901234567890")
    print("One Stop Insurance                Customer Invoice")
    print()
    print(f"Policy #{POLICY_NUM:<5}")
    print("--------------------------------------------------")
    print("Customer Information:                             ")
    print()
    print(f"Name:    {FirstName:<10s}{LastName:<10s}  Phone Number: {PhoNum:<10s}     ")
    print(f"Address: {Address:<20s}                           ")
    print(f"City:    {City:<15s}                                 ")
    print(f"Provence:{Prov:<2s}                     Postal Code: {PostCode:<7s}                   ")
    print(f"--------------------------------------------------")
    print(f"Options:                                          ")
    print()
    print(f"Number Of Cars:  {NumCars:<2d}                     ")
    print(f"Extra Liability: {InsurOpt:<2s}                    ")
    print(f"Glass Coverage:  {GlassCover:<2s}                  ")
    print(f"Loaner Car:      {LoanCar:<2s}                         ")
    print(f"--------------------------------------------------")
    print(f"Payment Information:                              ")
    print()
    print(f"Date Of Invoice:                  {InvoiceDate:<10s}")
    print(f"First Payent Starts:              {FirstPaymentDate:<10s}")
    print()
    print(f"Payment Type:                     {PayOptionDsp:<15s}")
    print(f"Down Payment Amount:              {FV.FDollar2(DownPay)}")
    print(f"Monthly Payment:                  {FV.FDollar2(MonthlyPayments)}")
    print(f"Added Costs:                      {FV.FDollar2(AddedCosts)}")
    print(f"Insurance Premium:                {FV.FDollar2(InsurePrem)}")
    print(f"HST:                              {FV.FDollar2(HST)}")
    print(f"Total:                            {FV.FDollar2(TotalCost)}")
    print("---------------------------------------------------")
    print(f"Customer Prvious Claim(s):")
    print()
    print(f"Claim #          Claim Date         Amount")
    print("--------------------------------------------")
    for claim in PrevCusClaimInfo:
         print(f"{claim[0]:<10} {claim[1]:<10} ${claim[2]:,.2f}\n")
    POLICY_NUM += 1
    print("Policy Data Has Been Saved. ")
    print()
    if input("Do you want to enter another customer? (Y/N): ").upper() != 'Y':
        break




    # House Keeping 
            
    # Defualt values back to defualt.dat
    f = open('defualts.dat', 'w')
    f.write("{}/n".format(str(POLICY_NUM)))
    f.write("{}/n".format(str(BASE_PREMIUM)))
    f.write("{}/n".format(str(DISS_CAR)))
    f.write("{}/n".format(str(LIABLE_COVER)))
    f.write("{}/n".format(str(GLASS_COVER)))
    f.write("{}/n".format(str(LOAN_COVER)))
    f.write("{}/n".format(str(HST_RATE)))
    f.write("{}/n".format(str(PRO_FEE_PAYMENT)))
    f.close()


            