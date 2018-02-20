# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.forms import DocumentForm
from polls.models import Document
from recognize.performRecognition import DigitRecognizer


def index(request):
    return render(request, 'polls/index.html', context=None)


def digit_recognize(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            digit_docfile = Document(docfile=request.FILES['docfile'])
            digit_docfile.save()
            objct = DigitRecognizer()
            mylist = []
            digit_list = objct.perform(digit_docfile.docfile.path)
            digit_image_url = digit_docfile.docfile.url

            for value in digit_list:
                mylist.append(int(value))
            context={'image_path':digit_image_url,'digit_value':mylist}
            return render(request,'polls/digit.html',context)

    else:
		form = DocumentForm()  # A empty, unbound form

	# # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,'polls/digit.html',
        {'documents': documents, 'form': form})
        