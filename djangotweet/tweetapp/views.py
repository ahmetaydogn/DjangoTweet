from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.
def list_tweet(request):
    # all_tweets = models.Tweet.objects.all().order_by("name").values()
    all_tweets = models.Tweet.objects.all()
    
    tweet_dict = {"tweets": all_tweets}
    return render(request, "tweetapp/list-tweet.html", context=tweet_dict)

@login_required(login_url="/login")
def add_tweet(request):
    if (request.method == "POST") and (request.POST is not None): 
        getProp = request.POST
        name = getProp['name']
        surname = getProp['surname']
        message = getProp['message']
        
        tweetObj = models.Tweet(name=name, surname=surname, username=request.user, message=message)
        tweetObj.save()
        # üstteki gösterim yerine böylede yapılabilir
        # models.Tweet.objects.create(name=name, surname=surname, nickname=nickname, message=message)
        return redirect(reverse('tweetapp:list-tweet'))

    elif request.method == "GET":
        print("Bu işlem gerçekleştirilemiyor.")
    return render(request, "tweetapp/add-tweet.html")

def add_tweet_by_form(request):
    if (request.method == "POST") and (request.POST is not None):
        form = AddTweetForm(request.POST)
        if form.is_valid():
            print("Your process is successful!")
            getProps = form.cleaned_data
            name = getProps['name_input']
            surname = getProps['surname_input']
            message = getProps['message_input']
            
            createdTweet = models.Tweet.objects.create(name=name, surname=surname, username=request.user, message=message)
            # createdTweet = models.Tweet(name=name, surname=surname, nickname=nickname, message=message)
            # createdTweet.save()
            
            # print(form.cleaned_data)
            return redirect(reverse('tweetapp:list-tweet'))
        else:
            print("Your process isn't successful!")
            return render(request, 'tweetapp/add-tweet-by-form.html', context={'form': form})
    else:
        form = AddTweetForm()
        return render(request, 'tweetapp/add-tweet-by-form.html', context={"form": form})
    
def add_tweet_by_model_form(request):
    if (request.method == "POST" and request.POST is not None):
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            getProps = form.cleaned_data
            name = getProps['name']
            surname = getProps['surname']
            message = getProps['message']
            createdTweet = models.Tweet.objects.create(name=name, surname=surname, username=request.user, message=message)
            
            return redirect(reverse('tweetapp:list-tweet'))
        else:
            return render(request, 'tweetapp/add-tweet-by-model-form.html', context={'form': form})
    else:
        form = AddTweetModelForm()
        return render(request, 'tweetapp/add-tweet-by-model-form.html', context={"form": form})
    
@login_required
def delete_tweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.get(pk=id).delete()
        return redirect('tweetapp:list-tweet')
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/sign-up.html"
    