from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

from cms0.forms import CommentForm, ContactForm, RegisterForm, LoginForm

