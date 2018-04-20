#-----------------------------------------------------------------------------------------#
#Written by Dimitris Sinanis on 05/11/2017.
#This program checks the validity of a credit card.
#Learn how this program works here : http://www.creditcard-validnumber.com/en/creditcard_digits
#Python version: 3.6.4
#-----------------------------------------------------------------------------------------#
"=================================The_code_begins_here===================================="
def Luhn_algorithm(credit_card):
    #Learn what is Luhn algorithm : https://en.wikipedia.org/wiki/Luhn_algorithm
    cc0=credit_card[::-1]
    cc1=[]
    cc2=[]
    gr_to_9=[]
    gr_to_9_str=[]
    gr_to_9_done=[]
    sm_to_9=[]
    for i in cc0[1::2]:
        cc1.append(i)
    for i in cc0[0::2]:
        cc2.append(int(i))
    cc1x2=[]
    for i in cc1:
        cc1x2.append(2*int(i))
    for i in cc1x2:
        if i>9:
            gr_to_9.append(i)
        else:
            sm_to_9.append(i)
    for i in gr_to_9:
        gr_to_9_str.append(str(i))
    for i in gr_to_9_str:
        gr_to_9_done.append(int(i[0])+int(i[1]))
    checksum=sum(cc2+gr_to_9_done+sm_to_9)
    if checksum%10==0:
        return "The credit card number is valid."
    else:
        return "The credit card number is not valid."
        
        
def Major_Industry_Indetifier(x):
    #Learn what is MII : http://mahercreditcard.blogspot.gr/2009/08/major-industry-identifier.html
    x=int(credit_card[0])
    if x==1 or x==2:
        return "Airlines"
    if x==3:
        return "Travel & Entertainment"
    if x==4 or x==5:
        return "Banking & Financial"
    if x==6:
        return "Merchandizing & Banking"
    if x==7:
        return "Petroleum"
    if x==8:
        return "Healthcare, Telecommunication"
    if x==9:
        return "For assignment by national standard bodies"

def IIN_ranges(credit_card):
    #Leran what is IIN : https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
    if (int(credit_card[0:2])==34 or int(credit_card[0:2])==37) and (len(credit_card)==15):
        return "American Express"
    elif int(credit_card[0])==4 and (len(credit_card)==13 or len(credit_card)==16 or len(credit_card)==19):
        return "Visa"
    elif ((int(credit_card[0:2]) in [x for x in range(51,56)]) or (int(credit_card[0:4]) in [x for x in range(2221,2721)]))  and (len(credit_card)==16):
        return "MasterCard"
    else:
        return "Unknown type of Credit Card"
        
def main():
    if Luhn_algorithm(credit_card)=="The credit card number is not valid.":
        print("The credit card number is not valid.")
    else:
        print("Luhn algorithm : The credit card number is valid.")
        print("Major_Industry_Indetifier : {}".format(Major_Industry_Indetifier(int(credit_card[0]))))
        print("Issuer Identification Number : {}".format(IIN_ranges(credit_card)))
    return
                
print("For example, if your credit card number equals to : 4012 8888 8888 1881 , just give :  4012888888881881")
credit_card=str(input("Give the credit card number : "))
main()
print("")
input("Press enter to close.")
"===========================================The_end=============================================="


