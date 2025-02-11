class Answer():
    def solution(h, x0, y0, xFinal):
        yPrime = x
        x = x0
        y = y0

        for x in range(xFinal - x0 / h):
            yPrime = x**2 + y**2 - 1
            y = y + h * yPrime
            x = x + h
        
        return y

def main():
    ans = Answer()
    ans.solution(0.1, 0, 0, 1.3)