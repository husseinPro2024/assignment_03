def countDigits(Input,count):
    if int(Input)==0 :
        print("Output:",count)
        return
    count+=1
    countDigits(Input/10,count)

def findMax(list,i):
     max=list[0]
     if max<list[i]:
         max=list[i]
     if i==len(list)-1 :
         print("Output:",max)
         return 
     findMax(list,i+1)

def countTags(html_code, tag):
    count=0
    opening_tag ="<"+tag+">"
    closing_tag ="</"+tag+">"

    if opening_tag not in html_code and closing_tag not in html_code:
        return 0  
    opening_index = html_code.find(opening_tag)
    closing_index = html_code.find(closing_tag)

    if opening_index != -1 and closing_index != -1:
      count+=1
      count += countTags(html_code[closing_index + len(closing_tag):], tag)

    return count

while True:
    print("1. Count Digits")
    print("2. Find Max")
    print("3. Count Tags")
    print("4. Exit")
    print("- - - - - - - - - - - - - - -")
    n=int(input("Enter a choice:"))
    if n==1 :
        Input=int(input("Input:"))
        countDigits(Input,0) 
        print("- - - - - - - - - - - - - - -")
    elif n==2 :
        list=[]
        print("Enter a list of integers when you finish,write stop")
        while True :
            Input=input("Input:")
            if Input=="stop" :
                break
            list.append(int(Input))
        if not list:
            print("The list is empty.OutPut:0")
        else:
             findMax(list,0) 
        print("- - - - - - - - - - - - - - -")
    elif n==3 :
        Input=input("Input:")
        tag=input("Enter the tag: ")
        count=countTags(Input,tag)
        print("OutPut:",count)
        print("- - - - - - - - - - - - - - -")
    elif n==4 :
        print("- - - - - - - - - - - - - - -")
        break
    else:
       print("Invalid Input.")
       print("- - - - - - - - - - - - - - -")

