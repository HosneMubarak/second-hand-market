from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostAd
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .choice import LOCATION_CHOICE


class PostDashboardView(LoginRequiredMixin, ListView):
    model = PostAd
    context_object_name = 'post_list_dashboard'
    query = PostAd.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostDashboardView, self).get_context_data(**kwargs)
        context['choice_list'] = LOCATION_CHOICE
        return context

    template_name = 'post/post_dashboard.html'

    def get_queryset(self):
        return PostAd.objects.filter(owner=self.request.user)


class PostListView(ListView):
    paginate_by = 8
    model = PostAd
    context_object_name = 'post_list'
    template_name = 'post/post_list.html'


class PostDetailView(DetailView):
    model = PostAd
    context_object_name = 'post_detail'
    template_name = 'post/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostAd

    fields = ['title', 'category', 'condition', 'location', 'mobile', 'price', 'image_main', 'image2',
              'image3',
              'description', ]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super(PostCreateView, self).form_valid(form)

    # This for were specific user not to set
    # def get_initial(self, *args, **kwargs):
    #     initial = super(PostCreateView, self).get_initial(**kwargs)
    #     initial['owner'] = self.request.user
    #     return initial

    # Set specific user to create post

    template_name = 'post/create_post.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = PostAd

    fields = ['title', 'category', 'condition', 'location', 'mobile', 'price', 'image_main', 'image2', 'image3',
              'description', ]

    # def get_initial(self, *args, **kwargs):
    #     initial = super(PostUpdateView, self).get_initial(**kwargs)
    #     initial['owner'] = self.request.user

    template_name = 'post/post_update.html'

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.owner != self.request.owner:
    #         raise PermissionDenied
    #     return super().dispatch(self, request, *args, **kwargs)


class PostDeleteView(DeleteView):
    model = PostAd
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post-dashboard')


class SearchPageView(ListView):
    model = PostAd
    context_object_name = 'search_list'
    template_name = 'post/search_list.html'

    def get_queryset(self):
        title = self.request.GET.get('title_q')
        location = self.request.GET.get('location_q')
        return PostAd.objects.filter(
            Q(title__icontains=title) & Q(location__location_category__icontains=location)
        )


class DhakaAllListView(ListView):
    model = PostAd
    template_name = 'post/all_dhaka_post.html'
    paginate_by = 8
    queryset = PostAd.objects.filter(location__location_category__contains='Dhaka')
    context_object_name = 'all_dhaka_post'


class KhulnaAlllListView(ListView):
    model = PostAd
    template_name = 'post/all_Khulna.html'
    paginate_by = 8
    queryset = PostAd.objects.filter(location__location_category__contains='Khulna')
    context_object_name = 'all_dhaka_post'


class ChattogramAllListView(ListView):
    model = PostAd
    template_name = 'post/all_chattogram_post.html'
    paginate_by = 8
    queryset = PostAd.objects.filter(location__location_category__contains='Chattogram')


class BarisalAllListView(ListView):
    model = PostAd
    template_name = 'post/all_Barishal.html'
    paginate_by = 8
    queryset = PostAd.objects.filter(location__location_category__contains='Barishal')


class RajshahilAllListView(ListView):
    model = PostAd
    template_name = 'post/all_Rajshahi.html'
    paginate_by = 8
    queryset = PostAd.objects.filter(location__location_category__contains='Rajshahi')


class RangpurAllListView(ListView):
    model = PostAd
    template_name = 'post/all_Rangpur.html'
    paginate_by = 8
    queryset = PostAd.objects.filter(location__location_category__contains='Rangpur')


class MymensinghAllListView(ListView):
    model = PostAd
    template_name = 'post/all_Mymensingh.html'
    paginate_by = 8
    queryset = PostAd.objects.filter(location__location_category__contains='Mymensingh')
