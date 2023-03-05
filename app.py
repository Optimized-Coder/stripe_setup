from flask import Flask, render_template, request, redirect
import stripe

import os


app = Flask(__name__)

DOMAIN = 'http://127.0.0.1:5000'

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html'
    )


@app.route('/create-checkout-session/', methods=['GET', 'POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [
            {
            'price': 'price_1MhBKGGp9TbKJ1EQMlu83zqn',
            'quantity': 1,
            },
            ],
            mode='payment',
            success_url=DOMAIN + '/success',
            cancel_url=DOMAIN + '/cancel',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

@app.route('/success')
def get_success():
    return render_template(
        'success.html'
    )
@app.route('/cancel')
def get_cancel():
    return render_template(
        'cancel.html'
    )

if __name__ == '__main__':
    app.run(debug=True)