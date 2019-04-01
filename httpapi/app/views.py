# -*- coding: utf-8 -*-
# ! /usr/bin/env python

import pysolr
from django.http import JsonResponse
from httpapi.settings import Solr_URL

from .models import *


# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes

# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))

def analysis_solr_api(request):
    area = request.GET.get('area', 0)
    credit_quality = request.GET.get('quality', 0)
    rows = request.GET.get('rows', 10)
    quarter = request.GET.get('quarter', "0")
    quarters = {"1": "[%s-01-01T00:00:00Z TO %s-03-31T00:00:00Z]" % (datetime.now().year, datetime.now().year),
                "2": "[%s-04-01T00:00:00Z TO %s-06-30T00:00:00Z]" % (datetime.now().year, datetime.now().year),
                "3": "[%s-07-01T00:00:00Z TO %s-09-30T00:00:00Z]" % (datetime.now().year, datetime.now().year),
                "4": "[%s-10-01T00:00:00Z TO %s-12-31T00:00:00Z]" % (datetime.now().year, datetime.now().year),
                "0": "[%s-%s-01T00:00:00Z TO *]" % (datetime.now().year, datetime.now().month)}
    if area == 0 or credit_quality == 0:
        return JsonResponse({"msg": "error", "data": u"请求参数未填写正确！"})
    q_dict = {'wt': 'json', "rows": rows, "fq": "sortpubtime:%s" % quarters.get(quarter)}
    result = SolrReKeyWord.objects.filter(credit_quality_id=credit_quality, flag=1).first()
    area_re = AreaReKeyWord.objects.filter(area=area, flag=1).first().word_re
    if result == None or area_re == None:
        return JsonResponse({"msg": "error", "data": u"指标参数或区域参数不正确！"})
    area_re = area_re + result.area_re
    word_re = result.word_re
    q = '((title:(('"%s"')AND('"%s"')))AND(content:(('"%s"')AND('"%s"'))))' % (area_re, word_re, area_re, word_re)
    print q
    try:
        solr = pysolr.Solr(Solr_URL, timeout=10)
    except:
        return JsonResponse({"msg": "error", "data": u"Solr请求超时..."})
    results = solr.search(q, **q_dict)
    numFound = results.hits
    data = results.docs
    raw_response = results.raw_response,
    keyword = raw_response[0]['responseHeader']['params']['q']
    QTime = raw_response[0]['responseHeader']['QTime']
    return JsonResponse({"msg": "sccuess", "QTime": QTime, "numFound": numFound, "keyword": keyword, "data": data})
