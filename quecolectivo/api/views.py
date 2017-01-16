from django.http import JsonResponse
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point as GeoPoint
from django.db.models import Q
from django.db import connection
from timeit import default_timer as timer
import json

from api.models import Line, Point


def within(point, distance):
    return Q(way__dwithin=(point, D(m=distance)))


# Create your views here.
def search(request, lng_orig, lat_orig, lng_dest, lat_dest, rad):
    lng_orig, lat_orig, lng_dest, lat_dest = map(float, [lng_orig, lat_orig, lng_dest, lat_dest])
    rad = int(rad)

    print(lat_orig, lat_dest, lng_orig, lng_dest, rad)

    p1 = GeoPoint(lng_orig, lat_orig, srid=4326)
    p2 = GeoPoint(lng_dest, lat_dest, srid=4326)

    # raw sql
    with connection.cursor() as cursor:
        query = """
            SELECT pid, ref, name,
            st_asgeojson(st_transform(way, 4326)) as geojson
            FROM planet_osm_line
            WHERE route='bus'
            AND st_dwithin(way, st_transform(st_geomfromewkt(%(p1)s), 3857), %(r)s)
            AND st_dwithin(way, st_transform(st_geomfromewkt(%(p2)s), 3857), %(r)s)
            ORDER BY (st_distance(way, st_transform(st_geomfromewkt(%(p1)s), 3857)) +
            st_distance(way, st_transform(st_geomfromewkt(%(p2)s), 3857)))
        """
        t1 = timer()
        cursor.execute(query, {'p1': p1.ewkt, 'p2': p2.ewkt, 'r': rad})
        results = cursor.fetchall()[:20]
        lines = list(map(lambda r: dict(zip(['pid', 'ref', 'name', 'geojson'], r)), results))

        # lineas = [dict(zip(['pid', 'ref', 'name'], result)) for result in results]

    # raw orm django
    # t1 = timer()
    # results = Line.objects.raw(
    #     """
    #     select pid, osm_id, ref, name, way
    #     from planet_osm_line
    #     where route='bus'
    #     and st_dwithin(way, st_transform(st_geomfromewkt(%(p1)s), 3857), %(r)s)
    #     and st_dwithin(way, st_transform(st_geomfromewkt(%(p2)s), 3857), %(r)s)
    #     """,
    #     {'p1': p1.ewkt, 'r': rad, 'p2': p2.ewkt})
    # lineas = [result.name for result in results]

    # django ORM
    # t1 = timer()
    # results = Line.objects.filter(within(p1, rad) & within(p2, rad), route='bus')
    # lineas = [result.ref for result in results]

    print(timer() - t1)
    return JsonResponse({'results': lines})


def routes(request, pid):
    pid = int(pid)
    with connection.cursor() as cursor:
        query = """
            SELECT st_x(st_transform((st_dumppoints(way)).geom, 4326)) as x, st_y(st_transform((st_dumppoints(way)).geom, 4326)) as y
            FROM planet_osm_line
            WHERE pid=%(pid)s
        """
        t1 = timer()
        cursor.execute(query, {'pid': pid})
        results = cursor.fetchall()
        print(timer()-t1)
        recorrido = [dict(zip(['x', 'y'], result)) for result in results]
        return JsonResponse({pid: recorrido})

