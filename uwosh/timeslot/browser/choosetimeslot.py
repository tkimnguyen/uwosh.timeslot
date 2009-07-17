from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from plone.memoize import instance

from uwosh.timeslot import timeslotMessageFactory as _

class IChooseTimeSlot(Interface):
    pass


class ChooseTimeSlot(BrowserView):
    implements(IChooseTimeSlot)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @instance.memoize
    def areAnyExtraFieldsRequired(self):
        return len(self.context.getExtraFields()) > 0

    @instance.memoize
    def isFieldRequired(self, field):
    	extraFields = self.context.getExtraFields()
        if field in extraFields:
            return True
        else:
            return False
    
    @instance.memoize
    def isCurrentUserLoggedIn(self):
        portal_membership = getToolByName(self, 'portal_membership')
        member = portal_membership.getAuthenticatedMember()
        return 'Anonymous' not in member.getRoles()

    @instance.memoize
    def showEditLinks(self):
        portal_membership = getToolByName(self, 'portal_membership')
        member = portal_membership.getAuthenticatedMember()
        return 'Manager' in member.getRoles()
