// get the stripe keys from the view
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
        // display error message
        displayError.textContent = error.message;
    } else {
        // clear display
        displayError.textContent = '';
    }
});

// Form submit handler to process stripe payment
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    // disable submitting the form yet
    ev.preventDefault();

    // disable submit button to prevent multiple submission
    $('#submit-button').attr('disabled', true);

    // execute stripe payment
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        // reenable submit button to fix errors
        $('#submit-button').attr('disabled', false);

        // get the result of the payment
        const displayError = document.getElementById('card-errors');
        if (result.error) {
            // display error messages
            displayError.textContent = result.error.message;
        } else {
            // if the payment was processed
            if (result.paymentIntent.status === 'succeeded') {
                // submit the form
                form.submit();
            }
        }
    });
});