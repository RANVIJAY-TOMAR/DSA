class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if(numerator < 0 and denominator < 0):
            negative = False
        elif(numerator < 0 and denominator > 0):
            negative = True
        elif(numerator > 0 and denominator < 0):
            negative = True
        else:
            negative = False

        numerator = abs(numerator)
        denominator = abs(denominator)
        
        if(numerator % denominator == 0):
            if(negative):
                return "-" + str(numerator // denominator)
            else:
                return str(numerator // denominator)


        Q = numerator // denominator
        r = numerator % denominator

        rem_dict = {r : 0}
        cnt = 1
        frac = []
        while(True):

            d = r * 10
            q = d // denominator
            r = d % denominator

            frac.append(str(q))

            if(r == 0 or r in rem_dict):
                break
            
            if(r not in rem_dict):
                rem_dict[r] = cnt

            cnt += 1
        
        
        if(r != 0):

            back_step = cnt - rem_dict[r]
            start_index = len(frac) - back_step
            frac.insert(start_index, "(")
            frac.append(")")

        if(negative):
            return f"-{Q}.{''.join(frac)}"
        else:
            return f"{Q}.{''.join(frac)}"