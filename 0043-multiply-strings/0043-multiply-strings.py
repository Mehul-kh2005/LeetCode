class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numbers_map={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,
                    "6":6, "7":7,"8":8,"9":9}

        lst1=[]
        lst2=[]
        for num in num1:
            lst1.append(numbers_map[num])

        for num in num2:
            lst2.append(numbers_map[num])

        val1=int("".join(num1))
        val2=int("".join(num2))
        
        return str(val1*val2)