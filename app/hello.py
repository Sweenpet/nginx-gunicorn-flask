""" hello.py """

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    factorize_naive(1000)
    return jsonify({
        'hello': 'world'
    })

def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1

if __name__ == '__main__':
    app.run(host='0.0.0.0')
