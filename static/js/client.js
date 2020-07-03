// get keys from the view
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// create a card element to display in view
var stripe = Stripe(stripePublicKey, {
    locale: 'en'
});
var elements = stripe.elements();
var card = elements.create('card');

card.mount('#card-element');

// Real-time error messages displayed
card.on('change', ({
    error
}) => {
    const displayError = document.getElementById('card-errors');
    if (error) {
        displayError.textContent = error.message;
    } else {
        displayError.textContent = '';
    }
});

// Form submit handler
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: 'test'
            }
        }
    }).then(function (result) {
        const displayError = document.getElementById('card-errors');
        if (result.error) {
            displayError.textContent = error.message;
        } else {
            // The payment has been processed!
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
