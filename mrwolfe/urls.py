from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from views.index import IndexView, AdminView
from views.issue import IssueCreate, IssueEdit, IssueView, \
    IssueAssigneeJSONEdit, IssueHistoryView
from views.service import ServiceJSONCreate, ServiceJSONEdit, \
    ServiceJSONDelete, ServiceJSONSetDefault
from views.rule import RuleJSONCreate, RuleJSONEdit, RuleJSONDelete
from views.sla import SLAView, SLAJSONCreate, SLAJSONEdit, SLAJSONDelete, \
    SLADelete, SLAEdit
from views.operator import OperatorJSONCreate, OperatorJSONEdit, \
    OperatorJSONDelete
from views.contact import ContactJSONCreate, ContactJSONEdit, \
    ContactJSONDelete
from views.mailqueue import MailQueueJSONCreate, MailQueueJSONEdit, \
    MailQueueJSONDelete
from views.status import StatusJSONCreate


admin.autodiscover()


urlpatterns = patterns('',
                       (r'^$', login_required(IndexView.as_view())),
                       (r'^config$', login_required(AdminView.as_view())),
                       (r'^openid/', include('django_openid_auth.urls')),
                       (r'^logout/$', 'django.contrib.auth.views.logout'),
                       (r'^admin/', include(admin.site.urls)),

                       # Issue
                       #
                       url(r'^create_issue/', 
                           IssueCreate.as_view(),
                           name="create_issue"),
                       url(r'^edit_issue/(?P<pk>[\d]+)$', 
                           IssueEdit.as_view(),
                           name="edit_issue"),
                       url(r'^view_issue/(?P<pk>[\d]+)$', 
                           IssueView.as_view(),
                           name="view_issue"),
                       url(r'^change_status/(?P<issue_pk>[\d]+)$', 
                           StatusJSONCreate.as_view(),
                           name="change_status"),
                       url(r'^change_assignee/(?P<pk>[\d]+)$', 
                           IssueAssigneeJSONEdit.as_view(),
                           name="change_assignee"),
                       url(r'^issue_history/(?P<pk>[\d]+)$', 
                           IssueHistoryView.as_view(),
                           name="issue_history"),

                       # Service
                       #
                       url(r'^create_service_json/(?P<sla_pk>[\d]+)$', 
                           ServiceJSONCreate.as_view(),
                           name="create_service_json"),
                       url(r'^edit_service_json/(?P<pk>[\d]+)$', 
                           ServiceJSONEdit.as_view(),
                           name="edit_service_json"),
                       url(r'^delete_service_json/(?P<pk>[\d]+)$', 
                           ServiceJSONDelete.as_view(),
                           name="delete_service_json"),
                       url(r'^set_default_service/(?P<pk>[\d]+)$',
                           ServiceJSONSetDefault.as_view(),
                           name="set_default_service"),

                       # Rule
                       #
                       url(r'^create_rule_json/(?P<sla_pk>[\d]+)$', 
                           RuleJSONCreate.as_view(),
                           name="create_rule_json"),
                       url(r'^edit_rule_json/(?P<pk>[\d]+)$', 
                           RuleJSONEdit.as_view(),
                           name="edit_rule_json"),
                       url(r'^delete_rule_json/(?P<pk>[\d]+)$', 
                           RuleJSONDelete.as_view(),
                           name="delete_rule_json"),

                       # SLA
                       # 
                       url(r'^create_sla_json/', 
                           SLAJSONCreate.as_view(),
                           name="create_sla_json"),
                       url(r'^edit_sla_json/(?P<pk>[\d]+)$', 
                           SLAJSONEdit.as_view(),
                           name="edit_sla_json"),
                       url(r'^edit_sla/(?P<pk>[\d]+)$', 
                           SLAEdit.as_view(),
                           name="edit_sla"),
                       url(r'^view_sla/(?P<pk>[\d]+)$', 
                           SLAView.as_view(),
                           name="view_sla"),
                       url(r'^delete_sla_json/(?P<pk>[\d]+)$',
                           SLAJSONDelete.as_view(),
                           name="delete_sla_json"),
                       url(r'^delete_sla/(?P<pk>[\d]+)$',
                           SLADelete.as_view(),
                           name="delete_sla"),
                       
                       # Operator
                       #
                       url(r'^create_operator_json/', 
                           OperatorJSONCreate.as_view(),
                           name="create_operator_json"),
                       url(r'^edit_operator_json/(?P<pk>[\d]+)$', 
                           OperatorJSONEdit.as_view(),
                           name="edit_operator_json"),
                       url(r'^delete_operator_json/(?P<pk>[\d]+)$', 
                           OperatorJSONDelete.as_view(),
                           name="delete_operator_json"),

                       # Contact
                       #
                       url(r'^create_contact_json/', 
                           ContactJSONCreate.as_view(),
                           name="create_contact_json"),
                       url(r'^edit_contact_json/(?P<pk>[\d]+)$', 
                           ContactJSONEdit.as_view(),
                           name="edit_contact_json"),
                       url(r'^delete_contact_json/(?P<pk>[\d]+)$', 
                           ContactJSONDelete.as_view(),
                           name="delete_contact_json"),

                       # MailQueue
                       #
                       url(r'^create_mailqueue_json/', 
                           MailQueueJSONCreate.as_view(),
                           name="create_mailqueue_json"),
                       url(r'^edit_mailqueue_json/(?P<pk>[\d]+)$', 
                           MailQueueJSONEdit.as_view(),
                           name="edit_mailqueue_json"),
                       url(r'^delete_mailqueue_json/(?P<pk>[\d]+)$', 
                           MailQueueJSONDelete.as_view(),
                           name="delete_mailqueue_json"),
)

urlpatterns += patterns('',
                        # Pattern for serving media while developing
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.STATIC_ROOT}),
                        )
