var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

var stripe = Stripe(stripePublicKey, {
    locale: 'en'
});
var elements = stripe.elements();
var card = elements.create('card');

card.mount('#card-element');
