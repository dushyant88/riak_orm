from db.models import RiakModel
from db.manager import RiakManager
from db.fields import RiakField


class NewActiveListingMaterialized(RiakModel):
    key = RiakField()
    base64key = RiakField(in_key=False, required=False)
    value = RiakField(in_key=False)

    key_order = ('key',)
    key_seperator = ':'
    objects = RiakManager()

class NewActiveListing(RiakModel):
    
    '''
    This model defines the fields for new active listing datapoint
    which will be saved in riak.
    '''
    date = RiakField()
    time = RiakField()
    site = RiakField()
    category = RiakField()
    language = RiakField()
    object_id = RiakField(in_key=False, required=False)
    user_id = RiakField(in_key=False, required=False)

    key_order = ('date','time','site','category', 'language')
    key_seperator = ':'

    objects = RiakManager()

    materialized = NewActiveListingMaterialized