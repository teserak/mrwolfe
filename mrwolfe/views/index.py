from django.conf import settings
from django.views.generic import TemplateView
from mrwolfe.models.sla import SLA
from mrwolfe.models.mailqueue import MailQueue
from mrwolfe.models.issue import Issue
from mrwolfe.models.operator import Operator
from mrwolfe.models.contact import Contact
from mrwolfe.models.setting import Setting
from mrwolfe.models.itconnector import ITConnector


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):

        ctx = super(IndexView, self).get_context_data(**kwargs)

        ctx.update({"view": self})

        return ctx

    def list_my_issues(self):

        return Issue.objects.filter(
            assignee__operator__user=self.request.user). \
            exclude(status=settings.ISSUE_STATUS_CLOSED)

    def list_unassigned_issues(self):

        return Issue.objects.filter(assignee__isnull=True,). \
            exclude(status=settings.ISSUE_STATUS_CLOSED)

    def list_unclosed_issues(self):

        return Issue.objects.all().exclude(status=settings.ISSUE_STATUS_CLOSED)


class AdminView(IndexView):

    template_name = "admin.html"

    def list_slas(self):

        return SLA.objects.all()

    def list_mailqueues(self):

        return MailQueue.objects.all()

    def list_operators(self):

        return Operator.objects.all()

    def list_contacts(self):

        return Contact.objects.all()

    def list_settings(self):

        return Setting.objects.all()

    def list_connectors(self):

        return ITConnector.objects.all()
