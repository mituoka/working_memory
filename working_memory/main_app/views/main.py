from django.shortcuts import render

def main(request):
    print('11111')
    
    params = {
        'title':'ワーキングメモリートレーニング',

    }

    if (request.method == 'POST'):
        print(30)


    return render(request,'main.html',params)