def test(request):
    
    geojson = "{\"type\":\"LineString\",\"coordinates\":[[-57.9940760058713,-34.9235408549118],[-57.9938754120684,-34.9235324583129],[-57.9936846997335,-34.9235421070361],[-57.9935923529223,-34.923531721769],[-57.9934998264481,-34.9235155178035],[-57.993428410383,-34.9234873081651],[-57.9933641808402,-34.9234532061609],[-57.9932809070133,-34.923330055825],[-57.9932438065921,-34.9232000554195],[-57.9932363505753,-34.9230586383138],[-57.991411333244,-34.9229737142785],[-57.9913252746398,-34.9229677482328],[-57.990516611221,-34.9229497027834],[-57.9904221982847,-34.9235985262657],[-57.9903470092954,-34.9239429331499],[-57.9902139688018,-34.9240369156158],[-57.9901280898607,-34.9240645358341],[-57.9900422109195,-34.9240670400668],[-57.9899519302334,-34.9240539296714],[-57.9898738666353,-34.924025720218],[-57.9898030793909,-34.9239818961132],[-57.9897506177783,-34.9239231202183],[-57.9897026477421,-34.9237846505249],[-57.9897819689817,-34.9233465544454],[-57.989816194794,-34.9230594485166],[-57.9898249084523,-34.9229151586263],[-57.9898298491863,-34.9228025401537],[-57.9898291305341,-34.922417323412],[-57.9898481748181,-34.9217529491805],[-57.9897764892585,-34.9213364972247],[-57.9896913289695,-34.9208885180711],[-57.989683423795,-34.9208343066824],[-57.9895018742761,-34.9199581543408],[-57.9893437707861,-34.9195773437235],[-57.9893151145285,-34.9195139242208],[-57.9892870870917,-34.919452051488],[-57.9889773479817,-34.9188946055256],[-57.9884440181975,-34.9183754584707],[-57.9875289942491,-34.9175402347159],[-57.9874470678952,-34.9174653963669],[-57.9873438514691,-34.9173792143253],[-57.9863398943075,-34.9164615541207],[-57.9854241517069,-34.9156452418873],[-57.9853669290233,-34.9155932368806],[-57.98531383859,-34.9155450622415],[-57.9842854472528,-34.9146172161232],[-57.983358116385,-34.9137870368815],[-57.9833272143392,-34.9137593395411],[-57.9832881376243,-34.9137241285471],[-57.9822654955049,-34.9127687114998],[-57.9813780498357,-34.9119627492749],[-57.9812592027236,-34.9118523257197],[-57.9811787136742,-34.9117756405615],[-57.9801408900264,-34.9108562234002],[-57.9792199371971,-34.9100195234718],[-57.9791856215533,-34.9099883625332],[-57.979121481842,-34.9099301659496],[-57.9781879525987,-34.9090611166156],[-57.9781405215517,-34.9090161058418],[-57.9772454402026,-34.9081845439315],[-57.9771852530786,-34.9081285561154],[-57.9771212031988,-34.9080689585167],[-57.976239596579,-34.9072523418201],[-57.9761739297317,-34.9071885444498],[-57.9752729195018,-34.9063612368782],[-57.9751686250973,-34.9062641400379],[-57.9739691945299,-34.9071069927736],[-57.9728268069831,-34.9079402599697],[-57.9717142435037,-34.9087668149553],[-57.9705814679305,-34.9096093473335],[-57.9694539924173,-34.9104354435195],[-57.9685994250876,-34.911078693684],[-57.9683723309838,-34.9112453986705],[-57.9682609398885,-34.9113283458775],[-57.9671256490324,-34.9121446273753],[-57.9660006888021,-34.9129818949566],[-57.964861984348,-34.9138753589231],[-57.9637486123849,-34.9146880056417],[-57.9626121537189,-34.9155202382956],[-57.9621336211671,-34.9158679938382],[-57.9620810697229,-34.916678705656],[-57.962078015451,-34.9167696027021],[-57.9619403037179,-34.9168624148171],[-57.9608005212854,-34.9168108525439],[-57.9602947697805,-34.9171982317435],[-57.9592114913794,-34.9179943458724],[-57.9582774231469,-34.9186773125353],[-57.9573920436029,-34.9193343458509],[-57.9566024244682,-34.9199378248438],[-57.9559894141183,-34.9204072434308],[-57.9558539481734,-34.920467715958],[-57.9559066792806,-34.9205161086791],[-57.9564343496785,-34.9209981192475],[-57.9566499453467,-34.9211901419234],[-57.9566869559364,-34.9213050459565],[-57.9566917170074,-34.921357636595],[-57.9566947712794,-34.9213884985925],[-57.9566937831325,-34.9214218648919],[-57.9566897407138,-34.9214576618338],[-57.9566805778979,-34.9215076007513],[-57.9566662946849,-34.9215485535873],[-57.9566500351782,-34.9215840558494],[-57.9566243433611,-34.9216185269107],[-57.9565928124946,-34.9216592587231],[-57.9565496035295,-34.9216979281466],[-57.956503969113,-34.9217362292718],[-57.9564295886075,-34.9217835164057],[-57.9563938356592,-34.9217979529707],[-57.9563429011826,-34.9218147465227],[-57.9562985244075,-34.9218265314695],[-57.956255584937,-34.9218358121138],[-57.9562094115314,-34.9218419255536],[-57.956165483914,-34.9218472287781],[-57.9560511283783,-34.9218539314641],[-57.9559682138776,-34.921859750279],[-57.9558923062361,-34.9218712405958],[-57.9558023848761,-34.9218913486463],[-57.955722973805,-34.9219132980878],[-57.9555736738048,-34.92195830179],[-57.9550033334309,-34.9224022240574],[-57.9549899485332,-34.9224319071763],[-57.9549617414332,-34.9224890637223],[-57.9549401818664,-34.9225605093489],[-57.9549174544897,-34.9226485273292],[-57.9549027221191,-34.9227496558209],[-57.9548946372815,-34.9228244156964],[-57.9548718200733,-34.9228882009157],[-57.9548516978109,-34.9229278272741],[-57.9548196279553,-34.9229729040748],[-57.9545682793388,-34.9231486444373],[-57.954505576932,-34.9231661006054],[-57.9544497017213,-34.9231778117034],[-57.9544009232014,-34.9231853244823],[-57.9543507972085,-34.9231853244823],[-57.9542942033456,-34.9231795057614],[-57.9542566537667,-34.9231686048655],[-57.9542107498557,-34.923144151499],[-57.9539322721176,-34.9228842235478],[-57.9534900315033,-34.9224981233259],[-57.953447990348,-34.9224610010417],[-57.9532522474476,-34.9222858484505],[-57.9530137447396,-34.9220727628135],[-57.952564317603,-34.9216713383164],[-57.9522331985892,-34.9214063234164],[-57.9520592847503,-34.9212663026915],[-57.9512848471438,-34.9205642067435],[-57.9511978003928,-34.9204845097822],[-57.9501987839653,-34.9195715247468],[-57.9498187966001,-34.9192247424526],[-57.9494954030978,-34.918931434789],[-57.9492712734345,-34.9187240121621],[-57.9491899759012,-34.9186497641626],[-57.9481923069467,-34.9177379372703],[-57.9476676908208,-34.9172585593151],[-57.9471605918429,-34.9167943526097],[-57.9470783959944,-34.9167205448275],[-57.9464264885927,-34.9160701200852],[-57.9463861542364,-34.9157974263213],[-57.9464275665711,-34.9155069055501],[-57.9467192495438,-34.9152833423398],[-57.9468682800494,-34.9151743964888],[-57.9479202970787,-34.9144057311524],[-57.9480607935891,-34.9143031191259],[-57.9481976070069,-34.9141968238334],[-57.9485012375729,-34.9139641965104],[-57.9485084240952,-34.9138811046406],[-57.9485211801722,-34.913735693666],[-57.9485277378738,-34.9135835054097],[-57.9485818164539,-34.9126031145694],[-57.948607508271,-34.9122201335563],[-57.948665808933,-34.9113519187807],[-57.9487263553831,-34.9104512080707],[-57.9487553709668,-34.9100173134765],[-57.9488321769236,-34.9088726016059],[-57.9488341532172,-34.9086803291104],[-57.948847717778,-34.9085070624759],[-57.9488554432894,-34.9082905523365],[-57.948917247381,-34.9071820615733],[-57.9489194033377,-34.9069611277851],[-57.9489348543606,-34.9068210087491],[-57.9481460437096,-34.9061333022323],[-57.9480395933484,-34.9060467399433],[-57.9479291005685,-34.9059600302229]]}"
    return JsonResponse(geojson, safe=False)