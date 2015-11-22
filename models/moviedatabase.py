# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

db.define_table('movie',
                Field('Title',requires=IS_NOT_EMPTY()),
                Field('Genre',requires=IS_NOT_EMPTY()),
                Field('TimeOfRelease','datetime'),
                Field('Description','text',requires=IS_NOT_EMPTY()),
                Field('Director',requires=IS_NOT_EMPTY()),
                Field('Writer',requires=IS_NOT_EMPTY()),
                Field('Actors',requires=IS_NOT_EMPTY()),
                Field('image','upload'),
                Field('Trailer',requires=IS_NOT_EMPTY()))



db.define_table('person',
                Field('pname',requires=IS_NOT_EMPTY()),
                Field('dob',requires=IS_NOT_EMPTY()),
                Field('description','text',requires=IS_NOT_EMPTY()),
                Field('gender',requires=IS_NOT_EMPTY()),
                Field('country',requires=IS_NOT_EMPTY()),
                Field('description',requires=IS_NOT_EMPTY()),
                Field('agentcontact',requires=IS_NOT_EMPTY()),
                Field('image','upload'))



db.define_table('review',
                Field('mv_id','reference movie'),
                Field('title',requires=IS_NOT_EMPTY()),
                Field('rating','float',requires=IS_INT_IN_RANGE(minimum=1,maximum=11),comment='Input something between 1 and 10'),
                Field('body','text',requires=IS_NOT_EMPTY()),
                auth.signature)
#db.review.mv_id.requires=IS_IN_DB(db,db.movie.id,'%(name)s')




db.define_table('useracc',
                Field('uname',requires=IS_NOT_EMPTY()),
                Field('dob',requires=IS_NOT_EMPTY()),
                Field('gender',requires=IS_NOT_EMPTY()),
                Field('email',requires=IS_NOT_EMPTY()),
                Field('country',requires=IS_NOT_EMPTY()),
                Field('pwd',requires=IS_NOT_EMPTY()))

db.define_table('awards',
                Field('m_id','reference movie'),
                Field('p_id','reference person'),
                Field('awardname',requires=IS_NOT_EMPTY()))

db.define_table('actors',
                Field('m_id','reference movie'),
                Field('p_id','reference person'),
                Field('role',requires=IS_NOT_EMPTY()))



db.define_table('friend_request',
                Field('from_id','integer',requires=IS_NOT_EMPTY()),
                Field('to_id','integer',requires=IS_NOT_EMPTY()),
                Field('status',requires=IS_NOT_EMPTY()))
