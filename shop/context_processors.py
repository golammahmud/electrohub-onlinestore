from .models import Subcategory,MyShop


# def mysession(request):
    
#     if 'customer' in request.session:
#         customer = request.session['customer']
#         return {'customer':customer}
    
def main_categories(request):
    
    # main_1st=main_categories[0:3]
    # subcategory=Subcategory.objects.all()
    
    main_categories=Subcategory.objects.filter(parent=None).order_by('pk')
    main_1st=main_categories[0:2]
    main_2nd=main_categories[2:]
    info=MyShop.objects.all()
    
    # return {'main_categories':main_categories,'subcategory':subcategory,'main_1st':main_1st}
    return {'main_categories':main_categories,'main_1st':main_1st,'main_2nd':main_2nd ,'info':info}