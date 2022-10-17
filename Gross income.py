 


#Global Variables
tb = "###############################"
tl = "-------------------------------"

#list of constant 
list_of_cons = ["Residential", "Commercial", "Industrial"]



###
def Residential(value):
    ################################
    add_cost_eleq = 0
    add_cost_gr = 0
    #//////////////////////////////#
    gmb_eleq = 5
    gmb_gr = 0
    #//////////////////////////////#
    rate_eleq = 18.75
    rate_gr = 17.70
    ################################
 

    ################################
    print("Residential Type")
    print(tl+"\n\n\n")
    if value >= 100:
        gmb = (value * rate_eleq)
        fmb = (gmb + add_cost_eleq ) + (gmb_eleq * gmb)  
        print("Final Monthly Bill : " + str(fmb) )
    elif value < 100 :
        gmb = (value * rate_gr)
        fmb = (gmb + add_cost_gr ) + (gmb_gr  * gmb)  
        print("Final Monthly Bill : " + str(fmb))
    else:
        print('err')
    
    

    #Final monthly bill - gmb + additional cos + tax 
    ################################
    print(tl)
    print(tb)



def Commercial(value):
    ################################
    add_cost_eleq = 200
    add_cost_gr = 100
    #//////////////////////////////#
    gmb_eleq = 10
    gmb_gr = 2
     #//////////////////////////////#
    rate_eleq = 20.25
    rate_gr = 19.75
    ################################
    print("Commercial Type ")
    print(tl+"\n\n\n")
    if value >= 100:
        gmb = (value * rate_eleq)
        fmb = (gmb + add_cost_eleq ) + (gmb_eleq * gmb)  
        print("Final Monthly Bill : " + str(fmb) )
    elif value < 100 :
        gmb = (value * rate_gr)
        fmb = (gmb + add_cost_gr ) + (gmb_gr  * gmb)  
        print("Final Monthly Bill : " + str(fmb))
    else:
        print('err')
        
    print(tl)
    print(tb)


def Industrial(value):
    ################################
    add_cost_eleq = 500
    add_cost_gr = 300
    #//////////////////////////////#
    gmb_eleq = 10
    gmb_gr = 5
     #//////////////////////////////#
    rate_eleq = 22.75
    rate_gr = 22.55
    print("Industrial Type")
    print(tl+"\n\n\n")
    if value >= 100:
        gmb = (value * rate_eleq)
        fmb = (gmb + add_cost_eleq ) + (gmb_eleq * gmb)  
        print("Final Monthly Bill : " + str(fmb) )
    elif value < 100 :
        gmb = (value * rate_gr)
        fmb = (gmb + add_cost_gr ) + (gmb_gr  * gmb)  
        print("Final Monthly Bill : " + str(fmb))
    else:
        print('err')
    print(tl)
    print(tb)

#__inter__
#Showing The Choices in screen
num = 0
for i in range(3):
    i + 1
    num = num + 1
    print(f" [{num - 1}] {list_of_cons[i]}")

#User ask if what is cons. type Either Residential, Commercial or Industrial .Input
cons_type = input("Cons. Type: ")
if int(cons_type) >= 3:
    print("err")
else:#__Main__
    print(">>>>>" + list_of_cons[int(cons_type)] + " Type")

    print(tl)
    #asking the wattage value
    curwat = float(input("Current Wattage : "))
    prewat = float(input("Current PreViews Wattage : "))
    wattage = curwat - prewat
    print(f'Total Wattage {wattage}')
    
    #wattage = input(" \n Wattage Input :")
    if int(cons_type) == 0:
        Residential(float(wattage))
    elif int(cons_type) == 1:
        Commercial(float(wattage))
    elif int(cons_type) == 2:
        Industrial(float(wattage))
    else:
        print('err')
    #debugg
    #print(float(wattage))