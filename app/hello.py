""" hello.py """

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    primes = primes_sieve2(10000000)
    return jsonify({
        'Primes': primes
    })

def primes_sieve2(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    primes = []
    for (i, isprime) in enumerate(a):
        if isprime:
            primes.append(i)
            for n in xrange(i * i, limit, i):  # Mark factors non-prime
                a[n] = False

    return primes


if __name__ == '__main__':
    app.run(host='0.0.0.0')
