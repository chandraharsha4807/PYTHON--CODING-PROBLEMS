def convert(num):
    units = ("", "One ", "Two ", "Three ", "Four ","Five ", "Six ", "Seven ","Eight ", 
            "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", 
            "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen ")
            
    tens =("", "", "Twenty ", "Thirty ", "Forty ", "Fifty ","Sixty ","Seventy ","Eighty ","Ninety ")
    if num < 10 ** 10:
        if num < 0:
            return "Minus "+ convert(-num)

        if num<20:
            return  units[num] 

        if num<100:

            return  tens[num // 10]  + units[int(num % 10)] 

        if num<1000:
            return units[num // 100]  +"Hundred " +convert(int(num % 100))

        if num<1000000: 
            return  convert(num // 1000) + "Thousand " + convert(int(num % 1000))

        if num < 1000000000:    
            return convert(num // 1000000) + "Million " + convert(int(num % 1000000))

        return convert(num // 1000000000)+ "Billion "+ convert(int(num % 1000000000))


n = int(input())
print(convert(n))