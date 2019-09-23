from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import json
import timeit


@api_view(['POST'])
def display_fib_series(num):
	a=1
	b=1

	try:
		n=json.loads(num.body)
		for i in range(n):
			if i==1 or i==0:
				c=b
			
			else:
				c=a+b
				a=b
				b=c
		start_time=timeit.timeit()
		end_time=timeit.timeit()
		ex_time=end_time-start_time
		return Response({'Nth term':b,'Time taken to execute':ex_time})

	except Exception as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

	
	



	
