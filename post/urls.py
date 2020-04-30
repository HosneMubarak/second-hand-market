from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDashboardView, PostDeleteView, \
    SearchPageView, DhakaAllListView, ChattogramAllListView, KhulnaAlllListView, BarisalAllListView, \
    RajshahilAllListView, RangpurAllListView, MymensinghAllListView

urlpatterns = [
    path('allpost/', PostListView.as_view(), name='post-list'),
    path('dashboard/', PostDashboardView.as_view(), name='post-dashboard'),
    path('<int:pk>/detail', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('search/', SearchPageView.as_view(), name='post-search'),
    path('allpost/dhaka/', DhakaAllListView.as_view(), name='dhaka-all-post'),
    path('allpost/chattogram/', ChattogramAllListView.as_view(), name='chattogram-all-post'),
    path('allpost/Khulna/', KhulnaAlllListView.as_view(), name='Khulna-all-post'),
    path('allpost/Barishal/', BarisalAllListView.as_view(), name='Barishal-all-post'),
    path('allpost/Rajshahi/', RajshahilAllListView.as_view(), name='Rajshahi-all-post'),
    path('allpost/Rangpur/', RangpurAllListView.as_view(), name='Rangpur-all-post'),
    path('allpost/Mymensingh/', MymensinghAllListView.as_view(), name='Mymensingh-all-post'),

]
