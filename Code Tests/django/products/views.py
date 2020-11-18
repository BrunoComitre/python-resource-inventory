from django.shortcuts import render, redirect, get_list_or_404
from .models import Product
from .forms import ProductForm

# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.views import generic
# from django.utils import timezone

# Create your views here.


def list_products(request):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    products = Product.objects.all()  # Lista de produtos pega do banco
    return render(request, 'products.html', {'products': products})

def create_product(request):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})

def update_product(request, id):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'product': product})

def delete_product(request):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'product': product})



'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
'''
