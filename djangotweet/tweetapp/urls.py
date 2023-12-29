from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path("", views.list_tweet, name='list-tweet'), # ahmetaydogan.com/tweetapp/list-tweet
    path("add-tweet/", views.add_tweet, name='add-tweet'), # ahmetaydogan.com/tweetapp/add-tweet
    path("add-tweet-by-form/", views.add_tweet_by_form, name='add-tweet-by-form'), # ahmetaydogan.com/tweetapp/add-tweet-by-form
    path("add-tweet-by-model-form/", views.add_tweet_by_model_form, name='add-tweet-by-model-form'),
    path("sign-up/", views.SignUpView.as_view(), name='sign-up'),
    path("delete-tweet/<int:id>", views.delete_tweet, name='delete-tweet'),
]