from django.conf.urls import url, include
from wkhtmltopdf.views import PDFTemplateView
from rest_framework.routers import DefaultRouter
from . import views, views_api

router = DefaultRouter()
router.register(r'election', views_api.ElectionInterface)
router.register(r'district', views_api.DistrictInterface)
router.register(r'municipality', views_api.MunicipalityInterface)
router.register(r'party', views_api.PartyInterface)
router.register(r'polling_station', views_api.PollingStationInterface)
router.register(r'list', views_api.ListInterface)
router.register(r'result', views_api.PollingStationResultInterface)
router.register(r'regional_electoral_district',
	views_api.RegionalElectoralDistrictInterface)

urlpatterns = [
	url(r'^$', views.viz, name='viz'),
	url(r'^viz/$', views.viz_overview, name='viz_overview'),
	url(r'^viz/results-bar/$', views.viz_results_bar, name='viz_results_bar'),
	url(r'^viz/results-map/$', views.viz_results_map, name='viz_results_map'),
	url(r'^viz/results-mapnrw13/$', views.viz_results_mapnrw13, name='viz_results_mapnrw13'),
	url(r'^viz/results-mapcanvas/$', views.viz_results_mapcanvas, name='viz_results_mapcanvas'),
	url(r'^viz/results-timeseries', views.viz_results_timeseries, name='viz_results_timeseries'),
	url(r'^pdf/$', PDFTemplateView.as_view(template_name='viz/index_viz.dtl', filename='viz.pdf'), name='pdf'),
	url(r'^pdf/results-bar/$', PDFTemplateView.as_view(template_name='viz/index_viz_result_bar.dtl', filename='result-bar.pdf'), name='pdf'),
	url(r'^pdf/results-map/$', PDFTemplateView.as_view(template_name='viz/index_viz_result_map.dtl', filename='result-map.pdf'), name='pdf'),
	url(r'^pdf/results-mapcanvas/$', PDFTemplateView.as_view(template_name='viz/index_viz_result_mapcanvas.dtl', filename='result-mapcanvas.pdf'), name='pdf'),
	url(r'^pdf/results-mapnrw13/$', PDFTemplateView.as_view(template_name='viz/index_viz_result_mapnrw13.dtl', filename='result-mapnrw13.pdf'), name='pdf'),
	url(r'^computing/', views.computing, name='computing'),
	url(r'^waiting/', views.waiting, name='waiting'),
	url(r'^test/', views.test, name='test'),
	url(r'^data/nrw13.csv$', views.serve_nrw13_csv, name='serve_nrw13_csv'),
	url(r'^api/', include(router.urls)),
	url(r'^api/geom/$', views.api_geom, name='api_geom'),
]
