class Answer:
    def solution(self, h, x0, y0, xFinal, digits):  
        x = x0
        y = y0

        steps = int((xFinal - x0) / h)  

        for _ in range(steps):  
            yPrime = x**2 + 6*(y**2) - 6
            y = y + h * yPrime  
            x = x + h  
        
        return round(y, digits)

def main():
    ans = Answer()
    correct = ans.solution(0.0001, 0, 0, 2,4)
    print(correct)

main()
