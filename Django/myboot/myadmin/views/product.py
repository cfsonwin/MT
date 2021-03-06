import folium
from django.shortcuts import render

from myadmin.models import Product, CPmapping, User, PMmapping, Manufacturer
from myadmin.util import get_center_coor, Manus


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
        loc_dic = {}
        m = folium.Map(width='100%', height='100%', location=get_center_coor(), zoom_start=8)
        for manufacturer in manufacturers:
            if manufacturer.m_pnode == 0:
                this_manu = Manufacturer.objects.get(m_id=manufacturer.m_id)
                m_list_0.append(this_manu.m_name)
                loc_dic[this_manu.m_name] = Manus(
                    this_manu.m_name,
                    this_manu.loc,
                    this_manu.addtime,
                    this_manu.modifytime,
                    this_manu.description
                )
            elif manufacturer.m_pnode != 0:
                this_manu = Manufacturer.objects.get(m_id=manufacturer.m_id)
                m_list.append(this_manu.m_name)
                parent_list.append(Manufacturer.objects.get(m_id=manufacturer.m_pnode).m_name)
                loc_dic[this_manu.m_name] = Manus(
                    this_manu.m_name,
                    this_manu.loc,
                    this_manu.addtime,
                    this_manu.modifytime,
                    this_manu.description
                )
        print(loc_dic)
        for key in loc_dic.keys():
            info = loc_dic[key]
            '''<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" type="text/css" href="{% static 'bootstrap.min.css'%}"><link rel="stylesheet" type="text/css" href="{% static 'css/Sidebar.css'%}"></head>'''
            iframe = folium.IFrame(
                '<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"></head><div class="card-body bg-light"><h4 class="card-text" style="margin-bottom:0px">%s</h4><p class="card-text" style="font-size:20px">Log:</br>%s</p><small class="text-muted" style="font-size:15px test-align:bottom">%s</small></div>'
                % (info.name, info.description, info.change_msg))
            popup = folium.Popup(iframe, min_width=400, max_width=400)
            folium.Marker([info.lat, info.lon], tooltip='click here for more',
                          popup=popup,
                          icon=folium.Icon(color='purple')).add_to(m)
        users = User.objects.filter(u_id__in=u_list)
        m_info = []
        m_html = m._repr_html_()
        for item in m_list_0:
            m_info.append(" name: %s, direct get from product constructor" % item)
        for i in range(len(m_list)):
            m_info.append(" name: %s, get from %s" % (m_list[i], parent_list[i]))
        context = {'product': product,
                   'owners': users,
                   'm_info': m_info,
                   'map': m_html,
                   'add_status': 1}

    except Exception as err:
        print('***************')
        print(err)
        context = {'info': "Showing information for product %s failed, Please try again." % product.p_name,
                   'add_status': 0}
    return render(request, 'myadmin/product/view.html', context)
