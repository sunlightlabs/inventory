#
# models.py
#

from django.db import models
from datetime import datetime, date

# Create your models here.

CATAGORIES = (
        ('O', 'Office Furniture'), 
        ('D', 'Desktop Computers'), 
        ('M', 'Monitors'), 
        ('L', 'Laptops'),
        ('T', 'Telephones'),
        ('P', 'Printer'),
        ('M', 'Misc Electronics'),
        ('A', 'Art'),
        ('F', 'Furniture'),
        ('S', 'Storage'),
        ('W', 'Software'),
        ('T', 'Other'),
)

"""
THINGs = (
        ('1', 'engagement'),
        ('2', 'natdatcat'),
        ('3', 'engagement'),
        ('4', 'policy reporting'),
        ('5', 'labs'),
        ('6', 'operations'),
        ('7', 'program indirect'),
        ('8', 'executive'),
        ('9', 'code for america'),
        ('10', 'npp'),
        ('11', 'natdatcat'),
        ('12', 'but distiguishable things....'),
        )
"""

OFFICE_NUMBER = (
        (300, "Reception"),
        (301, "Conference Room"),
        (302, "Conference Hallway"),
        (303, "Ellen Hallway"),
        (304, "Internpods"),
        (305, "Interpods Passthru"),
        (306, "Engagement Hallway"),
        (307, "Reporting Hallway"),
        (308, "Breakroom"),
        (309, "Kitchen"),
        (310, "Storage Room"),
        (311, "Server Room"),
        (312, "Pre-server room"),
        (313, "Labs Interns"),
        (314, "Labs Lounge"),
        (315, "Labs West"),
        (316, "Labs East"),
        (317, "Reporting"),
        (318, "Engagement South"),
        (319, "Engagement North"),
        (320, "Policy Team"),
        (321, "Administration"),
        (322, "Ellen's Office"),
        (323, ''),
        (324, ''),
        (325, ''),
        (326, ''),
        (327, ''),
        (328, ''),
        (329, ''),
        (330, ''),
        (331, ''),
        (332, 'Out-of-Office'),
        )

"""
COST_CENTER = (
        (1, 'c3'),
        (2, 'c4'),
        (3, 'subsidyscope'),
        (4, 'labs'),
        (5, 'blah'),
        )
"""

class Fund(models.Model):
    date_added          = models.DateTimeField(default=datetime.now)
    name                = models.CharField(max_length=24)
    description         = models.TextField(blank=True)

    def __unicode__ (self):
        return "%s" % (self.name)


class Item(models.Model):
    date_added          = models.DateTimeField(default=datetime.now)   # <--- automatic

#    id                  = models.PositiveIntegerField(primary_key=True)
    sticker_num         = models.PositiveIntegerField()
    name                = models.CharField(max_length=50)
    user                = models.CharField(max_length=50)
    date_of_purchase    = models.DateField(default=date.today)
    cost                = models.CharField(max_length=10)
    funding_src         = models.ForeignKey(Fund)
    category            = models.CharField(max_length=1, choices=CATAGORIES)
    serial_number       = models.CharField(max_length=255)
    specs               = models.TextField(blank=True)
    notes               = models.TextField(blank=True)

    is_assigned         = models.BooleanField(default=False)
    # example sell old macbook

    in_inventory        = models.BooleanField(default=True)
    out_of_inventory_reason = models.TextField(blank=True)
    
    where = models.IntegerField(choices=OFFICE_NUMBER)

#    improvments = Dict of Dates and Text of what items were added
#    dates_of_depreciation = Dict of Dates depreciation and rated Values 
#    photo = models.URLField(blank=True, verify_exists=False)
    photo = models.ImageField(blank=True, upload_to='uploads')

    def __unicode__ (self):
        return "%s, %s" % (self.name, self.user)


class Improvement(models.Model):
    item = models.ForeignKey(Item, related_name="improvements")
    date_improved = models.DateTimeField()
    text = models.TextField()


class Depreciation(models.Model):
    item = models.ForeignKey(Item, related_name="deprications")
    date_depricated = models.DateTimeField()
    rated_value = models.IntegerField()
