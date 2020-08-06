from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# third party
from datatableview.views import DatatableView
from datatableview import Datatable
# project import
from .models import Student


class ZeroConfigurationDatatableView(DatatableView):
    model = Student
    template_name = 'demo/index.html'


# class DemoIndexView(ListView):
# 	model = Student
# 	template_name = 'demo/index.html'
# 	context_object_name = 'students'


# def get_demo1_datatable_queryset(self):
#         return Student.objects.all()


# class ConfigureDatatableObject(DatatableView):
#     """
#     Like the built-in Django forms framework, configuration can be wrapped up into a subclass of
#     ``Datatable``, using class attributes to configure the columns (fields), while an inner ``Meta``
#     class manages the options that aren't the column declarations themselves.
#     """
#     model = Student
#     class datatable_class(Datatable):
#         class Meta:
#             model = Student
#             columns = ['name', 'course', 'college', 'fees']
#             ordering = ['-name']
#             page_length = 5
#             #search_fields = ['blog__name']
#             #unsortable_columns = ['n_comments']
#             #hidden_columns = ['n_pingbacks']
#             structure_template = 'demo/one.html'