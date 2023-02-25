import stripe
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from .models import Item
# Create your views here.


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class ProductLandingView(TemplateView):
    def get_context_data(self, **kwargs):
        product = Item.objects.all()
        context = {
            'product': product
        }
        return context
    template_name = 'payment_page.html'


class CreateCheckoutSession(View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        product = Item.objects.get(id=product_id)
        domain = "http://127.0.0.1:8000"
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': product.price,
                            'product_data': {
                                'name': product.name,
                            },
                        },
                        'quantity': 1,
                    },
                ],
                metadata={
                    "product_id": product.id
                },
                mode='payment',
                success_url=domain + '/success/',
                cancel_url=domain + '/cancel/',
            )
        except Exception as e:
            return HttpResponse(str(e))
        return redirect(checkout_session.url, code=303)

