"""Definition of the Time Slot content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from uwosh.timeslot import timeslotMessageFactory as _
from uwosh.timeslot.interfaces import ITimeSlot
from uwosh.timeslot.config import PROJECTNAME

TimeSlotSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

TimeSlotSchema['title'].storage = atapi.AnnotationStorage()
TimeSlotSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(TimeSlotSchema, folderish=True, moveDiscussion=False)

class TimeSlot(folder.ATFolder):
    """Description of the Example Type"""
    implements(ITimeSlot)

    portal_type = "Time Slot"
    schema = TimeSlotSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

atapi.registerType(TimeSlot, PROJECTNAME)
