from django.urls import path
from .views import page1, page2, page3, page4, page5



urlpatterns = [
	path('page1/', page1),
	path('page1/page2/', page2),
	path('page1/page2/page3/', page3),
	path('page1/page2/page3/page4/', page4),
	path('page1/page2/page3/page4/page5/', page5),

]