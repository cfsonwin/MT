import os
import random

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from myadmin.models import Product, CPmapping, User, PMmapping, Manufacturer


# Create your views here.
def show_all(request):
    product = Product.objects
    p_list = product.all()
    context = {'productlist': p_list}
    return render(request, 'myadmin/product/show.html', context)

def show_details(request, p_id=0):
    product = Product.objects.get(p_id=p_id)
    owners = CPmapping.objects.filter(p_id=p_id)
    manufacturers = PMmapping.objects.filter(p_id=p_id)
    # for i in range(1, 10):
    #     try:
    #         print(Product.objects.get(p_id=i))
    #     except:
    #         print('no such record from id = %d' % i)
    #         break

    u_list = []
    m_list_0 = []
    m_list = []
    parent_list = []
    try:
        for owner in owners:
            u_list.append(owner.c_id)
        for manufacturer in manufacturers:
            if manufacturer.m_pnode == 0:
                m_list_0.append(Manufacturer.objects.get(m_id=manufacturer.m_id).m_name)
            elif manufacturer.m_pnode != 0:
                m_list.append(Manufacturer.objects.get(m_id=manufacturer.m_id).m_name)
                parent_list.append(Manufacturer.objects.get(m_id=manufacturer.m_pnode).m_name)
        users = User.objects.filter(u_id__in=u_list)
        m_info = []
        for item in m_list_0:
            m_info.append(" name: %s, direct get from product constructor" % item)
        for i in range(len(m_list)):
            m_info.append(" name: %s, get from %s" % (m_list[i], parent_list[i]))
        context = {'product': product,
                   'owners': users,
                   'm_info': m_info,
                   'add_status': 1}

    except Exception as err:
        print('***************')
        print(err)
        context = {'info': "Showing information for product %s failed, Please try again." % product.name,
                   'add_status': 0}
    return render(request, 'myadmin/product/view.html', context)