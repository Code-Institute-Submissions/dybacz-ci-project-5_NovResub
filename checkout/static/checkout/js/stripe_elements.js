/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

let stripePublicKey = document.querySelector('#id_stripe_public_key').innerHTML.slice(1, -1);
let clientSecret = document.querySelector('#id_client_secret').innerHTML.slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
let card = elements.create('card', {
    style: style
});
card.mount('#card-element');

// Handle validaiton errors on the card element in real time
card.addEventListener('change', function (event) {
    let errorDiv = document.querySelector('#card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
let form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    let loadingOverlay = document.querySelector('#loading-overlay');
    loadingOverlay.style.display = "block";
    let cardSubmitBtn = document.querySelector('#submit-button');
    cardSubmitBtn.setAttribute('disabled', true);
    let saveInfoElement = document.querySelector("#id-save-info");
    let saveInfo = !saveInfoElement ? false : saveInfoElement.checked;
    let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]');
    let csrfToken = csrf.value;
    let postData = {
        'csrfmiddlwaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    let url = '/checkout/cache_checkout_data/';

    fetch(url, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            post_data: postData
        }),
    }).then(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name.value.trim(),
                    phone: form.phone_number.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.street_address1.value.trim(),
                        line2: form.street_address2.value.trim(),
                        city: form.town_or_city.value.trim(),
                        country: form.country.value.trim(),
                        state: form.county.value.trim(),
                    }
                }
            },
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    state: form.county.value.trim(),
                }
            }
        }).then(function (result) {
            if (result.error) {
                let errorDiv = document.querySelector('#card-errors');
                let html = `
                        <span class="icon" role="alert">
                            <i class="fas fa-times"></i>
                        </span>
                        <span>${result.error.message}</span>
                    `;
                errorDiv.innerHTML = html;
                loadingOverlay.style.display = "none";
                card.update({
                    'disabled': false
                });
                let cardSubmitBtn = document.querySelector('#submit-button');
                cardSubmitBtn.removeAttribute('disabled');
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).catch(function () {
        // page reload, error will be picked up by django messages
        location.reload();
    });
});