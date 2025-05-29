from Graphql.queries.queries import Query
from django.http import JsonResponse
from datetime import datetime

def info_about_news_and_photos_report(request):
        
    id_investigacion = request.GET.get('id')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')

    try:

        newss = Query.resolve_news_for_id_investigation(None, None,id_investigacion)


        #CALCULAR DIAS ACTIVOS

        fecha_novedades_por_investi = Query.resolve_calculate_active_days(None, None, id_investigacion)

        print('mia',fecha_novedades_por_investi)


        # print("t_n:",newss['total_novedades'])
        # print("n_f:",newss['con_foto'])
        # print("porcentaje:",newss['porcentaje'])


        
        if newss is None:
            return JsonResponse({'error': 'Novedades no encontrada'}, status=404)

        # fecha_inicio, fecha_fin, nombre = news_id



        return JsonResponse({
            "total_novedades": str(newss['total_novedades']),
            "novedades_con_foto": str(newss['con_foto']),
            "porcentaje": str(newss['porcentaje']),
            'fechas_novedades_activas': fecha_novedades_por_investi
            
        }, status=200) 

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

